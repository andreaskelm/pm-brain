# Eval Results

Local output from the harness, plus optional human review logs.

## Harness output

Runs write JSON here and auto-prune to the newest 2 per pattern (`--keep-results N`, or `PM_BRAIN_EVAL_KEEP=0` to disable). JSON is gitignored.

| File pattern | Source |
|---|---|
| `{scenario_id}-{timestamp}.json` | `harness/run_scenario.py` |
| `rubric-regression-{timestamp}.json` | `harness/run_rubric_regression.py` |

Each payload records `"dry_run": true|false`. Failed assertions name a `spec_owner` — edit that file, re-run.

**This is not where learning lives.** The agent never reads these files. Learning persists in the spec files you fix (`AGENTS.md`, `ORCHESTRATION.md`, skills) and, when a failure recurs, in a new scenario under `scenarios/behavior/`.

## Human review logs (optional)

After a session worth reviewing, save `YYYY-MM-DD-brief-description.md` here. Track them in git if you want pattern detection over time; otherwise add `*.md` to this folder's `.gitignore`.

```markdown
# Eval Log — YYYY-MM-DD — [brief description]

**Platform / model:** [Cursor + …]   **States:** [product_sense → execution_mode …]
**Closest scenario:** [NN-slug, or "none — new scenario?"]

## Dimensions
| Dimension | Strong / OK / Weak | Note |
|---|---|---|
| Questioning | | |
| Perspective | | |
| Framework fit | | |
| Voice | | |
| Guidance | | |
| User agency | | |
| Artifact clarity | | |

## What worked
[Specific moments, and why they worked.]

## What missed — and why it was structurally likely
[The miss, what should have happened, the structural cause. See the root-cause bar in ../README.md.]

## Fixes
| Change | File | Status |
|---|---|---|
| | | Open / Done YYYY-MM-DD |
```

Scan the **Fixes** column across logs to find recommendations that never got actioned. When the same root cause shows up twice, write the scenario.
