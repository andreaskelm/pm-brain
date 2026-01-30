# Brier Score Calculation

**Purpose:** Reference for how your **Weighted Brier Score** is computed. Use a spreadsheet or the optional script to compute Overall Brier from closed rows in [forecast-log.md](forecast-log.md).

*Source: Product Judgment Test (Viveck P Kumar).*

---

## Step 1: Individual Brier Scores

For each **closed** forecast (one where you have filled Outcome):

**Brier Score = (Your Probability − Actual Outcome)²**

- **Your Probability:** Your Confidence % as a decimal (e.g. 75% → 0.75).
- **Actual Outcome:** Numeric value for the result:
  - **Exceeded** = 1.0
  - **Met** = 0.8
  - **Failed** = 0.0

**Lower is better.** 0 = perfect prediction.

**Example:**
- You predicted 75% confidence.
- Result: Met target (0.8).
- Brier = (0.75 − 0.8)² = 0.0025.

---

## Step 2: Weighting by Importance

Not all forecasts are equally important. New Products are riskier than Iterations, so they count more toward your score.

**Weight = Bet Type Weight × Novelty Weight**

**Weighted Brier = Brier Score × Weight**

### Weight Table

| Bet Type | Weight | Novelty | Weight |
|----------|--------|---------|--------|
| New Product | 3.0 | New Behavior | 1.5 |
| Expansion | 2.0 | Known Problem | 1.0 |
| Iteration | 1.0 | — | — |

**Example:**
- Brier Score = 0.0025
- Bet Type: New Product (3.0), Novelty: New Behavior (1.5)
- Weight = 3.0 × 1.5 = 4.5
- Weighted Brier = 0.0025 × 4.5 = 0.01125

---

## Step 3: Overall Brier Score

**Overall Brier = Σ(Weighted Brier) ÷ Σ(Weights)**

Sum the Weighted Brier for all closed forecasts, then divide by the sum of all Weights. This weighted average ensures high-stakes forecasts (e.g. New Products) count more than low-stakes ones (e.g. Iterations).

**Example with 4 closed forecasts:**

| Forecast | Brier | Weight | Weighted Brier |
|----------|-------|--------|----------------|
| F1 | 0.0025 | 4.5 | 0.01125 |
| F2 | 0.16 | 4.5 | 0.72 |
| F3 | 0.64 | 1.5 | 0.96 |
| F4 | 0.00 | 1.95 | 0.00 |
| **Totals** | | **12.45** | **1.69125** |

**Overall Brier = 1.69125 ÷ 12.45 ≈ 0.136**

---

## Step 4: Interpretation

Your Overall Brier Score tells you how **calibrated** your judgment is:

| Score | Interpretation |
|-------|----------------|
| **< 0.10** | Elite Judgment |
| **0.10 – 0.15** | Strong Calibration |
| **0.15 – 0.25** | Typical PM |
| **0.25 – 0.40** | Overconfident |
| **> 0.40** | Uncalibrated |

**Lower = better.** The goal is not to be right 100% of the time; it is to be **calibrated**—when you say 70% sure, you're right about 7 out of 10 times.

---

## How to Compute Your Score

1. **From [forecast-log.md](forecast-log.md):** Copy only the **closed** rows (rows where Outcome is filled).
2. **Option A – Spreadsheet:** Paste into a spreadsheet. Add columns: Outcome numeric (Exceeded=1, Met=0.8, Failed=0), Brier = (Confidence/100 − Outcome)², Weight = Bet Type × Novelty, Weighted Brier = Brier × Weight. Sum Weighted Brier and Weights; divide for Overall Brier.
3. **Option B – Script:** Run the optional Python script (see repo root or `scripts/`) that reads the forecast log and outputs per-forecast Brier and Overall Brier.

---

## FAQ

**Q: What if I only have a few closed forecasts?**  
A: Your score is still calculated the same way, but it will fluctuate more until you have 20+ closed forecasts. Keep logging predictions.

**Q: Can I game the system by only making easy predictions?**  
A: No. Harder forecasts have higher weights, so gaming doesn't work. The best way to improve is genuine calibration across all bet types.

**Q: Why weighted average instead of simple average?**  
A: In real PM work, getting a New Product prediction right matters more than an A/B test prediction. The weighting reflects that reality.
