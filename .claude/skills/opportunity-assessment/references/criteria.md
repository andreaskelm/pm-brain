# Opportunity Assessment Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2), weighted score × multiplier, then top 3 fixes with before/after rewrites. Rough reading of the final score: 8+ ready for discovery or a PRD, 6–8 minor refinements, 4–6 significant gaps, under 4 rethink it.

## Red flags

- **No clear hypothesis** — the opportunity statement is vague or missing
- **Solution bias** — opens with the feature before the problem
- **Vague opportunity** — too broad to test, or not sized at all
- **No customer context** — "users" in general; no segment, situation, or job
- **Assumptions not identified** — no list, no confidence levels, facts and guesses mixed
- **Missing evidence plan** — no method, participants, or timeline for validation
- **Missing decision criteria** — no kill / pivot / commit thresholds
- **Missing success metrics** — no baseline, target, or guardrail

## Green flags

- A problem hypothesis that names who, what pain, and what outcome changes
- Sizing (who / how many / how painful) with the evidence tier visible
- Assumptions with confidence levels and "what would change our mind"
- One riskiest assumption named, with a cheap test, owner and date
- All four risks covered, and value risk not waved through
- Kill / pivot / commit thresholds written before the evidence arrives
- At least two solution concepts, kept to one-liners
- An explicit call (go / no-go / learn more) with a reopen trigger

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Hypothesis clarity** | 25% | Specific problem and outcome; obvious why it matters and why now | Mostly clear, minor gaps in specificity | Present but vague; needs domain knowledge to see the value | No hypothesis, or a solution dressed as one |
| **Assumption identification** | 20% | All key assumptions with confidence; facts vs. guesses separated; what would change our mind | Most identified, small gaps in confidence | Some listed, key ones or confidence missing | Hidden; can't tell known from assumed |
| **Evidence plan** | 20% | Methods, participants, sample size, timeline; kill/pivot/commit thresholds | Good plan, minor gaps in method or thresholds | Vague methods or no decision criteria | "Talk to some users" or nothing |
| **Customer & strategic fit** | 15% | Specific segment and job; clear link to strategy; stakeholder impact understood | Good customer definition, small gaps in job or fit | Customer vague or no strategic link | No target customer, no fit |
| **Success metrics & opportunity size** | 15% | Baselines, targets, guardrails; size estimated (revenue, time, risk) | Small gaps in baselines or sizing | Some metrics, no baselines or size | Purely qualitative |
| **Risk assessment** | 5% | Value, usability, feasibility, viability (incl. compliance) each with a test or mitigation | Minor gaps in coverage or mitigation | Partial coverage, e.g. feasibility only | Not assessed |

## Antipatterns (quote the instance when you find one)

- **Hypothesis:** no hypothesis; solution bias; scope too broad to test; features listed where outcomes should be
- **Assumptions:** none listed; no confidence levels; facts and hypotheses mixed; no "what would change our mind"
- **Evidence plan:** no plan; no kill/pivot/commit thresholds; vague methods (no participants or sample size); no timeline or decide-by date
- **Customer:** no customer; segment so broad it's everyone; no connection to strategy or business goals
- **Metrics & size:** no metrics; no baselines or targets; no sizing at all; sizing that's industry-tier presented as fact
- **Risks:** not assessed; feasibility only, value assumed; risks listed with no test or mitigation

## Rewrite examples

**Hypothesis**
- Before: "Build an alert system"
- After: "Ops teams spend ~30 min/day manually triaging alerts; 80% are false positives (documented: survey of 50 teams). Opportunity: cut triage time 75% through automated prioritization, roughly 2.5 hours/week back per person."
- Why: problem and outcome first, sized, evidence tier visible; the alert system might not even be the answer.

**Assumption**
- Before: "We assume teams want better alerts"
- After: "Assumption: 70% of ops teams spend >20 min/day on triage (High: 72% in a survey of 50 teams). Assumption: we can score alerts accurately enough to auto-dismiss (Low: untested). What would change our mind: fewer than 30% of interviewees report >20 min/day."
- Why: specific, confidence-marked, separates the solid assumption from the risky one, and says what would falsify it.

**Evidence plan and kill criteria**
- Before: "Talk to some users"
- After: "30-min interviews with 10 ops team members (2 per team, 5 teams) over 2 weeks. Kill if fewer than 30% report >20 min/day triage. Pivot if the pain is something other than time. Commit to a PRD if 70%+ report it and want automated prioritization."
- Why: method, sample, timeline, and thresholds set before anyone hears an answer they like.
