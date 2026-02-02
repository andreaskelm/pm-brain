# PM Brain – Architecture Overview

**What this file is:** Short visual reference for repo structure and methods flow. For full navigation: [README.md](README.md), [AGENTS.md](AGENTS.md). For product thinking: [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md). For “I need a template”: [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md). For “everything about topic X”: [1-frameworks-by-topic.md](02-Methods-and-Tools/1-frameworks-by-topic.md). For evals (methods + agent behavior): [.cursor/evals/README.md](.cursor/evals/README.md).

---

## Repo layers

**In plain English:** The repo has five main folders at the top level. Each holds a different kind of content. The box view below works in any preview; the list and table follow.

**Visual (boxes):**

```
┌─────────────────┐ ┌─────────────────────┐ ┌──────────────────────┐ ┌─────────────────────┐ ┌──────────────┐
│ 00-Meta         │ │ 01-Company-Context   │ │ 02-Methods-and-Tools  │ │ 03-Research-Artifacts│ │ 04-Initiatives│
│ practice, learn │ │ vision, strategy    │ │ frameworks (2.0–2.4)  │ │ research storage     │ │ active work   │
└─────────────────┘ └─────────────────────┘ └──────────────────────┘ └─────────────────────┘ └──────────────┘
```

**The five folders:**

- **00-Meta** — practice, learning log, growth portfolio, Product Judgment Test  
- **01-Company-Context** — vision, strategy, stakeholders  
- **02-Methods-and-Tools** — frameworks, guides, templates (2.0–2.4)  
- **03-Research-Artifacts** — research storage  
- **04-Initiatives** — active work, one folder per bet  

| Area | Purpose |
|------|---------|
| **00-Meta** | What you *do* and *learn* — daily log, learning log, growth portfolio, Product Judgment Test. Canonical prompts/templates live in 6-Product-Sense-Development. |
| **01-Company-Context** | Your company’s direction and constraints. Customize; keep current. |
| **02-Methods-and-Tools** | Reusable frameworks (2.0–2.4). Flow below. |
| **03-Research-Artifacts** | Research storage. Link to initiatives. |
| **04-Initiatives** | One folder per bet; day-to-day product work. |

---

## Methods flow (02-Methods-and-Tools)

**In plain English:** Inside `02-Methods-and-Tools/` you work in this order: **think** (Foundations) → **set direction** (Strategy) → **discover** (Discovery) → **build and ship** (Execution), while **communicating** all along (Communication). The box flow below works in any preview; the table follows.

**Visual (flow, left to right):**

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│ 2.0 Found.   │ ──► │ 2.1 Strategy │ ──► │ 2.2 Discovery│ ──► │ 2.3 Execution│ ──► │ 2.4 Communication│
│ think first  │     │ set direction│     │ discover     │     │ build & ship │     │ communicate      │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────────┘
```

**Flow (text):** `2.0 Foundations` → `2.1 Strategy` → `2.2 Discovery` → `2.3 Execution` → `2.4 Communication`

| Layer | Contents |
|-------|----------|
| **2.0 Foundations** | Think first — product sense entry, mental models, bias. Start here before templates. |
| **2.1 Strategy** | Direction, goals, roadmap, prioritization. |
| **2.2 Discovery** | Research, JTBD, opportunity assessment, idea validation. |
| **2.3 Execution** | PRDs, personas, metrics, execution rituals. |
| **2.4 Communication** | Stakeholder comms, one-pagers, crisis, escalation, saying no. |

---

## Agent mode flow (state diagram)

**In plain English:** The assistant switches between modes depending on whether you're thinking things through, asking for a specific doc, or wrapping up with reflection.

```mermaid
flowchart LR
  DefaultMode[Default]
  ProductSenseMode[ProductSenseMode]
  TemplateFinderPath[TemplateFinderPath]
  ExecutionMode[ExecutionMode]
  MetaSuggestion[MetaSuggestion]

  DefaultMode -->|"product or think-through topic"| ProductSenseMode
  DefaultMode -->|"write draft fill specific doc"| TemplateFinderPath

  ProductSenseMode -->|"braindump sufficient"| ExecutionMode
  ProductSenseMode -->|"more prompts"| ProductSenseMode

  TemplateFinderPath -->|"preflight + template"| ExecutionMode

  ExecutionMode -->|"substantial decision done"| MetaSuggestion
  MetaSuggestion -->|"suggest 00-Meta log or rule update"| DefaultMode
```

- **ProductSenseMode**: Entered when the topic is product/stakeholder/org/strategy/roadmap/prioritization/discovery/execution or \"help me think through something\". Stay here while you braindump using prompts from `2-product-sense-prompts.md` and the golden rule in `PRODUCT-SENSE-RULES.md`, until the \"braindump sufficient\" checklist is met.
- **TemplateFinderPath**: Entered when you explicitly ask to write/draft/fill a specific doc (PRD, OKR, one-pager, etc.). Use `02-Methods-and-Tools/0-template-finder.md` to jump straight to the right README + template, optionally asking 1–2 preflight prompts for non-trivial docs.
- **ExecutionMode**: After sufficient braindump (or via TemplateFinderPath), help structure thinking and apply the right framework/template from `02-Methods-and-Tools/`.
- **MetaSuggestion**: After substantial decision work, suggest logging in `00-Meta/` (forecast log, learning log, pattern recognition), optionally running the Level 2 checklist ([.cursor/evals/1-agent-behavior-guide.md](.cursor/evals/1-agent-behavior-guide.md)), and optionally updating rules (see `.cursor/rules/thinking.mdc`), then return to Default for the next conversation.

**Evals** are a separate workflow (see Evaluation system below), not a conversation state. The agent may suggest the Level 2 checklist in MetaSuggestion; you run evals when you choose.

---

## Evaluation system (evals)

**In plain English:** Evals are **guidance-based** (no scripts). Two levels: (1) **Level 1** = artifact quality (methods/frameworks) — lives in `02-Methods-and-Tools/` (Quick Quality Checks in `1-*-framework.md`, full review in `3-*-evaluation.md`); (2) **Level 2** = agent behavior — lives in `.cursor/evals/` ([1-agent-behavior-guide.md](.cursor/evals/1-agent-behavior-guide.md), [2-checklist.md](.cursor/evals/2-checklist.md), [agent-behavior-scenarios.json](.cursor/evals/agent-behavior-scenarios.json)). You run evals when it matters; when you learn something new, you update the right file (see "Where to update" in the evals guide).

**How evals are used (visual):**

```mermaid
flowchart TB
  subgraph level1 [Level 1: Artifact quality]
    UserCreates[User creates artifact]
    AgentScans[Agent scans for red flags]
    QC[Quick Quality Checks in 1-*-framework.md]
    FullEval[Optional: full 3-*-evaluation.md]
    UserCreates --> AgentScans
    AgentScans --> QC
    QC --> FullEval
  end
  subgraph level2 [Level 2: Agent behavior]
    UserReviews[You run Level 2 review]
    Guide[1-agent-behavior-guide.md]
    Scenarios[agent-behavior-scenarios.json]
    UserReviews --> Guide
    Guide -->|"Match chat to type"| Scenarios
  end
  Agent[Agent per evaluation-orchestration.mdc] --> level1
  MetaMode[Agent suggests checklist in meta_mode] --> level2
```

- **Level 1 during creation:** The agent uses Quick Quality Checks automatically per `.cursor/rules/evaluation-orchestration.mdc` when you work on frameworks with evaluation support (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap).
- **Level 2:** You (or an AI with the pasteable prompt) run the checklist when you choose; the agent may suggest it after substantial conversations (see [AGENTS.md](AGENTS.md) → meta_mode). Scenarios in JSON are reference only—you match your conversation to a scenario type and use success_indicators / failure_modes to score; the agent does not read the JSON.
- **Entry point:** [.cursor/evals/README.md](.cursor/evals/README.md) — intro, separation of evals, how it learns / ask user to adapt, pasteable prompts, file map.

---

## How the repo is used (entry points and flows)

**In plain English:** The repo has a few main entry points. Depending on what you're doing, the agent (or you) routes to the right place. The diagram below shows how those entry points connect to the rest of the repo.

```mermaid
flowchart LR
  User[You]
  ProductThink[Product thinking]
  TemplateFind[Template finder]
  Evals[Evals]
  Methods[02-Methods-and-Tools]
  Meta[00-Meta]
  Company[01-Company-Context]
  Initiatives[04-Initiatives]

  User -->|"Think through a decision"| ProductThink
  User -->|"Write / draft a doc"| TemplateFind
  User -->|"Review agent or artifacts"| Evals

  ProductThink --> Methods
  ProductThink -->|"After substantial work"| Meta
  TemplateFind --> Methods
  Evals -->|"Level 1 index"| Methods
  Evals -->|"Level 2 guide"| Evals

  Methods --> Company
  Methods --> Initiatives
```

| Entry point | Trigger | Where it leads |
|-------------|---------|----------------|
| **Product thinking** | You're braindumping, exploring, or asking for help with a decision | [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) → product_sense_mode → then [02-Methods-and-Tools/](02-Methods-and-Tools/README.md) (framework/template). After substantial work, agent may suggest [00-Meta/](00-Meta/README.md) (log, forecast, learning). |
| **Template finder** | You ask to write/draft/fill a specific doc (PRD, OKR, one-pager, etc.) | [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md) → right README + template in 02-Methods-and-Tools. For frameworks with evaluation support, agent uses Quick Quality Checks ([evaluation-orchestration.mdc](.cursor/rules/evaluation-orchestration.mdc)). |
| **Evals** | You want to review artifact quality or agent behavior | [.cursor/evals/README.md](.cursor/evals/README.md) → Level 1 (Methods) or Level 2 (agent-behavior guide, checklist, scenarios as reference). Agent may suggest Level 2 checklist after substantial conversations (meta_mode). |

---

## Linking Conventions

**Cross-domain references:** Point to domain `README.md` files (e.g., `2.0-Foundations/README.md`, `2.1-Strategy/README.md`). These serve as stable entry points for each domain.

**Within-domain references:** 
- Use sibling links for closely related files (e.g., `1-framework.md`, `2-template.md`)
- Use `../README.md` to reference the domain index
- Use stable paths for nearby subdomains (e.g., `../2.0.2-Bias/README.md`)

**Deep links:** Only use deep links (e.g., `../../2.0-Foundations/2.0.3-Self-Reflection/README.md`) when specifically referencing a particular framework in context, or in "Related frameworks" sections. Prefer domain indices for general navigation.

**When adding new frameworks:** Follow these conventions to maintain consistent navigation patterns.
