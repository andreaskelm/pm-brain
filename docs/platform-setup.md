# Multi-Platform Setup Guide

> **tl;dr:** PM Brain works on multiple platforms (Cursor, VS Code, Claude Code, ChatGPT, Claude.ai). Each loads configuration differently. This guide tells you exactly what to do on your platform.

---

## Model Selection

Pick this once, apply everywhere.

**For thinking and coaching conversations (default):** Use a mid-tier model — Sonnet-class (Claude), flagship (GPT), or equivalent. PM Brain's routing and golden rule depend on solid instruction-following. Fast/cheap models tend to skip the braindump and jump straight to templates — that defeats the whole point.

**For mechanical work (once thinking is done):** Switch to a fast/cheap model (Haiku-class, Flash-class) when filling templates, drafting artifacts from completed thinking, or running bulk repo operations. On Cursor you can do this mid-conversation via the model dropdown. On Claude Code, use a subagent at the cheaper tier.

**Avoid:** Models that don't follow complex multi-step instructions. If the agent skips braindump, jumps to templates, or ignores the golden rule — suspect the model first.

**Don't pin version numbers** — model SKUs go stale fast. Pick by capability tier and re-evaluate when you upgrade.

---

## Platform Overview

| Platform | Rules Auto-Load? | How to Load | Best For |
|----------|------------------|------------|----------|
| **Cursor** | Yes (`.cursor/rules/`) | Automatic | Full PM Brain experience; all features work |
| **VS Code + Copilot** | Yes (`.github/copilot-instructions.md`) | Automatic | Local IDE experience; full auto-load |
| **Claude Code** | No | Manual (read rules + context) | Web-based; need manual setup |
| **ChatGPT / Claude.ai** | No | Manual copy-paste | Simplest onboarding; lightweight |

---

## Setup by Platform

### Cursor (Recommended)

**What happens automatically:**
- `.cursor/rules/` files auto-load into every conversation
- Agent behavior rules applied from day one

**Setup steps:**
1. Clone or fork the repo: `git clone https://github.com/[you]/pm-brain.git`
2. Open in Cursor
3. Fill in [`USER.md`](../USER.md) at the repo root
4. Start a chat

**Watch out:**
- If you enable model auto-toggle, it may switch to a random model mid-conversation — turn it off
- If behavior feels wrong (skipping braindump, jumping to templates), check which model is active

---

### VS Code + GitHub Copilot

**What happens automatically:**
- `.github/copilot-instructions.md` auto-loads into every Copilot conversation
- Bootstrap set (AGENTS, ORCHESTRATION, voice, thinking, USER.md) is read at session start
- No setup prompt required

**Setup steps:**
1. Clone or fork the repo: `git clone https://github.com/[you]/pm-brain.git`
2. Open in VS Code
3. Install GitHub Copilot extension (`GitHub.copilot`)
4. Fill in [`USER.md`](../USER.md) at the repo root
5. **Important:** Set to Agent mode in Copilot Chat panel
6. Start chatting

**Watch out:**
- No persistent memory between conversations (each session starts fresh, but rules auto-load)
- If agent behavior feels off, check which model is active

**Known limitation — bootstrap compliance:**
The bootstrap instruction tells the agent to read 5 files before responding. In agent mode this is physically possible but not guaranteed — if your first message looks like a direct task, the model may skip bootstrap and respond immediately. In ask and plan modes it's impossible (no file read tools). Workaround: use agent mode, watch the tool call panel. If you don't see file reads at the start, say "load your bootstrap set."

**Known limitation — mid-session rule changes don't apply retroactively:**
If you edit a rule file or `USER.md` during a conversation, the change doesn't propagate back. Either tell the agent explicitly ("re-read `USER.md` now") or start a fresh conversation.

**Known quirk — VS Code sync button bypasses `.gitmessage` template:**
Committing via the VS Code Source Control panel ignores any `.gitmessage` template. Commit via terminal (`git commit` with no `-m` flag) to use the template.

---

### Claude Code

**Setup steps:**
1. Clone or fork the repo (local or GitHub)
2. Open this repo in Claude Code
3. Fill in [`USER.md`](../USER.md) at the repo root
4. **At start of each conversation**, say:

```text
I'm using PM Brain; load your bootstrap set. Then help me with: [your question/topic]
```

Or use the full prompt if the agent doesn't pick it up:

```text
Read in order: AGENTS.md, ORCHESTRATION.md, .cursor/rules/voice.mdc, .cursor/rules/thinking.mdc, USER.md — then help me with: [your topic]
```

**Gotchas:**
- Rules don't auto-load — you must ask the agent to read them each conversation
- Context window resets between conversations
- For subagent model efficiency, see [CLAUDE.md](../CLAUDE.md) → Subagents and Model Efficiency

---

### ChatGPT or Claude.ai (Web, No IDE)

**When to use:** Quick braindumps, lightweight one-off questions, learning the framework.

**Minimal setup:**
1. Start a new chat
2. Paste this:

```text
You are the PM Brain Coach (AGENTS.md persona).

Load this bootstrap context first:
- AGENTS.md
- ORCHESTRATION.md
- voice.mdc
- thinking.mdc
- USER.md

Key rules:
- Braindump BEFORE structure
- Ask hard questions; don't fill templates until thinking is done
- Communicate directly, grounded in experience

I need help with: [your topic]
```

**For ongoing work:** Save as a reusable custom instruction or workspace note.

---

## Troubleshooting

**"The agent is suggesting templates too early / skipping braindump"**
Model is likely too cheap or rules weren't loaded. Switch to a mid-tier model; reload rules; paste the setup prompt again.

**"Rules aren't auto-loading"**
On Cursor: check `.cursor/rules/` folder exists; restart Cursor. On all other platforms: manual loading is expected — use the setup prompt.

**"Agent behavior feels inconsistent"**
Stick to the same model tier for thinking conversations. If not on Cursor, paste setup rules at the start of each session.

**"I forked the repo and now it's public; I need it private"**
See `docs/setup.md` → Step 3 (Fork/Privacy).

---

## Summary

| Step | Cursor | VS Code+Copilot | Claude Code | ChatGPT/Claude.ai |
|------|--------|-----------------|-------------|-------------------|
| Clone/set up | `git clone` | `git clone` | Sync folder / GitHub | N/A (web only) |
| Load rules | Automatic | Automatic | Paste bootstrap prompt | Paste minimal bootstrap |
| Fill `USER.md` | Yes | Yes | Yes | Optional |
| Start chat | Normal | Normal | Paste setup first | Paste rules + question |

**If you're on Cursor:** You're ready. Open [`USER.md`](../USER.md), fill it in, start a chat.

**If you're on VS Code + Copilot:** You're ready — `.github/copilot-instructions.md` auto-loads. Fill `USER.md` and go.

**If you're on Claude Code or ChatGPT:** Bookmark this doc. Use the setup prompt at the top of each conversation.
