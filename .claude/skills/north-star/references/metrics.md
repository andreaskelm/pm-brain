# Which Metrics Matter

The North Star is the top of the tree. This file is the rest of it: the funnel, the timing of metrics, the guardrails, and how to tell a useful number from a flattering one. The test for every metric is the same: what decision would this help us make? If there isn't one, cut it.

## AARRR (pirate metrics) — where are users dropping off?

| Stage | Question | Example metrics | Common mistake |
|---|---|---|---|
| **Acquisition** | How do people find us? | Sign-ups by channel, cost per acquisition (CPA), channel quality (downstream activation and retention) | Optimizing volume over quality |
| **Activation** | Do they hit the value moment? | % reaching the activation milestone, time to first value, onboarding completion, activation by channel | Treating sign-up as activation. Users who register and never return were never activated |
| **Retention** | Do they come back? | D1 / D7 / D30 retention by cohort, WAU/MAU, DAU/MAU, churn, cohort curves | Scaling acquisition before retention is fixed |
| **Revenue** | Do they pay? | Free → paid conversion, ARPU, LTV, MRR/ARR, revenue churn, LTV:CAC | Monetizing before value is proven |
| **Referral** | Do they bring others? | Referral rate, referrals per user, referred-user activation, K-factor, referral cycle time | Forced, spammy referral programs |

Define the activation milestone per product: SaaS is setup done plus core feature used; e-commerce is first purchase; social is first post or connection; content is X pieces consumed.

How to use it:
- **Start at the biggest bottleneck,** not at Acquisition because it comes first. Don't pour users into a leaky bucket: fix retention before buying more traffic.
- **Pre-PMF:** activation and retention only. The full funnel is for after you have product-market fit.
- **1–2 metrics per stage,** tracked by cohort and by channel. Ratios over totals.
- **It's not a strict sequence.** Referral can drive activation; revenue (a paid commitment) can drive retention.
- **The North Star should span several stages.** AARRR breaks down where to push to move it.

Rough benchmarks (industry-tier evidence that varies a lot by product, so conversation starters rather than targets): 30–40%+ of sign-ups activate; D1 retention 40%+, D30 20%+; the retention curve should flatten, not decay to zero; LTV:CAC above 3:1; K above 1.0 is viral growth, below 1.0 needs paid acquisition alongside.

## Leading vs. lagging

**Lagging** metrics report results (revenue, churn, retention, market share). They validate the strategy, but by the time they move, it's too late to change the quarter. **Leading** metrics predict them, move in days or weeks, and are what teams can act on. Inputs should be leading; the North Star should lead revenue.

| Lagging (result) | Leading (predictor) | Typical head start |
|---|---|---|
| Revenue | Qualified pipeline | 30–60 days |
| Churn rate | Product engagement score | 14–30 days |
| Retention rate | Activation rate | 30–60 days |
| Customer satisfaction | Support ticket resolution time | 7–14 days |
| Market share | New user acquisition rate | 60–90 days |

**Validate the link, don't assume it.** For each leading → lagging pair, write down correlation, time lag and confidence. Example: activation rate → weekly active users, correlation 0.82, 14-day lag, high confidence; WAU → MRR, 0.87, 60 days, high; feature adoption → upgrade rate, 0.45, 30 days, medium. That last one is the input you shouldn't build a roadmap on yet. Rough portfolio balance: about 70% leading, 30% lagging.

## Guardrails

A guardrail is a metric that must not get worse while you push the North Star or an experiment metric. Goodhart's Law: when a measure becomes a target, it stops being a good measure. Guardrails are the counterweight.

Examples: North Star "weekly active users" with guardrails CSAT above 4.0/5, revenue per user not decreasing, churn under 5%. Experiment on checkout conversion with a guardrail on refund rate.

Gaming signals to watch for: the metric improves while satisfaction drops; one team's gain is another area's loss; the metric and qualitative feedback disagree; spikes that no product change explains.

## Input-metric trees

```
Business outcome:  revenue growth (lagging)
  └── North Star:  weekly active users completing a core action
        ├── Activation   (% new users running a first analysis in 7 days)  → Growth
        ├── Engagement   (analyses per active user per week)               → Core Product
        ├── Retention    (D30 retention by cohort)                          → Core Product
        └── Referral     (analyses shared with 2+ people)                   → Platform
              └── Feature / initiative metrics (time to first analysis, % finding personalized content)
```

Every arrow is a belief: "We believe activation drives WAU because activated users return 3× more often." Write the belief, its evidence tier, and decide in advance what you'll do at each level. For example, activation above 60%: scale acquisition. 50–60%: small experiments. Below 50%: stop new work and fix activation, escalate to the VP. Sanity check on sprawl, the 5-3-1 rule: 1 North Star company-wide, 3 core inputs for the product, no more than 5 key metrics per team.

## Vanity vs. actionable

| Vanity | Why it misleads | Actionable alternative |
|---|---|---|
| Total registered users | Only goes up; says nothing about value | Weekly or monthly active users |
| Page views | Activity, not value | Task completion rate, time to task |
| Downloads | Install isn't use | Daily active users |
| Email subscribers | List size, not interest | Email click-through rate |
| Social followers | No revenue link | Conversion or qualified leads from social |
| Server uptime % | System view, not user view | Error rate affecting users |
| Features shipped | Output | User problems solved |

**Vanity test.** Answer "no" to two or more and it's probably vanity: Can we take specific actions to move it? Does improving it definitely improve business outcomes? Can we reproduce the result on purpose? Does it tell us something we didn't know? Would it show bad news if things were going badly?

**Other smells:** it always goes up; leadership loves it but teams never use it; nobody can say why it's tracked; a team has more than 10 metrics; dashboards nobody opens in meetings.

Further reading: Amplitude's *North Star Playbook*; Alistair Croll and Benjamin Yoskovitz, *Lean Analytics*; Eric Ries, *The Lean Startup* (on vanity metrics).
