# North Star Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2, floor 0.1), weighted score × multiplier, then top 3 fixes with before/after rewrites. Rough bands: 8.0+ ready to run with, 6.0–7.9 minor refinements, 4.0–5.9 significant rework, below 4 start again from the value moment.

Gut check before scoring: "What's your gut on this North Star? What would make it obviously wrong?" Compare that answer to the score afterwards. The gaps between the two are where the learning is.

## Red flags

- **Vanity North Star** — looks good, captures no value (total registered users, page views, downloads)
- **Revenue or output as the North Star** — MRR, features shipped, experiments run; lagging or activity, not customer value
- **Unclear input → North Star links** — inputs listed with no stated belief about how they drive it
- **Not actionable** — teams can't say how their work moves an input
- **Misaligned with strategy** — the North Star rewards something the strategy doesn't bet on
- **Too many inputs** — more than 5, so nothing is really a focus
- **No work connections** — current initiatives don't map to any input
- **Unclear measurement** — no precise definition, baseline, or data source
- **Wrong product game** — e.g. a time-spent metric for a productivity tool, where less time can mean more value
- **No guardrail** — nothing says what must not break while the North Star is pushed

## Green flags

- North Star framed around value delivered, with a precise definition (who, which action, what window)
- Each input has a written belief ("we believe X drives Y because…") and an evidence tier
- Inputs owned by named teams, who can explain how their work moves them
- Strategic link stated in a sentence a skeptical exec would accept
- 3–5 inputs
- Initiatives mapped to inputs, with success criteria
- Baseline, 90-day target and data source for the North Star and each input
- Product game named, and the metric fits it
- 1–3 guardrails with thresholds

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Metric quality** | 30% | Captures customer value, predicts business outcomes, clear why it matters | Good metric, minor vanity or value-capture worries | Some value, but drifts toward activity or vanity | Vanity metric, or no link to customer value |
| **Input/output clarity** | 25% | Every input has a documented, evidenced link to the North Star | Links stated, small gaps in evidence | Some links, mostly unstated | No links, or inputs don't plausibly drive it |
| **Actionability** | 20% | Teams can move every input; work mapped; teams can explain it | Mostly actionable, minor mapping gaps | Some inputs actionable, work connections unclear | Inputs nobody can move; work unconnected |
| **Strategic alignment** | 10% | Clearly expresses the product strategy and company direction | Aligned, connection lightly argued | Alignment implied, not stated | Unconnected or contradicts strategy |
| **Scope appropriateness** | 10% | 3–5 inputs; product game right; fits team capacity | Minor concerns on count or game | More than 5 inputs or game unclear | More than 7 inputs or wrong game |
| **Measurement & operationalization** | 5% | Definition, baseline, target, dashboard; used in OKRs and roadmap | Measured, light operational use | Partly defined, no baseline or no ritual | No measurement approach |

## Antipatterns (quote the instance when you find one)

- **Metric:** vanity metric as North Star; output vs. outcome confusion (features shipped as success); no stated customer value; metric doesn't fit the product game
- **Inputs:** links undocumented; inputs that don't plausibly drive the North Star; fewer than 3 or more than 5 inputs
- **Actionability:** teams can't see their contribution; initiatives map to nothing; inputs outside the team's control (market size, seasonality)
- **Strategy:** North Star unconnected to strategic priorities; alignment assumed, never written down
- **Measurement:** no definition; no baseline or target; not used in planning (OKRs, roadmap, reviews); no guardrail
- **Structure:** one North Star per team instead of per product; a weighted composite (0.4 × WAU + 0.3 × engagement + 0.3 × revenue per user) that nobody can explain when it moves, usually a sign the team couldn't choose

## Rewrite examples

**North Star**
- Before: "Total registered users"
- After: "Weekly Learning Users: unique users who complete at least one learning activity (course completed, quiz passed, skill demonstrated) in a week. Baseline 5,000, target 10,000 in 6 months."
- Why: measures value delivered (learning) instead of a one-time activity (signing up), and it predicts retention.

**Input metric**
- Before: "Feature adoption"
- After: "New user activation rate within the first session, owned by Growth. Users who activate in the first session return weekly at 60% vs. 20% for those who don't (cohort analysis)."
- Why: specific, owned, a team can move it through onboarding, and the link to the North Star has evidence.

**Why this metric**
- Before: "It's easy to measure and our competitors use it."
- After: "It counts value exchanged between users, not logins, and in our cohort data it predicts 30-day retention and expansion revenue within 90 days."
- Why: argues customer value and prediction, not convenience or imitation.
