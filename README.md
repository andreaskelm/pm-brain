# 🧠 PM Brain-as-Code

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain) [![GitHub forks](https://img.shields.io/github/forks/andreaskelm/pm-brain?style=social)](https://github.com/andreaskelm/pm-brain/fork)

> **PM Brain-as-Code** — your **external product management OS**: a **second brain** you own in git. **Single source of truth for knowledge and decisions** — the latest commit.

<p align="center"><img src="assets/pm-brain-hero.png" alt="From messy thinking to structured insight" width="560"></p>

You have probably felt this before:

- *"Sprint planning starts in 30 minutes and we still do not have a clear prioritization call."*
- *"Leadership wants the strategy doc by EOD and I am still stitching context from Confluence, Jira, old email, and town-hall slides from four months ago."*
- *"A stakeholder flips right before go-live — and we postpone or kill launch over something we could have pressure-tested upfront."*

Product work is messy. A lot of the time it is brain soup. Context lives in Notion, Linear, Slack, dashboards, and slides — and six weeks after a prioritization fight, nobody remembers why you killed the other option. PM Brain keeps **knowledge, reasoning, and decisions** next to the work: plain markdown in a repo on your machine, versioned like code.

**A thinking partner that defaults to challenge, not validation** — not a template vending machine. The full behavior is spelled out under [What it actually is](#what-it-actually-is); skills (PRD, OKR, roadmap, discovery, prioritization, politics, weekly review, …) are how work gets structured once thinking is solid; `AGENTS.md` is who shows up in the conversation.

Jira, Confluence, and Figma stay where they are — you link out. This repo is the layer for **intent, bets, evidence, and the calls you would reopen if the world changed**.

If you want setup first, jump to [Getting started](#-getting-started).

---

## What it actually is

Most PM tools are built for execution. They assume the problem is already clear and the organization is already aligned.

PM Brain is built for everything that happens **before** that — the messy, ambiguous, politically loaded work of figuring out what is worth doing and getting people to agree.

**A thinking partner that defaults to challenge, not validation.**  
The PM Brain Coach does not start by handing you a template. It starts by asking for a braindump, then asks a few uncomfortable questions before any structure is suggested. It stays in **product_sense** until the [braindump floor](system/coaching/braindump.md#sufficiency-criteria) is real, not performative:

- Your assumptions are named  
- You have separated what you know from what you are guessing  
- At least one risk or second-order effect is on the table  
- At least one uncomfortable thought challenges the plan  

Only then does it route to a **skill** in `.claude/skills/` — workflows with templates and quality criteria, not a wall of generic framework docs. Along the way it names biases lightly, pressure-tests hypotheses (“what would be the first signal you’re wrong?”), and keeps the judgment call with you.

**An organizational survival system.**  
You build stakeholder avatars — profiles with goals, fears, incentives, real phrases, and historical behavior. You map power structures, alliances, fault lines, and veto holders. You log the “Red Weddings” so you do not walk into the same one twice. The agent can answer “What would my manager say about this?” with both an out-loud reaction and an inner monologue.

**A learning and growth system.**  
Most PMs have no idea if their judgment is actually improving — hindsight makes everyone sound calibrated. PM Brain treats **product sense** as a skill you can practice with evidence:

- **[decisions.md](5-Growth/decisions.md)** — log calls with confidence and reopen triggers *before* outcomes land; score calibration when you know the result ([background](2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/8-calibration.md))  
- **[weekly/](5-Growth/weekly/README.md)** — one short note per week: live assumptions, drift, what you are avoiding (weekly review skill drafts it; you correct it)  
- **Optional depth** — monthly synthesis, post-project reflection, and 1:1-ready narrative in [2-Methods/1-Foundations/3-Self-Reflection/](2-Methods/1-Foundations/3-Self-Reflection/README.md); research insights stay in [4-Research/](4-Research/README.md), not in Growth  

The folder is deliberately small so you actually use it. Rationale: [5-Growth/README.md](5-Growth/README.md).

**Context that does not rot.**  
The wake table in [AGENTS.md](AGENTS.md#where-things-live-wake-on-demand) tells the coach what to load when — company context, initiatives, research, stakeholders — instead of dumping the whole repo into context. That is **instruction to the agent** (minimal footprint), not a hard platform lock; it holds when your tool loads `AGENTS.md` and the model follows it. Long sessions: capture durable state in `5-Growth/` or `3-Work/[initiative]/` ([`system/ORCHESTRATION.md`](system/ORCHESTRATION.md)).

**Platform-agnostic.**  
Cursor, Claude Code, VS Code Copilot, Claude.ai, ChatGPT, or any tool that can read repo files. Bootstrap: **`AGENTS.md`** (+ **`USER.md`** when present). Workflows: **`.claude/skills/`**; delegation: **`.claude/agents/`**. Routing: `system/ORCHESTRATION.md` at state entry. Wiring: [docs/platform-setup.md](docs/platform-setup.md) (model tiers, hooks, live evals).

---

## What it is not

PM Brain is **not**:

- A productivity hack or checkbox system  
- A replacement for Jira, Confluence, or Figma — you link to those, you do not duplicate them  
- A magic-prompt generator that does the work for you  

You still own the thinking and the decisions. The agent is there to challenge, structure, and remember with you.

---

## How the agent works

The PM Brain Coach runs as a lightweight state machine defined in `system/ORCHESTRATION.md`. It operates in four modes:

- **product_sense** — Default when you are thinking through product, strategy, discovery, stakeholders, or organizational dynamics. The agent stays here until the four sufficiency criteria in [braindump.md](system/coaching/braindump.md) are met for real, not on paper.
- **execution_mode** — After enough thinking (or an explicit doc request with preflight), the agent loads the matching **skill** in `.claude/skills/` and guides you through templates and quality checks.
- **meta_reflection** — After substantial decisions or discovery work, the agent suggests logging forecasts, learnings, and patterns in `5-Growth/` and (optionally) running evaluation checklists.
- **conversation** — Navigation, repo questions, and lightweight topics.

State transitions and loading rules: [`system/ORCHESTRATION.md`](system/ORCHESTRATION.md). Maintainer detail: [`docs/architecture.md`](docs/architecture.md).

---

## Skills and subagents

**Skills** (`.claude/skills/`) own workflows — PRD, OKR, roadmap, prioritize, opportunity assessment, politics-coach, weekly review, and more. Pick from the table in [2-Methods/0-index.md](2-Methods/0-index.md) or invoke with `/skill-name` where your platform supports it.

**Subagents** (`.claude/agents/`) handle mechanical or independent work: `context-scout` (repo scan), `artifact-reviewer` (QQC without grading your own draft), `stakeholder-simulator` (avatar-based reactions). Coaching and judgment calls stay in the main thread — see [AGENTS.md](AGENTS.md) → Delegation.

Install skills into another repo (Cursor): `npx skills add andreaskelm/pm-brain` (ships `.claude/skills/` from upstream).

---

## System structure

At the top level, the repo looks like this:

```text
pm-brain/
|-- AGENTS.md                  # Bootstrap — persona, voice, wake table
|-- USER.md                    # Your personal context
|-- .claude/skills/            # Workflows (PRD, OKR, prioritize, …)
|-- .claude/agents/            # Subagents (scout, reviewer, simulator)
|-- system/                    # Orchestration, coaching, evals
|-- 1-Context/                 # Vision, strategy, stakeholders, org survival
|-- 2-Methods/                 # Reference — mental models, guides (0-index → skills)
|-- 3-Work/                    # Active initiatives
|-- 4-Research/                # Research artifacts
|-- 5-Growth/                  # decisions.md + weekly/
|-- docs/                      # Setup, principles, architecture (docs/README.md)
+-- .cursor/                   # Hooks (Cursor)
+-- .github/                   # CI workflows
```

**Latest commit = source of truth** for knowledge and decisions in this repo. Maintainer architecture: [`docs/architecture.md`](docs/architecture.md).

---

## The organizational survival layer

This is the part most PM systems ignore.

`1-Context/1.1-Stakeholder-Avatars/` holds your cast — one file per person. Each avatar captures:

- Explicit and implicit goals  
- Fears and incentives  
- Real phrases they use  
- Historical behavior and tells  

The `politics-coach` skill uses these to simulate reactions: out-loud response, inner monologue, top objections, and how to de-risk for that person specifically.

`1-Context/1.2-Organization-Survival/` maps the system:

- Power map — who formally owns decisions vs. who actually decides, who can quietly veto  
- Political landscape — alliances, fault lines, protected systems, narrative landmines  
- Stakeholder games — recurring behavior patterns and how to work with them  
- Coalitions and timing — what needs to be sequenced before big moves  
- Red flags and history — the “Red Weddings” log so you spot patterns earlier next time  

After a political incident or a “we should have seen this coming” moment, the agent nudges you to update these documents. The system learns from your actual organization, not an idealized one.

---

## Practice loop (`5-Growth/`)

Same story as [learning and growth](#what-it-actually-is) above — two files you can actually keep current: [decisions.md](5-Growth/decisions.md) and [weekly/](5-Growth/weekly/README.md). When you say 70%, are you right about seven times out of ten? That is the point. Details: [5-Growth/README.md](5-Growth/README.md).

---

## Evaluation system

PM Brain uses two related eval layers — do not conflate the naming:

- **Artifact QQC (methods “Level 1”).** Quick Quality Checks built into key frameworks (OKRs, roadmaps, PRDs, opportunity assessments, North Star, one-pagers). They run while you create artifacts to catch thin problem definitions, missing risks, or weak metrics. Rules: [system/EVALUATION.md](system/EVALUATION.md).
- **Harness tiers L0–L4 (`system/evals/`).** Repo health (L0), rubric regression (L1), behavior scenarios (L2), human review (L3), in-turn write hooks (L4). Use these to check whether the agent honored the golden rule, stayed in product_sense long enough, and surfaced meaningful risks.

Overview: [system/evals/README.md](system/evals/README.md). CI and local commands: [docs/evals-fork.md](docs/evals-fork.md).

---

## 🚀 Getting started

You can use PM Brain either directly in an AI chat tool or in an IDE.

### Option 1: AI chat tools (Claude.ai, ChatGPT, Gemini, etc.)

1. Browse to the folder you need in this repo.  
2. Copy the relevant `README` + framework + template files.  
3. Paste them into your AI chat with a prompt like:  
   > “Here is my PM system. First, help me braindump my thoughts on **[topic]**. Challenge my assumptions and help me think before we structure anything.”  
4. Save that context in your AI tool’s project or workspace feature for reuse.

### Option 2: IDE tools (Cursor, VS Code + Copilot, Claude Code)

1. **Clone or fork** (fork recommended if you will add company-specific context):

   ```bash
   git clone https://github.com/andreaskelm/pm-brain.git
   cd pm-brain
   ```

2. **Follow [`docs/setup.md`](docs/setup.md)** — configure Company Context, privacy mode, and optional `5-Growth/` setup.
3. **Wire the agent per tool:** [`docs/platform-setup.md`](docs/platform-setup.md) — AGENTS.md bootstrap, skills, model tiers.
4. **Use the repo in your IDE** — open a framework or start a conversation with the agent; it will guide you (think first, then structure, then templates).

**Using the agent in Cursor.**
Open this repo in Cursor and start a chat. Say what you are working on (“I am stuck on prioritization,” “Help me think through this feature,” “I need to write a PRD”). The agent will guide you and signal when it switches from exploring to structuring. Bootstrap: `AGENTS.md` + `USER.md`. Platform wiring: [docs/platform-setup.md](docs/platform-setup.md).

**Use PM Brain skills in another repo (Cursor):** `npx skills add andreaskelm/pm-brain` — installs `.claude/skills/` from upstream.

**Who it is for, a typical day, and upkeep cadence:** [docs/setup.md](docs/setup.md#who-its-for) (onboarding doc — keeps this README focused on *what* PM Brain is).

---

## Start here (quick navigation)

If you are new and just want the right entry point:

- **Setup & install:** [`docs/setup.md`](docs/setup.md)  
- **Agent wiring (AGENTS.md + skills per platform):** [`docs/platform-setup.md`](docs/platform-setup.md)  
- **All human docs index:** [`docs/README.md`](docs/README.md)  
- **Architecture:** [`docs/architecture.md`](docs/architecture.md)  
- **Design principles & repo maintenance:** [`docs/principles.md`](docs/principles.md)  
- **Migrating from old folder layout:** [`docs/legacy-migration.md`](docs/legacy-migration.md)  
- **I want to think through a product decision:**  
  → [`system/coaching/README.md`](system/coaching/README.md)  
- **I know the workflow I need (PRD, OKR, roadmap, etc.):**  
  → [`2-Methods/0-index.md`](2-Methods/0-index.md) → `.claude/skills/`  
- **I want to see or run evals:**  
  → [`system/evals/README.md`](system/evals/README.md) (CI/harness: [`docs/evals-fork.md`](docs/evals-fork.md))

Product sense (think first, then structure) is built into the agent; see `system/coaching/braindump.md` for the full golden-rule spec.

---

## 🤝 Contributing

- **Fork (private)** for real company context: after forking, tell the PM Brain agent your mode (public/private/team) and it will configure `.gitignore` and surface any sensitive files already tracked. See [`docs/setup.md`](docs/setup.md) → Step 3.  
- **Contribute back** improvements to the public template — new frameworks, better guides, clearer patterns. Keep examples generic and remove proprietary detail.  

Conventions: follow the existing folder and naming patterns, write clear commit messages, and prefer small, reviewable changes.

---

## Created by [Andreas Kelm](https://github.com/andreaskelm)

⭐ Star if useful · Fork to make it yours

---

## Credits & license

Frameworks build on the work of product management thought leaders. See [`docs/credits.md`](docs/credits.md) for attributions.

Licensed under **CC BY-NC-SA 4.0** — view, use, modify, and share with attribution for non-commercial purposes. See [`LICENSE`](LICENSE) for full terms.

