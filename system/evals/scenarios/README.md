# Eval scenarios

| Subfolder | Type | Runner | What it tests |
|---|---|---|---|
| `behavior/NN-slug/` | Live multi-turn agent behavior | `run_scenario.py` / `run_all.py` | Coaching, voice, routing, triggers |
| `rubric/<slug>/` | Rubric regression (`type: rubric_regression`) | `run_rubric_regression.py` | Does a criteria file PASS good and FAIL bad specimens? |

Catalog, schema, and how to add one: [../README.md](../README.md#behavior-scenarios). Each folder's `expected.yaml` is the spec — there is no separate index.
