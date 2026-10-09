# OKR Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2; floor 0.1×), weighted score × multiplier, then top 3 fixes with before/after rewrites. Rating: 8–10 ready to execute · 6–7.9 minor refinements · 4–5.9 significant rework · 2–3.9 major rewrite · below 2 start over.

## Red flags

- **Project-named objectives** — "Build X", "Implement Y", "Deploy Z"
- **Milestone KRs** — "Complete Phase 1", "Launch feature", "Finish integration"
- **No baseline or target** — "Improve conversion", "Increase quality"
- **No time bound** — "Increase revenue", "Reduce costs", by when?
- **No instrumentation** — no event, query, or dashboard named for any KR
- **More than 2 objectives per team** — focus is already diluted
- **5+ KRs per objective** — it's a checklist, not a goal
- **Activity KRs** — counts effort, not effect: "Run 20 interviews", "Ship 5 features"

## Green flags

- Objectives state a business or customer outcome, not a feature or project
- KRs with baseline → target and a pass/fail threshold
- Event definitions and dashboard links for each KR
- Leading and lagging indicators mixed
- Strategic link written out (the KR → company metric ladder)
- Dependencies with owners and dates
- Confidence scoring and a weekly check-in defined

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Outcome clarity** | 30% | Objectives state business outcomes; value obvious without domain knowledge | Mostly outcomes, some activity language | Mix of outcomes and outputs; needs context to see the value | Project or activity list, no outcome |
| **KR measurability** | 25% | All KRs specific, time-bound, baseline and target; leading + lagging | Most measurable, minor gaps | Some measurable, others vague or milestones | Vague, unmeasurable, or all milestones |
| **Evidence-based approach** | 20% | Instrumentation, event definitions, thresholds, dashboards | Good measurement, small instrumentation gaps | Some measurement; thresholds or sources missing | No measurement plan |
| **Strategic alignment** | 10% | Explicit link to company goals, customer job, or strategy | Good link, minor gaps | Alignment implied, not stated | No visible connection |
| **Scope appropriateness** | 10% | 1–2 objectives, 2–4 KRs each, fits capacity | Good scope, minor feasibility doubts | Too many objectives or unrealistic KRs | Massive or clearly infeasible |
| **Dependency clarity** | 5% | Dependencies with owners, dates, mitigation | Identified, minor gaps | Noted, no detail | Not identified |

## Antipatterns (quote the instance when you find one; deduction in brackets)

- **Objectives:** project or feature delivery as the objective [−2 outcome, critical]; vague aspiration like "improve quality" [−1 outcome]; business-as-usual dressed as strategy [−0.5 outcome]; more than 2 per team [−1 scope]
- **Key results:** milestones posing as metrics [−2 measurability, critical]; subjective or unverifiable criteria [−2 measurability, critical]; no baseline [−1 measurability]; input metrics (features shipped) instead of outcome [−1 outcome]; target with no threshold [−0.5 evidence]; vanity metric that's easy to move and proves nothing, like page views [name it]
- **Process:** no instrumentation plan [−1 evidence]; no confidence scoring or check-in [−0.5 evidence]; no owners [−0.5 scope]; no link to strategy [−1 alignment]; dependencies unowned [−1 dependencies]

Severity by count: 0 minor refinements · 1–2 targeted fixes · 3–5 major rewrite · 6+ the method itself isn't being used.

## Rewrite examples

**Objective**
- Before: "Implement customer portal"
- After: "Customers resolve billing questions without contacting support." KR: support tickets from 1,200 to 720/month by end of Q3 (threshold: 900), guardrail CSAT ≥ 4.2.
- Why: the portal might be the answer, but the objective now measures the support cost it's supposed to cut.

**Key result**
- Before: "Improve API performance"
- After: "p95 API response time from 2.1s to under 1.5s by end of Q3 (threshold: 1.8s), source: APM dashboard"
- Why: baseline, target, threshold, date, and where the number comes from.

**Milestone → outcome**
- Before: "Launch new analytics dashboard"
- After: "Weekly active users of analytics features from 2,000 to 5,000 by end of Q2"
- Why: measures whether anyone uses it, not whether it shipped. The launch moves to the initiative list under this KR.
