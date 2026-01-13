## Methods & Tools – The PM Operating System

This directory is the **core of the PM brain**: it contains the decision models, guides, templates, playbooks, and prompts you use every day.

**Important:** These frameworks are designed to **guide your thinking**, not replace it. Before jumping into templates:
1. **Braindump first** – Use the prompts in each framework to dump your raw thoughts
2. **Develop product sense** – Use the exercises to build judgment and taste
3. **Think critically** – Answer quiz questions honestly, challenge your assumptions
4. **Reflect** – Use self-reflection prompts to learn and improve

Content here is organized primarily by **domain** (Strategy, Communication, Discovery, Other), and within each domain by **numbered frameworks**.

---

## Structure

```text
02-Methods-and-Tools/
├── 2.1-Strategy/            # Strategy, OKRs, roadmap, PRDs, personas
│   ├── 2.1.1-Product-Strategy/
│   ├── 2.1.2-OKR/
│   ├── 2.1.3-Roadmap/
│   ├── 2.1.4-PRD/
│   ├── 2.1.5-Personas/
│   ├── 2.1.6-North-Star/
│   ├── 2.1.7-Prioritization/
│   ├── 2.1.8-MoSCoW-Prioritization/
│   └── 2.1.9-Kano-Model/
├── 2.2-Communication/       # Stakeholder comms, courses, formats
│   ├── 2.2.1-Newsletter/
│   ├── 2.2.2-Meeting-Agendas/
│   ├── 2.2.3-One-Pagers/
│   ├── 2.2.4-Crisis-Management/
│   ├── 2.2.5-Escalation/
│   ├── 2.2.6-Saying-No/
│   ├── 2.2.7-Stakeholder-Management/
│   └── 2.2.9-Courses/
├── 2.3-Discovery/           # Continuous discovery, JTBD, validation
│   ├── 2.3.1-Research-Interviews/
│   ├── 2.3.2-Continuous-Discovery-Habits/
│   ├── 2.3.3-Jobs-To-Be-Done/
│   ├── 2.3.4-Opportunity-Assessment/
│   ├── 2.3.5-Idea-Validation/
│   ├── 2.3.6-Problem-Solution-Space/
│   └── 2.3.7-Product-Market-Fit/
└── 2.9-Other/               # Supporting methods & mental models
    ├── 2.9.1-Mental-Models/
    ├── 2.9.2-Self-Reflection/
    ├── 2.9.3-Daily-Execution-And-Rituals/
    ├── 2.9.4-Bias/
    ├── 2.9.5-Metrics/
    └── 2.9.7-AARRR-Pirate-Metrics/
```

Inside each numbered framework folder (e.g. `2.3.2-Continuous-Discovery-Habits/`), files are usually numbered:

- `1-...` for the main framework or guide  
- `2-...`, `3-...`, etc. for templates, steps, or evaluations  
- Some frameworks include evaluation files (e.g., `3-okr-evaluation.md`, `3-roadmap-evaluation.md`) for structured assessment  

---

## When to use what

- **2.1-Strategy/** – When you need to **set direction or plan**:  
  - Vision & strategy, OKRs, roadmap, PRDs, personas, north star, prioritization.
- **2.2-Communication/** – When you need to **communicate or train**:  
  - Stakeholder newsletters, courses, (future) crisis comms, one-pagers, formats.
- **2.3-Discovery/** – When you need to **learn from customers or validate ideas**:  
  - Research interviews, continuous discovery habits, JTBD, idea validation, product-market fit assessment.
- **2.9-Other/** – When you need **supporting tools and mental models**:  
  - Metrics frameworks (AARRR, general metrics), mental models, bias awareness, self-reflection.

---

## Typical navigation examples

- **Prioritizing a backlog**
  - Start in `2.1-Strategy/2.1.7-Prioritization/` (when populated) or `2.3-Discovery/2.3.5-Idea-Validation/`.  
  - Use a decision log in your initiative folder under `04-Initiatives/`.

- **Running discovery**
  - Read `2.3-Discovery/2.3.1-Research-Interviews/1-interview-guide.md`.  
  - Use `2.3-Discovery/2.3.2-Continuous-Discovery-Habits/1-4-*.md` to snapshot, synthesize, create opportunities, and generate solutions.  
  - Save raw notes and synthesis outputs in `03-Research-Artifacts/`.

- **Writing a PRD**
  - Skim `2.1-Strategy/2.1.4-PRD/1-prd-framework.md`.  
  - Copy `2.1-Strategy/2.1.4-PRD/2-prd-template.md` or `3-prd-jtbd-template.md` and fill it in.  
  - Link back to discovery artifacts in `03-Research-Artifacts/` and initiatives in `04-Initiatives/`.

As you adapt these to your team, keep this structure but tune the content to match your reality.

---

## Quick start: self-quiz + AI collaboration for methods

Use this prompt to figure out **where to start in `02-Methods-and-Tools/`** when you're not sure which framework to use:

```markdown
Act as a product management coach. We'll work iteratively and challenge assumptions. Your role is to help me think, not to think for me.

1) First, help me braindump and locate the right area:
- Ask me to braindump: "What are you trying to do right now? Dump all your thoughts, concerns, and ideas - don't worry about structure yet."
- Based on my braindump, ask clarifying questions to understand my context and challenge my assumptions.
- Propose 1–3 starting points under `02-Methods-and-Tools/` using this structure:
  - 2.1-Strategy (2.1.1-Product-Strategy, 2.1.2-OKR, 2.1.3-Roadmap, 2.1.4-PRD, 2.1.5-Personas, 2.1.6-North-Star, 2.1.7-Prioritization, 2.1.8-MoSCoW-Prioritization, 2.1.9-Kano-Model)
  - 2.2-Communication (2.2.1-Newsletter, 2.2.2-Meeting-Agendas, 2.2.3-One-Pagers, 2.2.4-Crisis-Management, 2.2.5-Escalation, 2.2.6-Saying-No, 2.2.7-Stakeholder-Management, 2.2.9-Courses)
  - 2.3-Discovery (2.3.1-Research-Interviews, 2.3.2-Continuous-Discovery-Habits, 2.3.3-Jobs-To-Be-Done, 2.3.4-Opportunity-Assessment, 2.3.5-Idea-Validation, 2.3.6-Problem-Solution-Space, 2.3.7-Product-Market-Fit)
  - 2.9-Other (2.9.1-Mental-Models, 2.9.2-Self-Reflection, 2.9.3-Daily-Execution-And-Rituals, 2.9.4-Bias, 2.9.5-Metrics, 2.9.7-AARRR-Pirate-Metrics)

2) For the chosen starting framework:
- DON'T just ask me to paste notes. Instead, quiz me: "Before looking at your notes, tell me what you know about [topic]. What's your gut feeling? What assumptions are you making?"
- Help me braindump my thoughts on this topic first.
- Then ask me to paste any relevant notes or context.
- Challenge my thinking: "What biases might be affecting your view? What would someone with different product sense say?"
- Summarize which parts of the framework I've already covered vs what's missing.
- Suggest the next 1–3 concrete steps, but make me think: "What do you think should come next? Why?"

3) At the end of each pass:
- Ask me to reflect: "What did you learn? What would you do differently? What's your product sense telling you?"
- List: (a) the framework files I should touch next, (b) which repo directory to update in `04-Initiatives/` or `03-Research-Artifacts/`, and (c) any risks or open questions to track.

I'll start by telling you what I'm working on right now.
```


