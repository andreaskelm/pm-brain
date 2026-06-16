#!/usr/bin/env python3
"""Rubric regression — grade test specimens against framework evaluation docs (eval level L1)."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVALS = ROOT / "system" / "evals"
HARNESS = EVALS / "harness"
RESULTS_DIR = EVALS / "eval-results"

sys.path.insert(0, str(HARNESS))
from results_io import write_json_result  # noqa: E402

CURSOR_BIN = os.environ.get("PM_BRAIN_CURSOR_BIN", "cursor-agent")
RUBRIC_SCENARIO_TYPE = "rubric_regression"
RUBRIC_ROOT = EVALS / "scenarios" / "rubric"


def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise SystemExit("PyYAML required: pip install pyyaml") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def parse_verdict(text: str) -> str:
    match = re.search(r"VERDICT:\s*(PASS|FAIL|UNCERTAIN)", text, re.I)
    return match.group(1).upper() if match else "FAIL"


def resolve_path(rel: str) -> Path:
    p = Path(rel)
    if p.is_absolute():
        return p
    for base in (EVALS, ROOT):
        candidate = base / rel
        if candidate.exists():
            return candidate
    return ROOT / rel


def resolve_fixture(scenario_dir: Path, rel: str) -> Path:
    local = scenario_dir / rel
    if local.exists():
        return local
    return resolve_path(rel)


def run_fixture(
    *,
    artifact_text: str,
    rubric_text: str,
    judge_text: str,
    artifact_type: str,
    dry_run: bool,
    expect_verdict: str,
) -> dict:
    prompt = f"""Grade this {artifact_type} artifact.

## Judge contract
{judge_text}

## Framework rubric (canonical — apply fully)
{rubric_text[:12000]}

## Artifact to grade
{artifact_text}

Output exactly one line first:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>
"""

    if dry_run:
        verdict = expect_verdict
        raw = f"[DRY RUN] expected {verdict}"
    else:
        try:
            proc = subprocess.run(
                [CURSOR_BIN, "-p", "--output-format", "text", "--force", prompt],
                capture_output=True,
                text=True,
                timeout=180,
                check=False,
            )
        except FileNotFoundError:
            return {
                "passed": False,
                "verdict": "FAIL",
                "raw": f"{CURSOR_BIN} not found",
                "error": "cursor-agent missing",
            }
        raw = proc.stdout or proc.stderr
        verdict = parse_verdict(raw)

    passed = verdict == expect_verdict
    return {"passed": passed, "verdict": verdict, "expect_verdict": expect_verdict, "raw": raw[:500]}


def run_scenario(scenario_dir: Path, *, dry_run: bool = False) -> dict:
    expected_path = scenario_dir / "expected.yaml"
    if not expected_path.exists():
        raise SystemExit(f"Missing {expected_path}")

    spec = load_yaml(expected_path)
    if spec.get("type") != RUBRIC_SCENARIO_TYPE:
        raise SystemExit(f"{scenario_dir.name} is not type {RUBRIC_SCENARIO_TYPE}")

    rubric_path = resolve_path(spec["rubric_path"])
    judge_path = resolve_path(spec.get("judge", "judges/artifact_quality.md"))

    if not rubric_path.exists():
        raise SystemExit(f"Rubric not found: {rubric_path}")
    if not judge_path.exists():
        raise SystemExit(f"Judge not found: {judge_path}")

    rubric_text = rubric_path.read_text(encoding="utf-8")
    judge_text = judge_path.read_text(encoding="utf-8")
    artifact_type = rubric_path.parent.parent.name

    results = []
    for fixture in spec.get("fixtures", []):
        input_path = resolve_fixture(scenario_dir, fixture["input"])
        if not input_path.exists():
            raise SystemExit(f"Fixture not found: {fixture['input']} (looked in {scenario_dir})")
        expect = fixture["expect_verdict"].upper()
        artifact_text = input_path.read_text(encoding="utf-8")
        outcome = run_fixture(
            artifact_text=artifact_text,
            rubric_text=rubric_text,
            judge_text=judge_text,
            artifact_type=artifact_type,
            dry_run=dry_run,
            expect_verdict=expect,
        )
        outcome["fixture"] = str(fixture["input"])
        results.append(outcome)
        status = "OK" if outcome["passed"] else "MISMATCH"
        print(f"  {fixture['input']}: {outcome['verdict']} (expect {expect}) -> {status}")

    all_passed = all(r["passed"] for r in results)
    return {
        "scenario_id": spec.get("scenario_id", scenario_dir.name),
        "scenario_dir": str(scenario_dir.relative_to(EVALS)),
        "rubric_path": str(rubric_path.relative_to(ROOT)),
        "passed": all_passed,
        "fixtures": results,
        "spec_owner": spec.get("spec_owner", ""),
    }


def find_rubric_scenarios() -> list[Path]:
    if not RUBRIC_ROOT.exists():
        return []
    found: list[Path] = []
    for d in sorted(RUBRIC_ROOT.iterdir()):
        if not d.is_dir():
            continue
        expected = d / "expected.yaml"
        if not expected.exists():
            continue
        spec = load_yaml(expected)
        if spec.get("type") == RUBRIC_SCENARIO_TYPE:
            found.append(d)
    return found


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rubric regression (eval level L1): grade test specimens against 2-Methods rubrics"
    )
    parser.add_argument("scenario_dir", nargs="?", type=Path, help="e.g. scenarios/rubric/prd")
    parser.add_argument("--all", action="store_true", help="Run all rubric-regression scenarios")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--keep-results",
        type=int,
        default=None,
        metavar="N",
        help="Keep N newest rubric-regression JSON files (default: PM_BRAIN_EVAL_KEEP or 2; 0 = keep all)",
    )
    args = parser.parse_args()

    if args.all:
        dirs = find_rubric_scenarios()
    elif args.scenario_dir:
        d = args.scenario_dir
        if not d.is_absolute():
            d = EVALS / d if (EVALS / d).exists() else ROOT / d
        dirs = [d]
    else:
        parser.error("Provide scenario_dir or --all")

    if not dirs:
        print("No artifact-rubric scenarios found", file=sys.stderr)
        return 1

    all_results: list[dict] = []
    failed = 0
    for scenario_dir in dirs:
        print(f"\n=== {scenario_dir.name} ===")
        try:
            result = run_scenario(scenario_dir, dry_run=args.dry_run)
            all_results.append(result)
            if not result["passed"]:
                failed += 1
        except SystemExit as exc:
            print(exc, file=sys.stderr)
            failed += 1

    payload = {"timestamp": int(time.time()), "dry_run": args.dry_run, "scenarios": all_results}
    out = write_json_result(
        RESULTS_DIR,
        f"rubric-regression-{int(time.time())}.json",
        payload,
        prune_glob="rubric-regression-*.json",
        keep=args.keep_results,
    )
    print(f"\nWrote {out.relative_to(ROOT)}")
    print(f"{len(dirs) - failed}/{len(dirs)} rubric-regression scenarios passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
