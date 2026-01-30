# 00-Meta – Personal Practice & Evidence

**Purpose:** This folder is your personal product sense practice space.  
All canonical frameworks and templates live in Foundations; `00-Meta/` only stores what you actually *do* and *learn*.

Canonical Product Sense system:
- Framework, prompts, evaluation, and practice templates:  
  `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/`
- Golden Rule (braindump before structure): `PRODUCT-SENSE-RULES.md`

Use `00-Meta/` for:
- Daily and weekly logs
- Monthly/quarterly syntheses
- Decision and research logs
- Growth portfolio for reviews and self-reflection

---

## Modes & Privacy

Which content is tracked in git depends on your mode (Public / Private / Team).

- **Mode selection guide:** see `00-Meta/MODE-SELECTION-GUIDE.md` for:
  - What each mode means
  - Which paths are ignored via `.gitignore`
  - How to switch modes safely

Typical use:
- Public: everything (including `00-Meta/`) can be tracked.
- Private/Team: daily logs and detailed reflections are ignored; only shared templates/docs are committed.

---

## What Lives Here

**Root practice files**
- `1-daily-log-YYYY-QX.md` – your current quarter’s daily log (copied from the daily-log template in Product Sense Development).
- `2-prioritization-decision-log.md` – thin index of meaningful prioritization calls.
- `3-research-insight-log.md` – thin index of key research/discovery learnings.

**Learning log**
- `0.1-Learning-Log/[Year]-Q[#]/week-##.md` – weekly syntheses.
- `0.1-Learning-Log/[Year]-Q[#]/monthly-[month].md` – monthly patterns.

**Growth portfolio**
- `0.2-Growth-Portfolio/1-product-sense-journey.md` – long-term narrative.
- `0.2-Growth-Portfolio/2-decision-showcase.md` – selected decisions + outcomes.
- `0.2-Growth-Portfolio/3-metrics-dashboard.md` – any quantified view you want.

**Product Judgment Test**
- `0.3-Product-Judgment-Test/` – forecast log, Brier score, dashboard. Log predictions *before* you ship; resolve when data is in; track calibration over time.

All Product Sense structure, prompts, and exercises live in the Foundations folder above; `00-Meta/` only references them.

---

## How It Connects to the Rest of the Repo

PM Brain is a three-layer system:

```text
Layer 1 – How to Think
  Product Sense frameworks (Foundations) + your logs (00-Meta)

Layer 2 – How to Execute
  Frameworks, guides, templates in 02-Methods-and-Tools/

Layer 3 – What You're Building
  Initiatives and shipped work in 04-Initiatives/
```

Typical flow for any substantial piece of work:
1. **Think first (Foundations + Meta)**  
   - Braindump with Product Sense prompts (`2-product-sense-template.md`).  
   - Capture key thoughts/decisions in `1-daily-log-YYYY-QX.md` and the thin logs.
2. **Structure second (Methods & Tools)**  
   - Use PRD/OKR/Opportunity frameworks in `02-Methods-and-Tools/` to organize thinking.
3. **Execute and reflect (Initiatives + Meta)**  
   - Build under `04-Initiatives/`.  
   - Reflect in `0.1-Learning-Log/` and roll important evidence into `0.2-Growth-Portfolio/`.

---

## Minimal Workflow

You can run this system in a very lightweight way:

- **Daily (5–10 minutes)**
  - Append a short entry to `1-daily-log-YYYY-QX.md` if you practiced or made a meaningful decision.
  - Optionally add a line to:
    - `2-prioritization-decision-log.md` (for larger prioritization bets), or
    - `3-research-insight-log.md` (for discovery/research learnings).

- **Weekly (30 minutes)**
  - Create/update a `week-##.md` file in `0.1-Learning-Log/[Year]-Q[#]/`.
  - Summarize decisions, patterns, and what you want to change next week.

- **Monthly (60 minutes)**
  - Add or update a `monthly-[month].md` file in `0.1-Learning-Log/[Year]-Q[#]/`.
  - Move 1–2 highlights into `0.2-Growth-Portfolio/` as long-term evidence.
  - Resolve any closed bets in `0.3-Product-Judgment-Test/forecast-log.md`, update the dashboard, and note your Product Judgment Test trend in your monthly synthesis.

- **Before shipping a product/feature**
  - Log a forecast in `0.3-Product-Judgment-Test/forecast-log.md` (prediction, confidence %, bet type, novelty). Resolve the row when the deadline passes.

All prompts, exercises, and templates you need come from the Product Sense folder in `02-Methods-and-Tools/`. Here you only ever copy **small slices** into your logs and portfolio.

---

## What to Commit vs Keep Local

- **Ignored (personal, noisy)**
  - `1-daily-log-*.md` – private daily notes.
  - `0.1-Learning-Log/20*/` – detailed reflections.
  - `self-assessment-*.md` – if you choose to create them here.

- **Committed (reusable/shared)**
  - This `README.md` and `MODE-SELECTION-GUIDE.md`.
  - Growth portfolio files if you want them versioned and shareable.

Pattern: keep raw daily/weekly thinking private, commit higher-level syntheses and structure when useful.

---

## Quick Links

- **Product Sense framework & templates**  
  `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/`
- **Daily log template**  
  `6-Product-Sense-Development/templates/daily-log-template.md`
- **Product Judgment Test**  
  `0.3-Product-Judgment-Test/` – forecast log, Brier score, dashboard (calibration tracker)
- **Golden Rule**  
  `PRODUCT-SENSE-RULES.md`
- **This practice space**  
  `00-Meta/`

Start simple: one daily log file, one weekly summary, one monthly check-in. You can layer on more structure later.
