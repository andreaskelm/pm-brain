# Rubric regression — North Star

Tests whether the canonical North Star evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [2-Methods/2-Strategy/2-Strategic-Execution/3-North-Star/3-north-star-evaluation.md](../../../../../2-Methods/2-Strategy/2-Strategic-Execution/3-North-Star/3-north-star-evaluation.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/north-star
python system/evals/harness/run_rubric_regression.py --all --dry-run
```
