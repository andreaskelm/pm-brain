# 5-Growth — Personal Practice & Evidence

**Purpose:** This folder is your personal product sense practice space.  
All canonical frameworks and templates live in Foundations; `5-Growth/` only stores what you actually *do* and *learn*.

Canonical Product Sense system:
- **Entry point for product thinking:** [`system/coaching/README.md`](../system/coaching/README.md) (single file: simple prompt, persona, navigation, workflow).
- Framework, prompts, evaluation, and practice templates:  
  `2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/`
- Golden Rule (braindump before structure): `system/coaching/braindump.md`

Use `5-Growth/` for:
- Daily and weekly logs
- Monthly/quarterly syntheses
- Decision and research logs
- Growth portfolio for reviews and self-reflection

---

## Modes & Privacy

Which content is tracked in git depends on your mode (Public / Private / Team).

- **Privacy / git tracking:** See [docs/setup.md](../docs/setup.md) → [Step 3: Choose Public / Private / Team Mode](../docs/setup.md#step-3-choose-public--private--team-mode) and your `.gitignore` for what to track vs. keep local.

Typical use:
- Public: everything (including `5-Growth/`) can be tracked.
- Private/Team: daily logs and detailed reflections are ignored; only shared templates/docs are committed.

---

## What Lives Here

**Root practice files**
- `1-daily-log-YYYY-QX.md` — your current quarter—s daily log (copied from the daily-log template in Product Sense Development).
- `2-prioritization-decision-log.md` — thin index of meaningful prioritization calls.
- `3-research-insight-log.md` — thin index of key research/discovery learnings.

**Learning log**
- `1-Learning-Log/[Year]-Q[#]/week-##.md` — weekly syntheses.
- `1-Learning-Log/[Year]-Q[#]/monthly-[month].md` — monthly patterns.

**Growth portfolio**
- `2-Growth-Portfolio/1-product-sense-journey.md` — long-term narrative.
- `2-Growth-Portfolio/2-decision-showcase.md` — selected decisions + outcomes.
- `2-Growth-Portfolio/3-metrics-dashboard.md` — any quantified view you want.

**Product Judgment Test**
- `3-Product-Judgment-Test/` — forecast log, Brier score, dashboard. Log predictions *before* you ship; resolve when data is in; track calibration over time.

All Product Sense structure, prompts, and exercises live in the Foundations folder above; `5-Growth/` only references them.

---

## How It Connects to the Rest of the Repo

PM Brain is a three-layer system:

```text
Layer 1 — How to Think
 Product Sense frameworks (Foundations) + your logs (5-Growth)

Layer 2 — How to Execute
 Frameworks, guides, templates in 2-Methods/

Layer 3 — What You're Building
 Initiatives and shipped work in 3-Work/
```

Typical flow for any substantial piece of work:
1. **Think first (Foundations + 5-Growth)**  
   - Braindump with Product Sense prompts (`system/coaching/prompts.md`).  
   - Capture key thoughts/decisions in `1-daily-log-YYYY-QX.md` and the thin logs.
2. **Structure second (2-Methods)**  
   - Use PRD/OKR/Opportunity frameworks in `2-Methods/` to organize thinking.
3. **Execute and reflect (Initiatives + 5-Growth)**  
   - Build under `3-Work/`.  
   - Reflect in `1-Learning-Log/` and roll important evidence into `2-Growth-Portfolio/`.

---

## Minimal Workflow

You can run this system in a very lightweight way:

- **Daily (5–10 minutes)**
  - Append a short entry to `1-daily-log-YYYY-QX.md` if you practiced or made a meaningful decision.
  - Optionally add a line to:
    - `2-prioritization-decision-log.md` (for larger prioritization bets), or
    - `3-research-insight-log.md` (for discovery/research learnings).

- **Weekly (30 minutes)**
  - Create/update a `week-##.md` file in `1-Learning-Log/[Year]-Q[#]/`.
  - Summarize decisions, patterns, and what you want to change next week.

- **Monthly (60 minutes)**
  - Add or update a `monthly-[month].md` file in `1-Learning-Log/[Year]-Q[#]/`.
  - Move 1–2 highlights into `2-Growth-Portfolio/` as long-term evidence.
  - Resolve any closed bets in `3-Product-Judgment-Test/forecast-log.md`, update the dashboard, and note your Product Judgment Test trend in your monthly synthesis.

- **Before shipping a product/feature**
  - Log a forecast in `3-Product-Judgment-Test/forecast-log.md` (prediction, confidence %, bet type, novelty). Resolve the row when the deadline passes.

All prompts, exercises, and templates you need come from the Product Sense folder in `2-Methods/`. Here you only ever copy **small slices** into your logs and portfolio.

---

## What to Commit vs Keep Local

- **Ignored (personal, noisy)**
  - `1-daily-log-*.md` — private daily notes.
  - `1-Learning-Log/20*/` — detailed reflections.
  - `self-assessment-*.md` — if you choose to create them here.

- **Committed (reusable/shared)**
  - This `README.md` and coaching templates in `4-Coaching-Templates/`.
  - Growth portfolio files if you want them versioned and shareable.

Pattern: keep raw daily/weekly thinking private, commit higher-level syntheses and structure when useful.

---

## Quick Links

- **Start a product-thinking chat (entry point)**  
  [`system/coaching/README.md`](../system/coaching/README.md) — copy the simple prompt at the top into a new chat; agent will braindump with you before any framework.
- **Product Sense framework & templates**  
  `2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/`
- **Daily log template**  
  `5-Growth/4-Coaching-Templates/8-daily-log-template.md`
- **Product Judgment Test**  
  `3-Product-Judgment-Test/` — forecast log, Brier score, dashboard (calibration tracker)
- **Golden Rule**  
  `system/coaching/braindump.md`
- **This practice space**  
  `5-Growth/`

Start simple: one daily log file, one weekly summary, one monthly check-in. You can layer on more structure later.
