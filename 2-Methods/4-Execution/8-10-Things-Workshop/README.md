# 10 Things Workshop

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "10 things", "knowledge sharing workshop", "team alignment session", "surface what people know", "share tribal knowledge", "onboarding workshop", "what does the team actually know", "living problem list"
- User is in: **product_sense** (thinking about team dynamics, domain knowledge gaps, or alignment), or **execution_mode** (wants to run a workshop)
- Prerequisites: A group of 4–8 people with shared domain knowledge; no prior prep required from participants
- Output: A facilitated session → living doc of critical knowledge/problems (stored in `1-Context/` or `3-Work/[name]/`)

**How to introduce:**
"One thing that tends to surface hidden assumptions and build shared understanding fast is a '10 Things' workshop — a format Ebi Atawodi (YouTube/Uber) uses with her PM teams. Everyone gets 15 minutes and a post-it to write the 10 things they think the team should know about [X]. Then you share, cluster, and synthesize into a living doc. It takes 60 minutes and usually surfaces at least one thing that surprises everyone in the room. Does that sound useful here?"

**Common mistakes:**
- Making the prompt too narrow (kills diversity of output; keep it broad)
- Framing it as homework or formal deliverable (it should feel like a low-stakes conversation, not a review)
- Not documenting the output the same day (the synthesis fades fast)
- Scheduling it before the team has any trust in the facilitator (needs basic rapport first)

**When NOT to use:**
- Group is < 4 people (not enough perspective diversity)
- Team is in acute crisis mode (not the moment for reflection)
- People don't have shared context on the topic (the exercise surfaces knowledge gaps, not baseline education)

---

## Introduction

The 10 Things workshop is a **lightweight team alignment and knowledge-surfacing practice** — not a formal workshop, not a strategy off-site. It's a post-it exercise that takes 60 minutes and consistently surfaces things that aren't in any doc, creates shared vocabulary, and reveals where people's mental models diverge.

The format is adapted from Ebi Atawodi's (Director of PM at YouTube, formerly Uber and Netflix) living "10 Problems" practice, described in her Lenny's Podcast interview (Dec 2023). Ebi's key insight: the purpose isn't to produce a knowledge article — it's to **externalize and share the mental model of what's actually true about your domain**, so the whole team operates from the same picture. Run it as a workshop first; maintain it as a living doc after.

## Files

- `1-10-things-workshop-framework.md` — Full facilitation guide: prompt design, step-by-step process, synthesis approach, facilitation tips, and living doc practice
- `2-10-things-template.md` — Output template for the living doc (copy into `1-Context/` or `3-Work/[name]/`)

## How to Use This Framework

### Step 1: Read the framework
Open `1-10-things-workshop-framework.md` for the full facilitation guide and philosophy.

### Step 2: Choose your prompt
Pick a broad, open prompt suited to what the team most needs to surface. See the framework for prompt options by context.

### Step 3: Run the workshop (60 min)
Individual braindump (15 min) → Share round-robin (20 min) → Synthesize (15 min) → Document (10 min).

### Step 4: Create the living doc
Copy `2-10-things-template.md` into the right location (usually `1-Context/10-things-[topic].md`) and fill it with the output.

### Step 5: Maintain quarterly
The doc is living — revisit it every quarter or after a major context shift. What changed → What's no longer true → What emerged?

## When to Run This

- **New team / new role:** Week 1–4, to ramp context fast and surface unwritten rules
- **New initiative:** Before discovery kicks off, to surface domain assumptions
- **Strategy alignment:** Quarterly, to refresh the team's shared picture of what's true
- **Knowledge transfer:** When someone is leaving or a new person is joining
- **Stuck situation:** When you sense the team is operating from different assumptions but nobody's named it
