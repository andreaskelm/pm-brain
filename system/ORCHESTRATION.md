# PM Brain ORCHESTRATION

**What this file is:** Routing detail, state behavior, context loading, and cross-cutting rules. Load on-demand at state entry or when routing is ambiguous — not at bootstrap. Persona and invariant principles: [AGENTS.md](../AGENTS.md). Sleeping memory manifest: [MEMORY.md](MEMORY.md).

**Mid-conversation transitions:** Reload the relevant section at each state transition. Do not coast on earlier loads.

---

   Routing Decision Tree

- **Product keywords** (strategy, discovery, prioritization, roadmap, PRD, stakeholder, organization, "help me think through", politics) **and no explicit doc request** → **product_sense**
- **Explicit doc request** ("write PRD", "create OKR", "draft roadmap") → **execution_mode** (template-finder path; preflight first)
- **Substantial decision work complete or clear pause** → suggest **meta_reflection**
- **End-of-week signal** ("wrap up", "Friday", "close the week", `/week`) → suggest learning log + daily log close ([5-Growth/1-Learning-Log/](../5-Growth/1-Learning-Log/)) **and** Friday drift sweep (scan episodic logs per `/week` or [2-weekly-cadence.md](../2-Methods/4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md) STEP 1b)
- **Otherwise** → **conversation**

---

   Cross-Cutting (any state)

**Intent disambiguation:** When "roadmap" could mean background context OR build-a-roadmap — state interpretation in one sentence and confirm before loading.

**Company context guard:** Before updating numbered company docs in `1-Context/`, check `Maintained?` in [CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md). `Reference` or `External` → route to `3-Work/[initiative]/` or stakeholder avatar. `1.1-Stakeholder-Avatars/` is always Maintained.

**Skills dispatch** — load on topic signal in any state:

| Topic signal | Load |
|---|---|
| Roadmap, OKRs, prioritization, strategy, north star | [skills/strategy-planning/SKILL.md](skills/strategy-planning/SKILL.md) |
| Discovery, interviews, JTBD, OA, research | [skills/discovery-research/SKILL.md](skills/discovery-research/SKILL.md) |
| Stakeholder comms, one-pager, newsletter, escalation | [skills/stakeholder-management/SKILL.md](skills/stakeholder-management/SKILL.md) |
| Politics, power dynamics, "what would X say" | [skills/politics-coach/SKILL.md](skills/politics-coach/SKILL.md) |
| Framework navigation, where to start | [skills/pm-brain-workflow/SKILL.md](skills/pm-brain-workflow/SKILL.md) |

**Token efficiency:** Capable model for coaching; fast/cheap for mechanical work after thinking is done. Subagents: `explore` / `shell` for mechanical; `generalPurpose` only when judgment needed.

**Named stakeholder:** Auto-load avatar from [1-Context/1.1-Stakeholder-Avatars/](../1-Context/1.1-Stakeholder-Avatars/README.md).

**End-of-week:** Unconditional learning log suggestion — don't wait to be asked.

**Contradiction detection (decision-level):** When new info in conversation contradicts a logged decision, forecast, reopen trigger, or stated belief in repo files, surface it in one sentence ("this cuts against X you decided in March — revisit?"). Before asserting a contradiction, check `5-Growth/3-Product-Judgment-Test/forecast-log.md`, `5-Growth/2-prioritization-decision-log.md`, and relevant `3-Work/[initiative]/decisions.md` if they exist. Compare against stored reopen triggers. Belief-level contradiction stays conversational (hypothesis stress-test lens) plus the live-assumptions block in the weekly reflection template.

**Evidence strength:** When a load-bearing claim appears, name its tier in passing (documented > verbal > hunch > industry). Vocabulary only — see [evidence-strength.md](../2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/7-evidence-strength.md).

---

   STATE: product_sense

**Entry:** Load [coaching/README.md](coaching/README.md) — it drives the sequence. Eval harness: [evals/harness/run_scenario.py](evals/harness/run_scenario.py); checks in [evals/eval-functions.md](evals/eval-functions.md).

**Behavior:**
1. Product mode check — ask whether this is product mode (why, goals, trade-offs) or project mode (when, who, completion). If project mode, switch to product mode before continuing. See [coaching/README.md](coaching/README.md) step 1.
2. Name situation or ask 1–2 clarifiers (strategy / prioritization / discovery / stuck / stakeholders / crisis).
3. Context check — wake company/initiative/research per [MEMORY.md](MEMORY.md) if relevant.
4. Pull 3–5 prompts per batch from [coaching/prompts.md](coaching/prompts.md). Challenge; don't validate.
5. Summarize and check before next batch. If stuck: [coaching/evaluation.md](coaching/evaluation.md).
6. Before any framework: verify braindump sufficient per [coaching/braindump.md](coaching/braindump.md). Name the phase change.
7. When sufficient: offer execution_mode. Offer politics pass via avatars if dynamics are in play.

**Override:** "Skip braindump" → acknowledge, suggest 2-minute braindump, proceed if they insist.

---

   STATE: execution_mode

**Entry:** Load [2-Methods/0-template-finder.md](../2-Methods/0-template-finder.md) FIRST, then matched framework README + `1-*-framework.md`. No match → [2-Methods/1-frameworks-by-topic.md](../2-Methods/1-frameworks-by-topic.md) → new framework path in EVALUATION.md.

**Preflight (non-trivial docs):** "Why this, why now?", "What do you know vs. guess?", "Who is this for?" — even on explicit requests. Trivial docs (agenda, newsletter): optional.

**Behavior:**
1. Apply framework; pull from braindump where possible.
2. Template: `2-*-template.md`. Quality: `3-*-evaluation.md` + [EVALUATION.md](EVALUATION.md) QQC rules.
3. Raw material / transcripts: clarify scope; ask 12 "what's YOUR read?" before structuring.
4. Stakeholder cross-reference: load avatars; offer updates when new signal emerges.
5. **Quality gate:** Auto-QQC before presenting non-trivial artifacts as complete.

**Exit:** Offer self-reflection ([2-Methods/1-Foundations/3-Self-Reflection/1-self-reflection-framework.md](../2-Methods/1-Foundations/3-Self-Reflection/1-self-reflection-framework.md) if yes). Suggest meta_reflection.

**New framework creation:** Load [2-Methods/0-Template-Structure/](../2-Methods/0-Template-Structure/README.md) before writing. Update template-finder after.

---

   STATE: meta_reflection

**Entry:** [5-Growth/README.md](../5-Growth/README.md) for logging options.

**Behavior:** Offer PJT, learning log, pattern log. PJT exit checklist on every exit: "Any decisions with confidence levels to log?" Include reopen trigger when logging forecasts or prioritization decisions. Rule updates go to AGENTS.md (principles), system/ORCHESTRATION.md (routing), system/MEMORY.md (wake triggers) — not scattered catch-alls.

---

   STATE: conversation

Answer questions; point to docs. Repo hygiene → [docs/principles.md](../docs/principles.md). Re-route when product/doc triggers appear.

---

   Context Loading Table

| Trigger | Load |
|---------|------|
| Enter product_sense | coaching/README.md (drives the sequence) |
| Enter execution_mode | template-finder → framework README + 1-*-framework.md |
| Filling template | 2-*-template.md |
| Quality check | 3-*-evaluation.md + EVALUATION.md |
| Enter meta_reflection | 5-Growth/ target log |
| Company/org context | 1-Context/ per MEMORY.md; check CONTEXT-HEALTH.md |
| Named stakeholder | 1-Context/1.1-Stakeholder-Avatars/ |
| Initiative | 3-Work/[name]/ |
| Research | 4-Research/ or 3-Work/[name]/research/ |
| End-of-week | 5-Growth/1-Learning-Log/ daily + learning log; drift sweep via `/week` or 2-weekly-cadence STEP 1b |
| Decision + confidence | 5-Growth/3-Product-Judgment-Test/forecast-log.md |
| Contradiction vs logged decision | forecast-log, prioritization-decision-log, 3-Work/[initiative]/decisions.md |
| Evidence strength depth | 2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/7-evidence-strength.md |
| Friday drift sweep | `/week` command or 2-Methods/4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md STEP 1b |
| Repo usage | docs/principles.md |
| Repo structure change | docs/architecture.md |
| Bias deep-dive | 2-Methods/1-Foundations/2-Bias/ |
| Four risks | 2-Methods/1-Foundations/1-Mental-Models/2-Product-Thinking/4-four-risks.md |
| Team alignment | 2-Methods/1-Foundations/1-Mental-Models/5-Team-Dynamics/1-alignment-check.md |

Check filesystem before asking user whether context exists.

---

   Context Health

**Conversation rot:** At product_sense → execution_mode transition, ~25–30 turns with heavy loaded context, or when quality drops — suggest the user start a **fresh conversation** using native platform continuity (Cursor agent resume, Claude thread, etc.). Before switching: capture durable state in `5-Growth/` (daily log, prioritization log, pattern recognition) or the relevant `3-Work/[initiative]/` artifact — not a separate checkpoint folder.

**Content rot:** Consult [1-Context/CONTEXT-HEALTH.md](../1-Context/CONTEXT-HEALTH.md) when using company/initiative docs as inputs to roadmap/OKR/strategy/PRD/politics flows. One optional freshness question if overdue.

**Error recovery:** Golden rule violation → acknowledge and back up. Lost thread → summarize state in one paragraph and point to where work was saved (`3-Work/`, `5-Growth/`).

---

   Eval Checkpoints

- **Level 1:** QQC during creation — see [EVALUATION.md](EVALUATION.md)
- **Level 2:** After substantial product_sense or when behavior slips — [evals/1-agent-behavior-guide.md](evals/1-agent-behavior-guide.md), [evals/behavior-assertions.md](evals/behavior-assertions.md)
