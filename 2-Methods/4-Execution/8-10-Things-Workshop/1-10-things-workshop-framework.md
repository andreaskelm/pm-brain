# 10 Things Workshop — Framework

## Overview

A 60-minute team exercise that surfaces critical knowledge, aligns mental models, and reveals where people's understanding of the domain diverges. Low effort. Consistently produces at least one genuine surprise.

The exercise externalizes what people know but haven't written down, surfaces misalignment before it creates friction, and produces a living doc the team can actually use.


---

## The Philosophy

The point is not to produce documentation. The point is to **update the team's shared mental model** of what's true about their domain, their customers, or their product — so everyone is making decisions from the same picture.

"User research not to define what to build next, but to update your mental model of the customers, their problems and solutions, to then make better assumptions about what to build next." The 10 Things doc is that mental model, written down and shared.

A few principles that make it work:

- **It's per-PM, not just one team document.** Each PM maintains their own living "10 Things" document for their domain. They're separate, shared, and discussed together. A team workshop produces a consolidated view — but the individual living documents are the ongoing practice.
- **Broad prompt, not narrow.** The broader the prompt, the more diverse the outputs. Narrow prompts produce safe answers. "What are the 10 things you'd tell someone joining tomorrow?" gets more honest responses than "list 10 product requirements."
- **Individual before collective.** Everyone writes alone first. If you share before people have written, the first person to speak shapes everyone else's list.
- **No right or wrong.** Qualitative and quantitative, tactical and strategic, obvious and surprising — all valid. Technical debt, cultural norms, unwritten rules, customer behaviors, organizational quirks. Whatever feels genuinely important to know.
- **Bring some joy to it.** Add personality to the documents: "Money Problems, More Money More Problems" (Uber), "go/studio-problems" (YouTube creator team). A fun name signals this is a living practice, not a formal deliverable.
- **It's a living document.** The workshop produces v1. Quarterly reviews keep it current. When something changes — strategy, market, leadership — the document updates.
- **You start with 10, you end up with 3.** The full list lives internally; what you communicate to leadership or stakeholders is the sharpest 3–4.
- **The alignment success metric.** If you've done your job, your 1-1s and your engineering and design partner's    1-1s should all give you the same answer when asked "what are the top five problems for [X]?"

---

## When to Run It

| Context | Recommended prompt angle |
|---------|--------------------------|
| New role / new team | "10 things you'd tell me on my first day" |
| New initiative | "10 things true about this domain that should shape how we work" |
| Strategy alignment | "10 problems we haven't fully solved for our customer" |
| Domain onboarding | "10 things you know about this customer/market that surprised you" |
| Knowledge transfer | "10 things that live only in your head that the team needs to know" |
| Operating model reflection | "10 things about how we work that are true but we don't talk about" |

---

## Two Modes

**Mode 1 — Team workshop (this guide).** Everyone in the room is from the same team or value stream. You share a domain. Output is one consolidated living document. Used for onboarding, alignment, quarterly refresh.

**Mode 2 — Strategy session input.** You're opening a strategy session and want genuine cross-functional perspective before deciding which problems to focus on. Invite each function separately (marketing, communications, support, research, data science) and give them the same prompt: *"Give me 10 things you should know from your perspective."* Collect all inputs, then run synthesis to find the consolidated list that anchors the strategy.

This cross-functional consolidation becomes the **insights day** in a 3-day strategy session format: Day 1 (insights / 10 Things) → Day 2 (strategy: which problems to focus on, in what order) → Day 3 (big rocks: how we get there).

---

## Facilitator Guide

### Before the workshop

**Group size:** 4–8 people is ideal. Under 4 and you don't get enough perspective diversity. Over 8 and the share-out takes too long and quieter people don't contribute.

**Roles:**
- **Facilitator** — Keeps time, asks follow-up questions, doesn't dominate or share their own list during the round-robin (they're listening)
- **Scribe** — Captures on whiteboard or Miro as people share; clusters naturally as themes emerge
- **Participants** — Everyone else; no prep required

**Materials (physical):** Post-its (multiple colors is nice), markers, a wall or table to cluster on

**Materials (virtual):** Miro or FigJam board with a brainstorm section and a synthesis section

**Invite message (keep it casual):**
> "I want to run a quick exercise with you all — 60 minutes, no prep needed. The prompt is simple: what are the 10 things you think everyone on the team should know about [X]→ We'll each write independently, share round-robin, and synthesize into a living document we can actually use. No wrong answers. See you [day/time]."

---

### Step 1: Set the stage (5 min)

Open the session with something like:

> "Thanks for being here. The goal of this session is simple: we each carry around a ton of knowledge that isn't written down anywhere. Today we're going to pull that out of our heads, share it, and see where we agree, where we diverge, and what surprises us. There's no right answer. Qualitative, quantitative, tactical, strategic — all valid. Think about what you'd tell someone joining tomorrow. Think about what took you months to figure out that should have taken minutes. Think about the unwritten rules, the landmines, the opportunities people miss."

> "We've got [15 min] to write. Then we'll share. I'll capture on the board. No debate during the share-out — we save that for synthesis."

---

### Step 2: Individual braindump (15 min)

Set a timer. Everyone writes independently.

Hand everyone post-its (physical) or give them a sticky note section on the board (virtual). One post-it per thing. Or just a numbered list — whatever flows.

**Prompts to offer if people get stuck:**
- What would you tell someone joining the team tomorrow?
- What's not in the docs but everyone knows?
- What took you months to learn that should have taken minutes?
- What do people consistently misunderstand about our customers / our platform / how we work?
- What's the unwritten rule here?
- What's the landmine to avoid?
- What do we assume everyone knows but probably don't?

Facilitate the silence. People are thinking. Don't fill it.

---

### Step 3: Share round-robin (20 min)

Go around the room. Each person shares **their top 3** (not all 10 — you'll run out of time, and the top 3 per person gets the most important things out first).

Scribe captures on the board as people share, clustering naturally as themes emerge. Don't force the clusters — let them appear.

**What the facilitator watches for:**

| Signal | What it means |
|--------|--------------|
| 3+ people mention the same thing | Critical truth — goes in the Real 10 |
| Person A says X, Person B says opposite | Misalignment — flag for synthesis |
| Only 1 person mentions something critical | Knowledge silo — needs to be documented and shared |
| Nobody mentions customers | Possible blind spot — probe gently in synthesis |
| Everyone only mentions positive things | People aren't being fully honest — create more safety |

**Facilitator moves:**
- When people start explaining at length: "Great — let's hold the full context for synthesis. What's the one-liner?"
- When contradictions emerge: "Interesting — I'm hearing two different pictures here. Let's note that and come back to it."
- When something surprises the room: "I notice a few people reacting to that. Let's make sure we don't lose it."

---

### Step 4: Synthesize (15 min)

Now you can discuss. The facilitator guides the group through what emerged:

**The Real 10 (what showed up multiple times)**
What did 3+ people independently mention → These are the highest-confidence truths. Start here.

**Controversial (misalignment)**
Where did people disagree → Don't resolve it now — name it, flag an owner, and note it needs a decision or more research.

**Surprising (knowledge silos)**
What did only 1–2 people know that everyone now agrees is important → Document explicitly — this is the most actionable output.

**Missing (blind spots)**
What didn't come up that should have → Common gaps: customers, competitors, why the company exists, what success actually looks like, what we're NOT doing.

**Synthesis prompts:**
- "I see [X] coming up four times. Why does this matter so much?"
- "We have two different pictures on [Y]. Does anyone know which is more current?"  
- "Only [Name] mentioned [Z], but everyone's nodding. Is this critical → Should everyone know this?"
- "What didn't show up that surprises you?"

**Physical card variation:** Print all items on cards. Scatter groups around tables. Have people discuss and vote on the most painful ones. Works well with 10+ people or when you want visible energy and movement in the room.

---

### Step 5: Document (10 min)

While you're all still in the room, open the template (see `2-10-things-template.md`) and fill in the Real 10, the controversies, the surprises, and any open questions. Names, dates, next review date.

Don't wait until later. The synthesis fades.

Decide where it lives:
- General team/domain knowledge → `1-Context/10-things-[topic].md`
- Initiative-specific → `3-Work/[name]/10-things-[topic].md`

---

## Red Flags During the Session

| What you see | What it probably means |
|--------------|----------------------|
| Nobody mentions customers or users | Team is too internally focused |
| Only process, nothing about outcomes | Execution theater — team has lost sight of the why |
| Only problems, no strengths at all | Team might be burned out |
| People look to the most senior person before writing | Psychological safety is lower than you think |
| Nobody can think of 10 things | Prompt is too narrow, or people are new and genuinely don't know |

---

## After the Workshop: Living Document Practice

The output is version 1. It gets stale. The cadence: quarterly minimum, plus whenever there's a major context shift.

**Quarterly review (30 min):**
- What's no longer true?
- What changed?
- What new things emerged that should be on the list?
- Does the list still reflect your actual mental model?

**Trigger-based updates:**
- New strategy direction
- Major customer insight
- Leadership change
- A new person joins who brings new context
- Someone says "I wish I'd known that sooner"

---

## Common Pitfalls

**Too abstract:** "We value innovation" is useless. Push for: "Leadership says innovation but rewards shipping fast — people cut corners to avoid slipping dates." Ask "what does that mean in practice?" until it gets concrete.

**Too obvious:** "We use Slack" is not worth writing down. Push for: "Slack is where actual decisions happen — email is FYI only. If you're not in the right channels, you're out of the loop." Ask "would a new person know this?" — if yes, push deeper.

**No "so what":** A fact without implication isn't helpful. "We have 10,000 customers" → "We have 10,000 customers but 80% of revenue is from the top 50 — optimize for enterprise, not long tail." Always push for the implication.

**Too formal:** The moment it starts feeling like a deliverable or a performance review, honesty drops. Keep it light. The post-it format helps. Humor helps - "bring joy to it" isn't decoration — it's a safety signal.
