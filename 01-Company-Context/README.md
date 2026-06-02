# Company Context

This directory contains the foundational company context documents that provide strategic direction, organizational structure, and product principles. These documents serve as the source of truth for company-wide product and technology strategy.

**For agents:** This folder is one of the context sources the PM Brain agent asks about early in product_sense (and when starting execution_mode for non-trivial docs). If the user has not added relevant company context to the conversation, suggest adding or @-mentioning key docs from here (e.g. vision, strategy, roadmap, stakeholders); having them in context speeds up thinking and keeps answers aligned to the user's actual strategy. Paths below are from repo root.

## First Time Setup

**New to this directory?** Start with the main setup guide: [`docs/setup.md`](../docs/setup.md) — it covers company context setup as part of the overall PM Brain configuration.

**Personalization:** Fill out [`USER.md`](../USER.md) at the repo root with your name, role, company, team, and how you work.

**Onboarding:** Once basic context exists, read [`1.3-Onboarding/1-top-10-things-you-should-know.md`](1.3-Onboarding/1-top-10-things-you-should-know.md) for a fast tour of how company context, metrics, acronyms, and methods fit together.

## Overview

These documents should be the outcome of actual strategic work and organizational planning. The placeholder content should be replaced with your company's actual information developed through proper processes.

**Structure:** Flat is fine for most orgs (all docs at root level). If you have distinct business units with separate strategies, add BU subfolders (e.g. `1.1-Business-Unit-A/`). Start flat and add structure when you need it.

## Document Structure

The documents are numbered in a logical flow that follows the strategic planning and execution process:

### 1. Vision → 2. Strategy → 3. Principles → 4. Portfolio → 5. Roadmap → 6. Stakeholders

**Why this order?**
- **Vision** (1) provides the foundational "why" - mission, vision, and values that everything else builds upon
- **Strategy** (2) defines the "what" - strategic priorities and initiatives that execute the vision
- **Principles** (3) establishes the "how" - core principles that guide all product work
- **Portfolio** (4) documents "what exists" - current products and customer segments
- **Roadmap** (5) plans the "when" - execution timeline that brings strategy to life
- **Stakeholders** (6) identifies the "who" - organizational context for all activities

This structure creates a natural flow: **Why → What → How → What Exists → When → Who**

## Documents

### Strategic Foundation
- **`1-company-vision.md`** - Company mission, vision, values, and competitive position
- **`2-company-strategy.md`** - Strategic priorities, initiatives, and success metrics

### Product & Technology
- **`3-company-product-principles.md`** - Core product principles and development process
- **`4-company-product-explanation.md`** - Product portfolio and customer segments
- **`5-company-roadmap.md`** - Company-wide roadmap across all business units

### Organizational
- **`6-company-stakeholders.md`** - Technology & Product organization stakeholder directory
- **`1.1-Stakeholder-Avatars/`** - Stakeholder and peer avatars (brainfeed cast) for simulation and politics checks — one file per person (e.g. 1-jane-manager.md). Naming: single digit, name, role, optional organization. See [1.1-Stakeholder-Avatars/README.md](1.1-Stakeholder-Avatars/README.md) for naming and how to add; setup method: [02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/](../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md).
- **`1.2-Organization-Survival/`** - Organization-level politics and survival cheat sheet (power map, alliances, games, timing, red flags). Personal and agent-facing only. See [1.2-Organization-Survival/README.md](1.2-Organization-Survival/README.md) for structure and prompts.

## How to Use This Directory

**First time setup:** See [`docs/setup.md`](../docs/setup.md) → Step 4. Fill out [`USER.md`](../USER.md), then create the core docs that apply to your org; skip what doesn't.

**Ongoing use:**
1. **Start with Vision & Strategy** - These documents should be created first through the Product Strategy framework
2. **Define Principles** - Use product principles to guide decision-making
3. **Document Portfolio** - Catalog your products and customer segments
4. **Build Roadmap** - Create company-wide roadmap aligned with strategy (and BU/team roadmaps if applicable)
5. **Maintain Stakeholders** - Keep stakeholder directory current
6. **Update structure** - When organizational changes occur (new BUs, teams), add subfolders as needed and update [`USER.md`](../USER.md) and the relevant company docs

---

## Quick start: self-quiz + AI collaboration for company context

Use this prompt when you want to **(re)build your company context** and aren’t sure where to start:

```markdown
Act as a product strategy coach helping me build a minimal but useful company context (vision, strategy, principles, portfolio, roadmap, stakeholders).

1) First, help me locate my starting point:
- Ask what’s most clear today (vision, strategy, principles, products, roadmap, stakeholders) and what feels fuzzy.
- Based on my answers, propose 1–2 starting documents under `01-Company-Context/` to work on next:
  - 1-company-vision.md
  - 2-company-strategy.md
  - 3-company-product-principles.md
  - 4-company-product-explanation.md
  - 5-company-roadmap.md
  - 6-company-stakeholders.md
  - 1.1-Stakeholder-Avatars/ (optional; for brainfeed cast / "what would my manager say?" simulation)

2) For the chosen document:
- Ask me to paste any existing notes, slides, or docs.
- Draft an updated version using the structure in that file, clearly marking [placeholders] and [open questions].
- Suggest which related methods in `02-Methods-and-Tools/` I should use next (e.g. Product Strategy, OKR, Roadmap, Personas).

3) At the end of each pass:
- Summarize the updated company context in 3–5 bullets.
- Propose the next 1–2 `01-Company-Context` documents to refine, and which `02-Methods-and-Tools` frameworks to use alongside them.

I'll start by telling you which parts of our company context feel most unclear right now.
```

## Maintenance

- **Quarterly Reviews**: Review all documents quarterly for accuracy and relevance
- **After Major Changes**: Update relevant documents when strategy, organization structure, or priorities change
- **Organizational Structure Changes**: When new BUs, teams, or strategic planning structures emerge, add subfolders as needed and update [`USER.md`](../USER.md) and the relevant company docs accordingly
- **Version Control**: Use git to track changes and maintain history
- **Stakeholder Updates**: Update stakeholder directory when organization changes occur

## Related Methods & Tools

- Strategic foundations: [02-Methods-and-Tools/2.1-Strategy/2.1.1-Strategic-Foundations/](../02-Methods-and-Tools/2.1-Strategy/2.1.1-Strategic-Foundations/README.md)
- Roadmap: [02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/](../02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md)
- OKRs: [02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/](../02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md)
- Personas: [02-Methods-and-Tools/2.3-Execution/2.3.5-Personas/](../02-Methods-and-Tools/2.3-Execution/2.3.5-Personas/README.md)
- Self-Reflection: [02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection/](../02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection/README.md)


