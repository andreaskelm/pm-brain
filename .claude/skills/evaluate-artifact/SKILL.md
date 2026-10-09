---
name: evaluate-artifact
description: Evaluate quality of a PM artifact or substantive session output using the shared evaluation procedure — gut check, red/green flags, optional full scored review. Use when the user says "evaluate this", "is this good enough", "quality check", "review the PRD/OKR/roadmap we just wrote", or after finishing an artifact. Includes end-of-session personal capture scan.
---

# Evaluate artifact

One procedure for every artifact type. What changes is only the **criteria file** — red/green flags, weighted dimensions, antipatterns, rewrites. Process, math, and output format: **`system/EVALUATION.md`** (follow it; don't improvise scoring).

Agent *behavior* evals are different: `system/evals/README.md`. This skill is for **artifacts** and **session capture**, not grading the coach.

## Step 1 — Identify what to evaluate

Ask if unclear. In practice after a substantive session, run all three dimensions — they take different time:

| Dimension | What | When |
|-----------|------|------|
| **Level 1 — Artifact** | PRD, OKR, roadmap, etc. | User points at a doc or draft in thread |
| **Level 2 — Agent behavior** | Did the coach follow PM Brain? | User wants conversation review |
| **Level 3 — Personal capture** | Decisions, assumptions, growth | End of any substantive session (always) |

## Step 2 — Map artifact → criteria file

Load the matching criteria. Prefer skill-local files when they exist; otherwise `2-Methods/` evaluation docs from `system/EVALUATION.md`.

| Artifact | Criteria path |
|----------|----------------|
| PRD | `.claude/skills/write-prd/references/criteria.md` |
| Opportunity assessment | `.claude/skills/opportunity-assessment/references/criteria.md` |
| OKR | `.claude/skills/okr/references/criteria.md` |
| Roadmap | `.claude/skills/roadmap/references/criteria.md` |
| North Star | `.claude/skills/north-star/references/criteria.md` |
| Strategy doc | `.claude/skills/strategy/references/criteria.md` |
| Prioritization output | `.claude/skills/prioritize/references/criteria.md` |
| One-pager | `.claude/skills/stakeholder-comms/references/criteria-one-pager.md` |

**No criteria file?** Use the red-flag table in `system/EVALUATION.md` plus gut check — don't invent a rubric on the fly.

## Step 3 — While creating (lightweight, if still drafting)

Scan for type-specific red flags from `system/EVALUATION.md` (OKR activity objectives, roadmap system names, PRD missing metrics, etc.). When one appears: name it, one question, suggest fix — don't silently rewrite.

Occasionally: "What feels right? What feels off?" and "Explain this to a skeptical stakeholder in two minutes."

## Step 4 — Before calling it done (quick check)

Default offer — not full scoring unless they want it or stakes are high:

- Red/green flags from criteria file
- Top 3 issues, one strength
- Gut check: skeptical engineer/exec in two minutes — what gets poked first?

**Independent review:** if `artifact-reviewer` subagent is available (mid tier, `.claude/agents/artifact-reviewer.md`), offer it. It reads artifact + criteria without conversation bias. Discuss findings in the main thread; user decides.

## Step 5 — Full evaluation (on request)

Follow **`system/EVALUATION.md`** exactly:

0. **Gut check first** — record their read before scoring.
1. **Flags** — count red/green; quality multiplier (red bands + green bonus cap).
2. **Weighted dimensions** — score 1–10 per criteria file; raw × multiplier, cap 10.
3. **Antipatterns** — quote instances from the artifact.
4. **Top 3 improvements** — before/after rewrites from real lines.
5. **Output** — use the markdown format in `system/EVALUATION.md`.
6. **Close the loop** — where gut agreed with score; what gut caught that scoring missed.

Score is a conversation starter, not a verdict. An 8/10 solving the wrong problem is still wrong.

## Step 6 — Agent behavior (Level 2, if requested)

Use "Reviewing a real conversation" in `system/evals/README.md`. Match closest scenario in `system/evals/scenarios/behavior/`; read `expected.yaml`. Flag repo fixes: rules, ORCHESTRATION, scenarios, framework gaps.

Optional: suggest a short entry for `system/evals/eval-results/` per `system/evals/eval-results/README.md`.

## Step 7 — Personal capture scan (always at session end)

Condensed from evaluate command — one pass, don't force entries:

- **Decisions** with stated confidence → `5-Growth/decisions.md` + reopen trigger?
- **Thinking / bias / updated assumption** → this week's `5-Growth/weekly/YYYY-Www.md`?
- **PM Brain friction** → system learnings in `3-Work/[initiative]/` or relevant initiative file?

Most sessions produce nothing for most targets. The point is asking.

## Step 8 — Log key findings (when doing Level 2 or meta)

Summarize: what worked, what to improve, which files to update (AGENTS, ORCHESTRATION, rules, frameworks), now vs later.

## Org reality

- **Rubric theater.** Leadership may want a number; still run gut check first or the score flatters bad strategy.
- **Author-owned PRDs.** Evaluation is for the PM's judgment, not a quality gate weapon — frame as "what I'd fix before the room."
- **No time for full eval.** Quick check is enough; offer full scoring before exec review only.
- **Reviewer as cover.** artifact-reviewer supplements; it doesn't replace ownership.

## References

- `system/EVALUATION.md` — canonical procedure and shared red-flag table
- `system/evals/README.md` — coach behavior evals
- Criteria paths in table above
