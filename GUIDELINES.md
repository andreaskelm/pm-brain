## 🧭 PM Brain Usage Guidelines

> **Purpose:** Make this repository a reliable, maintainable **golden record** of your product management thinking and work.

These guidelines describe **how to use and evolve** this repo so it stays useful over time.

---

## 1. Golden Record & External Links

- **Golden record, not full archive**  
  - This repo is the **single source of truth** for product decisions, frameworks, and synthesized knowledge.  
  - It **does not need to contain every artifact** (raw data, full decks, recordings, etc.).

- **Link, don’t duplicate**  
  - Store **structure, decisions, and summaries** here.  
  - Link out to external systems where artifacts live:
    - Docs: Confluence / Notion / SharePoint
    - Dashboards: BI tools, analytics platforms
    - Design: Figma / design system
    - Assets: DAM / shared drives
    - Recordings: meeting / interview recordings

- **Examples**
  - Research:
    - Summary + insights in `03-Research-Artifacts/`
    - Links to full recordings / transcripts in your research tool
  - Metrics:
    - Definitions + targets in metrics docs
    - Links to live dashboards in a “Dashboard links” section
  - Designs:
    - Decision + rationale in initiative docs
    - Links to Figma files / design system components

---

## 2. Where Things Go

- **00-Meta/**  
  - Personal practice: daily log, weekly/monthly reflection, growth portfolio, Product Judgment Test (forecast log, calibration).  
  - Canonical prompts and templates live in `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/`; `00-Meta/` stores what you *do* and *learn*.  
  - See [00-Meta/README.md](00-Meta/README.md) and [MODE-SELECTION-GUIDE.md](00-Meta/MODE-SELECTION-GUIDE.md) for modes (Public/Private/Team).

- **01-Company-Context/**  
  - Vision, strategy, principles, roadmap, stakeholders.  
  - Keep this aligned with **current reality**; update when strategy shifts.

- **02-Methods-and-Tools/**  
  - Frameworks, guides, templates, playbooks.  
  - **2.0-Foundations** (product sense, mental models, bias) → **2.1-Strategy** → **2.2-Discovery** → **2.3-Execution** → **2.4-Communication**.  
  - **Entry point for product thinking:** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md). Prefer **generic, reusable** content here (not initiative-specific).

- **03-Research-Artifacts/**  
  - Research plans, notes, synthesis, key findings.  
  - Link to raw data (recordings, spreadsheets) instead of embedding everything.

- **04-Initiatives/**  
  - Opportunity assessments, PRDs, roadmaps, decision logs, risks, metrics, etc.  
  - One folder per initiative; this is where **day-to-day product work** lives.

When in doubt:  
- **Personal practice / calibration → `00-Meta/`**  
- **Strategy / long-lived context → `01-Company-Context/`**  
- **Reusable method / template → `02-Methods-and-Tools/`**  
- **Evidence / research → `03-Research-Artifacts/`**  
- **Specific bet / project → `04-Initiatives/`**

---

## 3. Naming & Structure Conventions

- **Follow existing patterns**
  - Folders: `X.Y-Name/` (e.g. `2.1-Strategy/`, `4.1-Initiative-Codename/`)
  - Files inside frameworks:
    - `README.md` – overview / navigation
    - `1-*-framework.md` – how to think
    - `2-*-template.md` – fill-in-the-blanks
    - `3-*-evaluation.md` – reflection / assessment (when present)

- **Initiatives**
  - Start from the example in `04-Initiatives/4.1-Initiative-Codename/`
  - Keep a small, predictable set of docs:
    - `summary.md`, `opportunity-assessment.md`, `prd.md`, `roadmap.md`, `decisions.md`, etc.

- **New content**
  - Reuse patterns where possible instead of inventing new structures.  
  - If you need a new framework:
    - Add a folder under the right domain in `02-Methods-and-Tools/`
    - Include at least a `README.md` and a `1-*-framework.md`

---

## 4. Collaboration & Git Habits

- **Small, meaningful commits**
  - Group changes by topic (e.g. “Update opportunity assessment for X”, “Add new research notes for Y”).
  - Write commit messages that explain **what changed and why**.

- **Branches (if working in a team)**
  - Use feature branches for bigger changes:
    - `feature/update-company-context`
    - `initiative/feature-x-prd`
  - Merge via PRs when collaborating, so changes are reviewed.

- **History as thinking log**
  - Treat git history as a **timeline of your product thinking**.
  - Don’t worry about being perfect—opt for frequent, honest commits.

---

## 5. Using AI with This Repo

- **Think first, template second (golden rule)**  
  - See [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md). Start product/stakeholder/org thinking from the **entry point** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md): copy the simple prompt into a new chat; the agent will braindump with you, then point to Strategy, Discovery, Execution, or Communication.  
  - Use frameworks’ **braindump prompts** ([2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md)) before filling in templates.  
  - Ask AI to challenge assumptions, not just “fill the blanks”.

- **Good patterns**
  - “I want to think through something about my product / stakeholder / org…” (then use the prompts the agent suggests).
  - “Help me braindump everything I know about [initiative] before we touch the template.”
  - “Based on my current `opportunity-assessment.md`, what’s unclear or risky?”
  - “Summarize changes between these two versions of the PRD.”

- **Bad patterns**
  - “Write my strategy from scratch” with no context.
  - Jumping straight to a PRD or OKR template without braindumping first.
  - Copy-pasting templates without thinking, then never revisiting.

---

## 6. Privacy & Sensitivity

- **Public vs. private**
  - If this is a public repo or fork, **keep real company-sensitive details in a private fork**.
  - Avoid:
    - Customer PII
    - Confidential financials
    - Security details and secrets

- **Safe patterns**
  - Use anonymized examples and initials where needed.
  - Link to internal systems that require auth for sensitive detail.

---

## 7. Keeping the System Healthy

- **Update when reality changes**
  - Company context, strategy, and principles should match how you actually operate.
  - If frameworks no longer match how you work, update them.

- **Archive stale initiatives**
  - Move completed/abandoned initiatives into an archive folder (e.g. `4.99-Archive/`) while keeping their learnings.

- **Document decisions**
  - Use `decisions.md` in initiatives for:
    - Date
    - Decision
    - Context
    - Owner
    - Links to supporting artifacts

- **Iterate on guidelines**
  - If you notice repeated confusion (“Where do we put X?”, “How do we store Y?”), update this file.

---

## 8. Version Management

**Version tracking:** The repository uses semantic versioning in `version.json` (repo root) to track major structural changes. This helps agents detect when repository structure changes and coordinates with GitHub releases.

**📖 New to versioning?** See [VERSION-WORKFLOW-SIMPLE.md](VERSION-WORKFLOW-SIMPLE.md) for a plain-language explanation.

**When to update:**
- **MAJOR** (e.g. 1.0.0 → 2.0.0): Breaking changes to AGENTS.md, ORCHESTRATION.md, ARCHITECTURE.md, MEMORY.md, or framework structure
- **MINOR** (e.g. 1.0.0 → 1.1.0): New frameworks, rules, skills, or significant documentation additions
- **PATCH**: Typically not tracked (bug fixes don't require version bumps)

**How to update:**
1. Make the structural change
2. Update `version.json`: bump version, add changelog entry, update `lastUpdated`, update `structure` counts if needed
3. Commit `version.json` with the changes
4. **Optional:** Create GitHub release with matching tag (e.g., `v1.0.0`) and copy changelog to release notes

**Important:** You DON'T update version.json on every push—only when you make significant structural changes (new frameworks, breaking changes, etc.). Most pushes don't need a version bump.

See [ARCHITECTURE.md](ARCHITECTURE.md) → "Version Management", [ORCHESTRATION.md](ORCHESTRATION.md) → Version Management, and `RELEASE-PROCESS.md` for detailed guidelines.

---

## 9. Quick Checklist

- **Before starting a product/strategy/discovery/execution task**
  - [ ] Did I braindump first (or use the product-thinking entry point)?  
  - [ ] Am I using the right domain (Strategy / Discovery / Execution / Communication) after the braindump?  

- **Before adding something new**
  - [ ] Does it already fit an existing folder pattern?  
  - [ ] Can I link to an external system instead of duplicating content?  
  - [ ] Is the filename consistent with existing naming?  

- **Before committing**
  - [ ] Are my changes scoped to one clear concern?  
  - [ ] Is the commit message understandable to “future me”?  
  - [ ] Did I add links to any important external artifacts?  

