# Rubric regression — PRD

Tests whether the canonical PRD evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [2-Methods/4-Execution/4-PRD/3-prd-evaluation.md](../../../../../2-Methods/4-Execution/4-PRD/3-prd-evaluation.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/prd
python system/evals/harness/run_rubric_regression.py --all --dry-run
```

To add another rubric: copy this folder to `scenarios/rubric/<slug>/`, set `rubric_path`, add specimens under `fixtures/`.
