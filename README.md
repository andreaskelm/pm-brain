# 🧠 PM Brain-as-Code

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain) [![GitHub forks](https://img.shields.io/github/forks/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain/fork)

> **Your external product management brain. Single source of truth = latest commit.**

A living knowledge base that bridges the gap between Product Management frameworks and actual execution. Git-versioned, shareable, ready to use.

**Product teams drown in blog posts and frameworks** but don't know *how* to run sprint planning or write a strategy document by EOD. This gives you battle-tested guides, templates, and playbooks—and **product sense is built in**: when you work with the repo (e.g. in Cursor), the agent guides you to think first, then structure.

---

## Start here

**I'm a human.**  
→ [docs/setup.md](docs/setup.md) for installation and configuration.  
→ [docs/architecture.md](docs/architecture.md) for repo layers and methods flow.  
→ Browse [02-Methods-and-Tools/](02-Methods-and-Tools/) for frameworks.  
→ [docs/guidelines.md](docs/guidelines.md) for how to use and maintain.

**I'm an AI agent (Cursor / Claude Code / etc.).**  
→ Load [AGENTS.md](AGENTS.md) (persona), [ORCHESTRATION.md](ORCHESTRATION.md) (routing, states), [MEMORY.md](MEMORY.md) (what to wake when).  
→ Product thinking entry: [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md).  
→ Template finder: [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md).  
→ Golden rule: braindump before structure; check [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md). Always check the filesystem before asking the user if context exists.

**I'm forking this for my company.**  
→ Fork the repo, then follow [docs/setup.md](docs/setup.md) (modes, Company Context, agent config).  
→ Fill `01-Company-Context/` with your context.  
→ Optional: append `.gitignore.private` or `.gitignore.team` to `.gitignore` (see [00-Meta/MODE-SELECTION-GUIDE.md](00-Meta/MODE-SELECTION-GUIDE.md)).

---

## 📦 What's inside

```text
pm-brain/
├── 00-Meta/                    # Personal practice (daily log, learning log, growth portfolio, Product Judgment Test)
├── 01-Company-Context/         # Vision, strategy, principles, stakeholders
├── 02-Methods-and-Tools/       # Frameworks, guides, templates (think → strategy → discovery → execution → communication)
├── 03-Research-Artifacts/     # Research storage
├── 04-Initiatives/             # Active bets (opportunity assessments, PRDs, docs)
└── docs/                       # Setup, guidelines, architecture, credits, agent-manifest
```

**Latest commit = current reality.** No stale Notion or Confluence pages.

---

## 💡 What this is / What it isn't

**What it is:**  
A bridge from PM theory to daily execution: frameworks plus an agent that guides you to think first, then structure your messy thinking into clear artifacts. A place to store the messy reality of product work using git as the single source of truth. A way to make AI useful for product work: give it your company context, a framework, and a template, and it helps condense your braindump into structured thinking.

**What it isn't:**  
Not a productivity tool that saves hours on trivial tasks (it's about better thinking, not faster checkboxes). Not a replacement for project management tools (link to Jira, Confluence, Figma instead of duplicating). Not about perfect prompts (the agent guides; you do the thinking, deciding, and writing).

---

## 🚀 Get started (humans)

1. **Clone or fork** (fork recommended if you'll add company-specific context):
   ```bash
   git clone https://github.com/andreaskelm/pm-brain.git
   cd pm-brain
   ```
2. **Follow [docs/setup.md](docs/setup.md)** — Company Context, AI/agent config, optional 00-Meta setup.
3. **Use the repo** — Open a framework or start a conversation with the agent; it will guide you (think first, then structure, then templates).

**Using the agent (Cursor):** Open this repo in Cursor and start a chat. Say what you're working on ("I'm stuck on prioritization," "Help me think through this feature," "I need to write a PRD"). The agent will guide you and signal when it switches from exploring to structuring. Behavior is defined in [AGENTS.md](AGENTS.md), [ORCHESTRATION.md](ORCHESTRATION.md), and [MEMORY.md](MEMORY.md); see [.cursor/rules/](.cursor/rules/README.md).

**Use PM Brain in any project (Cursor only):**
```bash
npx skills add andreaskelm/pm-brain
```
Installs the workflow skill from [skills.sh](https://skills.sh/).

---

## 🏗️ Structure & navigation

- **Visual & design principles:** [docs/architecture.md](docs/architecture.md) — repo layers, methods flow, why the repo is structured this way.
- **Agent behavior:** [ORCHESTRATION.md](ORCHESTRATION.md) — routing, states, context loading; [MEMORY.md](MEMORY.md) — when to load company/initiatives/research.
- **I need a template:** [02-Methods-and-Tools/0-template-finder.md](02-Methods-and-Tools/0-template-finder.md).
- **Everything about a topic:** [02-Methods-and-Tools/1-frameworks-by-topic.md](02-Methods-and-Tools/1-frameworks-by-topic.md).
- **Evals:** [.cursor/evals/README.md](.cursor/evals/README.md) — when to run and where to update; see ORCHESTRATION.md → Eval Checkpoints.
- **How to use and maintain:** [docs/guidelines.md](docs/guidelines.md).

Product sense (think first, then structure) is built into the agent; see [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) and [0-start-here-product-thinking](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md).

---

## 🤝 Contributing

- **Fork (private)** for company context: after forking, append `.gitignore.private` or `.gitignore.team` to `.gitignore`. See [00-Meta/MODE-SELECTION-GUIDE.md](00-Meta/MODE-SELECTION-GUIDE.md).
- **Contribute** improvements to the public repo (frameworks, guides, patterns); keep examples generic.

Conventions: follow folder/naming in the repo, clear commit messages, no proprietary info in examples.

---

## 👤 Created by [Andreas Kelm](https://github.com/andreaskelm)

⭐ Star if useful · 🔀 Fork to make it yours

---

## 📚 Credits & license

Frameworks from product management thought leaders. See [docs/credits.md](docs/credits.md).

CC BY-NC-SA 4.0 — view, use, modify, share with attribution; non-commercial. See [LICENSE](LICENSE).
