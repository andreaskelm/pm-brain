# Judge: Artifact Quality (L1 — generic)

Grade a produced artifact against the **framework rubric provided below**.

The rubric is the canonical source of truth — usually a `3-*-evaluation.md` from `2-Methods/`. Do not invent criteria beyond what the rubric specifies.

## How to grade

1. Read the rubric fully before scoring.
2. Apply the rubric's quality checks, antipatterns, and success criteria to the artifact.
3. PASS only if the artifact would pass a peer review using that rubric — not "good enough for a draft."

## Output contract

Output exactly one line first:

`VERDICT: PASS|FAIL|UNCERTAIN — <one sentence reason>`

Then optionally add 2–3 bullet findings (strengths + gaps). Keep brief.

## Verdict bands

- **PASS** — Meets rubric bar; no critical antipatterns.
- **FAIL** — Critical gaps (e.g. no metrics, solution-first, placeholder boxes, missing assumptions per rubric).
- **UNCERTAIN** — Borderline; human should review.
