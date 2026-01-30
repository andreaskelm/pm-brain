#!/usr/bin/env python3
"""
Compute Weighted Brier Score from Product Judgment Test forecast log.

Reads forecast-log.md (markdown table), parses closed rows (Outcome filled),
and outputs per-forecast Brier and Overall Brier Score.

Usage:
  python compute_brier.py [path/to/forecast-log.md]
  Default path: ../forecast-log.md (relative to this script)
"""

import sys
from pathlib import Path
from typing import List

# Weights (from BRIER-CALCULATION.md)
BET_TYPE_WEIGHT = {"New Product": 3.0, "Expansion": 2.0, "Iteration": 1.0}
NOVELTY_WEIGHT = {"New Behavior": 1.5, "Known Problem": 1.0}
OUTCOME_VALUE = {"Exceeded": 1.0, "Met": 0.8, "Failed": 0.0}

# Table column indices (0-based after split by "|")
IDX_DATE = 1
IDX_BET = 2
IDX_CONFIDENCE = 5
IDX_BET_TYPE = 6
IDX_NOVELTY = 7
IDX_OUTCOME = 11


def parse_table(path: Path) -> List[dict]:
    """Parse markdown table from forecast-log.md. Return list of row dicts (only closed rows)."""
    text = path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line == "|" or "---" in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 12:
            continue
        outcome = cells[IDX_OUTCOME].strip()
        if outcome not in OUTCOME_VALUE:
            continue
        try:
            confidence_pct = float(cells[IDX_CONFIDENCE].strip().replace("%", ""))
        except ValueError:
            continue
        bet_type = cells[IDX_BET_TYPE].strip()
        novelty = cells[IDX_NOVELTY].strip()
        if bet_type not in BET_TYPE_WEIGHT or novelty not in NOVELTY_WEIGHT:
            continue
        rows.append({
            "date": cells[IDX_DATE],
            "bet": cells[IDX_BET],
            "confidence": confidence_pct / 100.0,
            "bet_type": bet_type,
            "novelty": novelty,
            "outcome": outcome,
        })
    return rows


def brier(probability: float, outcome: float) -> float:
    return (probability - outcome) ** 2


def interpret(score: float) -> str:
    if score < 0.10:
        return "Elite Judgment"
    if score < 0.15:
        return "Strong Calibration"
    if score < 0.25:
        return "Typical PM"
    if score < 0.40:
        return "Overconfident"
    return "Uncalibrated"


def main() -> None:
    if len(sys.argv) > 1:
        log_path = Path(sys.argv[1])
    else:
        log_path = Path(__file__).resolve().parent / ".." / "forecast-log.md"
    if not log_path.exists():
        print(f"Error: {log_path} not found.", file=sys.stderr)
        sys.exit(1)

    rows = parse_table(log_path)
    if not rows:
        print("No closed forecasts found (rows with Outcome = Exceeded | Met | Failed).")
        print("Fill Resolution columns in forecast-log.md and run again.")
        sys.exit(0)

    total_weighted_brier = 0.0
    total_weight = 0.0
    print("Per-forecast Brier:")
    print("-" * 60)
    for i, r in enumerate(rows, 1):
        outcome_val = OUTCOME_VALUE[r["outcome"]]
        b = brier(r["confidence"], outcome_val)
        w = BET_TYPE_WEIGHT[r["bet_type"]] * NOVELTY_WEIGHT[r["novelty"]]
        wb = b * w
        total_weighted_brier += wb
        total_weight += w
        print(f"  {i}. {r['date']} | {r['bet'][:30]:30} | Brier={b:.4f} Weight={w} Weighted={wb:.4f}")
    print("-" * 60)
    overall = total_weighted_brier / total_weight
    print(f"Overall Brier Score: {overall:.4f}")
    print(f"Interpretation: {interpret(overall)}")
    print(f"(Closed forecasts: {len(rows)})")


if __name__ == "__main__":
    main()
