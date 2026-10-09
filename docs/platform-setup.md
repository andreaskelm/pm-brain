# Multi-Platform Setup Guide

> **tl;dr:** One always-on file — [`AGENTS.md`](../AGENTS.md) — which Cursor, Claude Code (v2.1.277+), and VS Code Copilot all load natively. Skills live in [`.claude/skills/`](../.claude/skills/) and subagents in [`.claude/agents/`](../.claude/agents/); all three platforms read those folders. No per-platform wrapper files.

---

## How the agent is wired

| Layer | Path | Loaded |
|-------|------|--------|
| Persona, voice, lenses, principles, wake table, tier policy | `AGENTS.md` | Always (native) |
| Personal context | `USER.md` | First response (AGENTS.md tells the agent to read it) |
| State behavior | `system/ORCHESTRATION.md` | At state transitions |
| Deep coaching loop | `system/coaching/` | Entering product thinking |
| Workflows (PRD, OKR, prioritization, weekly review…) | `.claude/skills/*/SKILL.md` | When the request matches the skill description, or `/skill-name` |
| Subagents | `.claude/agents/*.md` | When the main agent delegates |
| Reference (mental models, bias, org-reality guides) | `2-Methods/` | On demand via skills or the wake table |

---

## Model Tiers

Behavior files name **tiers**, never models. This table is the only place model names live — update it when the landscape shifts.

**Last checked: 2026-10.** My read from daily use, not a benchmark — swap freely.

| Tier | Job | Cursor | Claude Code | VS Code Copilot |
|------|-----|--------|-------------|-----------------|
| **Top** | The coaching conversation; voice-sensitive writing; deciding what to keep when trimming | Claude Opus 5.5, Claude Fable 5.1, GPT-5.6 Sol | `opus` / `fable` | Strongest Claude or GPT in the picker |
| **Mid** | Independent review (`artifact-reviewer`); drafting artifacts after the braindump | Claude Sonnet 5.5, GPT-5.6 Sol (medium) | `sonnet` | Sonnet-class |
| **Fast** | Repo scans (`context-scout`), bulk renames, link fixes | Composer 2.5 (fast), Claude Haiku 5.5, Gemini 3.8 Flash | `haiku` | Fastest in the picker |

**Rule of thumb:** fast models tend to skip the braindump and flatten the voice. Run coaching on the top tier; push mechanical work down.

**Subagent models.** The shared files in `.claude/agents/` use `model: inherit`, because model values don't translate across platforms (Claude aliases like `haiku` aren't Cursor model IDs). To pin a cheaper model:

- **Claude Code:** set `model: haiku` (or `sonnet`) in the agent's frontmatter, or `CLAUDE_CODE_SUBAGENT_MODEL`.
- **Cursor:** add a local `.cursor/agents/<same-name>.md` copy with a Cursor model ID — it overrides the `.claude/agents/` file on name conflict. Keep it out of upstream PRs.

---

## Cursor

Nothing to configure. Cursor loads `AGENTS.md` as an always-on rule, discovers skills in `.claude/skills/` and subagents in `.claude/agents/`.

**Verify:** start a new chat and say "I'm stuck on prioritization." The agent should braindump before suggesting any framework, talk in prose, and name a lens in passing.

**Hooks** ([`.cursor/hooks.json`](../.cursor/hooks.json)): `postToolUse` runs [`system/evals/hooks/validate_write.py`](../system/evals/hooks/validate_write.py), which blocks template scaffolds written into `3-Work/` without any thinking markers. Cursor-only.

## Claude Code

Claude Code v2.1.277+ reads `AGENTS.md` natively **when there is no `CLAUDE.md`** — so the repo ships none. Skills in `.claude/skills/` appear as `/skill-name`; subagents in `.claude/agents/`.

**Older Claude Code** (or sessions that can't read `AGENTS.md` natively): create a one-line `CLAUDE.md` at the repo root containing `@AGENTS.md`. Don't commit it upstream. Check what loaded with `/memory`.

New or edited skills and subagents become visible at the **next session start**, not mid-session.

## VS Code + GitHub Copilot

Copilot reads `AGENTS.md` and project skills in `.claude/skills/`. Pick a top-tier model for coaching.

**Mid-session rule edits:** changes to `AGENTS.md` or skills don't take effect in the running conversation. Say "re-read AGENTS.md" or start a fresh chat.

**Commits:** VS Code's Sync button bypasses the `.gitmessage` template — commit from the terminal if you want the template.

## ChatGPT / Claude.ai / Gemini

Paste `AGENTS.md` (and `USER.md`) into the project's custom instructions. For a workflow, paste the relevant `SKILL.md` plus its `references/` files.

---

## Live evals (optional)

The eval harness can run real agent turns through the headless Cursor CLI. Install:

```powershell
irm 'https://cursor.com/install?win32=true' | iex   # Windows
```

```bash
curl https://cursor.com/install -fsS | bash          # macOS / Linux / WSL
```

Verify with `agent --version` (or `cursor-agent --version`), authenticate with `agent auth` or `CURSOR_API_KEY`, and point the harness at your binary if needed: `PM_BRAIN_CURSOR_BIN=agent`. Commands and scenarios: [system/evals/README.md](../system/evals/README.md).

---

## Troubleshooting

**Skipping the braindump:** check the model tier first. Then confirm `AGENTS.md` is loading (Claude Code: `/memory`; Cursor: Customize → Rules).

**Claude Code ignores AGENTS.md:** a `CLAUDE.md` exists somewhere from the repo root down to your working directory, or Claude Code is older than 2.1.277.

**Too much context loaded:** the agent should follow minimal footprint (AGENTS.md principle 3) and delegate scans to `context-scout`.

**Private fork:** see [setup.md](setup.md) → Step 3 (public / private / team mode).
