# Product Judgment Test – Forecast Log

**Purpose:** Record your predictions *before* you ship. Resolve rows when the deadline passes and data is in.

**Workflow:** Log forecast (2 min) → Classify (Bet Type + Novelty) → When deadline hits: fill Resolution columns (5 min) → Update [dashboard.md](dashboard.md) monthly.

---

## Bet Type and Novelty (Weights)

Weights are used to compute your **Weighted Brier Score**. High-stakes bets count more. See [BRIER-CALCULATION.md](BRIER-CALCULATION.md) for the full table and formula.

| Bet Type | Weight | Novelty | Weight |
|----------|--------|---------|--------|
| New Product | 3.0 | New Behavior | 1.5 |
| Expansion | 2.0 | Known Problem | 1.0 |
| Iteration | 1.0 | — | — |

**Weight for a forecast** = Bet Type Weight × Novelty Weight (e.g. New Product × New Behavior = 3.0 × 1.5 = 4.5).

---

## Forecast Log

**Instructions:**
- **Forecast columns:** Fill *before* you ship. Be specific: metric must be numeric (e.g. "Increase Task Completion from 60% to 70%").
- **Confidence %:** 0–100. 50% = coin flip; 70% = some evidence, risks; 90% = almost certain (wrong at 90% = big Brier hit).
- **Resolution columns:** Fill when the deadline has passed and you have actual data. Outcome: Exceeded | Met | Failed.

| Date | Bet | Metric (target) | Deadline | Confidence % | Bet Type | Novelty | Target | Actual | % of Target | Outcome | Surprise note |
|------|-----|-----------------|----------|-------------|----------|---------|--------|--------|------------|---------|----------------|
| *(example)* | New checkout flow | Task completion 60% → 70% | 2026-02-28 | 75 | Iteration | Known Problem | 70 | — | — | — | — |
| *(example resolved)* | Signup step removal | Signup completion 40% → 55% | 2026-01-15 | 70 | Iteration | Known Problem | 55 | 58 | 105 | Exceeded | Users completed faster than expected; fewer drop-offs at step 2. |

*(Add your rows below. Leave Resolution columns blank until the deadline.)*

| Date | Bet | Metric (target) | Deadline | Confidence % | Bet Type | Novelty | Target | Actual | % of Target | Outcome | Surprise note |
|------|-----|-----------------|----------|-------------|----------|---------|--------|--------|------------|---------|----------------|
| | | | | | | | | | | | |
