# Stakeholder Avatars Framework

## Overview

Stakeholder avatars are **reusable, structured profiles** of real people you work with. Each profile captures what they say they want (explicit goals), what they might not say (implicit goals, fears), what moves them (incentives), how they talk (tone, example phrases), and how they’ve behaved with you (history). The agent uses these profiles to simulate how they’d react to a plan, PRD, or decision when they’re not in the room — so you can pressure-test ideas and communication before live conversations.

**Concepts:**
- **Avatar** = one person’s profile in a file [01-Company-Context/1.1-Stakeholder-Avatars/N-name-role.md](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) (one file per person; see that folder’s README for naming).
- **Brainfeed cast** = your full set of avatars (manager, Eng lead, designer, etc.).
- **Simulation** = agent reads an avatar and answers as that person (out loud + inner monologue + concerns + how to de-risk).

---

## Step 1: Pick the cast (3–7 people)

Suggest a mix such as:

- **Manager** (direct report)
- **Eng lead / Director** (eng partner for your area)
- **Design lead**
- **Product leadership** (e.g. VP Product / CPO) if they affect your work
- **Cross-functional partner** (Sales, Marketing, CS, etc.)
- **Political ghost** (e.g. former exec whose preferences still shape decisions)

Ask: "Who are the 3–7 people who most affect your work or whose reaction you care about when you change plans or ask for something?" List them; then for each person run the quiz below and write the result into a new file in [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) with filename `N-name-role.md` (e.g. 2-alex-eng-lead.md). Use the [avatar template](2-avatar-template.md). See the folder README for the full naming convention (number, name, role, optional organization).

---

## Step 2: Per-stakeholder quiz (what to ask)

For **each** person, ask these in order and map answers into the avatar sections. Encourage **concrete examples and real phrases**, not abstract labels.

### Identity & Relationship
- What’s their role and where do they sit in the organization chart relative to you?
- How long have you worked with them?
- In one sentence, how would you describe your relationship right now?

### Explicit Goals (What they say they care about)
- If you asked them what success looks like this year, what would they say?
- Which metrics or outcomes do they bring up the most?

### Implicit Goals (What they might not say out loud)
- What do you suspect they personally want in the next 12–24 months? (promotion, stability, less chaos, bigger scope, survival, legacy project, etc.)
- Where do you sense they feel insecure or threatened?

### Fears & Risks
- What are they afraid could go wrong that would land badly on them?
- What types of incidents would they see as career-limiting?

### Incentives & Levers
- What actually moves them to support something? (metrics, exec enthusiasm, user feedback, narrative, peer adoption, "board wants this", etc.)
- What kind of evidence has changed their mind in the past? (concrete example)

### Tone of Voice & Behaviour
- How do they usually communicate in group settings vs 1:1?
- Are they blunt or indirect? Optimistic or cautious? Detail-oriented or big-picture?
- Give 3–5 example phrases they actually use.

### History With You
- Where have they backed you in the past?
- Where have they blocked or slowed you down?
- Any unresolved tension or a scar from a past incident?

### Brainfeed Stream (How they’d react)
- Imagine you share **good news** with them about your area — what do they say out loud, and what do you think they’d *think* but not say?
- Same for **bad news** or a **surprise change**.

---

## Step 3: Write to 01-Company-Context/1.1-Stakeholder-Avatars/

Use the structure in [2-avatar-template.md](2-avatar-template.md). One **file** per person: create a new file in [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) with filename `N-name-role.md` (e.g. 1-jane-manager.md, 2-alex-eng-lead.md). Keep headings identical so the agent can parse them. Prefer short, specific bullets over long paragraphs.

---

## Step 4: When to refresh

- After a big 1:1 or decision: add a note to the relevant avatar (new phrase, new fear, or updated relationship).
- If their role or incentives change (reorg, new boss, new strategy), update their section.
- If simulations feel off, re-run the quiz for that person and overwrite their file.

---

## Relation to other frameworks

- **2.4.7-Stakeholder-Management**: Mapping and engaging stakeholders; communication tactics. Use that for *how* to communicate. Use avatars for *simulating* how specific people will react before you communicate.
- **Politics-coach skill**: The agent uses this framework when you say "set up my brainfeed" or "add/update avatars"; it uses the *data* in [01-Company-Context/1.1-Stakeholder-Avatars/](../../../01-Company-Context/1.1-Stakeholder-Avatars/README.md) (one file per avatar) when you say "what would [Name] say?" or "run a politics check."
- **01-Company-Context/1.2-Organization-Survival/**: Use this for **system-level politics** (power map, alliances, games, timing, red flags). Person-level patterns go into avatars; system-level patterns go into `1.2-Organization-Survival/`.
