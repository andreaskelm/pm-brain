# Idea validation & RAT

Test **falsifiable** beliefs before heavy build. Riskiest Assumption Testing (RAT): one assumption at a time, cheapest test that could kill the idea.

## When to use

- An opportunity or solution is on the OST and needs evidence before engineering.
- Stakeholders ask "prove it"—you still define what would count as proof.
- After synthesis points to a bet, before `opportunity-assessment` or PRD.

**Skip formal doc when** experiment is <1 week and team already agrees on metric—use a half-page note with hypothesis + threshold.

## Four lenses (hypotheses)

| Lens | Example hypothesis |
|------|-------------------|
| Desirability | Segment will [behavior] when exposed to [stimulus], metric ≥ threshold |
| Usability | Users complete [task] with ≤ N errors in ≤ T minutes |
| Feasibility | Spike shows [constraint] achievable within [limit] |
| Viability | Unit economics / channel within [bounds] |

## Process

1. Problem + audience (job/outcome language).
2. List assumptions; rate risk (H/M/L) and confidence (0–5).
3. Pick **riskiest** assumption—not easiest test.
4. Design experiment: method, primary metric, **success threshold**, sample, duration, ethics.
5. Run minimal build (fake door, concierge, prototype, spike).
6. Grade evidence strength; update confidence.
7. Decide: Proceed / Pivot / Re-test / Stop—log rationale.

## Methods by assumption type

- **Desirability:** problem interviews (past behavior), fake door, waitlist, pre-order, WTP probe, concept test.
- **Usability / value:** lo-fi prototype, usability test, wizard-of-oz, concierge.
- **Feasibility:** spike, architecture review, integration mock.
- **Viability:** cost model, channel test, legal/ops review.

## Evidence strength

- **Stronger:** revealed behavior (payment, repeat use, task completion in realistic context), multiple sources.
- **Weaker:** stated preference, hypotheticals, vanity traffic without intent.

## Artifact

**Save as:** `3-Work/[initiative]/research/validation-[idea]-[YYYY-MM-DD].md` or `4-Research/` if reusable.

Sections: meta, problem, hypotheses, assumptions table, experiment plan, results, decision, learnings, links to snapshots/OST.

## Pitfalls

- Vague hypotheses ("users will like it").
- No pre-set threshold → post-hoc rationalization.
- Over-built prototype for a learning goal.
- Single anecdote as validation.

## Connection

- Assumption nodes on OST ([problem-solution](problem-solution.md)).
- After proceed: `opportunity-assessment` or `write-prd` skill.
