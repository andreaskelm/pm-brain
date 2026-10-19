---
name: opportunity-assessment
description: Assess whether an idea or initiative is worth pursuing before a PRD, using the Opportunity Assessment framework (objective, target customer, metrics, what we know, research plan, solution ideas, risks). Use when the user asks "is this worth pursuing", "should we build this", "assess this opportunity", "opportunity assessment", "evaluate this idea before a PRD", "is this a real problem", or brings a stakeholder pet idea to sanity-check. Runs braindump/preflight before the canonical template. For raw interview notes without a named opportunity, use discovery-synthesis first.
---

# Assess an Opportunity

An opportunity assessment structures early thinking before you commit build capacity. It captures what you know, what you assume, what to research, and kill/pivot/commit criteria. The failure mode I see most is a doc written after everyone already chose the solution — a justification memo, not an assessment. The useful version could still come back **no**.

**Canonical library (load for depth, templates, and full eval):**

| Piece | Path |
|--------|------|
| Framework guide + quick quality checks | `2-Methods/3-Discovery/4-Opportunity-Assessment/1-opportunity-assessment-framework.md` |
| **Template to draft into** | `2-Methods/3-Discovery/4-Opportunity-Assessment/2-opportunity-assessment-template.md` |
| Full scored evaluation | `2-Methods/3-Discovery/4-Opportunity-Assessment/3-opportunity-assessment-evaluation.md` |
| Domain README | `2-Methods/3-Discovery/4-Opportunity-Assessment/README.md` |

Save drafts to `3-Work/[initiative]/opportunity-assessment.md`. Quick red/green flags while drafting: [references/criteria.md](references/criteria.md) (excerpt; full rubric is the `3-*-evaluation` file above).

## Is this the right thing?

**Assess when** the idea has real cost (more than a sprint or two, or a commitment someone will hold you to), and you cannot yet say with evidence who has the problem and what you'd measure.

**Don't, and say so, when:**

- The opportunity is validated and you're specifying build → `write-prd` skill.
- You have notes/interviews but no named opportunity → `discovery-synthesis` skill first.
- Several validated bets compete for capacity → `prioritize` skill.
- Reversible work under ~a week → ship and measure; skip a full assessment.

## Step 1 — Braindump and preflight (before the template)

Follow the domain README: braindump first ([system/coaching/prompts.md](../../../system/coaching/prompts.md) — discovery / early problem). Then pick 2–3 gaps:

- What outcome and **why now**? (maps to **Objective**)
- Who specifically, what job, what channel to reach them? (**Target Customer**)
- What do you know vs. guess? Name evidence tier on load-bearing claims ([evidence strength](../../../2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/7-evidence-strength.md): documented > verbal > hunch > industry).
- What would make you **kill** this?
- What are you most worried about?

Check `3-Work/[initiative]/`, `4-Research/`, `1-Context/` before re-asking. Quote what's written. If they insist on skipping: one-sentence risk, then draft with `[to fill]` / `[GAP: …]` — never invent metrics.

## Step 2 — Draft using the canonical template (section order)

Copy structure from `2-opportunity-assessment-template.md`. Work **in this order** (same as `1-opportunity-assessment-framework.md`):

1. **Objective** — outcome, business value hypothesis, time horizon, exit criteria.
2. **Target Customer** — segment + JTBD/context, stakeholders and success for each, channels/touchpoints.
3. **Success Metrics** — leading, lagging, guardrails (baseline → target → date).
4. **What We Know** — facts with sources, constraints, assumptions with **High/Med/Low** confidence (confidence in the assumption being true).
5. **What We Should Research** — questions, methods, participants/sample/timeline, **kill / pivot / commit** thresholds (written before evidence).
6. **Solution Ideas** — at least two one-liner concepts + MVP slice; **out of scope**.
7. **Risks and Questions to Validate** — use the framework taxonomy: **Desirability, Viability, Feasibility/Tech, Usability, Compliance/Legal, Dependencies, Unknowns/red flags** and how you'll de-risk. (Do not replace this with a standalone "four risks" table only — those map inside desirability/viability/feasibility/usability; compliance and dependencies are explicit in the template.)
8. **Next Steps** — owners and dates.
9. **Links & Artifacts** — research, data, decision log, discovery methods used.

Principles while filling: outcomes before solutions; living doc — update after discovery; link to discovery folders under `2-Methods/3-Discovery/` when planning research.

## Step 3 — Conduct discovery and update

Use discovery methods named in the framework (interviews, continuous discovery, JTBD, idea validation). Store artifacts in `4-Research/` or `3-Work/[initiative]/research/`. Revisit assumptions and decision criteria as evidence arrives.

## Step 4 — Decide next step

Per framework process: use decision criteria to **kill, pivot, or commit**. Commit → `write-prd` with the same metrics and constraints. Kill → log why and reopen trigger in `5-Growth/decisions.md` or initiative `decisions.md`. "Learn more" only with named test, owner, and decide-by date.

## Red flags while drafting

Scan using Quick Quality Checks in `1-opportunity-assessment-framework.md` and [references/criteria.md](references/criteria.md). Name the flag, one question, suggest the fix — don't silently rewrite.

## Before calling it done

- **Gut check:** skeptical executive in two minutes; what would make this "obviously wrong"?
- **Quick check:** red/green flags in [references/criteria.md](references/criteria.md).
- **Full evaluation** (peer review, quality gate, learning): follow `system/EVALUATION.md` and load `3-opportunity-assessment-evaluation.md` — do not improvise a shorter rubric.
- **`artifact-reviewer`:** offer for independent pass; quick check uses criteria excerpt, full eval uses the `3-*` file when requested.
- **Log the bet:** offer `5-Growth/decisions.md` row when there's a go/no-go/learn-more with confidence and reopen trigger.

## Org reality

- **CEO pet idea:** frame as de-risking — same research plan and kill criteria, evidence not opinion.
- **Already promised to a customer:** label as commitment; assess generalization (n=1).
- **No user access:** proxies (support, CS, usage); mark verbal-tier; state gap in risks.
- **Sunk cost on a prototype:** assess as if starting today; use real usage data if it exists.

## References (in skill folder)

- [references/criteria.md](references/criteria.md) — creation-time red/green flags (excerpt aligned with framework)
- [references/template.md](references/template.md) — copy of canonical template for portable installs; **prefer** `2-Methods/.../2-opportunity-assessment-template.md` in this repo
