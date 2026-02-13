# Braindump Prompts - Think Before You Structure

## For Agents

This file is **situation-based braindump prompts** for product_sense. Use the **Situation → section (quick map)** table below to find the right section for the user's situation. For **AI product decisions**, use the [For AI Product Decisions](#for-ai-product-decisions) section near the end of the file. Do not duplicate the prompt lists here—reference the section and pull 3–5 questions that fit.

---

**What this file is:** The **questions** (prompts) and red flags by situation. Not a fill-in form—you (or the agent) use these to drive thinking *before* opening any execution template (PRD, OKR, Opportunity Assessment, etc.). Fill-in templates live in `02-Methods-and-Tools/` (e.g. `2.3-Execution/2.3.4-PRD/2-prd-template.md`).

**Purpose:** Help you think deeply *before* jumping into frameworks, so artifacts reflect real judgment instead of shallow, filled‑in boxes.

**Mindset:** You are a product sense coach for your future self—capture honest thinking, not polished prose.

**How to use:**

1. Pick the scenario that matches your situation
1. Write/speak your answers without editing (voice memos work great)
1. Don't worry about structure or completeness
1. THEN open the relevant framework/template
1. Use your braindump to inform structured thinking

**Before you start:** Am I in product mode (why, goals, second-order, trade-offs) or project mode (when, who, completion)? If you're about to fill boxes, switch to product mode first. For thinking modes, assumptions, and biases, see [6-meta-thinking-for-product-sense.md](6-meta-thinking-for-product-sense.md).

**30-second pre-flight** (before any major decision):

| Check | Question |
|-------|----------|
| **Why** | Can I articulate WHY this matters in one sentence? |
| **Second-order** | Have I asked "and then what?" at least twice? |
| **Edge cases** | Have I identified 3+ ways this could break? |
| **Trade-offs** | Do I know who loses from this choice? |
| **Bias** | What bias might I be falling for? (See [6-meta-thinking](6-meta-thinking-for-product-sense.md) and [2.0.2-Bias](../../2.0.2-Bias/1-bias-framework.md).) |
| **Information** | Do I have enough info to decide with 70%+ confidence? |
| **Reversibility** | Do I know if this is reversible? |
| **Communication** | Can I explain this decision clearly to a skeptic? |

**Red flags (STOP if any):** I can't explain why this matters; I haven't thought through what could go wrong; I'm deciding on one data point; I'm afraid to share this reasoning publicly; this feels rushed but I can't say why; I haven't considered alternatives; I don't know what success looks like.

**Green lights (PROCEED if most):** I can explain the rationale; I've identified second-order effects; I've anticipated edge cases; I know what we're trading off; I'd defend this publicly; I've considered alternatives; I know how we'll measure success; I've set a review date.

**Time box:** 10–30 minutes for the braindump. Don't aim to answer everything; aim for honest, messy thinking.

You do **not** need to answer every question below. A small set of simple prompts, used consistently, does most of the work. **Pick 3–5 that make you uncomfortable—those are the important ones.**

---

### Situation → section (quick map)

| Situation | Section in this file |
|-----------|----------------------|
| PRD / feature | [Before Writing a PRD](#before-writing-a-prd) |
| Prioritization | [Before Making a Prioritization Decision](#before-making-a-prioritization-decision) |
| Strategy | [Before a Product Strategy Session](#before-a-product-strategy-session) |
| Research / discovery | [Before User Research / Discovery](#before-user-research--discovery) |
| Stuck | [When You're Stuck on a Product Decision](#when-youre-stuck-on-a-product-decision) |
| Crisis / incident | [When Something Goes Wrong (Crisis / Incident)](#when-something-goes-wrong-crisis--incident) |
| Teardown | [Before a Product Teardown](#before-a-product-teardown) |
| Stakeholders | [Before Talking to Stakeholders](#before-talking-to-stakeholders) |
| Stakeholder mapping | [Before Stakeholder Mapping](#before-stakeholder-mapping) |
| Saying no | [Before Saying No](#before-saying-no) |
| Escalation | [Before Escalation](#before-escalation) |
| Meeting / agenda | [Before Scheduling a Meeting](#before-scheduling-a-meeting) |
| Self-reflection / retro | [Before Self-Reflection](#before-self-reflection) |
| Continuous discovery | [Before Continuous Discovery](#before-continuous-discovery-interviews-synthesis-opportunities) |
| Any framework (generic) | [Generic Step 0 (any framework)](#generic-step-0-any-framework) |
| AI product | [For AI Product Decisions](#for-ai-product-decisions) |
| Not sure which | [Meta-Prompt: When You Don't Know Which Prompts to Use](#meta-prompt-when-you-dont-know-which-prompts-to-use) |

---

### Golden nuggets (one-liners that work almost everywhere)

Keep these in your back pocket. They cut through shallow thinking in almost any situation:

- **Who is this really for, and what is their day like?** (Not "users"—a specific human.)
- **What job is this doing for them?** (JTBD lens.)
- **What assumptions am I making? What don't I actually know yet?**
- **If this works, what second-order effects might it create?** ("And then what?" twice.)
- **What could go wrong, and what would I do if it did?** (Inversion.)
- **What am I hoping NOT to hear?** (Red flag—investigate that.)
- **What's the one thing that, if I knew it, would make this easy?**
- **Am I missing information, or am I uncomfortable making a call in ambiguity?**

For more mental models (first principles, one-way doors, opportunity cost), see [4-mental-models-product-sense-bridge.md](4-mental-models-product-sense-bridge.md).

---

### Progressive depth ladder (surface → strategic)

Use this to deepen thinking. **Don't skip levels.**

| Level | Focus | Prompts |
|-------|--------|---------|
| **1. Surface** | What user said | What did they request? What problem did they describe? What words did they use? |
| **2. Behavioral** | What they're trying to do | What job are they hiring this for? What would they do if this didn't exist? What alternatives or workarounds? |
| **3. Motivational** | Why it matters to them | What progress are they trying to make? What emotional need does this serve? What forces push or hold them back? |
| **4. Strategic** | What it means for us | How does this fit our strategy? Is this our target segment? What does this unlock or prevent? What second-order effects at scale? |

---

### Second-order exploration (quick pass)

For any significant decision, run through:

- **First-order:** What happens directly and immediately?
- **Second-order:** And then what? (User behavior changes? System effects? Team/org effects? Market/competitor response?)
- **Third-order:** And then what after that? (What compounds? What becomes irreversible? What new equilibrium?)
- **Feedback loops:** What reinforces? What balances? What lags?
- **Tipping points:** At what point does this break, flip, or become irreversible?

For a fuller worksheet (mitigation table, decision confidence), see [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md) and [4-mental-models-product-sense-bridge.md](4-mental-models-product-sense-bridge.md).

---

### Always-Ask Core Prompts

Before you dive into any specific section, quickly run through these:

- Who is this really for, and what is their day like?
- What job is this doing for them?
- What assumptions am I making? What don't I actually know yet?
- If this works, what second-order effects might it create later—for users, the product, the team, or the business?
- What could go wrong, and what would I do if it did?

**If it helps, name the situation:** Strategy / Design / Prioritization / Discovery / Stuck / Crisis—then lean on that section's questions.

**Quick situation check** (1–2 bullets per situation):

- **Strategy:** Can I explain why in one sentence? Who are we not serving?
- **Design:** What human need does this serve? What could users misuse?
- **Prioritization:** What are we NOT doing? Is this reversible?
- **Discovery:** What assumption, if wrong, changes everything? What am I hoping NOT to hear?
- **Stuck:** What's the one thing that, if I knew it, would make this easy? Am I missing info or avoiding the call?
- **Crisis:** Who's affected? What stops it now? What would have prevented it?

**Red flags by situation** (self-check before you finish a braindump or move to a framework):

- **Strategy:** Strategy sounds like it could apply to any company; no clear trade-offs; can't explain who we're NOT serving; unclear what becomes easier/harder.
- **Design:** Only optimizing for happy path; assuming users read instructions; adding features without removing complexity; no consideration of failure states.
- **Prioritization:** Prioritizing based on who shouted loudest; no clear hypothesis or assumption to test; can't explain opportunity cost; treating everything as urgent.
- **Discovery:** Asking leading questions; only talking to friendly users; confusing what users say with what they need; not observing actual behavior.
- **Stuck:** Rushing to decide without naming the block; waiting for permission you don't need; overthinking to avoid accountability.
- **Crisis:** Rushing to fix without understanding; not communicating proactively; blaming people vs. fixing systems; not documenting learnings.

-----

## Before Writing a PRD

### User Understanding

- Who is this really for? Not the persona - the actual human. What's their day like?
- What are they currently doing instead? Why does that suck for them?
- What have they told us they want? What do they actually need? (Often different)
- If this works, what changes in their day? What doesn't change?
- Who will hate this feature? Why?

### Problem Clarity

- What's the job they're hiring this feature to do?
- Why hasn't this been solved already? (Market gap? Technical limitation? Wrong priority?)
- What's the simplest possible version that would still be useful?
- What assumptions am I making about how they'll use this?
- What could go catastrophically wrong?
- If this feature really works, what second-order effects might it create for users, our product surface area, or our team 6–12 months from now?
- If this fails or gets half-adopted, what becomes harder or messier later?

### Business Reality

- Why this, why now?
- What happens if we don't build this?
- What metrics actually change if this succeeds?
- Who internally cares most about this? Why?
- What will we stop doing to make time for this?

### Behavioral Analysis (when behavior change matters)

- If this works perfectly, what behavior changes?
- What new habits would form? What old habits would break?
- What makes this habit-forming vs. one-time?

### Trust & Risk

- If this fails, what trust do we lose?
- What's the worst unintended consequence?
- What could users misuse this for?
- What liability or compliance risks exist?

### Edge Case Hunting

- What if 10x more people use this than expected?
- What if users hack or game the system?
- What if adjacent systems fail?
- What breaks at scale? What happens in different cultures or regions?

-----

## Before Making a Prioritization Decision

### Opportunity Assessment

- What evidence do I have this matters? (Real data, not vibes)
- How many users does this affect? How deeply?
- What's my confidence level? (Wild guess? Educated? Very confident?)
- What would make me 10x more confident?
- Am I falling in love with my solution vs. the problem?

### Tradeoff Thinking

- What are we NOT doing if we do this?
- What's the opportunity cost?
- Is this reversible? If yes, bias toward action. If no, what don't we know?
- Does this make other things easier or harder?
- What do I wish we knew that we don't?
- If we say yes to this, what doors does it open or close for us later (for users, teams, roadmap options)?

### Organizational Reality

- Who needs to believe in this for it to succeed?
- What's the internal political reality?
- Do we have the right team/skills to execute this?
- What dependencies am I hand-waving away?

### Reversibility Test

- Is this reversible? (If yes → lower risk, decide faster.)
- What's the cost to undo? How long until we know if it worked?
- Can we prototype or test cheaply first?

### Dependency Mapping

- What does this enable later? What becomes impossible if we don't do this?
- What creates lock-in or dependency? What opens future options?

### Learning Value

- What do we learn per dollar or hour spent?
- What assumptions does this test? Does this reduce critical uncertainty?

### Prioritization gut check

- If you could only ship ONE thing in the next quarter, what would it be? Why?
- Which initiatives feel like they'll move the needle vs. just keep things running?
- Are you prioritizing based on what's loudest or what's most valuable?
- What would make you say "this prioritization is obviously wrong"? "Obviously right"?

-----

## Before a Product Strategy Session

### Current State

- What's actually working? (Be honest)
- What's definitely not working? (Be honest)
- What do we keep saying we'll do but never do? Why?
- What's changed in the last 3-6 months that we're not talking about?

### Future Vision

- If everything goes right, what does success look like in 2 years?
- What would have to be true for that to happen?
- What are we uniquely positioned to do?
- What are we deluding ourselves about?
- If this strategy works, what second-order effects will it create across users, org, and product over time?

### Market & Competition

- What's our actual sustainable advantage? (Not marketing fluff)
- Who's solving this better than us? How?
- What trends are we riding? Which ones are we fighting?
- Where is the market going that we're not ready for?

### Time Horizon

- What compounds over 12 months?
- What becomes easier or harder in 2 years?
- What would we regret NOT doing now?

### Strategic Validation

- Does it clearly identify target AND non-target segments?
- Does it highlight trade-offs with rationale?
- Does it build on existing advantages?
- Is it easy to remember and repeat?
- Does it differentiate meaningfully?

-----

## Before User Research / Discovery

### What We Don't Know

- What question keeps me up at night about our users?
- What assumption, if wrong, would completely change our plans?
- What do I think I know that I'm not actually sure about?
- What evidence would change my mind?
- If you had to explain this problem to a 5-year-old, what would you say? (Simplification test)

### Curiosity Check

- What would surprise me to learn?
- What would I be disappointed to discover?
- What am I hoping NOT to hear? (Red flag - investigate this)
- If I learned one thing that changed everything, what would it be?

### Past Patterns

- What did we learn last time that we ignored?
- What user feedback keeps coming up that we haven't acted on?
- When have we been most wrong about users before?

### Jobs-to-be-Done Lens

- What job is the user hiring this product for?
- What alternatives have they tried? What forces push them to switch? What hold them back?
- What does "progress" look like to them?

### Context Mining

- When did this problem last occur? Walk me through exactly what happened.
- What would make this problem go away forever? Who else experiences this?
- What's the cost of NOT solving this?

### Interview Question Quality

**Before preparing interview questions, ask yourself:**
- Am I asking about past behavior or future intentions? (Past = "Tell me about the last time you..."; Future = "Would you use..." — avoid future)
- Am I asking about specific instances or hypotheticals? (Specific = "When was the last time this happened?"; Hypothetical = "What if we built X?" — avoid hypotheticals)
- Am I asking about facts or opinions? (Facts = "What did you actually do?"; Opinions = "What do you think about X?" — prefer facts)
- Can they lie about this answer? (If yes, reframe to past behavior and concrete examples)

**Red flags in their responses:** If they're complimenting your idea, asking about pricing, or saying "I would definitely use that"—you're probably asking the wrong questions. Switch to past behavior and specific instances.

**For deeper interview techniques:** See [2.2.1-Research-Interviews/](../../../2.2-Discovery/2.2.1-Research-Interviews/1-interview-guide.md) and [The Mom Test](https://momtestbook.com/) by Rob Fitzpatrick.

-----

## When You're Stuck on a Product Decision

### Uncertainty Type

- Am I stuck because:
- I don't understand the user need well enough?
- I don't know if it's technically feasible?
- I don't know if it aligns with strategy?
- I don't know how to prioritize it?
- I'm worried about organizational pushback?
- I don't know what success looks like?
- Am I actually missing information, or am I uncomfortable making a call in ambiguity?

### Missing Information

- What's the ONE thing that, if I knew it, would make this easy?
- Can I get that information? How? How long would it take?
- Is this decision reversible? If yes, just try something.
- What's the cheapest way to reduce uncertainty?

### Decision Quality

- Am I overthinking this because it's actually low-stakes?
- Am I underthinking this because I'm avoiding hard truths?
- What would [person I respect] ask me right now?
- What am I afraid of?
- What will likely still be unknown no matter how much research I do, and how will I choose to move anyway?

-----

## When Something Goes Wrong (Crisis / Incident)

### Root Cause

- What's the immediate cause? What's the underlying cause?
- What systemic issue allowed this? What assumptions failed?
- What signal did we miss?

### Impact Assessment

- Who is affected? How many?
- What's the severity? (Revenue, trust, safety.) What's the blast radius?
- What else could this break?

### Containment

- What stops it from getting worse NOW?
- What's the minimal viable fix? Can we roll back safely?
- What communication is urgent?

### Prevention

- What would have prevented this?
- What early warning signals exist? What process failed?
- How do we detect this earlier next time?

-----

## Before a Product Teardown

### Initial Impressions

- What's my gut reaction to this product? Why?
- What did I notice first? What did I ignore?
- What emotion does this product evoke?
- Would I recommend this to a friend? Why/why not?

### Hypothesis Formation

- Who do I think this is for?
- What job is it trying to do?
- What's the business model? (How do they make money?)
- What design decisions seem odd? (Often intentional - dig in)

### Questions to Investigate

- What's NOT here that I expected?
- What IS here that surprises me?
- What would I do differently? Why? (Be specific)
- What can I steal for my own products?

-----

## Before Talking to Stakeholders

### Their Perspective

- What do they care about that I don't?
- What pressures are they under?
- What does success look like from their seat?
- What am I asking them to risk?

### Your Ask

- What do I actually need from them?
- What's the minimum viable version of what I need?
- What's in it for them?
- What objections do I expect? How will I address them?

### Relationship Reality

- Do they trust me? If not, why not?
- Have I delivered for them before?
- What's the history I'm not accounting for?
- Who influences them that I should talk to first?

-----

## Generic Step 0 (any framework)

Use this when a framework has a "Step 0: Braindump" and no situation-specific section fits. Combine with the [Golden nuggets](#golden-nuggets-one-liners-that-work-almost-everywhere) and [30-second pre-flight](#30-second-pre-flight-before-any-major-decision).

- What are you trying to do? Dump your thinking - don't structure yet.
- What does your product sense tell you? What feels right or wrong?
- What assumptions are you making? List them explicitly.
- What biases might be affecting you? (See [2.0.2-Bias](../../2.0.2-Bias/1-bias-framework.md) for checklist.)

**Product sense exercise:**
- If you had to defend this to a skeptic, what would you say?
- What would make you say "this is obviously wrong"? "Obviously right"?

-----

## Before Stakeholder Mapping

- Who affects or is affected by your work? Dump everyone - don't filter yet.
- What does your product sense tell you? Who really matters?
- What assumptions are you making about relationships? List them.
- What biases might affect your stakeholder view? (Overvaluing some? Undervaluing others?)

**Product sense exercise:**
- If you had to get buy-in from ONE person, who would it be? Why?
- What would make you say "this stakeholder map is obviously wrong"?

-----

## Before Saying No

- What are they really asking for? Dump your understanding - don't judge yet.
- What does your product sense tell you? Is there a yes hidden in this request?
- What assumptions are you making? What's the real need behind the request?
- What biases might affect your response? (People-pleasing? Avoiding conflict?)

**Product sense exercise:**
- If you had unlimited resources, would you say yes?
- What would make you say "I obviously need to say no"?

-----

## Before Escalation

- What's the issue? Dump everything you know - don't structure yet.
- What does your product sense tell you? Can you handle this?
- What assumptions are you making? What have you tried?
- What biases might affect your decision? (Escalating too quickly? Avoiding escalation?)

**Product sense exercise:**
- If you had full authority, what would you do?
- What would make you say "I obviously need to escalate this"? "I can obviously handle this myself"?

-----

## Before Scheduling a Meeting

- What are you trying to accomplish? Dump everything - don't structure yet.
- What does your product sense tell you? Is a meeting really needed?
- What assumptions are you making? Could this be async instead?
- What biases might affect your meeting planning? (Meeting for meeting's sake? Status update trap?)
- If you had to accomplish this in 15 minutes, how would you do it? (Time constraint test)

-----

## Before Self-Reflection

Use after a decision, launch, or retro.

- What did you just work on? Dump everything - don't structure yet.
- What does your product sense tell you about what happened? What feels right or wrong?
- What assumptions did you make? List them explicitly.
- What biases might have affected your thinking? (Confirmation? Anchoring? Sunk cost?)

**Product sense exercise:**
- If you had to explain what happened to a mentor, what would you say?
- What would make you say "this outcome was obviously wrong"? "Obviously right"?

-----

## Before Continuous Discovery (interviews / synthesis / opportunities)

**Before conducting interviews:**
- What do you think you know about customers? Dump all assumptions.
- What biases might affect your interviews? (Confirmation bias? Solution bias?)
- What does your product sense tell you? What feels off or interesting?
- What would great product sense notice here? What would an experienced PM see?

**Before synthesizing:**
- What patterns do you think you're seeing? Dump your initial thoughts.
- What biases might affect your synthesis? (Pattern matching bias? Availability bias?)
- What does your gut tell you? What feels important?

**Before creating opportunities:**
- What opportunities do you think exist? Dump everything.
- What does your product sense tell you? What feels like a real opportunity?
- What biases might be affecting your view? (Solution bias? Feature bias?)

-----

## For AI Product Decisions

For deeper patterns (model capability tiers, prompt engineering as product design, safety/trust), see [5-ai-product-sense.md](5-ai-product-sense.md).

### Model Capabilities

- Can the current model even do this reliably?
- Am I designing for capabilities that don't exist yet?
- What happens when the model fails? (It will)
- How will users know when to trust vs. verify the output?

### Probabilistic Thinking

- This isn't deterministic - what's the accuracy range I need?
- What's the cost of false positives vs. false negatives?
- How do I handle edge cases without destroying UX?
- What does "good enough" look like here?
- If this succeeds, how might it change user behavior and expectations over time (second-order effects)?

### Safety & Ethics

- What could go wrong if this works perfectly?
- What biases might be lurking in the training data?
- Who could be harmed by this?
- What's my mitigation plan for hallucinations/mistakes?

### Human-AI Collaboration

- Where do I want the AI to decide vs. suggest vs. assist?
- How do I keep the human in control?
- What context does the AI need that it won't have?
- How do I build trust without over-trusting?

-----

## Meta-Prompt: When You Don't Know Which Prompts to Use

Ask yourself:

1. What decision am I trying to make?
1. What's blocking me from making it?
1. Is it knowledge gap, uncertainty, complexity, or fear?
1. What type of thinking would help most right now?

Then pick the relevant section above.

-----

## Remember

Use second-order thinking ("and then what?") and inversion ("what could go wrong?") in every braindump; they're the two mental models that most improve product sense. For when and how to use other mental models (first principles, one-way vs two-way doors, pre-mortems, opportunity cost, regret minimization), see [4-mental-models-product-sense-bridge.md](4-mental-models-product-sense-bridge.md).

These prompts are conversation starters, not a checklist. Skip what feels irrelevant; lean into what feels uncomfortable. Your braindump doesn't need to be pretty—only honest.

**After a major decision or braindump:** Capture learnings in [00-Meta/](../../../../../00-Meta/) — e.g. [daily log](../../../../../00-Meta/1-daily-log-YYYY-QX.md), [prioritization decision log](../../../../../00-Meta/2-prioritization-decision-log.md), [pattern recognition log](templates/6-pattern-recognition-log.md), or [forecast log](../../../../../00-Meta/0.3-Product-Judgment-Test/forecast-log.md). See [0-start-here](0-start-here-product-thinking.md) → Learnings & growth for links.
