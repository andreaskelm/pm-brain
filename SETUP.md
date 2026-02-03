# 🚀 PM Brain Setup Guide

> **Welcome!** This guide will help you get your PM Brain repository configured and ready to use. No technical knowledge required—just follow the steps.

## 📋 Quick Start Checklist

- [ ] Clone or fork the repository
- [ ] Read this SETUP guide
- [ ] Review the main README.md
- [ ] Read [GUIDELINES.md](./GUIDELINES.md) for best practices
- [ ] Customize Company Context (Priority 1)
- [ ] Review AI/Agent configuration (if using Cursor or similar)
- [ ] Try your first framework
- [ ] Set up your first initiative

---

## 🎯 Step 1: Get the Repository

### Option A: Personal Use (Clone or Private Fork)

- If you’re experimenting or building a **personal public portfolio**, you can clone directly:

  ```bash
  git clone https://github.com/andreaskelm/pm-brain.git
  cd pm-brain
  ```

- If you’re working with **real company context**, prefer a **private fork**:

  1. Click “Fork” on GitHub and set visibility to **Private**.  
  2. Then:

     ```bash
     git clone https://github.com/YOUR-USERNAME/pm-brain.git
     cd pm-brain
     ```

  This lets you keep company‑specific context private while still pulling updates from the main repository.

### Option B: Team/Company Framework Repo

If you want a shared repo for your team’s frameworks/templates:

1. Fork the repo into your org (public or private as appropriate).  
2. Treat this fork as the **team library**:
   - Track `02-Methods-and-Tools/` and any sanitized examples.  
   - Keep everyone’s personal `00-Meta/` logs private via **Team mode** (see below).

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
- `02-Methods-and-Tools/` = **READY TO USE** — **2.0-Foundations** (think first, product sense), **2.1-Strategy**, **2.2-Discovery**, **2.3-Execution**, **2.4-Communication**. Start product thinking from [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md).
- `03-Research-Artifacts/` = **YOUR RESEARCH** (add your interview notes, findings)
- `04-Initiatives/` = **YOUR WORK** (document your active initiatives)

---

## ⚙️ Step 3: Choose Public / Private / Team Mode

This repo supports three usage modes. Setup is **manual and simple**: you choose a mode by appending the right `.gitignore` template and committing. No scripts required.

### Modes at a Glance

- **🌍 Public** (default)
  - **Best for**: open learning, public examples, blog/portfolio content.  
  - **Tracked**: everything (frameworks, Meta logs, company context, initiatives).  

- **🔒 Private**
  - **Best for**: real company work or personal growth where content must not leak.  
  - **Tracked**: frameworks and docs.  
  - **Ignored** (via `.gitignore.private`): Meta logs, growth portfolio, company context, active initiatives (per patterns).  

- **👥 Team**
  - **Best for**: a shared frameworks repo, with each person keeping their own practice private.  
  - **Tracked**: `02-Methods-and-Tools/` and any shared docs.  
  - **Ignored** (via `.gitignore.team`): each contributor’s `00-Meta` logs and personal growth artefacts.

### How to Apply a Mode (Manual)

Run **one** of these in your fork’s root:

- **Public (do nothing)**  
  - Leave `.gitignore` as‑is. Everything can be tracked.

- **Private mode**:

  ```bash
  cat .gitignore.private >> .gitignore
  git add .gitignore
  git commit -m "setup: configure private mode"
  ```

- **Team mode**:

  ```bash
  cat .gitignore.team >> .gitignore
  git add .gitignore
  git commit -m "setup: configure team mode"
  ```

For details and decision help, see `00-Meta/MODE-SELECTION-GUIDE.md`.

---

## 📚 Step 4: Required Customizations (Priority Order)

### Priority 1: Company Context (`01-Company-Context/`)

**This is the most important step.** Set up your company context structure based on your unique organizational setup.

#### Step 1: Personalize Your Context

1. **Fill out `CONTEXT.md`** (2-3 minutes)
   - Your name and role
   - Company name (this replaces `[Company]` placeholders throughout)
   - Team and business unit names (if applicable)

#### Step 2: Run the Setup Guide

2. **Follow the setup guide** [`01-Company-Context/SETUP.md`](01-Company-Context/SETUP.md)
   - Discover your organizational structure through probing questions
   - Plan the right document structure (flat, BU-level, team-level, etc.)
   - Implement incrementally - you don't need to do everything at once

**The setup guide helps you:**
- Understand if you need business unit subfolders
- Determine how to organize OKRs (company/BU/team level)
- Plan roadmap structure (single vs BU-specific vs team-specific)
- Set up stakeholder organization

#### Step 3: Create Core Documents

3. **Create core documents** (30-60 minutes):
   - `1-company-vision.md` - Company mission, vision, values
   - `2-company-strategy.md` - Strategic priorities and initiatives
   - `3-company-product-principles.md` - Product principles
   - `4-company-product-explanation.md` - Product portfolio
   - `5-company-roadmap.md` - Company roadmap (if applicable)
   - `6-company-stakeholders.md` - Stakeholder directory

**How to update:**
- Replace `[Company]` placeholders with your company name from CONTEXT.md
- Replace `[Placeholder]` text with your actual content
- Keep the structure, customize the content
- Commit your changes: `git commit -am "Add company context"`

**Time estimate:** 
- Personalization: 2-3 minutes
- Setup guide: 15-30 minutes (discovery and planning)
- Core documents: 30-60 minutes
- **Total: 1-2 hours** (can be done incrementally)

---

### Priority 2: AI/Agent Configuration (If Using Cursor or Similar IDE)

If you're using **Cursor** (or similar AI-powered IDE), the repository includes agent configuration files.

#### Location: `.cursor/rules/`

**Files:**
- `AGENTS.md` (root) - PM Brain Assistant instructions (source of truth, already configured)
- `.cursor/rules/AGENTS.template.md` - Template/guide for creating custom agents (separate from root `AGENTS.md`)
- `thinking.mdc` - High-level thinking support rules
- `thinking.personal.mdc` - Personal context (you can customize this)

**What to do:**
1. **Review** `AGENTS.md` (root) - Understand how the PM Brain Assistant is configured
2. **Fill out** `01-Company-Context/CONTEXT.md` - Add your name, company name, and team/BU names (organizational context)
   - **Note:** In private/team modes, this file is ignored by default. In team mode, you can optionally track it for team consistency (see `.gitignore.team` comments).
3. **Customize** `.cursor/rules/thinking.personal.mdc` - Add your personal working style, preferences, and communication style (how you like to work)
   - **Note:** Both files may include your name - keep them consistent. `CONTEXT.md` focuses on organizational context; `thinking.personal.mdc` focuses on how you work.
   - **Git tracking:** This file is ignored in private and team modes (kept private). In public mode, sanitize any sensitive personal information.
4. **Optional:** Use `AGENTS.template.md` to create additional custom agents if needed
5. **Optional:** Add company-specific rules if needed

**Example personal context to add:**
```markdown
# Personal Context

## Working Style
- I prefer detailed explanations
- I like examples with real scenarios
- I want to understand the "why" behind recommendations

## Common Challenges
- I struggle with stakeholder alignment
- I need help prioritizing competing requests
- I want to improve my product sense

## Goals
- Become better at discovery
- Improve my communication with engineering
- Build stronger product intuition
```

**Time estimate:** 15-30 minutes

---

### Priority 3: 00-Meta (Personal Practice) — Optional

If you want to build product sense deliberately (daily log, weekly reflection, growth portfolio, forecast calibration):

1. **Read** [00-Meta/README.md](00-Meta/README.md) for what lives there and the minimal workflow.
2. **Copy** the daily log template from `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/templates/daily-log-template.md` to `00-Meta/1-daily-log-YYYY-QX.md` (e.g. `1-daily-log-2026-Q1.md`).
3. **Optional:** Before shipping a feature, log a forecast in `00-Meta/0.3-Product-Judgment-Test/forecast-log.md`; resolve when data is in (calibration).

Mode (Public/Private/Team) affects what in `00-Meta/` is tracked in git; see Step 3 and `00-Meta/MODE-SELECTION-GUIDE.md`.

---

### Priority 4: Optional Customizations

#### Customize Templates (If Needed)

The templates in `02-Methods-and-Tools/` work as-is, but you can customize them for your workflows:

- **PRD Template** (`2.3-Execution/2.3.4-PRD/2-prd-template.md`) - Add company-specific sections
- **Meeting Agendas** (`2.4-Communication/2.4.2-Meeting-Agendas/`) - Add your team's standard agenda items
- **One-Pagers** (`2.4-Communication/2.4.3-One-Pagers/`) - Customize for your communication style

**When to customize:**
- Your team has specific requirements
- You want to add company-specific sections
- You've found a better structure through experience

**When NOT to customize:**
- First time using the framework (try it as-is first)
- You're not sure what to change (use it, then iterate)

---

## 🧪 Step 5: Try Your First Framework

**Don't wait until you need it!** Try a framework now to get familiar with the system.

### Start with product thinking (braindump first)

1. **Open the entry point:** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md)
2. **Copy the "Simple prompt to start"** at the top into a new chat (e.g. with Cursor or any AI). The agent will ask hard questions and braindump with you before suggesting any framework.
3. **Only after a braindump** use the **Frameworks by situation** table in that file (or the domain READMEs) to open the right framework: Strategy, Discovery, Execution, or Communication.

**Golden rule:** Braindump before structure. See [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md).

### Then try a framework

- **PRD:** `02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/` — after braindump, read README + framework, then template
- **OKRs:** `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/` — goal-setting
- **Opportunity Assessment:** `02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment/` — evaluating new ideas
- **Meeting Agendas / One-Pagers:** `02-Methods-and-Tools/2.4-Communication/` — stakeholder communication

---

## 📝 Step 6: Set Up Your First Initiative

Create your first initiative folder to see how the system works:

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

## 🤖 Step 7: Using with AI Tools

### Option A: Cursor (Recommended for Technical Users)

If you're using **Cursor**:

1. **Open the repository** in Cursor
2. **The AI already knows** the repo (via root `AGENTS.md`). For **product/stakeholder/org thinking**, it will start from the entry point [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md): braindump first, then suggest a framework (Strategy, Discovery, Execution, Communication).
3. **Use slash commands** for common workflows (see `.cursor/commands/`):
   - `/start` - Launch a new initiative end-to-end
   - `/review` - Review current doc or selection for PM Brain alignment
   - `/day` - Plan your day with PM rituals
   - `/week` - Plan your week with strategic focus
   - `/focus` - Get help when you're stuck or need focus
   - `/unstuck` - Get unstuck from blockers
   - `/navigate` - Find the right framework for your situation
   - `/bias` - Check for cognitive biases in your thinking
4. **To start a product-thinking chat:** Paste the simple prompt from the top of `0-start-here-product-thinking.md` (e.g. "I want to think through something about my product / stakeholder / org…"). The AI will ask hard questions and braindump with you before suggesting frameworks.

**Use PM Brain in any project (Cursor only):**
```bash
npx skills add andreaskelm/pm-brain
```
Installs the workflow skill from [skills.sh](https://skills.sh/); use it in any repo where you do PM work.

### Option B: ChatGPT, Claude, Gemini (Copy-Paste Method)

1. **Browse** to the framework you need
2. **Copy** the README + framework + template files
3. **Paste** into your AI chat with a prompt like:
   ```
   Here's the PRD framework I use. First, help me braindump my thoughts 
   on [feature]. Then help me fill out the template.
   ```

### Option C: Upload to AI Projects

Many AI tools support "Projects" where you can upload files:

- **ChatGPT:** Create a GPT and upload key files
- **Claude:** Use Claude Projects feature
- **GitHub Copilot:** Point it at this repository

**For persistent product coaching in ChatGPT/Claude:** If you want consistent product coaching across multiple sessions (same persona and workflow as Cursor's `product_sense_mode`), use the [Product Coach setup template](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/templates/6-product-coach-setup.md). Copy it into a ChatGPT or Claude Project to get the same braindump-first coaching approach.

---

## ✅ Step 8: Verify Your Setup

Run through this checklist to ensure everything is configured:

- [ ] Company Context files updated with your information
- [ ] Agent rules reviewed (if using Cursor)
- [ ] Know the product-thinking entry point (`0-start-here-product-thinking.md`) and braindump-first rule
- [ ] Tried at least one framework successfully (after a braindump)
- [ ] Created your first initiative folder
- [ ] Understand where to store research (`03-Research-Artifacts/`)
- [ ] Know where to document active work (`04-Initiatives/`)
- [ ] (Optional) Set up `00-Meta/` daily log or forecast log if you want to practice product sense

---

## 🆘 Common Questions

### "Do I need to install anything?"

**No!** This is a markdown-based system. You just need:
- A text editor (VS Code, Cursor, Notepad, etc.)
- Git (if you want version control)
- Optional: AI tool (Cursor, ChatGPT, Claude, etc.)

### "What if I make a mistake?"

**No problem!** This is git-versioned:
- `git status` - See what changed
- `git diff` - See exact changes
- `git checkout -- <file>` - Undo changes to a file
- `git log` - See your history

### "Can I use this with my team?"

**Yes!** 
- Fork the repo for your team
- Customize Company Context together
- Share frameworks and templates
- Use git to collaborate

### "How do I keep it updated?"

If you forked from the main repo:
```bash
# Add the original repo as upstream
git remote add upstream https://github.com/andreaskelm/pm-brain.git

# Pull updates (merge carefully!)
git fetch upstream
git merge upstream/main
```

**Be careful:** Only merge framework updates. Don't overwrite your Company Context!

### "What if I don't know what to customize?"

**Start simple:**
1. Update Company Context (Priority 1)
2. Use frameworks as-is
3. Customize only when you discover a need

**Don't optimize prematurely!** Use the system first, then improve it.

---

## 🎓 Next Steps

Once you're set up:

1. **Read the main README.md** - Understand the philosophy
2. **Browse frameworks** - See what's available in `02-Methods-and-Tools/`
3. **Start using it** - Don't wait for perfect setup, start with real work
4. **Iterate** - Customize as you learn what works for you

---

## 📚 Additional Resources

- **Main README:** [README.md](README.md) — Overview and philosophy
- **Product thinking entry point:** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) — Simple prompt to start; braindump first, then frameworks by situation
- **Golden rule:** [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) — Braindump before structure
- **Guidelines:** [GUIDELINES.md](GUIDELINES.md) — Best practices for using and maintaining your PM brain
- **Agent Configuration:** [AGENTS.md](AGENTS.md) — PM Brain Assistant instructions; `.cursor/rules/AGENTS.template.md` for custom agents
- **Framework Navigation:** [02-Methods-and-Tools/README.md](02-Methods-and-Tools/README.md) — Strategy, Discovery, Execution, Communication
- **00-Meta (practice):** [00-Meta/README.md](00-Meta/README.md) — Daily log, learning log, growth portfolio, Product Judgment Test
- **Credits:** [CREDITS.md](CREDITS.md) — Attribution for frameworks and methods

---

## 💡 Pro Tips

1. **Braindump first, structure second** - Every framework encourages this. Don't skip it!
2. **Use git commits** - Commit after each major update. Your git history becomes your thinking log.
3. **Start small** - Don't try to set up everything at once. Use it, then improve it.
4. **Keep it updated** - Company Context should reflect current reality. Update it regularly.
5. **Share learnings** - If you improve a framework, consider contributing back!

---

## 🐛 Troubleshooting

### "I can't find a framework for X"

- Check `02-Methods-and-Tools/README.md` for navigation
- Search the repository for keywords
- Check `TODO.md` to see what's planned

### "The AI assistant doesn't understand my question"

- Make sure you're in the repository directory
- Check that `AGENTS.md` (root) exists (this defines the PM Brain Assistant)
- Try rephrasing your question more specifically

### "I'm overwhelmed by all the files"

- **Start with Company Context** - That's the most important
- **Pick one framework** - Try PRD or OKRs
- **Use it for real work** - You'll learn as you go

---

## ✨ You're Ready!

You've completed the setup. Now go build great products! 🚀

**Remember:** This is a living system. It should evolve with you. Don't be afraid to customize, experiment, and improve it.

---

**Questions?** Check the main `README.md` or explore the framework folders. The system is designed to be self-explanatory as you use it.

**Created by:** [Andreas Kelm](https://github.com/andreaskelm)  
**Last updated:** 2026-01-31
