# Experiment Design Template

One per test that could change a ship decision. Fill what you know; mark `[unknown]` or `[GAP: …]`. Decision criteria written before launch are the part people wish they had when results are muddy.

```markdown
# [Experiment name] — Design

**Owner (PM):** [name]   **Analysis owner:** [name]   **Date:** [date]
**Status:** Designing | Running | Analyzing | Decided
**Related initiative / PRD:** [name or link in repo]

## Decision this experiment settles
[One sentence: what we will do differently based on the outcome]

## Hypothesis
We believe [change] for [who / segment] will [improve/decrease] [primary metric]
from [baseline or range] by [minimum effect we'd act on] because [mechanism / user insight].

**Evidence tier for baseline and expected lift:** documented / verbal / hunch

## Primary metric
| Metric | Definition | Baseline | MDE / target | Window |
|---|---|---|---|---|
| [one metric only] | [exactly how counted] | | | |

**Why this metric:** [tie to user outcome and decision]

## Secondary metrics (diagnostic, not deciding unless pre-stated)
| Metric | Purpose |
|---|---|
| | |

## Guardrails
| Guardrail | Pause threshold | Stop / roll back threshold |
|---|---|---|
| | | |

## Population and assignment
- **Who is in:** [eligibility rules]
- **Who is out:** [internal users, bots, regions, etc.]
- **Split:** [e.g. 50/50 control/variant] or [ramp %]
- **Assignment unit:** [user / account / device] — [how sticky]
- **Known biases / caveats:** [seasonality, concurrent launches, platform mix]

## Sample size and duration (practical)
- **Required sample / events per variant:** [from data partner or estimate]
- **Expected traffic:** [per day/week]
- **Planned runtime:** [dates] — [includes full weeks? Y/N]
- **If underpowered:** [fallback: extend / directional only / don't run]

## Implementation
- **Feature flag / config:** [name, owner, kill switch]
- **Ramp plan:** [%, gates between steps]
- **Instrumentation:** [events, dashboards]
- **QA checklist:** [assignment, tracking, rollback tested]

## Peeking and analysis plan
- **Fixed horizon or sequential rules:** [which, and who agreed]
- **Analysis method:** [simple comparison / CUPED / etc. — owner names it]
- **Segment cuts pre-planned:** [list or "none — avoid fishing"]

## Decision criteria (written before launch)
- **Ship variant if:** [primary + guardrails + practical bar]
- **Kill / keep control if:** [conditions]
- **Pivot if:** [conditions]
- **If inconclusive:** [extend with rule / revert / qualitative follow-up]
- **Decide by:** [date]

## Operational log (update during run)
| Date | Event (launch, ramp, incident, campaign) | Notes |
|---|---|---|
| | | |

## Result summary (after analysis)
- **Outcome vs criteria:** [ship / kill / pivot / inconclusive]
- **Primary metric:** control [x] vs variant [y] — [practical + statistical read in plain language]
- **Guardrails:** [clean / breached]
- **Confidence / caveats:** [% or qualitative] — [what would reopen this]
- **Next steps:** [owner → action by date]
```

## Quick prompts (when filling gaps)

- **Baseline missing?** Pull last 28 days for the same population as the test; note seasonality.
- **MDE feels huge?** The test might only detect swings you'd notice without math — say that aloud.
- **Multiple variants?** Split traffic or sequence tests; don't stack unrelated changes in one bucket.
- **Ethical / UX floor:** even "losers" should get a acceptable experience; guardrails are not optional for revenue tests on vulnerable flows.
