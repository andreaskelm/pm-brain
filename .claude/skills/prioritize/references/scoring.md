# Scoring Methods

Scores organize judgment; they don't replace it. Write the assumption behind every number, because the assumption is what people will argue about, and it's what you'll check later.

## RICE — bigger bets, some data

**Score = (Reach × Impact × Confidence) ÷ Effort**

| Factor | What it means | Scale |
|---|---|---|
| **Reach** | People or events affected per period (usually per quarter). Real numbers, not T-shirt sizes. Account for adoption: not everyone who *could* see it will. | e.g. 500 signups/mo × 80% see the change = 1,200/quarter |
| **Impact** | How much each person moves the metric you care about | 3 massive · 2 high · 1 medium · 0.5 low · 0.25 minimal |
| **Confidence** | How sure you are about R, I and E together | 100% strong data / proven · 80% some data · 50% mostly assumption |
| **Effort** | Total person-months across all functions (PM, design, eng, QA) | 0.5 < 2 weeks · 1 ≈ month · 2–3 a quarter · 5+ major · 10+ multi-quarter |

**Worked example**

| Initiative | Reach/qtr | Impact | Confidence | Effort | Score |
|---|---|---|---|---|---|
| Dark mode | 80,000 | 1 | 0.8 (survey data) | 2 | 32,000 |
| AI recommendations | 150,000 | 2 | 0.5 (untested) | 6 | 25,000 |

Dark mode wins *on these numbers*. The interesting conversation is about the 0.5. What would it take to move AI recommendations to 0.8, and is that test cheaper than building dark mode?

**Rationale quality:** "Reach: 5,000 enterprise users, 90% adoption = 4,500/qtr" beats "big reach". "Impact 3: directly addresses #1 churn reason (12 of 15 exit interviews)" beats "high impact". If the rationale is "leadership wants this" or "competitors have it", that's not a score. That's the political conversation the score is hiding.

## ICE — quick calls, early ideas, growth experiments

**Score = Impact × Confidence × Ease** (each 1–10). Some teams average instead of multiply. Pick one and stay consistent, because mixing them is how scores get gamed.

Impact: 10 transformative → 1 low. Confidence: 10 proven → 1 gut feel. Ease: 10 hours → 1 months.

Use ICE to triage many items fast, then re-score the top handful with RICE.

## Impact–Effort matrix — workshops, alignment, first pass (30–45 min)

Plot items as a group: impact on Y, effort on X. Timebox discussion per item.

| | Low effort | High effort |
|---|---|---|
| **High impact** | Quick wins: do first | Big bets: do next, deliberately |
| **Low impact** | Fill-ins: when capacity allows | Money pits: cut, and ask why they exist |

Variations: use *complexity* instead of effort when estimates are fuzzy; add a red/amber/green dot for confidence and revisit the red ones with better data. The real output is the **assumptions** that surfaced when people disagreed about placement. Write those down.

## Bugs — severity × frequency

| Severity → / Frequency ↓ | Critical (10) | High (7) | Medium (5) | Low (2) |
|---|---|---|---|---|
| **Everyone (100%)** | P0 | P1 | P1 | P2 |
| **Many (50%)** | P1 | P1 | P2 | P3 |
| **Some (10%)** | P2 | P2 | P3 | P4 |
| **Few (1%)** | P3 | P4 | P4 | P5 |

P0 drop everything · P1 this sprint · P2 next sprint · P3 normal backlog · P4–P5 when convenient or won't fix. Critical = data loss, security, complete blocker. Keep real P0s under ~5% of the backlog.

## Which method by item type

| Item | Method |
|---|---|
| Strategic initiative (months) | RICE |
| Feature (weeks) | ICE, then RICE for the top items |
| Improvement / tech debt | Impact–Effort, or Value–Complexity |
| Bug | Severity × frequency |
| Fuzzy item | Define it better first. You can't score what you can't describe |

## Portfolio balance (after scoring, not instead of it)

Rough starting point, adjust to context: ~70% committed/high-confidence work, ~20% medium-confidence bets, ~10% experiments; and reserve 10–20% of capacity for tech debt *before* the scoring starts. Otherwise it never scores high enough to win. Also check: does the top 20 reflect your OKR distribution? Are you over-serving one segment?

## Calibrating your scores

Once a quarter, compare predicted impact against what actually happened for the 3–5 items you shipped. If your "Impact 3" items consistently land as 1s, your scale is inflated, and you now have evidence instead of a feeling.
