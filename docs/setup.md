# 🚀 PM Brain Setup Guide

> **Welcome!** This guide gets you from zero to running in under 30 minutes.

## ⚠️ Fork it — but make it private

PM Brain is designed to be **forked and made your own** — but the original repo is public, so any fork defaults to public too. Your company context, roadmaps, and stakeholder info should NOT be visible to everyone.

Fork it, make it private, then add your context. Don't accidentally push company strategy to the internet.

See [Step 1: Get the Repository](#-step-1-get-the-repository) for exact instructions.

---

## 🔧 First: Choose Your AI Tool

Your tool choice affects how PM Brain configures itself — some tools auto-load rules, others require a manual setup prompt each session.

| Tool | Rules auto-load? | Setup effort |
|------|-----------------|---------------|
| **Cursor** | Yes (`.cursor/rules/`) | Minimal |
| **VS Code + GitHub Copilot** | Yes (`.github/copilot-instructions.md`) | Minimal |
| **Claude Code** | No — manual per session | Some |
| **ChatGPT / Claude.ai** | No — copy-paste per session | More |

See [platform-setup.md](platform-setup.md) for full per-tool instructions.

**The fastest path:** once you have the repo open in your AI tool, say **"help me set up PM Brain"** — the agent reads the repo, flags placeholders, and guides you through the rest.

---

## 📋 Quick Start

1. **Get the repo** — fork it privately, clone locally, or stay local (Step 1)
2. **Open in your AI tool** — IDE (Cursor, VS Code) or web-based (Claude.ai, ChatGPT) — see the [AI Tool section above](#-first-choose-your-ai-tool) and [platform-setup.md](platform-setup.md) for per-platform details
3. **Say "help me set up PM Brain"** — the agent reads the repo, flags placeholders, guides you

---

## 🎯 Step 1: Get the Repository

**Recommended: Fork → make private → clone**

1. **Fork** this repo on GitHub (top right: Fork)
2. **Make it private**: go to your fork → Settings → Danger Zone → Change visibility → Private
3. **Clone** your private fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/pm-brain.git
   cd pm-brain
   ```
4. **Add upstream** to pull future PM Brain updates:
   ```bash
   git remote add upstream https://github.com/andreaskelm/pm-brain.git
   ```

That's it. Your private copy is ready. Changes you push stay in your private repo; you can pull framework updates from upstream whenever you want.

**Pulling updates from upstream (syncing your fork):**
```bash
git fetch upstream
git merge upstream/main
```
If you get a merge conflict, it's almost always in a file where you have real company content that the upstream version replaced with a placeholder — keep yours (`git checkout --ours <file>`). Private fork note: GitHub won't let you open a PR from a private fork to the public upstream directly. If you want to contribute improvements back, either push a branch directly to upstream (if you have access) or make the branch temporarily public.

**Alternatives**

- **Local only (no GitHub):** Clone directly — no GitHub account, no privacy risk, no syncing.
  ```bash
  git clone https://github.com/andreaskelm/pm-brain.git
  cd pm-brain
  ```
- **Private from the start (no public footprint):** Create an empty private repo on GitHub first, then clone PM Brain into it:
  ```bash
  git clone https://github.com/andreaskelm/pm-brain.git
  cd pm-brain
  git remote set-url origin https://github.com/YOUR-USERNAME/pm-brain-private.git
  git push -u origin main
  git remote add upstream https://github.com/andreaskelm/pm-brain.git
  ```
- **Team/org repo:** Fork into a private org repo instead of a personal one, then follow [Step 3](#️-step-3-choose-public--private--team-mode) → Team mode.

---

## 📚 Step 2: Understand the Structure

Before customizing, understand what each folder does:

```
pm-brain/
├── 00-Meta/                   # 🧠 Personal practice (daily log, learning log, growth portfolio, Product Judgment Test)
├── 01-Company-Context/        # 🏢 YOUR company vision, strategy, stakeholders
├── 02-Methods-and-Tools/      # 🧭 Frameworks & templates (Strategy, Discovery, Execution, Communication)
├── 03-Research-Artifacts/     # 🔍 Your research notes and findings
└── 04-Initiatives/            # 🚧 Your active product work
```

**Key insight:** 
- `00-Meta/` = **YOUR PRACTICE** (daily log, weekly/monthly reflection, growth portfolio, forecast calibration). Canonical prompts and templates live in `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/`.
- `01-Company-Context/` = **YOU MUST CUSTOMIZE THIS** (your company info)
- `02-Methods-and-Tools/` = **READY TO USE** — **2.0-Foundations** (think first, product sense), **2.1-Strategy**, **2.2-Discovery**, **2.3-Execution**, **2.4-Communication**. Start product thinking from [0-start-here-product-thinking.md](../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md).
- `03-Research-Artifacts/` = **YOUR RESEARCH** (add your interview notes, findings)
- `04-Initiatives/` = **YOUR WORK** (document your active initiatives)

---

## ⚙️ Step 3: Choose Public / Private / Team Mode

This repo supports three usage modes. The `.gitignore` file contains all three as clearly labeled, commented-out blocks — public is active by default, and private/team are ready to uncomment.

### Modes at a Glance

- **🌍 Public** (default, nothing to do)
  - **Best for**: open learning, public examples, blog/portfolio content.
  - **Tracked**: everything (frameworks, Meta logs, company context, initiatives).

- **🔒 Private**
  - **Best for**: real company work or personal growth where content must not leak.
  - **Tracked**: frameworks and docs only.
  - **Ignored**: Meta logs, growth portfolio, company context, active initiatives, personal configuration.

- **👥 Team**
  - **Best for**: a shared frameworks repo, with each person keeping their own practice private.
  - **Tracked**: `02-Methods-and-Tools/` and shared docs.
  - **Ignored**: each contributor's `00-Meta` logs, personal growth artefacts, personal configuration.

### How to Apply a Mode

**Tell the agent your mode** — the simplest path:

> "Switch me to private mode" (or team / public)

The agent will uncomment the right block in `.gitignore`, commit it, and list any files already tracked in git that might contain sensitive information so you can decide whether to un-track them.

**⚠ Check your GitHub repo visibility** before your first push. If you're in private or team mode, your repo must be set to Private on GitHub: Settings → Danger Zone → Change visibility.

**⚠ Switching modes after already committing files:** `.gitignore` only gates future untracked files. Files already in git history stay tracked regardless. To un-track a file that was already committed:

```bash
git rm --cached <file>
git commit -m "setup: un-track sensitive file"
```

Or ask the agent: *"what tracked files might be sensitive in private mode?"*

---

## 📚 Step 4: Customize

**Minimum to start (10 minutes):**

- [`USER.md`](../USER.md) at the repo root — your name, role, company, team, what you build, and how you work (working preferences, strengths, challenges, communication style). For other tools without repo file access, paste this content as part of your system prompt — see [platform-setup.md](platform-setup.md).

That's it. The agent loads `USER.md` on every conversation (part of the bootstrap set).

**Add as you go:**

- Full `01-Company-Context/` docs (vision, strategy, stakeholders) when you want grounded strategic advice
- `01-Company-Context/CONTEXT-HEALTH.md` to track freshness once you have multiple docs
- `01-Company-Context/1.1-Stakeholder-Avatars/` if you want the agent to simulate stakeholder reactions
- `00-Meta/` daily log + forecast calibration if you want to build product sense deliberately

**Not sure what context you have?** Start with your team. Fill in what you know, mark gaps with "TBD" or "unclear", and treat the files as working hypotheses — not finished documents. As you learn more, you update them.

If your org has layers (company → division → business unit → team), don't try to model all of them upfront. Start at the level you actually work at — usually your team or business unit — and add layers only when the distinction matters for your work.

**A note on git tracking:** In private/team modes, `USER.md` is ignored by git — your personal context stays private. See Step 3 to configure your mode.

---

## 🧪 Step 5: Start Using It

Bring a real problem you're working on — a feature you're scoping, a decision you're stuck on, a stakeholder situation you're navigating. Open a chat with your AI tool and describe it.

Don't try to pick the right framework first. The agent's job is to help you think through the mess before suggesting any structure. Lead with the problem; let the conversation go where it needs to go.

The frameworks are there when you need them. [0-start-here-product-thinking.md](../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) is the entry point — it has a simple prompt to start, then maps frameworks by situation. Or browse [02-Methods-and-Tools/README.md](../02-Methods-and-Tools/README.md) directly. But the braindump comes first.

---

## 📝 Step 6: Set Up Your First Initiative

When you have something worth tracking, create an initiative folder:

1. **Navigate to:** `04-Initiatives/`
2. **Create a new folder:** `4.2-Your-Initiative-Name/` (or use the example: `4.1-Initiative-Codename/`)
3. **Copy the structure from the example:**
   - `README.md`
   - `summary.md`
   - `opportunity-assessment.md`
   - `prd.md`
   - `roadmap.md`
   - `decisions.md`

4. **Start with:** `summary.md` - Write a brief summary of what you're working on

**This is where you'll do your actual product work!**

---

## ✅ Step 7: You're Ready

Open a chat with your AI tool and say: **"verify my PM Brain setup is complete and aligned with best practices"** — it will read your context files, check that placeholders are filled, and flag anything missing.

From here, everything is driven by real work and real problems.

---

## 📚 Reference

- **Overview and philosophy:** [README.md](../README.md)
- **Product thinking entry point:** [0-start-here-product-thinking.md](../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md)
- **Golden rule:** [PRODUCT-SENSE-RULES.md](../PRODUCT-SENSE-RULES.md) — Braindump before structure
- **Best practices:** [guidelines.md](guidelines.md)
- **Per-tool instructions:** [platform-setup.md](platform-setup.md)
- **Framework navigation:** [02-Methods-and-Tools/README.md](../02-Methods-and-Tools/README.md)