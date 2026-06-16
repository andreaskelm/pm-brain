# Rubric regression — Opportunity Assessment

Tests whether the canonical OA evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [2-Methods/3-Discovery/4-Opportunity-Assessment/3-opportunity-assessment-evaluation.md](../../../../../2-Methods/3-Discovery/4-Opportunity-Assessment/3-opportunity-assessment-evaluation.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/oa
python system/evals/harness/run_rubric_regression.py --all --dry-run
```
