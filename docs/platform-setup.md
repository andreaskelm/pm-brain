# Multi-Platform Setup Guide

> **tl;dr:** Bootstrap is always **AGENTS.md** + **`.cursor/rules/pm-brain.mdc`** + **system/MEMORY.md** + **USER.md** (if filled) — on every platform. Cursor auto-injects `pm-brain.mdc`; Claude Code and Copilot must read it explicitly via their entry-point checklists.

---

## Bootstrap (all platforms)

```
Load before responding (read each file in full):
1. AGENTS.md
2. .cursor/rules/pm-brain.mdc   ← enforcement (voice, lenses, braindump floor)
3. system/MEMORY.md
4. USER.md (if present)

Follow system/MEMORY.md for on-demand loading.
system/ORCHESTRATION.md loads at state entry — not bootstrap.
```

**Two-tier enforcement:** Cursor auto-injects `pm-brain.mdc` via `alwaysApply: true`. Claude Code and Copilot do **not** — their entry points ([`CLAUDE.md`](../CLAUDE.md), [`.github/copilot-instructions.md`](../.github/copilot-instructions.md)) include a compliance checklist and inline guardrails so coaching behavior survives when bootstrap reads are skipped. Same content, different wiring — see [architecture.md](architecture.md#why-pm-brainmdc-exists).

**Why a separate mdc file?** On Cursor it is the only always-on hook that does not depend on the agent choosing to read bootstrap. It overlaps AGENTS.md by design; see architecture for the tradeoff.

---

## Model Selection

**Thinking/coaching:** Mid-tier model (Sonnet-class, flagship GPT). Fast/cheap models skip braindump.

**Mechanical work (templates, bulk ops):** Fast/cheap model after thinking is done.

---

## Cursor (required setup)

The repo ships **[`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc)** — do not skip this step.

**What it does:** Cursor injects `alwaysApply: true` rules into every conversation. Without it, coaching lenses, voice, braindump floor, and minimal footprint only apply if the agent manually loads AGENTS.md.

**What it contains (enforcement, not identity):**
- 8 coaching lenses (with full upstream language)
- Voice and communication style
- Braindump sufficiency criteria (all 4)
- Minimal footprint as agent behavior
- Bootstrap reminder → AGENTS.md for persona and routing

**Verify:** Start a new Cursor chat. Agent should braindump before templates, use prose over bullets, and load context on demand — not dump the whole repo.

If you forked an older version without `pm-brain.mdc`, copy it from upstream or recreate per the file in this repo.

---

## Cursor CLI (optional — live evals)

The **Cursor IDE** (`cursor.exe`) is not the same as the **headless agent CLI** used by the eval harness for live runs (L1 rubric grading, L2 content judges). CI uses `--dry-run --skip-content` and does not need the CLI.

**Install** (Windows PowerShell):

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

macOS / Linux / WSL:

```bash
curl https://cursor.com/install -fsS | bash
```

**Verify:** `agent --version` or `cursor-agent --version` (binary name varies by install). Add the install directory to PATH if needed (often `~/.local/bin` on Unix, user-local bin on Windows).

**Authenticate:** `agent auth`, or set `CURSOR_API_KEY` from [Cursor dashboard → Integrations](https://cursor.com/dashboard?tab=integrations).

**Point the harness at your binary** if the default name does not match:

```powershell
$env:PM_BRAIN_CURSOR_BIN = "agent"   # or cursor-agent
```

Both `run_scenario.py` and `run_rubric_regression.py` honor `PM_BRAIN_CURSOR_BIN`.

**Live eval commands** (after install + auth):

```bash
pip install -r system/evals/requirements.txt
python system/evals/harness/run_rubric_regression.py --all
python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/01-braindump-floor-gate
```

Omit `--dry-run` and `--skip-content` for real agent + judge runs. Full eval docs: [system/evals/README.md](../system/evals/README.md).

---

## Other Platforms

### VS Code + GitHub Copilot

The repo ships [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) — it auto-loads as Copilot's system prompt and instructs the agent to **read** the bootstrap set in full (including `pm-brain.mdc`). Verify paths match the bootstrap block above. Copilot does not auto-inject rules files; the compliance checklist in copilot-instructions is required.

### Claude Code

The repo ships [`CLAUDE.md`](../CLAUDE.md) at repo root — Claude Code auto-discovers it. It instructs the agent to **read** the bootstrap set in full (including `pm-brain.mdc`). At session start you can also say: "Load your bootstrap set." Claude Code does not auto-inject `pm-brain.mdc`; the compliance checklist in CLAUDE.md is required.

**Private fork note:** This repo may include fork-only eval CI ([`.github/workflows/evals.yml`](../.github/workflows/evals.yml)) and the executable eval stack under [`system/evals/`](../system/evals/README.md). Upstream ships prose eval guides under `.cursor/evals/` only. On upstream merge, reconcile prose into `system/evals/`; do not blind-overwrite harness files. Full maintainer guide: [evals-fork.md](evals-fork.md).

### ChatGPT / Claude.ai

Paste the bootstrap block at the start of each chat, or save as custom instructions.

---

## Setup Steps

1. Clone or fork the repo
2. Fill in [USER.md](../USER.md)
3. **Cursor:** Confirm `.cursor/rules/pm-brain.mdc` exists (ships with repo)
4. **Other platforms:** Verify shipped wrappers (Copilot, Claude) or paste bootstrap (ChatGPT/Claude.ai)
5. Start chatting — default posture is product sense / braindump first

---

## Troubleshooting

**Skipping braindump:** Check model tier; confirm AGENTS.md loaded; in Cursor, confirm `pm-brain.mdc` exists and `alwaysApply: true`.

**Rules not loading (Cursor):** Ensure `.cursor/rules/pm-brain.mdc` is present. Reopen project or start fresh chat.

**Too much context loaded:** Agent should follow minimal footprint — load only what the conversation needs. See AGENTS.md Principle 3.

**Mid-session edits:** Re-read AGENTS.md or start fresh conversation.

**Private fork:** See [setup.md](setup.md) → [Step 3: Choose Public / Private / Team Mode](#step-3-choose-public--private--team-mode).

---

## Platform Summary

| Platform | Enforcement layer | Bootstrap (read in full) |
|----------|-------------------|--------------------------|
| Cursor | `.cursor/rules/pm-brain.mdc` auto-injected (`alwaysApply`) | AGENTS.md + pm-brain.mdc + system/MEMORY.md + USER.md |
| VS Code + Copilot | `.github/copilot-instructions.md` auto-loads + compliance checklist | Same (manual read via tool) |
| Claude Code | `CLAUDE.md` auto-discovered + compliance checklist | Same (manual read via tool) |
| ChatGPT / Claude.ai | Custom instructions | Paste bootstrap block + guardrails |
