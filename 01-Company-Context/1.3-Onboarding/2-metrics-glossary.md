## Metrics glossary (quick reference)

This is a lightweight glossary of the core metrics you will see across PM Brain and your company context. It is meant as a quick-reference surface, not a full metrics textbook.

When you need depth, examples, or formulas, follow the links into the metrics and measurement frameworks under `02-Methods-and-Tools/` (for example, strategy, OKR, and daily execution docs that talk about metrics).

### How to use this

- When a metric shows up in vision, strategy, OKRs, or roadmaps and you are not sure what it really means, find it in this table first.
- Use the \"Why it matters\" column as a fast mental handle for what the metric is a proxy for.
- If the stakes are high, click through to the linked framework sections and read the deeper guidance before you commit.

### Core product and usage metrics

| Metric | Definition (short) | Why it matters / proxy for | Typical pitfalls | Where to go deeper |
|--------|--------------------|----------------------------|------------------|--------------------|
| DAU / WAU / MAU | Count of distinct active users in a day/week/month, based on your chosen activity definition | Overall product reach and habit strength | Using logins instead of meaningful activity; ignoring quality of usage | See strategy and OKR methods under `02-Methods-and-Tools/2.1-Strategy/` for how to pick the right activity definition |
| Activation rate | Share of new users who reach a defined \"aha\" moment or activation milestone within a time window | How well onboarding and first-run experience turn signups into real users | Defining activation as shallow events (e.g. signup only); ignoring time-to-activation | Pair with discovery methods under `02-Methods-and-Tools/2.3-Execution/` to refine your activation moment |
| Conversion rate | Fraction of users who move from one funnel step to the next (e.g. visit → signup, free → paid) | Effectiveness of your funnel, pricing, and value communication | Focusing on one step in isolation; ignoring sample size and seasonality | See PRD and experiment frameworks under `02-Methods-and-Tools/2.3-Execution/` for funnel experiments |
| Retention (cohort) | Share of a cohort still active after a given time (D7, D30, M3, etc.) | Product stickiness and long-term value | Mixing cohorts; using averages that hide segment differences | Combine with roadmap and strategy docs to decide where to invest for long-term health |
| Churn rate | Share of users or accounts that stop using or cancel in a time period | Revenue and usage leakage; health of product/fit | Treating all churn as equal; ignoring reasons and segments | Use discovery and escalation frameworks when churn is concentrated in specific segments |

### Revenue and value metrics

| Metric | Definition (short) | Why it matters / proxy for | Typical pitfalls | Where to go deeper |
|--------|--------------------|----------------------------|------------------|--------------------|
| ARPU / ARPA | Average revenue per user/account over a period | Monetization effectiveness per user or account | Comparing across products with different pricing models; ignoring mix shift | Connect to strategy and pricing discussions in `02-Methods-and-Tools/2.1-Strategy/` |
| LTV (Lifetime value) | Estimated total revenue or margin you earn from a user/account over their lifetime | How valuable a customer is; how much you can spend to acquire/retain them | Using overly optimistic retention assumptions; ignoring margin and payback time | Tie this to OKR and roadmap work when deciding which segments to prioritize |
| CAC (Customer acquisition cost) | All-in cost to acquire a user/account (marketing, sales, etc.) | Efficiency of growth and go-to-market motion | Ignoring overhead; comparing CAC and LTV on mismatched time horizons | Use with LTV in strategy docs to reason about sustainable growth |

### Quality and satisfaction metrics

| Metric | Definition (short) | Why it matters / proxy for | Typical pitfalls | Where to go deeper |
|--------|--------------------|----------------------------|------------------|--------------------|
| NPS (Net Promoter Score) | Survey-based score from \"How likely are you to recommend us?\" aggregated into detractors/passives/promoters | High-level signal of user satisfaction and word-of-mouth potential | Treating it as a target in itself; overreacting to small sample sizes | See communication and discovery frameworks in `02-Methods-and-Tools/2.4-Communication/` and `2.3-Execution/` for how to use NPS feedback |
| CSAT | Short \"How satisfied were you?\" rating, often post-interaction | Point-in-time satisfaction with a feature or interaction | Asking in the wrong moments; bias from only happy/unhappy extremes | Use with support/operations docs when tuning experiences and processes |
| Error rate / incident rate | Frequency of errors, failed requests, or incidents over time | Reliability and technical quality of the product | Focusing only on severity, not frequency or user impact; hiding issues in aggregates | Connect to roadmap and escalation frameworks to prioritise reliability work |

---

If you add new metrics that show up repeatedly in company context (strategy, OKRs, roadmap), consider adding a row here with a short definition and a pointer to the deeper framework or dashboard that owns it.

