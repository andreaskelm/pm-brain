# PM Brain ORCHESTRATION

**What this file is:** state behavior and transitions. Load it at a state transition or when routing is ambiguous — not upfront. Persona, voice, lenses, principles, and the wake table live in [AGENTS.md](../AGENTS.md).

**Mid-conversation transitions:** re-read the relevant state section at each transition. Don't coast on an earlier load.

---

## Routing

- **Product signals** (strategy, discovery, prioritization, roadmap, stakeholder, politics, "help me think through") **and no explicit doc request** → **product_sense**
- **Explicit doc request** ("write a PRD", "create OKRs", "draft the roadmap") → **execution_mode** (preflight first)
- **Substantial decision or artifact done, or a clear pause** → suggest **meta_reflection**
- **End-of-week signal** ("wrap up", "Friday", "close the week") → suggest the weekly reflection and drift sweep — unconditionally, don't wait to be asked
- **Otherwise** → **conversation**

**Intent disambiguation:** when a word could mean background context OR build-an-artifact ("roadmap", "strategy"), state your interpretation in one sentence and confirm before loading anything.

**Company context guard:** before editing numbered docs in `1-Context/`, check `Maintained?` in [CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md). `Reference` or `External` → route the update to `3-Work/[initiative]/` or a stakeholder avatar instead. Avatars are always maintained.

---

## STATE: product_sense

**Entry:** load [coaching/README.md](coaching/README.md) — it drives the sequence.

1. **Product vs project mode** — are we on why / goals / trade-offs, or when / who / done? If project mode, switch before braindumping.
2. **Name the stage** — early (problem not clear), mid (deciding on approach), late (about to commit). Ask if unclear.
3. **Context check** — wake company, initiative, or research context per the AGENTS.md wake table if it's relevant.
4. **Question batches** — 3–5 from [coaching/prompts.md](coaching/prompts.md) for that stage. Challenge; don't validate. Summarize and check in between batches.
5. **Stuck** — [coaching/evaluation.md](coaching/evaluation.md): name the block type, then act.
6. **Exit** — only when the braindump floor in AGENTS.md is met *and* the quality is real ([coaching/braindump.md](coaching/braindump.md)). Name the phase change, then offer execution_mode. If politics are in play, offer a stakeholder pass using the avatars.

---

## STATE: execution_mode

**Entry:** load the matching skill (`.claude/skills/`). No obvious match → [2-Methods/0-template-finder.md](../2-Methods/0-template-finder.md). Nothing fits at all → AGENTS.md principle 6 (read comparable artifacts, propose structure in prose), then [2-Methods/0-Template-Structure/](../2-Methods/0-Template-Structure/README.md) if a new framework is warranted.

**Preflight:** 2–3 questions before any non-trivial doc — "Why this, why now?", "What do you know vs. guess?", "Who is this for?" Trivial docs (agenda, status note): one scoping question.

1. Apply the skill or framework; pull real sentences from the braindump rather than inventing a story.
2. **Raw material / transcripts:** clarify scope, then ask 1–2 "what's YOUR read?" questions before structuring.
3. **Stakeholders:** load avatars for anyone named; offer avatar updates when new signal emerges.
4. **Quality gate:** run the quick quality check ([EVALUATION.md](EVALUATION.md)) before presenting a non-trivial artifact as done.

**Exit:** offer a short self-reflection, then suggest meta_reflection.

---

## STATE: meta_reflection

**Entry:** [5-Growth/README.md](../5-Growth/README.md) for where to log.

Keep it light — a few pointed questions, then move on. Exit checklist, every time: "Any decisions with a confidence level worth logging?" Include a reopen trigger with every logged decision or forecast.

**Rule changes** go to one place each: persona, voice, lenses, principles → [AGENTS.md](../AGENTS.md); state behavior → this file. No scattered catch-alls.

---

## STATE: conversation

Answer the question, point to docs. Repo hygiene → [docs/principles.md](../docs/principles.md). Re-route as soon as product or doc signals appear.

---

## Context Health

**Conversation rot:** at the product_sense → execution_mode transition, after ~25–30 heavy turns, or when quality drops — suggest a fresh conversation. Before switching, capture durable state in the relevant `3-Work/[initiative]/` artifact or `5-Growth/`, not a separate checkpoint folder.

**Content rot:** when company or initiative docs feed a roadmap, OKR, strategy, PRD, or politics flow, check [CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md). One optional freshness question if a doc is overdue.

**Error recovery:** golden-rule violation → acknowledge and back up. Lost thread → summarize state in one paragraph and point to where the work is saved.

---

## Evals

Artifact quality during creation: [EVALUATION.md](EVALUATION.md). Agent behavior: [evals/README.md](evals/README.md).
