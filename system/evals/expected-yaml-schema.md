# expected.yaml Schema

Ground-truth assertions for harness scenarios.

**Behavior:** `system/evals/scenarios/behavior/<NN-slug>/`  
**Rubric:** `system/evals/scenarios/rubric/<slug>/`

## File layout (behavior)

```
system/evals/scenarios/behavior/01-braindump-floor-gate/
├── README.md
├── inputs/
│   └── turn-01-user.md
└── expected.yaml
```

## Schema

```yaml
scenario_id: braindump_floor_gate_001   # listed in agent-behavior-scenarios.json with harness_path
description: |
  User requests a PRD immediately. Agent must braindump first.

pass_threshold:
  structural: 1.0    # must pass every run
  content: 0.8       # 4 of 5 runs minimum (when judges enabled)

turns:
  - turn: 1
    input: turn-01-user.md
    structural:
      - type: file_not_created_glob
        arg: "3-Work/**/*.md"
        spec_owner: .cursor/rules/pm-brain.mdc
      - type: question_count_at_least
        arg: 1
        spec_owner: AGENTS.md
    content:
      - judge: preflight_before_template
        rubric: judges/preflight_before_template.md
        spec_owner: AGENTS.md
        expected_meaning: "Agent asks preflight questions before loading any PRD template"

final_state:
  structural:
    - type: all_internal_links_valid
      spec_owner: system/evals/checks/verify-markdown.py
```

## Assertion types (structural)

| type | arg | Purpose |
|------|-----|---------|
| `file_exists` | path | File exists after turn |
| `file_exists_glob` | glob | Glob matches at least one file |
| `file_not_created_glob` | glob | No new file matching glob this turn |
| `file_modified` | path | File mtime changed this turn |
| `file_modified_or_created` | path | File exists or was created this turn |
| `question_count_at_least` | N | Agent response contains ≥ N `?` |
| `forecast_log_row_added` | (none) | PJT forecast-log.md gained a row |
| `no_duplicate_content` | path | File does not duplicate linked source |
| `response_contains` | string | Agent response must contain substring (case-insensitive) |
| `response_not_contains` | string | Agent response must not contain substring |
| `response_not_links_template` | (none) | Agent must not link to any `2-Methods/` template path |
| `all_internal_links_valid` | (none) | All relative markdown links resolve |

## Content (judge) assertions

Each entry invokes the Cursor CLI headless agent (`PM_BRAIN_CURSOR_BIN`, default `cursor-agent`) with the rubric. Judge must output exactly one line:

`VERDICT: PASS|FAIL|UNCERTAIN — <reason>`

`UNCERTAIN` counts as FAIL. Aggregate pass rate across N runs handles variance.

## spec_owner field

Every assertion should name the file that owns the behavior. On failure, edit that file — not a random rule elsewhere.

├──

## Rubric regression (`type: rubric_regression`)

Scenarios live under `scenarios/rubric/<slug>/` with test specimens in `fixtures/good.md` and `fixtures/bad.md`. They do not replay agent turns — they grade specimens against a framework rubric pointed to by `rubric_path`.

```yaml
scenario_id: rubric_prd_001
type: rubric_regression
description: |
  Grade PRD test specimens against canonical rubric.

rubric_path: 2-Methods/4-Execution/4-PRD/3-prd-evaluation.md
judge: judges/artifact_quality.md
spec_owner: 2-Methods/4-Execution/4-PRD/3-prd-evaluation.md

fixtures:
  - input: fixtures/good.md
    expect_verdict: PASS
  - input: fixtures/bad.md
    expect_verdict: FAIL
```

Run: `python system/evals/harness/run_rubric_regression.py scenarios/rubric/prd`
