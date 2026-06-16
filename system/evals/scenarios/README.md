# Eval scenarios

Two scenario types — do not mix them in one folder.

| Subfolder | Type | Runner | What it tests |
|---|---|---|---|
| `behavior/` | Turn-based agent coaching | `run_scenario.py` / `run_all.py` | Questions before templates, PJT trigger, routing |
| `rubric/<slug>/` | Rubric regression (`type: rubric_regression`) | `run_rubric_regression.py` | Can a `3-*-evaluation.md` rubric grade good vs bad specimens? |

**Canonical spec for behavior scenarios:** each folder's `expected.yaml` + `README.md`.

**Index only:** [agent-behavior-scenarios.json](../agent-behavior-scenarios.json) lists `scenario_id` → `harness_path` for discovery and stub generation.
