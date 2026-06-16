#!/usr/bin/env python3
"""Generate stub behavior scenario dirs from agent-behavior-scenarios.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
data = json.loads((ROOT / "evals/agent-behavior-scenarios.json").read_text(encoding="utf-8"))
scenarios_dir = ROOT / "evals/scenarios/behavior"

for s in data["scenarios"]:
    harness_path = s.get("harness_path", "")
    if not harness_path.startswith("behavior/"):
        continue
    slug = harness_path.removeprefix("behavior/")
    d = scenarios_dir / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "inputs").mkdir(exist_ok=True)
    inp = d / "inputs" / "turn-01-user.md"
    if not inp.exists() and s.get("initial_prompt"):
        inp.write_text(s["initial_prompt"] + "\n", encoding="utf-8")
    readme = d / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# Scenario {slug.split('-', 1)[0]} — {slug.split('-', 1)[1].replace('-', ' ').title() if '-' in slug else slug}\n\n"
            f"**scenario_id:** `{s['scenario_id']}`  \n"
            f"**Type:** {s.get('scenario_type', '')}  \n"
            f"**Status:** Stub — calibrate `expected.yaml` before relying on harness.\n",
            encoding="utf-8",
        )
    exp = d / "expected.yaml"
    if not exp.exists():
        exp.write_text(
            f"scenario_id: {s['scenario_id']}\n"
            f"description: |\n  Stub scenario — add assertions.\n\n"
            f"pass_threshold:\n  structural: 1.0\n  content: 0.8\n\n"
            f"turns:\n"
            f"  - turn: 1\n"
            f"    input: turn-01-user.md\n"
            f"    structural:\n"
            f"      - type: question_count_at_least\n"
            f"        arg: 1\n"
            f"        spec_owner: AGENTS.md\n"
            f"    content: []\n\n"
            f"final_state:\n  structural: []\n",
            encoding="utf-8",
        )

print(f"Ensured {len(data['scenarios'])} behavior scenario dirs under evals/scenarios/behavior/")
