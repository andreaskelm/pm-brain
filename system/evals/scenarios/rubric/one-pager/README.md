# Rubric regression — One-Pager

Tests whether the canonical One-Pager evaluation rubric correctly PASSes a good specimen and FAILs a bad one.

**Rubric:** [.claude/skills/stakeholder-comms/references/criteria-one-pager.md](../../../../../.claude/skills/stakeholder-comms/references/criteria-one-pager.md)

**Test specimens:** `fixtures/good.md`, `fixtures/bad.md` (synthetic — not real work)

```bash
python system/evals/harness/run_rubric_regression.py scenarios/rubric/one-pager
python system/evals/harness/run_rubric_regression.py --all --dry-run
```
