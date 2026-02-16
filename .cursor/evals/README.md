# PM Brain Evals

**What this folder is:** The evaluation system for PM Brain. It has **two levels** and is **guidance-based**—no scripts to run. You use prompts and checklists to reflect on artifact quality and agent behavior, and to know **where to update** when you learn something new.

**Orchestration:** Evals are wired into the repo in three places: (1) **Level 1** lives in `02-Methods-and-Tools/` (Quick Quality Checks + `3-*-evaluation.md` per framework); (2) **Level 2** lives here ([1-agent-behavior-guide.md](1-agent-behavior-guide.md), [2-checklist.md](2-checklist.md)); (3) the **agent** uses Level 1 during creation (`.cursor/rules/evaluation-orchestration.mdc`) and can suggest the Level 2 checklist after substantial conversations. Routing and when to run evals: [ORCHESTRATION.md](../ORCHESTRATION.md) → Eval Checkpoints; persona: [AGENTS.md](../AGENTS.md). For the big picture and a visual, see [docs/architecture.md](../../docs/architecture.md) → "Evaluation system (evals)" and "How the repo is used".

**When and how scenarios are used:** The agent does **not** read or run `agent-behavior-scenarios.json`. Scenarios are **reference only**: when you (or an AI using the pasteable prompt) run a Level 2 review, you match your conversation to a scenario type (e.g. "user said something like 'I want to build an app for remote teams'"), then use the JSON's success_indicators and failure_modes to score. They are generic, static patterns so reviewers have a consistent checklist per conversation type. You can add or edit scenarios when you discover new failure modes (see [2-checklist.md](2-checklist.md)).

---

## Separation of evals

| Level | What it evaluates | Where it lives | When it runs |
|-------|-------------------|----------------|---------------|
| **Level 1** | Methods and frameworks (artifact quality) | `02-Methods-and-Tools/` — Quick Quality Checks in `1-*-framework.md`, full review in `3-*-evaluation.md` | During creation (agent); or on demand for peer review / quality gate |
| **Level 2** | Agent behavior (does AGENTS.md + ORCHESTRATION + rules guide correctly?) | This folder — [1-agent-behavior-guide.md](1-agent-behavior-guide.md), [2-checklist.md](2-checklist.md) | After important conversations or when tuning the agent; see [ORCHESTRATION.md](../ORCHESTRATION.md) → Eval Checkpoints |

---

## Level 1: Methods and frameworks

**What it is:** Quality of artifacts and methods (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap).

**Where it lives:**

- **Creation-time:** "Quick Quality Checks" in each `1-*-framework.md`. The agent uses these automatically per `.cursor/rules/evaluation-orchestration.mdc`.
- **Deeper review:** `3-*-evaluation.md` in each framework folder. Full list: [02-Methods-and-Tools/README.md](../02-Methods-and-Tools/README.md) → "Evaluation Frameworks".

**When to use:** During creation (agent applies lightweight checks), or when you do peer review / quality gate / learning review (use the full `3-*-evaluation.md`).

**When to update:** When you learn that a check is wrong, missing, or that the method has evolved—edit the relevant `1-*-framework.md` (Quick Quality Checks) and/or `3-*-evaluation.md`, and optionally `.cursor/rules/evaluation-orchestration.mdc` if the list of frameworks with evaluation support changes.

---

## Level 2: Agent behavior

**What it is:** Whether [AGENTS.md](../AGENTS.md), [ORCHESTRATION.md](../ORCHESTRATION.md), and `.cursor/rules` are guiding the user and answering correctly.

**Where it lives:** [1-agent-behavior-guide.md](1-agent-behavior-guide.md) — dimensions, reflection prompts, checklist, "where to update" map, scenario-based prompts.

**When to use:** After important conversations or when tuning the agent. Work through the checklist (or use the pasteable prompts below with an AI).

---

## How it learns and how you adapt

Evals are **guidance-based**: they don’t produce scores in a dashboard. They help you **learn** and **adapt** in two ways.

1. **You run evals when it matters** — Use [2-checklist.md](2-checklist.md): e.g. run one Level 1 evaluation on an artifact; run the Level 2 checklist on 2–3 conversations. When you spot a pattern (e.g. "agent keeps jumping to template"), use the "Where to update" map in [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and edit the right file.

2. **You update the repo when you learn something new** — If a method check is wrong or the method has evolved → edit `1-*-framework.md` or `3-*-evaluation.md`. If agent behavior should change → use the "Where to update" map in [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and edit AGENTS.md, ORCHESTRATION.md, or the relevant `.cursor/rules` file.

The agent can **ask you to adapt** after substantial conversations: it may suggest running the agent-behavior checklist or logging in `00-Meta/`. That keeps evals and practice in the loop without requiring scripts. A post-conversation hook (`.cursor/hooks/log-eval.js`) is available to append lightweight summary entries to `eval-results/` for pattern detection, but it is **currently disabled** in `.cursor/hooks.json` (was creating empty files; re-enable there when the hook payload/behavior is fixed).

---

## This folder (file map)

Numbered files follow the same pattern as `02-Methods-and-Tools/` (1 = main guide, 2 = operational/how-to). Level 1 lives in `02-Methods-and-Tools/`; this folder owns **Level 2** (agent behavior) and the evals entry point.

| File | Purpose |
|------|---------|
| **README.md** (this file) | Entry point: intro, separation of levels, orchestration, how it learns, pasteable prompts. |
| **1-agent-behavior-guide.md** | Level 2 guide: dimensions, reflection checklist, "where to update" map, scenario-based review prompts. |
| **2-checklist.md** | When to run Level 1/2, when to update, ongoing rhythm. |
| **agent-behavior-scenarios.json** | Level 2 scenario definitions (success_indicators, failure_modes). Reference only—you use them when you run the guide and match a chat to a scenario type; the agent does not read this file. |
| **eval-functions.md** | Optional instrumentation hooks: structured eval functions (`check_braindump_sufficient()`, `check_questions_before_framework()`, etc.) that agents can call at checkpoints. Non-blocking; used for pattern detection. |
| **eval-results/README.md** | Log format and usage guide for eval results. When eval checkpoints are hit, results can be logged here for pattern detection over time. |

---

## How to run agent evals with the test generator

You can turn the scenarios in `agent-behavior-scenarios.json` into **concrete test conversations** and log files using [`test-generator.md`](test-generator.md).

### Steps

1. **Pick a scenario**
   - Open `agent-behavior-scenarios.json` and choose a `scenario_id` (e.g. `vague_product_idea_001`).

2. **Choose or create a test file**
   - Look in `eval-results/` for an existing file named like `test-[scenario_id]-YYYY-MM-DD-XX.md`.
   - If none exists, create one following the guidance in `test-generator.md` (copy an existing test as a starting point).

3. **Replay the conversation with the agent**
   - Paste each `User:` line into the agent, in order.
   - After each agent reply, compare what it actually did with the **Expected Behavior (Checkpoints)** in the test file.

4. **Log the outcome**
   - In the same test file, fill in an **Eval Run** section (`Result: PASS / FAIL / MIXED`, plus notes).
   - Alternatively, create a separate log in `eval-results/` using the format from `eval-results/README.md` and reference the test file.

5. **Feed patterns back into the repo**
   - When you see recurring failures (e.g. “suggests templates too early for `vague_product_idea_001`”), use:
     - `1-agent-behavior-guide.md` → “where to update” map
     - `ORCHESTRATION.md` → routing and state transitions
     - `.cursor/rules/*.mdc` → detailed behavior tweaks
   - For meaningful behavior changes, bump `version.json` (see `docs/architecture.md` → Version Management).

The goal is fast, **low-friction** testing: a handful of short, realistic conversations that reveal whether the agent is honoring the golden rule and the scenario success indicators.

---

## Pasteable generic prompts

Use these with an AI assistant to run guidance-based evals. Copy-paste into a chat; then share the transcript (or AGENTS.md/rules) as needed.

**Note:** These evals are guidance-based (no scripts). If you see a generic prompt that asks for `eval_suite.py` or "user-facing functions," it’s for code-style repos. For PM Brain, use the prompts below instead.

### 1. Transcript review (main use)

Paste when you have a conversation transcript and want an AI to review it against the agent-behavior guide:

```
You are an expert at evaluating AI assistant behavior. I'll share a conversation transcript and this repo's agent instructions (AGENTS.md). Using the dimensions and checklist in `.cursor/evals/1-agent-behavior-guide.md`, (1) assess each dimension with brief rationale, (2) note any checklist items that failed, (3) suggest specific edits using the "where to update" map (file and section). Do not run any code or scripts.
```

### 2. Rules-only review (optional)

Use when you’re tuning AGENTS.md or rules and want a pass without a transcript:

```
Using `.cursor/evals/1-agent-behavior-guide.md`, review AGENTS.md and the .cursor/rules that apply to product chats. For each dimension, does the written guidance clearly support it? List gaps and suggest concrete edits (file + section).
```
