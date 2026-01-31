# 🧠 PM Brain-as-Code

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain) [![GitHub forks](https://img.shields.io/github/forks/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain/fork)

> **Your external product management brain. Single source of truth = latest commit.**

A living knowledge base that bridges the gap between Product Management frameworks and actual operational execution. Git-versioned, shareable, ready to use.

**Product teams drown in blog posts and frameworks** but don't know *how* to run sprint planning on Tuesday morning or write a strategy document by end-of-day. This gives you battle-tested guides, templates, and playbooks. Built for everyone from junior PMs to senior leads.

🚀 **Get started:** clone the repo → add your context → start shipping

**Quick links:** [Setup Guide](./SETUP.md) · [Guidelines](./GUIDELINES.md) · [Quick Start](#-how-to-get-started) · [What's Inside](#-whats-inside) · [Structure](#-system-structure-philosophy) · [Daily Workflow](#-daily-workflow)

## 📦 What's Inside

```text
📦 PM Brain-as-Code
├── 🧭 Frameworks: decision models and methods that actually help you choose what to do next  
├── 📋 Step-by-step guides: checklists and how-tos for running key rituals and processes  
├── 📄 Copy-paste templates: PRDs, one-pagers, roadmaps, communication, and more, ready to fill in  
├── 🚨 Scenario playbooks: what to do when things go sideways (incidents, tough conversations, tradeoffs)  
├── 🏢 Company context: vision, strategy, principles, portfolio, roadmap, and stakeholders that don't go stale  
└── 🤖 Prompt libraries: structured thinking prompts for AI tools (ChatGPT, Claude, Gemini, GitHub Copilot, Cursor, etc.)
```

**Always up-to-date:** Latest commit = current reality. No stale documents or long forgotten context in Notion, SharePoint or Confluence that nobody updates.  

---

## 🚀 How to Get Started

> **New to this repository?** Start with [`SETUP.md`](./SETUP.md) for detailed setup instructions, including how to customize Company Context, configure AI tools, and get started with your first framework.

### Option 1: Manual (Copy-Paste into AI Tools)

**Best for:** ChatGPT, Claude, Gemini, Microsoft Copilot, or other chat-based AI tools.

1. **Browse** to the folder you need:
   - `00-Meta/` – for personal practice (daily log, learning log, growth portfolio, Product Judgment Test)
   - `01-Company-Context/` – for company strategy, vision, stakeholders
   - `02-Methods-and-Tools/` – for frameworks, guides, templates, playbooks
   - `03-Research-Artifacts/` – for research storage structure
   - `04-Initiatives/` – for opportunity assessments and initiative planning

2. **Before using templates: Braindump first**
   - Don't jump straight to filling templates. Start by dumping your thoughts, ideas, and concerns.
   - **To start a product-thinking chat (e.g. with Cursor):** Open [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) and copy the **Simple prompt to start** at the top into a new chat.
   - Use the braindumping prompts in each framework to capture your raw thinking first.
   - Let your product sense and intuition guide initial thoughts before structuring them.

3. **Copy** the relevant README + template files.

4. **Paste** into your AI chat session with a prompt like:
   ```
   Here's the structure I use for [product strategy / PRDs / OKRs / etc.].
   
   First, help me braindump my thoughts on [topic]. Quiz me, challenge my assumptions, and help me think through this before we structure it.
   
   Then help me fill it out / adapt it for [my context].
   ```
4. **Save for reuse** (recommended):
   - Upload files to your AI tool's project feature (ChatGPT's "My GPTs", Claude's "Projects", etc.)
   - Or save the conversation for future reference
   - Reuse templates without re-copying each time

### Option 2: Technical (Clone & Use with IDE AI Tools)

**Best for:** GitHub users with VS Code, Cursor, GitHub Copilot, Replit, or similar IDE AI tools.

1. **Clone** the repo:
   ```bash
   git clone https://github.com/andreaskelm/pm-brain.git
   cd pm-brain
   ```

2. **Plug in your context:**
   - Replace placeholders in `01-Company-Context/` with your actual vision, strategy, principles
   - Customize templates in `02-Methods-and-Tools/` for your workflows

3. **Start using (think first, structure second):**
   - **Braindump before structuring**: Use the braindumping prompts in each framework to capture your raw thoughts first
   - **Develop product sense**: Use the product sense exercises and reflection prompts to build judgment
   - **Think critically**: Let frameworks guide your thinking, not replace it. Answer the quiz questions honestly.
   - Use `00-Meta/` for daily log, learning log, growth portfolio, and the Product Judgment Test (log forecasts before ship, track calibration)
   - Use frameworks and guides in `02-Methods-and-Tools/` for daily work
   - Store research in `03-Research-Artifacts/`
   - Document initiatives in `04-Initiatives/`

4. **Optional:** Point your IDE's AI tools at this repo as project context.

### Option 3: Install as a Cursor skill (skills.sh)

**Best for:** Cursor users who want the PM Brain workflow skill in any project without cloning the full repo.

Install the PM Brain skill so Cursor’s agent can use it when you work on product management tasks:

```bash
npx skills add andreaskelm/pm-brain
```

This installs the skill from the [Agent Skills Directory](https://skills.sh/) into your `.cursor/skills/` directory. The skill guides the AI through PM Brain frameworks (braindump-first, strategy → discovery → execution, product sense). Use it in any repo where you do PM work.

---

## 🏗️ System Structure Philosophy

This is a **PM brain-as-code**, not a random notes folder. The directories represent different **types of work** and **layers of your product system**, not a rigid sequential process.

> **📖 Want to know more about how to use this system?** See [`GUIDELINES.md`](./GUIDELINES.md) for best practices on linking to external sources, collaboration, and maintaining your PM brain.

### Four Core Layers

```text
pm-brain/
├── 00-Meta/                    # 🧠 Personal practice (daily log, learning log, growth portfolio, Product Judgment Test)
├── 01-Company-Context/        # 🏢 Strategic foundation (vision, strategy, metrics, stakeholders)
├── 02-Methods-and-Tools/      # 🧭 PM operating system (frameworks, guides, templates, prompts)
├── 03-Research-Artifacts/     # 🔍 Evidence layer (interview notes, synthesis, findings)
└── 04-Initiatives/            # 🚧 Active bets (early thinking, opportunity assessments, docs)
```

### Optional Layers

```text
├── 08-Prototypes/             # 🧪 Experiments and prototype implementations
└── 09-Personal-Context/       # 🧑 Personal notes (keep sensitive content in private fork)
```

---

## 🧠 Product Sense: The Thread Through Everything

Strategy, discovery, execution, and communication only work if you *think* before you structure. Product sense is what ties that thinking together—braindump first, then pick the right framework. No template can replace it.

**Golden rule:** [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) — braindump before structure.

**Start here:** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md). Copy the simple prompt at the top into a new chat; the agent will ask hard questions and braindump with you, then point you to Strategy, Discovery, Execution, or Communication. After that, practice and track in `00-Meta/` (daily log, learning log, growth portfolio, [Product Judgment Test](00-Meta/0.3-Product-Judgment-Test/) for calibration). Full guide: [00-Meta/README.md](00-Meta/README.md).

---

## 🔄 Daily Workflow

1. **Practice & track** `00-Meta/` for daily log, learning log, growth portfolio, and Product Judgment Test (log forecasts before ship, resolve when data is in).
2. **Reference** `01-Company-Context/` for strategic direction and company information.
3. **Use** `02-Methods-and-Tools/` when you need a process, framework, template, or playbook.
4. **Store** research outputs in `03-Research-Artifacts/` after completing discovery work.
5. **Do** your active product work in `04-Initiatives/` (planning, documenting, iterating).

### How Frameworks Work Together

The frameworks follow a natural product development flow:

**0. Early Thinking** (`04-Initiatives/`) → Capture ideas and hypotheses

**1. Discover** (`2.2-Discovery/`) → Interview users, observe behavior, collect stories

**2. Define** (`2.2.3-Jobs-To-Be-Done/`) → Frame problems as jobs and opportunities

**3. Assess** (`2.2.4-Opportunity-Assessment/`) → Document and assess opportunities

**4. Decide** (`2.2.5-Idea-Validation/`) → Generate solutions and validate assumptions

**5. Deliver** (`2.3-Execution/2.3.4-PRD/`) → Write requirements and build

**6. Launch & Learn** (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/` and `2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/`) → Measure outcomes and iterate

See `02-Methods-and-Tools/README.md` for complete navigation guide.

---

## 📋 Quick Start Guides

**New Team Member:**
1. Read `01-Company-Context/` to understand vision, strategy, decision-making
2. Browse `02-Methods-and-Tools/` to see team approaches
3. Study `03-Research-Artifacts/` before talking to customers
4. Review `04-Initiatives/` to see what's in-flight

**Experienced PM:**
1. Go to `02-Methods-and-Tools/` for the topic you need (PRDs, discovery, OKRs)
2. Grab the relevant framework + guide + template
3. Use `00-Meta/` for daily log, learning log, growth portfolio, and Product Judgment Test if you track calibration
4. Update frameworks when reality diverges — commit improvements
5. Keep `01-Company-Context/` updated for newcomers

**Crisis or Time Pressure:**
1. Go to relevant framework in `02-Methods-and-Tools/` (e.g., `2.4-Communication/2.4.4-Crisis-Management/`)
2. Use connected guides and templates to respond quickly
3. Log learnings in framework guides to improve the system

---

## 🤝 Contributing

Two ways to use this:

1. **Fork privately** (recommended for real company context)
   - After forking, choose **Private** or **Team** mode manually: append `.gitignore.private` or `.gitignore.team` to `.gitignore`, then commit
   - See [`00-Meta/MODE-SELECTION-GUIDE.md`](./00-Meta/MODE-SELECTION-GUIDE.md) for details
   
2. **Contribute improvements** to public template (generic frameworks, guides, patterns)
   - Keep this repo in **Public** mode (default)
   - Share sanitized learnings and framework improvements

When contributing:
1. Follow established folder and naming conventions
2. Keep examples generic (no proprietary information)
3. Use clear commit messages (what changed, why, for whom)
4. Share learnings: mention scenarios the guide handles
5. Respect placeholders: use brackets where teams plug in context

---

## 👤 Created by [Andreas Kelm](https://github.com/andreaskelm)

⭐ Star this repo if you find it useful • 🔀 Fork it to customize for your team

---

## 📚 Credits & Attributions

This repository builds on frameworks from product management thought leaders. See [CREDITS](./CREDITS.md) for full attributions and ways to support the original creators.

**Related documentation:**
- [Setup Guide](./SETUP.md) - Detailed setup instructions
- [Guidelines](./GUIDELINES.md) - Best practices for using and maintaining your PM brain

---

## 📄 License

This work is licensed under CC BY-NC-SA 4.0.

Copyright © 2025 Andreas Kelm. You may view, use, modify, and share this repo with attribution for non-commercial purposes. Commercial sale is not permitted, but you may use it internally for work and business.

See [`LICENSE`](./LICENSE) for full terms, or view the [Creative Commons legal code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
