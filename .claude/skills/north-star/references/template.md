# North Star Template

One page per product, not per team. Fill the North Star and the belief tree first. If you can't write the "because" in the belief tree, the inputs aren't ready.

```markdown
# North Star — [Product] — [Date]

**Disclaimer:** This North Star reflects our current strategy and beliefs about customer value. It will change as we learn.
**Product game:** [Attention / Transaction / Productivity] (why: [one line])
**Owner:** [name]   **Updated:** [date]   **Next review:** [date]

## North Star metric

| Element | Details |
|---|---|
| **Metric name** | [customer-value framed, e.g. "Weekly Learning Users"] |
| **Definition** | [who counts, which action, what time window] |
| **Why this metric** | [how it captures customer value and predicts the business outcome; 2–3 sentences] |
| **Business outcome it predicts** | [e.g. retention, expansion revenue] |
| **Current value (baseline)** | [number + date measured] |
| **Target (90 days)** | [number] |
| **Data source** | [event / table / dashboard] |

## Input metrics (3–5)

Repeat per input.

| Element | Details |
|---|---|
| **Input name** | [action-oriented] |
| **Definition** | [how it's measured] |
| **How it influences the North Star** | [the causal belief, with evidence] |
| **Evidence tier** | [documented / verbal / hunch / industry] |
| **Owning team** | [team] |
| **Current value** | [baseline] |
| **Target (90 days)** | [goal] |

## Guardrails (must not get worse)

| Guardrail | Current | Threshold | What we do if it's breached |
|---|---|---|---|
| [e.g. CSAT] | [4.3] | [stays > 4.0] | [pause the experiment, review] |

## Belief tree

Business outcome: [e.g. net revenue retention]
└── North Star: [metric]
    ├── Input 1: [metric] → owned by [team] → work: [initiatives]
    ├── Input 2: [metric] → owned by [team] → work: [initiatives]
    └── Input 3: [metric] → owned by [team] → work: [initiatives]

- We believe [Input 1] drives [North Star] because [reason + evidence].
- We believe [Input 2] drives [North Star] because [reason + evidence].
- We believe [North Star] drives [business outcome] because [reason + evidence].

## Work connections

| Initiative / bet | Input(s) it moves | Expected impact | Success criteria | Owner |
|---|---|---|---|---|
| | | | | |

## Review cadence
- **Weekly (15–30 min):** inputs, trends, anomalies
- **Monthly (60 min):** North Star + inputs, initiative results, tactics
- **Quarterly:** is the North Star still valid? Are the inputs still the right levers?
- **Annually:** does the North Star still match the strategy?

## The bet (for your own records)
- **Input belief this rests on most:** [belief + evidence tier]
- **Confidence the inputs move the North Star:** [%]
- **Reopen trigger:** [observable signal, e.g. "inputs at target for 2 months, North Star flat"]
```

## Worked example

| Element | Details |
|---|---|
| **North Star** | Weekly Learning Users (WLU) |
| **Definition** | Active users who shared a learning that at least two other people consumed in the last 7 days |
| **Why** | Measures value exchange rather than passive usage, reflects the collaborative-learning strategy, and connects to retention and account expansion |
| **Input** | New user activation rate: % of new signups who complete setup and run a first analysis within 7 days. 42% → 55%. Owner: Growth. Activated users are 3× more likely to become WLU within 30 days. |

| Initiative | Input it moves | Expected impact | Success criteria | Owner |
|---|---|---|---|---|
| Redesigned onboarding | New user activation | +13 pts | 42% → 55% activated within 7 days | Growth |
| Smart insight recommendations | Content discovery | +10 pts | 40% → 50% of WAU find personalized content | Core Product |
| Team collaboration features | Sharing behaviour | +6 pts | 20% → 26% of analyses shared with 2+ people | Platform |

## Writing it well

- **North Star names:** "Nights booked", "Messages sent per week", "Items received on time monthly". Not "Total registered users", "Page views", "API calls", "Features shipped".
- **Inputs:** "New user activation rate in first 7 days", "Average insights shared per active user". Not "Engagement", "Stickiness", "Adoption", "Quality".
- **Connections:** "Users who discover personalized content return 2.5× more often than those who don't". Not "Activation is important" or "Users like this".

## When to change the North Star

**Change it when** the strategy has fundamentally shifted, you now serve a different segment, the metric no longer predicts business outcomes, or it's saturated and too easy to move.

**Don't change it when** it isn't moving fast enough (that's a learning signal), you're missing targets (fix execution, not the metric), leadership wants different numbers (that's a strategy disagreement, surface it as one), or a competitor uses something else.

## Health check (quarterly)

Working: anyone can explain the North Star and their contribution; fewer prioritization fights; experiments target inputs; the North Star moves with qualitative customer feedback.

Not working: only the product team mentions it; the metric is being gamed; features ship with no input connection; the North Star moves but business outcomes don't; inputs don't correlate with the North Star; nobody has reviewed it in 6+ months.
