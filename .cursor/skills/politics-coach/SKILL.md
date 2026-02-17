---
name: politics-coach
description: Help PMs navigate organization politics, simulate stakeholder/peer feedback when people aren't in the room, and run politics checks on plans and Comms.
---

# Politics Coach Skill

Use this skill when the user is focused on **organization politics, power dynamics, or "what would X say?"** rather than only the content of the product work. It aligns with the other skills: it tells you **when** to load which frameworks and **how** to simulate from stakeholder avatars. Setup (the quiz that creates avatars) lives in the framework; this skill only navigates to it and uses the resulting data.

---

## When to use this skill

Trigger this skill when the user:

- Mentions **politics, landmines, power games, or career risk**, e.g.:
  - "The politics on this are tricky."
  - "I don't want to step on toes."
  - "This VP could kill the project."
  - "My manager is risk-averse about this."
- Asks for **stakeholder POVs** in absentia:
  - "What would my manager say about this plan?"
  - "How will Eng + Design react to this roadmap change?"
  - "Can you sanity-check this through my stakeholders' eyes?"
- Wants help **sequencing conversations** or building a **coalition**:
  - "Who should I talk to first?"
  - "How do I avoid surprising people?"

If they're mainly focused on **documents and tactics** (one-pagers, escalations, saying no), prefer `stakeholder-management` and combine with this skill when politics are a big part of the problem.

---

## Relevant framework and data locations

| Purpose | Path |
|--------|------|
| **Set up or update avatars** (guided quiz, methodology) | [02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md) — load README + 1-stakeholder-avatars-framework.md and walk the user through; write each avatar to a new file in [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) using the naming convention in that folder's README |
| **Avatar data** (who to simulate) | [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) — one file per person (e.g. 1-jane-manager.md); list folder and load the relevant N-name-role.md by name/role |
| **Stakeholder Comms tactics** (one-pagers, saying no, escalation) | [02-Methods-and-Tools/2.4-Communication/](../../02-Methods-and-Tools/2.4-Communication/) — use with stakeholder-management skill |

---

## Typical flows

### 1. "Set up my stakeholder brainfeed" / "Create stakeholder avatars"

- Load [2.4.8-Stakeholder-Avatars README](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md) and [1-stakeholder-avatars-framework.md](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/1-stakeholder-avatars-framework.md).
- Run the framework's quiz (pick cast, then per-person questions from the framework).
- Write each avatar to a new file in [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) using the naming convention in that folder's README (e.g. 1-jane-manager.md) and the structure in [2-avatar-template.md](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/2-avatar-template.md).

### 2. "What would [Name] say about this?" (single-stakeholder simulation)

1. List [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) and load the file matching the name/role (e.g. 1-jane-manager.md).
2. Summarize their lens in 1–2 lines (goals, fears, style).
3. Respond in three parts:
   - **Out-loud reaction** — what they'd likely say in the meeting.
   - **Inner monologue** — what they'd be thinking but not say.
   - **Top 2–3 concerns / objections** — concrete, not generic.
4. Close with **how to de-risk** for that person: evidence that would help, framing or sequencing that would land better.

If no avatars exist, offer to run the setup framework (2.4.8) first, or do a lightweight inline simulation if the user has given enough context and doesn't want to set up avatars yet.

### 3. "How will [Manager], [Eng], [Design] react?" (panel simulation)

1. Load each relevant avatar file from [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md).
2. For each: name/role, likely stance (supportive / cautious / opposed / conflicted), key concern.
3. Synthesis: where they align, where they disagree, suggested **conversation sequence** (who to talk to first, who to warm up, who to keep in the loop).

### 4. Politics pass in product_sense or execution_mode

- After braindump is sufficient (product_sense): optionally offer "Do you want to run a quick politics check on this through your manager / key stakeholders' eyes?"
- When drafting communication (execution_mode): use this skill with stakeholder-management to check the draft against relevant avatars and suggest tone, ordering, and conversation sequence.

---

## Guardrails

- Treat avatars as **caricatures, not truth**; add a short caveat when stakes are high.
- Encourage the user to **validate** in real conversations; suggest 1–2 concrete questions they could ask to test assumptions.
- Surface biases (e.g. all avatars described as hostile, or underestimating a powerful stakeholder).

---

## For Agents

- When you see politics-heavy language or "what would X say?":
  - Wake this skill and [01-Company-Context/1.1-Stakeholder-Avatars/](../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) (list folder and load the relevant N-name-role.md by name/role) if the folder exists.
  - If avatars don't exist and the user wants simulation, offer to run [2.4.8-Stakeholder-Avatars](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md) to create them.
- When simulating: use the three-part structure (out-loud, inner monologue, concerns + de-risking). Make it clear when you're speaking as a stakeholder vs as the agent.
- Nudge occasionally to **update avatars** after real conversations.

## Org survival docs

- For **system-level politics** (power, alliances, games, timing, history), wake [01-Company-Context/1.2-Org-Survival/](../../01-Company-Context/1.2-Org-Survival/README.md):
  - Use `1-power-map.md` for who really decides and who can veto.
  - Use `2-political-landscape.md` for alliances, fault lines, and protected systems.
  - Use `3-stakeholder-games.md` for recurring behaviour patterns and how to work with them.
  - Use `4-coalitions-and-timing.md` to think through timing and sequencing before big moves.
  - Use `5-red-flags-and-history.md` to log Red Weddings, slow kills, and recurring political failure modes.
- After a politics pass or a real incident, suggest updating the relevant org-survival files, especially `1-power-map.md` and `5-red-flags-and-history.md`, so future runs can spot patterns earlier.

---

## Ready-to-use prompts (for the user)

- "Help me set up my stakeholder brainfeed cast."
- "Create or update stakeholder avatars for my manager, Eng lead, and Design lead."
- "Run a politics check on this plan through my manager's eyes."
- "How would [Name] react to this roadmap / PRD / decision memo?"
- "Simulate a panel of [Manager], [Eng lead], and [Design] reacting to this change."
- "Given these avatars, what's a smart sequence of conversations to avoid surprises?"
