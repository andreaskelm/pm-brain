#!/usr/bin/env python3
"""Run a single PM Brain eval scenario against cursor-agent headless."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
EVALS = ROOT / "system" / "evals"
HARNESS = EVALS / "harness"
RESULTS_DIR = EVALS / "eval-results"

sys.path.insert(0, str(HARNESS))
from checks.structural import run_assertions, snapshot_files  # noqa: E402
from results_io import write_json_result  # noqa: E402

CURSOR_BIN = os.environ.get("PM_BRAIN_CURSOR_BIN", "cursor-agent")
TURN_TIMEOUT = int(os.environ.get("PM_BRAIN_TURN_TIMEOUT", "600"))
JUDGE_TIMEOUT = int(os.environ.get("PM_BRAIN_JUDGE_TIMEOUT", "180"))
TURN_MODEL = os.environ.get("PM_BRAIN_TURN_MODEL", "")
JUDGE_MODEL = os.environ.get("PM_BRAIN_JUDGE_MODEL", "")

SKIP_COPY = {
    ".git",
    "system/evals/eval-results",
    "__pycache__",
    ".cursor/worktrees",
}


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "PyYAML required for harness. Install: pip install pyyaml"
        ) from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def copy_brain(dest: Path) -> None:
    for item in ROOT.iterdir():
        rel = item.name
        if rel in {".git"}:
            continue
        target = dest / rel
        if item.is_dir():
            shutil.copytree(
                item,
                target,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
                dirs_exist_ok=True,
            )
        else:
            shutil.copy2(item, target)
    # Remove heavy/ephemeral paths
    for skip in SKIP_COPY:
        p = dest / skip
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            else:
                p.unlink(missing_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def invoke_agent(
    prompt: str,
    workdir: Path,
    *,
    model: str = "",
    timeout: int = TURN_TIMEOUT,
    dry_run: bool = False,
) -> tuple[str, float]:
    if dry_run:
        return (
            "What problem are you solving, and for whom? "
            "What assumptions are you making? "
            "Would you like to log this in the Product Judgment Test forecast log? "
            "[DRY RUN — mock response for harness plumbing]",
            0.0,
        )

    cmd = [
        CURSOR_BIN,
        "-p",
        "--output-format",
        "json",
        "--workspace",
        str(workdir),
        "--force",
        "--trust",
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)

    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=workdir,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError:
        return (
            f"[SKIP] {CURSOR_BIN} not found — set PM_BRAIN_CURSOR_BIN or install Cursor CLI",
            0.0,
        )
    except subprocess.TimeoutExpired:
        return (f"[TIMEOUT] after {timeout}s", 0.0)

    elapsed = time.time() - start
    stdout = proc.stdout.strip()
    if stdout:
        try:
            data = json.loads(stdout)
            return data.get("result", stdout), elapsed
        except json.JSONDecodeError:
            return stdout, elapsed
    return proc.stderr or f"[exit {proc.returncode}]", elapsed


def parse_verdict(text: str) -> tuple[str, str]:
    match = re.search(r"VERDICT:\s*(PASS|FAIL|UNCERTAIN)\s*[—\-]\s*(.+)", text, re.I)
    if match:
        return match.group(1).upper(), match.group(2).strip()
    return "FAIL", "no VERDICT line in judge output"


def run_judge(
    assertion: dict[str, Any],
    *,
    agent_response: str,
    scenario_desc: str,
    workdir: Path,
    dry_run: bool = False,
) -> dict[str, Any]:
    rubric_path = EVALS / assertion["rubric"]
    if not rubric_path.exists():
        rubric_path = HARNESS / assertion["rubric"]
    rubric = rubric_path.read_text(encoding="utf-8") if rubric_path.exists() else ""

    prompt = f"""You are an eval judge for PM Brain agent behavior.

## Rubric
{rubric}

## Scenario
{scenario_desc}

## Expected meaning
{assertion.get('expected_meaning', '')}

## Must not
{assertion.get('must_not', 'N/A')}

## Agent response to grade
{agent_response}

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <one sentence reason>
"""

    model = assertion.get("model", JUDGE_MODEL)
    text, cost_proxy = invoke_agent(prompt, workdir, model=model, timeout=JUDGE_TIMEOUT, dry_run=dry_run)
    verdict, reason = parse_verdict(text)
    passed = verdict == "PASS"
    return {
        "type": "judge",
        "judge": assertion.get("judge", ""),
        "passed": passed,
        "verdict": verdict,
        "reason": reason,
        "spec_owner": assertion.get("spec_owner", ""),
        "raw": text[:500],
        "cost_proxy_sec": cost_proxy,
    }


def run_single(
    scenario_dir: Path,
    *,
    dry_run: bool = False,
    skip_content: bool = False,
    stop_after_turn: int | None = None,
) -> dict[str, Any]:
    expected = load_yaml(scenario_dir / "expected.yaml")
    inputs_dir = scenario_dir / "inputs"
    turn_files = sorted(inputs_dir.glob("turn-*.md"))

    workdir = Path(tempfile.mkdtemp(prefix="pm-brain-eval-"))
    copy_brain(workdir)

    turn_results: list[dict[str, Any]] = []
    total_cost_proxy = 0.0

    try:
        for spec in expected.get("turns", []):
            turn_num = spec["turn"]
            if stop_after_turn is not None and turn_num > stop_after_turn:
                break

            input_name = spec.get("input", "")
            input_path = inputs_dir / input_name
            user_text = input_path.read_text(encoding="utf-8") if input_path.exists() else ""

            before = snapshot_files(workdir)
            prompt = f"""You are the PM Brain coach agent. Respond to this user message.

Load AGENTS.md, system/MEMORY.md, and follow all routing rules.

User message:
{user_text}
"""
            agent_response, elapsed = invoke_agent(
                prompt, workdir, model=TURN_MODEL, dry_run=dry_run
            )
            total_cost_proxy += elapsed
            after = snapshot_files(workdir)

            structural = run_assertions(
                workdir,
                spec.get("structural", []),
                before=before,
                after=after,
                agent_response=agent_response,
            )
            struct_payload = [
                {
                    "type": r.assertion_type,
                    "arg": r.arg,
                    "passed": r.passed,
                    "message": r.message,
                    "spec_owner": r.spec_owner,
                }
                for r in structural
            ]

            content_payload: list[dict[str, Any]] = []
            if not skip_content:
                for judge_assert in spec.get("content", []):
                    jr = run_judge(
                        judge_assert,
                        agent_response=agent_response,
                        scenario_desc=expected.get("description", ""),
                        workdir=workdir,
                        dry_run=dry_run,
                    )
                    content_payload.append(jr)
                    total_cost_proxy += jr.get("cost_proxy_sec", 0)

            turn_results.append(
                {
                    "turn": turn_num,
                    "input": input_name,
                    "structural": struct_payload,
                    "content": content_payload,
                    "agent_response_preview": agent_response[:300],
                }
            )

        # final_state
        before = snapshot_files(workdir)
        after = before
        final_struct = run_assertions(
            workdir,
            expected.get("final_state", {}).get("structural", []),
            before=before,
            after=after,
            agent_response="",
        )
        final_content: list[dict[str, Any]] = []
        if not skip_content:
            for judge_assert in expected.get("final_state", {}).get("content", []):
                jr = run_judge(
                    judge_assert,
                    agent_response=json.dumps(turn_results, indent=2)[:4000],
                    scenario_desc=expected.get("description", ""),
                    workdir=workdir,
                    dry_run=dry_run,
                )
                final_content.append(jr)

        return {
            "scenario": expected.get("scenario_id", scenario_dir.name),
            "scenario_dir": str(scenario_dir.relative_to(ROOT)),
            "turns": turn_results,
            "final_state": {
                "structural": [
                    {
                        "type": r.assertion_type,
                        "passed": r.passed,
                        "message": r.message,
                        "spec_owner": r.spec_owner,
                    }
                    for r in final_struct
                ],
                "content": final_content,
            },
            "cost_proxy_sec": total_cost_proxy,
        }
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def aggregate(runs: list[dict[str, Any]], thresholds: dict[str, float]) -> dict[str, Any]:
    struct_pass = 0
    struct_total = 0
    content_pass = 0
    content_total = 0

    for run in runs:
        for turn in run.get("turns", []):
            for s in turn.get("structural", []):
                struct_total += 1
                if s.get("passed"):
                    struct_pass += 1
            for c in turn.get("content", []):
                content_total += 1
                if c.get("passed"):
                    content_pass += 1
        for s in run.get("final_state", {}).get("structural", []):
            struct_total += 1
            if s.get("passed"):
                struct_pass += 1
        for c in run.get("final_state", {}).get("content", []):
            content_total += 1
            if c.get("passed"):
                content_pass += 1

    struct_rate = struct_pass / struct_total if struct_total else 1.0
    content_rate = content_pass / content_total if content_total else 1.0

    return {
        "runs": len(runs),
        "structural_pass_rate": struct_rate,
        "content_pass_rate": content_rate,
        "structural_threshold": thresholds.get("structural", 1.0),
        "content_threshold": thresholds.get("content", 0.8),
        "passed": struct_rate >= thresholds.get("structural", 1.0)
        and content_rate >= thresholds.get("content", 0.8),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PM Brain eval scenario")
    parser.add_argument("scenario_dir", type=Path, help="Path to scenario folder")
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--skip-content", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Skip real agent calls")
    parser.add_argument("--stop-after-turn", type=int, default=None)
    parser.add_argument("--max-cost", type=float, default=20.0, help="Abort if cost proxy exceeds")
    parser.add_argument(
        "--keep-results",
        type=int,
        default=None,
        metavar="N",
        help="Keep N newest JSON files per scenario (default: PM_BRAIN_EVAL_KEEP or 2; 0 = keep all)",
    )
    parser.add_argument("--plumbing", action="store_true", help="Exit 0 if harness ran (ignore assertion results)")
    args = parser.parse_args()

    scenario_dir = args.scenario_dir.resolve()
    if not (scenario_dir / "expected.yaml").exists():
        print(f"Missing expected.yaml in {scenario_dir}", file=sys.stderr)
        return 1

    expected = load_yaml(scenario_dir / "expected.yaml")
    thresholds = expected.get("pass_threshold", {"structural": 1.0, "content": 0.8})

    all_runs: list[dict[str, Any]] = []
    total_cost = 0.0
    for i in range(args.runs):
        print(f"Run {i + 1}/{args.runs}...")
        result = run_single(
            scenario_dir,
            dry_run=args.dry_run,
            skip_content=args.skip_content,
            stop_after_turn=args.stop_after_turn,
        )
        all_runs.append(result)
        total_cost += result.get("cost_proxy_sec", 0)
        if total_cost > args.max_cost:
            print(f"Aborted: cost proxy {total_cost:.1f}s exceeds --max-cost {args.max_cost}")
            break

    summary = aggregate(all_runs, thresholds)
    payload = {"summary": summary, "dry_run": args.dry_run, "runs": all_runs}

    scenario_id = expected.get("scenario_id", scenario_dir.name)
    out_name = f"{scenario_id}-{int(time.time())}.json"
    out_path = write_json_result(
        RESULTS_DIR,
        out_name,
        payload,
        prune_glob=f"{scenario_id}-*.json",
        keep=args.keep_results,
    )
    print(f"Wrote {out_path.relative_to(ROOT)}")
    print(json.dumps(summary, indent=2))

    return 0 if (summary["passed"] or args.plumbing) else 1


if __name__ == "__main__":
    raise SystemExit(main())
