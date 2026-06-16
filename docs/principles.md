# PM Brain Principles

> **Why this repo is designed the way it is.** Agent enforcement lives in [AGENTS.md](../AGENTS.md). Deep coaching process: [system/coaching/](../system/coaching/).

---

## 1. Golden Record & Minimal Footprint

This repo is the **single source of truth** for product decisions, frameworks, and synthesized knowledge — not a full archive.

**Link, don't duplicate.** Store structure, decisions, and summaries here. Link out to Confluence, Notion, dashboards, Figma, recordings.

**Agent rules:** AGENTS.md Principles 2–3 — storage SSoT (link don't duplicate) and response discipline (load only what the conversation needs).

**Examples:**
- Research summaries in `4-Research/`; raw recordings external
- Metrics definitions here; live dashboards linked
- Design decisions in `3-Work/`; Figma linked

---

## 2. Where Things Go

| Content | Folder |
|---------|--------|
| Company vision, strategy, stakeholders | `1-Context/` |
| Frameworks, templates, playbooks | `2-Methods/` |
| Active bets, PRDs, roadmaps | `3-Work/` |
| Research evidence | `4-Research/` |
| Personal practice, logs, PJT | `5-Growth/` |
| Agent infrastructure | `system/` |

**Coaching process** → `system/coaching/` (how the agent runs braindump sessions)  
**PM mental models** → `2-Methods/1-Foundations/` (reference content the coaching draws from)

---

## 3. Think First, Then Structure

**The golden rule:** Braindump before structure. Enforced in AGENTS.md Principle 1.

- **Deep sessions:** [system/coaching/README.md](../system/coaching/README.md) → [braindump.md](../system/coaching/braindump.md) + [prompts.md](../system/coaching/prompts.md)
- **Doc requests:** 2–3 preflight questions still required — lenses never go dormant
- **Bad pattern:** "Write my PRD" with no thinking → agent should push back lightly first

---

## 4. Using AI with This Repo

**Good:** "Help me think through X" — braindump before template — challenge assumptions  
**Bad:** Jump straight to templates — fill boxes without revisiting — duplicate content across files

Setup: [setup.md](setup.md) — enforcement via `.cursor/rules/pm-brain.mdc` on **all platforms** (Cursor auto-injects; Claude Code and Copilot read it via bootstrap checklists in [platform-setup.md](platform-setup.md))

---

## 5. Privacy & Health

Keep sensitive company detail in private forks. Update `1-Context/` when reality changes. Archive stale initiatives to `3-Work/99-Archive/`. Document decisions in initiative `decisions.md`.

Git history is the version history — no separate version file required.

---

## Quick Checklist

- [ ] Braindump or preflight done?
- [ ] Right folder for this content?
- [ ] Can I link instead of duplicate?
- [ ] Commit scoped to one concern?
