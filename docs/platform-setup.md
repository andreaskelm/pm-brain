# Multi-Platform Setup Guide

> **tl;dr:** Bootstrap is always **AGENTS.md** + **system/MEMORY.md** + **USER.md** (if filled). In Cursor, **pm-brain.mdc** is required — it enforces coaching lenses, voice, and braindump floor at the platform level.

---

## Bootstrap (all platforms)

```
Load before responding:
1. AGENTS.md
2. system/MEMORY.md
3. USER.md (if present)

Follow system/MEMORY.md for on-demand loading.
system/ORCHESTRATION.md loads at state entry — not bootstrap.
```

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

The repo ships [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) — verify the bootstrap block matches the section above. Note: no always-on lens enforcement — rely on AGENTS.md content.

### Claude Code

The repo ships [`CLAUDE.md`](../CLAUDE.md) at repo root with the bootstrap block above — verify it matches. At session start say: "Load your bootstrap set."

**Private fork note:** This repo may include fork-only eval CI ([`.github/workflows/evals.yml`](../.github/workflows/evals.yml)) and the executable eval stack under [`system/evals/`](../system/evals/README.md). Upstream ships prose eval guides under `.cursor/evals/` only. On upstream merge, reconcile prose into `system/evals/`; do not blind-overwrite harness files.

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

| Platform | Enforcement layer | Bootstrap |
|----------|-------------------|-----------|
| Cursor | `.cursor/rules/pm-brain.mdc` (required, ships with repo) | AGENTS.md + system/MEMORY.md + USER.md |
| VS Code + Copilot | `.github/copilot-instructions.md` (ships with repo; verify bootstrap) | Same |
| Claude Code | `CLAUDE.md` (ships with repo; verify bootstrap) | Same + manual prompt |
| ChatGPT / Claude.ai | Custom instructions | Paste bootstrap block |
