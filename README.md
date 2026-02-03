# 🧠 PM Brain-as-Code

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain) [![GitHub forks](https://img.shields.io/github/forks/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain/fork)

> **Your external product management brain. Single source of truth = latest commit.**

A living knowledge base that bridges the gap between Product Management frameworks and actual execution. Git-versioned, shareable, ready to use.

**Product teams drown in blog posts and frameworks** but don't know *how* to run sprint planning or write a strategy document by EOD. This gives you battle-tested guides, templates, and playbooks—and **product sense is built in**: when you work with the repo (e.g. in Cursor), the agent guides you to think first, then structure.

**Quick links:** [Setup](./SETUP.md) · [Guidelines](./GUIDELINES.md) · [Architecture](./ARCHITECTURE.md) · [Template finder](02-Methods-and-Tools/0-template-finder.md)

**New here?** Open this repo in Cursor and start a conversation—the agent will guide you. No special phrase; say what you're working on (e.g. "I'm stuck on prioritization" or "I need to write a PRD") and you'll be guided.

---

## 📦 What's Inside

```text
pm-brain/
├── 00-Meta/                    # Personal practice (daily log, learning log, growth portfolio, Product Judgment Test)
├── 01-Company-Context/         # Vision, strategy, principles, stakeholders
├── 02-Methods-and-Tools/      # Frameworks, guides, templates (think → strategy → discovery → execution → communication)
├── 03-Research-Artifacts/     # Research storage
└── 04-Initiatives/             # Active bets (opportunity assessments, PRDs, docs)
```

**Latest commit = current reality.** No stale Notion or Confluence pages.

---

## 💡 What this is / What it isn't

**What it is:**
- A bridge from PM theory to daily execution: frameworks plus an agent that guides you to think first, then structure your messy thinking into clear artifacts
- A place to store the messy reality of product work—your raw thinking, decisions, and day-to-day adjustments—using git as the single source of truth
- A way to make AI useful for product work: give it your company context, a framework, and a template, and it helps condense your messy braindump into structured thinking

**What it isn't:**
- Not a productivity tool that saves hours on trivial tasks (it's about better thinking, not faster checkboxes)
- Not a replacement for project management tools (link to Jira, Confluence, Figma instead of duplicating everything here)
- Not about perfect prompts (the agent guides the conversation; you do the thinking, deciding, and writing)

---

## 🚀 Get Started

1. **Clone or fork** (fork recommended if you’ll add company-specific context):
   ```bash
   git clone https://github.com/andreaskelm/pm-brain.git
   cd pm-brain
   ```
2. **Follow [SETUP.md](./SETUP.md)** — Company Context, AI/agent config, optional 00-Meta setup.
3. **Use the repo** — Open a framework or start a conversation with the agent; it will guide you (think first, then structure, then templates).

**Using the agent (Cursor):** Open this repo in Cursor and start a chat. You don't need a special phrase—say what you're working on ("I'm stuck on prioritization," "Help me think through this feature," "I need to write a PRD"). The agent will guide you and signal when it switches from exploring to structuring so you're never lost. [AGENTS.md](./AGENTS.md) and [.cursor/rules/](.cursor/rules/README.md) define this behavior; no copy-paste required.

**Use PM Brain in any project (Cursor only):**
```bash
npx skills add andreaskelm/pm-brain
```
Installs the workflow skill from [skills.sh](https://skills.sh/); use it in any repo where you do PM work.

---

## 🏗️ Structure & Navigation

- **Visual:** [ARCHITECTURE.md](./ARCHITECTURE.md) — repo layers and methods flow.
- **I need a template:** [02-Methods-and-Tools/0-template-finder.md](02-Methods-and-Tools/0-template-finder.md).
- **Everything about a topic:** [02-Methods-and-Tools/1-frameworks-by-topic.md](02-Methods-and-Tools/1-frameworks-by-topic.md).
- **Evals (methods + agent behavior):** [.cursor/evals/README.md](.cursor/evals/README.md) — guidance-based; how it learns and asks you to adapt.
- **How to use and maintain:** [GUIDELINES.md](./GUIDELINES.md).

Product sense (think first, then structure) is **built into** the agent and framework flow; see [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) and [0-start-here-product-thinking](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) if you want the full story.

---

## 🤝 Contributing

- **Fork (private)** for company context: after forking, append `.gitignore.private` or `.gitignore.team` to `.gitignore`. See [00-Meta/MODE-SELECTION-GUIDE.md](00-Meta/MODE-SELECTION-GUIDE.md).
- **Contribute** improvements to the public repo (frameworks, guides, patterns); keep examples generic.

Conventions: follow folder/naming in the repo, clear commit messages, no proprietary info in examples.

---

## 👤 Created by [Andreas Kelm](https://github.com/andreaskelm)

⭐ Star if useful · 🔀 Fork to make it yours

---

## 📚 Credits & License

Frameworks from product management thought leaders. See [CREDITS](./CREDITS.md).

CC BY-NC-SA 4.0 — view, use, modify, share with attribution; non-commercial. See [LICENSE](./LICENSE).
