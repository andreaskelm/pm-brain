# Rubric regression — OKR

Tests whether the canonical OKR evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [2-Methods/2-Strategy/2-Strategic-Execution/1-OKR/3-okr-evaluation.md](../../../../../2-Methods/2-Strategy/2-Strategic-Execution/1-OKR/3-okr-evaluation.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/okr
python system/evals/harness/run_rubric_regression.py --all --dry-run
```
