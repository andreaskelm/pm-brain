# Rubric regression — Roadmap

Tests whether the canonical Roadmap evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [.claude/skills/roadmap/references/criteria.md](../../../../../.claude/skills/roadmap/references/criteria.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/roadmap
python system/evals/harness/run_rubric_regression.py --all --dry-run
```
