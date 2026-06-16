# PM Brain Setup Guide

> **Welcome!** This guide gets you from zero to running in under 30 minutes.

## Fork it—but make it private

PM Brain is designed to be **forked and made your own**—but the original repo is public, so any fork defaults to public too. Your company context, roadmaps, and stakeholder info should NOT be visible to everyone.

Fork it, make it private, then add your context. Don't accidentally push company strategy to the internet.

See [Step 1: Get the Repository](#step-1-get-the-repository) for exact instructions.

---

## First: Choose Your AI Tool

Your tool choice affects how PM Brain wires the agent bootstrap—some platforms auto-inject enforcement rules, others require the agent to read the full bootstrap set explicitly each session.

| Tool | Entry point auto-loads? | Bootstrap read |
|------|-------------------------|----------------|
| **Cursor** | Yes — `.cursor/rules/pm-brain.mdc` injected | AGENTS + pm-brain.mdc + MEMORY + USER |
| **VS Code + GitHub Copilot** | Yes — `.github/copilot-instructions.md` | Same four files (agent reads via tool) |
| **Claude Code** | Partial — `CLAUDE.md` auto-discovered | Same four files (agent reads via tool) |
| **ChatGPT / Claude.ai** | No — paste bootstrap block | Same four files (manual paste) |

See [platform-setup.md](platform-setup.md) for full per-tool instructions.

**The fastest path:** once you have the repo open in your AI tool, say **"help me set up PM Brain"**—the agent reads the repo, flags placeholders, and guides you through the rest.

---

## Quick Start

1. **Get the repo**—fork it privately, clone locally, or stay local (Step 1)
2. **Open in your AI tool**—IDE (Cursor, VS Code) or web-based (Claude.ai, ChatGPT). See the [AI Tool section above](#first-choose-your-ai-tool) and [platform-setup.md](platform-setup.md) for per-platform details
3. **Say "help me set up PM Brain"**—the agent reads the repo, flags placeholders, guides you

---

## Step 1: Get the Repository

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
If you get a merge conflict, it's almost always in a file where you have real company content that the upstream version replaced with a placeholder—keep yours (`git checkout --ours <file>`). Private fork note: GitHub won't let you open a PR from a private fork to the public upstream directly. If you want to contribute improvements back, either push a branch directly to upstream (if you have access) or make the branch temporarily public.

**Alternatives**

- **Local only (no GitHub):** Clone directly—no GitHub account, no privacy risk, no syncing.
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
- **Team/org repo:** Fork into a private org repo instead of a personal one, then follow [Step 3](#step-3-choose-public--private--team-mode) → Team mode.

## Step 2: Understand the Structure

PM Brain uses **numbered top-level folders (1–5)** so you always know *what kind of content* belongs where. The number is not decorative—it is the mental model for the repo.

### The 1–5 model

| # | Folder | What goes here | You customize? |
|---|--------|----------------|----------------|
| **1** | `1-Context/` | Company vision, strategy, stakeholders, org survival | **Yes**—your company |
| **2** | `2-Methods/` | Frameworks, templates, playbooks (Strategy → Communication) | Mostly no—use as reference |
| **3** | `3-Work/` | Active initiatives—one folder per bet (PRD, roadmap, decisions) | **Yes**—your work |
| **4** | `4-Research/` | Research artifacts—interviews, synthesis, qualitative findings | **Yes**—your evidence |
| **5** | `5-Growth/` | Personal practice—logs, learning log, growth portfolio, Product Judgment Test | **Yes**—your growth |

**Unnumbered infrastructure** (not part of the 1–5 content model):

| Folder / file | Role |
|---------------|------|
| `system/` | Agent orchestration, coaching prompts, skills, evals |
| `docs/` | Human docs (this guide, architecture, principles) |
| `AGENTS.md` | Persona, principles, routing intent — bootstrap file 1 |
| `.cursor/rules/pm-brain.mdc` | Enforcement (voice, lenses, braindump floor) — bootstrap file 2 |
| `system/MEMORY.md` | Sleeping memory manifest — bootstrap file 3 |
| `USER.md` | Your profile — bootstrap file 4 (customize in Step 4) |
| `CLAUDE.md` | Claude Code entry point (auto-discovered) |
| `.github/copilot-instructions.md` | GitHub Copilot entry point (auto-loads) |

**Nested numbering inside `2-Methods/`:** Subfolders use their own 1–5 sequence (`1-Foundations` → `5-Communication`). That is *domain* numbering inside the methods library—not the same as the top-level 1–5 folders.

### Folder tree (canonical layout)

```text
pm-brain/
|-- 1-Context/                 # YOUR company direction & constraints
|   |-- CONTEXT-HEALTH.md      # Freshness tracker (add when you have multiple docs)
|   |-- 1-company-vision.md
|   |-- 2-company-strategy.md
|   |-- 1.1-Stakeholder-Avatars/   # Optional: simulate stakeholder reactions
|   +-- 1.2-Organization-Survival/ # Power map, politics, red flags
|-- 2-Methods/                 # Frameworks & templates (ready to use)
|   |-- 1-Foundations/         # Think first, mental models, bias, product sense
|   |-- 2-Strategy/              # OKRs, roadmap, north star, prioritization
|   |-- 3-Discovery/             # Interviews, JTBD, opportunity assessment
|   |-- 4-Execution/             # PRD, backlog, metrics, rituals
|   +-- 5-Communication/         # Stakeholders, one-pagers, documentation standards
|-- 3-Work/                    # YOUR active initiatives (one folder per bet)
|   +-- 1-Initiative-Codename/   # Example structure—copy when starting real work
|-- 4-Research/                # YOUR research storage (link to initiatives)
|   |-- 1-User-Interviews/
|   +-- 2-Qualitative-Research/
|-- 5-Growth/                  # YOUR personal practice & evidence
|   |-- 1-Learning-Log/
|   |-- 2-Growth-Portfolio/
|   |-- 3-Product-Judgment-Test/
|   +-- 4-Coaching-Templates/
|-- system/                    # Agent infrastructure (orchestration, coaching, skills)
|-- docs/                      # Human documentation
|-- .cursor/rules/             # Cursor always-on rules (pm-brain.mdc)
|-- .github/                   # Copilot instructions, CI workflows
|-- AGENTS.md                  # Bootstrap anchor
|-- CLAUDE.md                  # Claude Code entry point
+-- USER.md                    # Customize first (Step 4)
```

### How the pieces connect

Typical flow across the numbered folders:

```text
1-Context (constraints) → 2-Methods (how to think) → 4-Research (evidence)
        → 3-Work (initiative docs) → 5-Growth (what you learned)
```

- **`1-Context/`** grounds advice in *your* strategy and stakeholders.
- **`2-Methods/`** is the library—braindump first via [system/coaching/README.md](../system/coaching/README.md), then pick a framework.
- **`4-Research/`** stores evidence; link from initiative `research/` folders in `3-Work/`.
- **`3-Work/`** is where day-to-day product work lives—PRDs, roadmaps, decision logs.
- **`5-Growth/`** captures practice over time—daily logs, learning syntheses, forecast calibration.

More detail: [principles.md](principles.md) (where things go) and [architecture.md](architecture.md) (system overview). If you see legacy `00–04` prefixed folders, see [legacy-migration.md](legacy-migration.md).

## Step 3: Choose Public / Private / Team Mode

This repo supports three usage modes. The `.gitignore` file contains all three as clearly labeled, commented-out blocks—public is active by default, and private/team are ready to uncomment.

### Modes at a Glance

- **Public** (default, nothing to do)
 - **Best for**: open learning, public examples, blog/portfolio content.
 - **Tracked**: everything (frameworks, `5-Growth/` logs, `1-Context/`, `3-Work/` initiatives).

- **Private**
 - **Best for**: real company work or personal growth where content must not leak.
 - **Tracked**: frameworks and docs only.
 - **Ignored**: `5-Growth/` practice logs, growth portfolio, `1-Context/`, `3-Work/` initiatives, `4-Research/` artifacts, personal configuration (`USER.md`).

- **Team**
 - **Best for**: a shared frameworks repo, with each person keeping their own practice private.
 - **Tracked**: `2-Methods/` and shared docs.
 - **Ignored**: each contributor's `5-Growth/` logs, `1-Context/`, `3-Work/`, `4-Research/`, personal growth artefacts, personal configuration (`USER.md`).

### How to Apply a Mode

**Tell the agent your mode**—the simplest path:

> "Switch me to private mode" (or team / public)

The agent will uncomment the right block in `.gitignore`, commit it, and list any files already tracked in git that might contain sensitive information so you can decide whether to un-track them.

**Check your GitHub repo visibility** before your first push. If you're in private or team mode, your repo must be set to Private on GitHub: Settings → Danger Zone → Change visibility.

**Switching modes after already committing files:** `.gitignore` only gates future untracked files. Files already in git history stay tracked regardless. To un-track a file that was already committed:

```bash
git rm --cached <file>
git commit -m "setup: un-track sensitive file"
```

Or ask the agent: *"what tracked files might be sensitive in private mode?"*

---

## Step 4: Customize

**Minimum to start (10 minutes):**

- [`USER.md`](../USER.md) at the repo root—your name, role, company, team, what you build, and how you work (working preferences, strengths, challenges, communication style). For other tools without repo file access, paste this content as part of your system prompt—see [platform-setup.md](platform-setup.md).

**Agent bootstrap (every conversation, all platforms):** The agent reads four files in order before responding: [AGENTS.md](../AGENTS.md) → [`.cursor/rules/pm-brain.mdc`](../.cursor/rules/pm-brain.mdc) → [system/MEMORY.md](../system/MEMORY.md) → [USER.md](../USER.md). Cursor auto-injects `pm-brain.mdc`; Claude Code and Copilot read it via their entry-point checklists. Per-tool wiring: [platform-setup.md](platform-setup.md).

**Add as you go (follow the 1–5 model):**

| When you need— | Start here |
|----------------|------------|
| Grounded strategic advice | `1-Context/` (vision, strategy, stakeholders) |
| Freshness tracking for context docs | `1-Context/CONTEXT-HEALTH.md` |
| Stakeholder simulation | `1-Context/1.1-Stakeholder-Avatars/` |
| Deliberate product sense practice | `5-Growth/` daily log + forecast calibration |
| Evidence from discovery | `4-Research/` then link from `3-Work/[initiative]/research/` |

**Not sure what context you have?** Start with your team. Fill in what you know, mark gaps with "TBD" or "unclear", and treat the files as working hypotheses—not finished documents. As you learn more, you update them.

If your org has layers (company → division → business unit → team), don't try to model all of them upfront. Start at the level you actually work at—usually your team or business unit—and add layers only when the distinction matters for your work.

**A note on git tracking:** In private/team modes, `USER.md` is ignored by git—your personal context stays private. See Step 3 to configure your mode.

---

## Step 5: Start Using It

Bring a real problem you're working on—a feature you're scoping, a decision you're stuck on, a stakeholder situation you're navigating. Open a chat with your AI tool and describe it.

Don't try to pick the right framework first. The agent's job is to help you think through the mess before suggesting any structure. Lead with the problem; let the conversation go where it needs to go.

The frameworks are there when you need them. [system/coaching/README.md](../system/coaching/README.md) is the entry point—it has a simple prompt to start, then maps frameworks by situation. Or browse [2-Methods/README.md](../2-Methods/README.md) directly. But the braindump comes first.

---

## Step 6: Set Up Your First Initiative

When you have something worth tracking, create an initiative under **`3-Work/`** (folder **3** in the 1–5 model—active work):

1. **Navigate to:** `3-Work/`
2. **Create a new folder:** `[initiative-name]/` (or copy the example: `1-Initiative-Codename/`)
3. **Use this structure** (from the example initiative):
   - `README.md`—folder overview
   - `opportunity-assessment.md`—early thinking and hypotheses
   - `summary.md`—one-pager when more concrete
   - `prd.md`—requirements when ready to build
   - `roadmap.md`—milestones and sequencing
   - `decisions.md`—decision log (what / why / who / when)
   - `risks.md`—key risks and mitigations
   - `research/`—links to artifacts in `4-Research/`
   - `stakeholders/`—stakeholder map and comms plan
   - `metrics/`—initiative success metrics

4. **Start with:** `opportunity-assessment.md` or `summary.md`—whatever matches how concrete the idea is.

Store raw research (recordings, large files) externally; keep analysis and links in `4-Research/` and reference them from `3-Work/[initiative]/research/`.

**This is where you'll do your actual product work!**

---

## Step 7: You're Ready

Open a chat with your AI tool and say: **"verify my PM Brain setup is complete and aligned with best practices"**—it will read your context files, check that placeholders are filled, and flag anything missing.

From here, everything is driven by real work and real problems.

---

## Reference

- **Overview and philosophy:** [README.md](../README.md)
- **Where things go (1–5 summary):** [principles.md](principles.md)
- **System architecture:** [architecture.md](architecture.md)
- **Product thinking entry point:** [system/coaching/README.md](../system/coaching/README.md)
- **Golden rule:** [system/coaching/braindump.md](../system/coaching/braindump.md)—braindump before structure
- **Best practices:** [principles.md](principles.md)
- **Per-tool instructions:** [platform-setup.md](platform-setup.md)
- **Fork eval CI and harness:** [evals-fork.md](evals-fork.md)
- **Legacy folder migration:** [legacy-migration.md](legacy-migration.md)
- **All human docs index:** [README.md](README.md)
- **Framework navigation:** [2-Methods/README.md](../2-Methods/README.md)
- **Template finder:** [2-Methods/0-template-finder.md](../2-Methods/0-template-finder.md)
