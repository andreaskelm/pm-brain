#!/usr/bin/env python3
"""Run all PM Brain eval scenarios."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEHAVIOR_SCENARIOS = ROOT / "system" / "evals" / "scenarios" / "behavior"
RUNNER = ROOT / "system" / "evals" / "harness" / "run_scenario.py"


def is_behavior_scenario(scenario_dir: Path) -> bool:
    expected = scenario_dir / "expected.yaml"
    if not expected.exists():
        return False
    try:
        import yaml  # type: ignore
    except ImportError:
        return True
    spec = yaml.safe_load(expected.read_text(encoding="utf-8")) or {}
    return spec.get("type") != "rubric_regression"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all PM Brain eval scenarios")
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--skip-content", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-cost", type=float, default=50.0)
    parser.add_argument("--plumbing", action="store_true")
    args = parser.parse_args()

    if not BEHAVIOR_SCENARIOS.exists():
        print("No scenarios/behavior directory", file=sys.stderr)
        return 1

    scenario_dirs = sorted(
        d for d in BEHAVIOR_SCENARIOS.iterdir() if d.is_dir() and is_behavior_scenario(d)
    )
    if not scenario_dirs:
        print("No scenarios with expected.yaml found", file=sys.stderr)
        return 1

    failed = 0
    for scenario_dir in scenario_dirs:
        print(f"\n=== {scenario_dir.name} ===")
        cmd = [
            sys.executable,
            str(RUNNER),
            str(scenario_dir),
            "--runs",
            str(args.runs),
            "--max-cost",
            str(args.max_cost),
        ]
        if args.skip_content:
            cmd.append("--skip-content")
        if args.dry_run:
            cmd.append("--dry-run")
        if args.plumbing:
            cmd.append("--plumbing")
        rc = subprocess.run(cmd, check=False).returncode
        if rc != 0 and not args.plumbing:
            failed += 1
        elif rc != 0 and args.plumbing:
            print(f"Plumbing warning: {scenario_dir.name} returned {rc}")

    print(f"\n{len(scenario_dirs) - failed}/{len(scenario_dirs)} scenarios passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
