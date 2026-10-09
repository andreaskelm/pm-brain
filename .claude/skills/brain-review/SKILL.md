---
name: brain-review
description: Review files or folders in the PM Brain repo for quality, freshness, consistency, and system health. Slash-command style — invoke when the user explicitly asks for a repo review, context health check, or alignment pass on an initiative folder. Not for auto-invocation on casual chat.
disable-model-invocation: true
---

# Brain review (repo health)

Structured pass over **what's on disk** — not the conversation you just had (that's `evaluate-artifact`). Use when they want to know if an avatar, initiative folder, context cluster, or PM Brain setup is still true, good, and aligned.

**Invoke when:** user asks for `/brain-review`, "review this folder", "is my context stale", "health check on 1-Context", or names a specific file set.

## Step 1 — Scope

Clarify:

- **Target** — single file, artifact, initiative folder (`3-Work/[name]/`), cluster (`1-Context/`, all avatars), or **system health** (rules, ORCHESTRATION, evals).
- **Depth** — quick pass vs fix-in-session for small clear edits.

Don't load the whole repo. Read the target and its obvious neighbors.

## Step 2 — Review types (pick what fits)

Run one or combine — say which you're doing.

### Quality review — Is this artifact good?

- Load criteria via `evaluate-artifact` mapping (`.claude/skills/*/references/criteria.md` or `2-Methods/` `3-*-evaluation.md` + Quick Checks in `1-*-framework.md`).
- Gut check, red/green flags, scored rubric only if they want depth.
- Flag missing, stale, or inconsistent vs decisions elsewhere.

### Freshness review — Is this still current?

- `lastUpdated` or implicit age vs recent `5-Growth/weekly/` notes and initiative activity.
- Contradictions with newer decisions or observations.
- **`5-Growth/decisions.md` reopen triggers** — would current content fire a stored trigger?
- Company context: **`1-Context/CONTEXT-HEALTH.md`** — maintained? stale signals? contradictions with weekly/initiative logs?

### Consistency review — Does it align with the repo?

- Cross-check related initiative files, avatars, strategy, OKRs.
- Contradictions between files (avatar vs initiative notes).
- Link rot, orphaned references, duplicate content that should link instead.

### System health review — Is PM Brain working?

- `AGENTS.md` and `system/ORCHESTRATION.md` — known gaps, TODOs, contradictions.
- `system/evals/eval-results/` — patterns not fixed in rules or scenarios.
- `system/evals/scenarios/behavior/` — missing scenario types from eval logs.
- System learnings in `3-Work/[initiative]/` (e.g. pm-brain meta work) — open gaps.

**Do not** reference or load `system/MEMORY.md` — removed; routing lives in ORCHESTRATION, AGENTS, and on-demand loads.

## Step 3 — Output

Summarize in prose:

- **Solid** — what to trust as-is.
- **Update** — specific file + recommended change (not vague "refresh strategy").
- **Stale / broken** — with evidence (date, contradicting file, fired trigger).
- **Actions** — small fixes → offer to implement now; large or decision-heavy → open item in initiative or learnings folder.

## Step 4 — Capture routing (before close)

One question, one pass:

- Decision worth tracking → `5-Growth/decisions.md`?
- Pattern in thinking or blind spot → this week's `5-Growth/weekly/YYYY-Www.md`?
- System or agent gap → system learnings / relevant `3-Work/` folder?

Most reviews produce nothing for the portfolio — still ask.

## Related skills

- Fresh artifact or just finished doc → **evaluate-artifact**
- Thinking, not files → **braindump**
- Friday beliefs and decisions → **weekly-review**

## Org reality

- **Context docs as wallpaper.** Freshness review matters when nobody reads them except you before a big meeting.
- **Perfect repo fantasy.** Flag the highest-leverage stale file; don't boil the ocean.
- **Maintained? column.** `CONTEXT-HEALTH.md` tells you what you're allowed to treat as canonical — respect `Maintained?` before editing company context.
