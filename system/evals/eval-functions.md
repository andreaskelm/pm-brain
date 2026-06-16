# Eval Functions — pointer

Behavior checks from the original spec are **implemented in code**:

| Conceptual check | Implementation |
|------------------|----------------|
| `check_braindump_sufficient()` | L2 harness + `hooks/validate_write.py` (structural gate) |
| `check_questions_before_framework()` | `harness/checks/structural.py` → `question_count_at_least` |
| `check_golden_rule_violation()` | `file_not_created_glob` in scenario `expected.yaml` |
| `match_scenario_type()` | `agent-behavior-scenarios.json` + harness scenarios |

**Run structural checks:** `python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/<slug>`

**Schema for assertions:** [expected-yaml-schema.md](expected-yaml-schema.md)

**Human checkpoint prompts** (when not running the harness): see [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and braindump sufficiency in [../coaching/README.md](../coaching/README.md).

Log format for manual runs: [eval-results/README.md](eval-results/README.md).
