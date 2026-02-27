## Product Judgment Test – Brier Calculation

This file makes the scoring math fully transparent so you can:
- Do it by hand with a basic calculator, or
- Recreate the exact same logic in Excel/Google Sheets.

No scripts are required.

---

## 1. Inputs You Need per Forecast

For each **closed** forecast (row) in your `forecast-log.md`, you need:

- **Confidence %** — what you logged before shipping (0–100).
- **Bet Type** — `New Product`, `Expansion`, or `Iteration`.
- **Novelty** — `New Behavior` or `Known Problem`.
- **Outcome** — once resolved: `Exceeded`, `Met`, or `Failed`.

Those four things are enough to compute:
- A **Brier score** per forecast.
- A **weight** per forecast.
- A **Weighted Brier** per forecast.

---

## 2. Map Outcome to a Numeric Value

Outcomes are mapped to a numeric value between 0 and 1:

- `Exceeded` → **1.0**
- `Met` → **0.8**
- `Failed` → **0.0**

Call this numeric value **Outcome Value**.

---

## 3. Convert Confidence % to Probability

Take your **Confidence %** and convert it to a probability:

- If Confidence % is `75`, then  
  \\( p = 75 / 100 = 0.75 \\)

In general:

\\[
p = \\text{Confidence %} / 100
\\]

---

## 4. Per‑Forecast Brier Score

For each forecast, compute the **Brier score**:

\\[
\\text{Brier} = (p - \\text{Outcome Value})^2
\\]

Where:
- \\( p \\) is your confidence as a probability (0–1).
- **Outcome Value** is 1.0, 0.8, or 0.0 (from Section 2).

This penalizes both **being wrong** and **being overconfident**.

---

## 5. Weights (Bet Type × Novelty)

High‑leverage bets should count more in your overall score.

### 5.1 Bet Type Weights

- `New Product` → **3.0**
- `Expansion` → **2.0**
- `Iteration` → **1.0**

### 5.2 Novelty Weights

- `New Behavior` → **1.5**
- `Known Problem` → **1.0**

### 5.3 Weight per Forecast

For each forecast:

\\[
\\text{Weight} = \\text{Bet Type Weight} \\times \\text{Novelty Weight}
\\]

Examples:

- New Product × New Behavior → \\( 3.0 \\times 1.5 = 4.5 \\)
- Expansion × Known Problem → \\( 2.0 \\times 1.0 = 2.0 \\)
- Iteration × Known Problem → \\( 1.0 \\times 1.0 = 1.0 \\)

---

## 6. Weighted Brier per Forecast

For each closed forecast, compute:

\\[
\\text{Weighted Brier} = \\text{Brier} \\times \\text{Weight}
\\]

You’ll use this to aggregate across all forecasts.

---

## 7. Overall Weighted Brier Score

Once you’ve computed **Weighted Brier** and **Weight** for all closed forecasts:

\\[
\\text{Overall Brier} =
\\frac{
\\sum \\text{Weighted Brier}
}{
\\sum \\text{Weight}
}
\\]

In words:
- Add up **all** Weighted Brier values.
- Add up **all** Weights.
- Divide total Weighted Brier by total Weight.

This is the single number you record in `dashboard.md`.

---

## 8. Interpretation Bands

Use the Overall Brier Score to categorize your calibration:

- **Elite Judgment** → Overall Brier **< 0.10**
- **Strong Calibration** → Overall Brier **< 0.15**
- **Typical PM** → Overall Brier **< 0.25**
- **Overconfident** → Overall Brier **< 0.40**
- **Uncalibrated** → Overall Brier **≥ 0.40**

Lower is better. Elite/Strong bands usually require a **decent number of bets** (10–20+) before you trust the signal.

---

## 9. Worked Example

Imagine this resolved forecast:

- Confidence %: **70**
- Bet Type: **Expansion**
- Novelty: **Known Problem**
- Outcome: **Met**

Step by step:

1. **Outcome Value**  
   - Outcome = `Met` → Outcome Value = **0.8**.

2. **Probability from Confidence %**  
   - Confidence % = 70 → \\( p = 70 / 100 = 0.7 \\).

3. **Brier score**  
   \\[
   \\text{Brier} = (p - \\text{Outcome Value})^2
   = (0.7 - 0.8)^2
   = (-0.1)^2
   = 0.01
   \\]

4. **Weight**  
   - Bet Type = Expansion → Bet Type Weight = **2.0**.  
   - Novelty = Known Problem → Novelty Weight = **1.0**.  
   - Weight = 2.0 × 1.0 = **2.0**.

5. **Weighted Brier**  
   \\[
   \\text{Weighted Brier} = 0.01 \\times 2.0 = 0.02
   \\]

When you aggregate:
- Add 0.02 to your **total Weighted Brier**.
- Add 2.0 to your **total Weight**.

Overall Brier will be:

\\[
\\text{Overall Brier} =
\\frac{\\text{Total Weighted Brier}}{\\text{Total Weight}}
\\]

Use that single number to:
- Update `dashboard.md` (Overall Brier).
- Pick the **Interpretation** band from Section 8.

That’s all the math—everything else is just copying these steps into a sheet or calculator.

