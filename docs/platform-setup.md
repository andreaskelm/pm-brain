# Multi-Platform Setup Guide

> **tl;dr:** PM Brain works on multiple platforms (Cursor, VS Code, Claude Code, ChatGPT, Claude.ai). Each loads configuration differently. This guide tells you exactly what to do on your platform.

---

## Platform Overview

| Platform | Rules Auto-Load? | How to Load | Model Selection | Best For |
|----------|------------------|------------|-----------------|----------|
| **Cursor** | Yes (`.cursor/rules/`) | Automatic | Built-in model selector | Full PM Brain experience; all features work |
| **VS Code + Copilot** | Yes (`.github/copilot-instructions.md`) | Automatic | VS Code settings | Local IDE experience; full auto-load |
| **Claude Code** | No | Manual (read rules + context) | Explicit in first turn | Web-based; need manual setup |
| **ChatGPT / Claude.ai** | No | Manual copy-paste | Model picker in UI | Simplest onboarding; lightweight |

---

## Setup by Platform

### Cursor (Recommended)

**What happens automatically:**
- `.cursor/rules/` files auto-load into every conversation
- Model defaults to your selected Cursor model
- `CLAUDE.md` is metadata (for reference only)
- Agent behavior rules applied from day one

**Setup steps:**
1. Clone or fork the repo: `git clone https://github.com/[you]/pm-brain.git`
2. Open in Cursor
3. Done - rules auto-apply
4. Fill in `01-Company-Context/CONTEXT.md` and `thinking.personal.mdc`
5. Start a chat

**Model selection in Cursor:**
- Cursor settings -> Model -> Pick Claude (Sonnet 4.6+ ), Haiku 4.5, or GPT-5.4
- **Recommended for PM Brain:** Claude Haiku 4.5 or Claude Sonnet 4.6+
- **Avoid:** Grok, older models that don't follow instructions well

**Gotchas:**
- If you enable model auto-toggle, it may switch to a random model mid-conversation
- Turn OFF auto-toggle and pick a stable model
- If behavior feels wrong, check which model is active (model icon in chat)

---

### VS Code + GitHub Copilot

**What happens automatically:**
- `.github/copilot-instructions.md` auto-loads into every Copilot conversation
- The Copilot bootstrap reads the always-on bootstrap set at the start of each session: `AGENTS.md`, `ORCHESTRATION.md`, `voice.mdc`, `thinking.mdc`, and `thinking.personal.mdc`
- Always-on rules (voice, thinking, personal context) are part of bootstrap, not sleeping memory
- No setup prompt required

**Setup steps:**
1. Clone or fork the repo: `git clone https://github.com/[you]/pm-brain.git`
2. Open in VS Code
3. Install GitHub Copilot extension (`GitHub.copilot`)
4. Fill in `01-Company-Context/CONTEXT.md` and `.cursor/rules/thinking.personal.mdc`
5. **Important** Set to Agent mode in Copilot Chat panel
6. Start chatting - the agent initializes automatically

**Model selection:**
- VS Code + Copilot defaults to whatever model is configured (Claude Sonnet 4.6+ recommended)
- Change model via the model picker in the Copilot Chat panel
- **Recommended:** Claude Sonnet 4.6 or newer
- **Avoid:** Grok, older models that don't follow instructions well

**Gotchas:**
- No persistent memory between conversations (each session starts fresh, but rules auto-load)
- If agent behavior feels off, check which model is active - model quality matters
- The `.cursor/rules/` files still drive Cursor behavior; `.github/copilot-instructions.md` is the VS Code equivalent

**Known limitation - bootstrap compliance (as of April 2026):**
The bootstrap instruction in `copilot-instructions.md` tells the agent to read 5 files before responding. In **agent mode** this is physically possible (file read tools are available) but not guaranteed - if your first message looks like a direct task, the model may skip the bootstrap and respond immediately as a generic coding assistant. In **ask and plan modes** it's impossible regardless, since file read tools don't exist in those modes.

Practical workaround: use agent mode, and watch the tool call panel at the start of each conversation. If you don't see file reads happening before the first response, the bootstrap was skipped - you can call it out directly ("load your bootstrap set") and the agent will usually comply. This is a model compliance issue, not a configuration issue, and may improve in future model versions.

**Known limitation - mid-session rule changes don't apply retroactively:**
If you update a rule file (e.g. `voice.mdc`, `thinking.personal.mdc`) during a conversation, the change does NOT propagate back into the active context window. The agent will keep using whatever version of the file was loaded at session start. If you want the updated rule to take effect immediately, either: (a) tell the agent explicitly ("re-read `thinking.personal.mdc` and apply it from now on"), or (b) start a fresh conversation. Don't assume edits take effect mid-session.

**Known quirk - VS Code sync button bypasses `.gitmessage` template:**
When you commit via the VS Code Source Control panel (the sync/checkmark button), any `.gitmessage` commit template configured in your git settings is ignored. Copilot generates its own commit message from the diff — usually a wall of text. If you want clean, template-respecting commit messages, commit via terminal: `git commit` (no `-m` flag) — this opens the template in your editor. This is a VS Code + Copilot platform behaviour, not a PM Brain bug.

---

### Claude Code

**What you need to do manually:**
- Read CLAUDE.md at the start (it tells you exactly what to load)
- Manually read `.cursor/rules/` files in first turn
- Model: Use Claude (you pick version in Claude.ai settings)

**Setup steps:**
1. Clone or fork the repo (local or GitHub)
2. Open this repo in Claude Code
3. Fill in `01-Company-Context/CONTEXT.md` and `thinking.personal.mdc`
4. **At start of each conversation**, say something like:

```text
Let's set up PM Brain for this conversation.

Read:
1. AGENTS.md (persona, golden rules)
2. ORCHESTRATION.md (routing, state machine)
3. .cursor/rules/voice.mdc (communication style)
4. .cursor/rules/thinking.mdc (coaching workflow)
5. .cursor/rules/thinking.personal.mdc (my personal context)

Then help me with: [your question/topic]
```

5. Or shorter: Just say "I'm using PM Brain; load your bootstrap set" and the agent should handle it

**Model selection:**
- Claude Code lets you pick model in claude.ai settings (Sonnet, Haiku, etc.)
- **Recommended:** Claude Haiku 4.5 or Claude Sonnet 4.6+
- **Avoid:** Grok, older models
- **Best practice:** Lock in Haiku 4.5 in settings and don't toggle

**Gotchas:**
- Rules don't auto-load - you must ask the agent to read them
- Context window resets between conversations
- If setup is tedious, create a "system prompt" or reusable setup message in Claude.ai settings

---

### ChatGPT or Claude.ai (Web, No IDE)

**When to use:** Quick braindumps, lightweight project, learning the framework

**What you need to do:**
- Copy-paste relevant docs into chat manually
- No persistent workspace (paste fresh each time)
- Model: ChatGPT 5.4+ or Claude Sonnet 4.6+ (you pick)

**Minimal setup for one question:**
1. Start a new chat
2. Paste this:

```text
You are the PM Brain Coach (AGENTS.md persona).

Load this bootstrap context first:
- AGENTS.md
- ORCHESTRATION.md
- voice.mdc
- thinking.mdc
- thinking.personal.mdc

Key rules:
- Braindump BEFORE structure
- Ask hard questions; don't fill templates until thinking is done
- Communicate directly, grounded in experience

I need help with: [your topic]
```

3. Ask your question

**For ongoing work:**
Save your context as a reusable ChatGPT "custom instruction" or workspace note (if available).

**Model selection:**
- ChatGPT: Use GPT-5.4+ (don't use 4-Turbo, it's older)
- Claude.ai: Use Claude Sonnet 4.6+ or Haiku 4.5
- **Avoid:** Grok, older models

---

## Model Selection: Why It Matters

**The issue:** PM Brain relies on **instruction-following** and **nuanced routing** (product_sense vs execution_mode). Weaker models don't follow the golden rule; they skip braindump and jump to templates. Better models respect the workflow.

**Model Tier List:**
- Excellent: Claude Haiku 4.5, Claude Sonnet 4.6+, Claude Opus 4.6+, GPT-5.4+, 
- Good: GPT-4 (older), Claude 3 Sonnet
- Avoid: Grok, older Claude/GPT models, local models (unless specifically tuned)

**Pro tip:** Lock your model choice in settings and turn OFF auto-toggle. Consistency matters.

---

## Troubleshooting

### "The agent isn't following the golden rule; it's suggesting templates too early"
- **Cause:** Weak model or rules not loaded
- **Fix:** Switch to Haiku 4.5 or Sonnet 4.6+; reload rules; paste the setup prompt again

### "Rules aren't auto-loading"
- **If Cursor:** Check `.cursor/rules/` folder exists; restart Cursor
- **If VS Code / Claude Code / ChatGPT:** You're on a platform that requires manual loading - expected behavior

### "Agent behavior feels inconsistent"
- **Cause:** Model toggled between conversations or rules loaded unevenly
- **Fix:** Lock the model in settings; at start of each conversation (if not Cursor), paste setup rules again

### "I forked the repo and now it's public; I need it private"
- **See:** docs/setup.md -> Step 3 (Fork/Privacy) for migration instructions

---

## Summary Table: What You Need to Do

| Step | Cursor | VS Code+Copilot | Claude Code | ChatGPT/Claude.ai |
|------|--------|-----------------|-------------|-------------------|
| Clone/set up | `git clone` | `git clone` | Sync folder / GitHub | N/A (web only) |
| Load rules | Automatic | Automatic (`.github/copilot-instructions.md`) | Paste bootstrap prompt | Paste minimal bootstrap |
| Model selection | Cursor settings | Copilot model picker | claude.ai settings | Site model picker |
| Fill personal context | `thinking.personal.mdc` | Same | Same | (Optional) |
| Start chat | Normal | Normal - no setup prompt needed | Paste setup first | Paste rules + question |
| Lock model | Yes (recommended) | Yes (recommended) | Yes (recommended) | Yes (recommended) |

---

## Next Steps

**If you're on Cursor:** You're ready. Start with [01-Company-Context/CONTEXT.md](../01-Company-Context/CONTEXT.md).

**If you're on VS Code + Copilot:** You're ready too - `.github/copilot-instructions.md` auto-loads. Just open a chat and go.

**If you're on Claude Code or ChatGPT:** Bookmark this doc. Use the setup prompt at the top of each conversation.

**If you're deploying PM Brain for a team:** Highlight this doc. Every team member needs to know their platform's setup flow.

---

## Questions?

If something doesn't work on your platform, [log it as a gap](../04-Initiatives/) so we can improve the docs.
