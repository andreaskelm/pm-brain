# Product Sense Rules - The Golden Rule

**What this doc is:** The canonical definition of the **golden rule** (one sentence below) and the **braindump workflow** (why it matters + 3 steps). Read it when you want the rationale and the step-by-step. For *where to go* and *how the agent moves*, see [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md). For the **actual questions** (prompts by situation), see [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md).

**For agents (read-only spec):** This file is the *canonical specification* of the golden rule and workflow. For *behavioral enforcement* (when to apply it, eval checkpoints, mode transitions), see [AGENTS.md](AGENTS.md) and [ORCHESTRATION.md](ORCHESTRATION.md). This doc defines the *what* and *why*; orchestration defines the *when* and *how*.

---

**The Golden Rule: Braindump before structure.**

Before you open any framework, template, or structured thinking tool: **brain dump first**.

**Single entry point:** [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) — navigation, simple prompt to start, [when is what invoked](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md#when-is-what-invoked-what-controls-what), [how the agent moves](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md#how-the-agent-moves-workflow).

Your raw, unstructured thinking is more valuable than perfectly formatted templates filled with shallow answers.

-----

## Why This Matters

**The problem with frameworks:** They're seductive. They promise clarity. They give you boxes to fill.

**The trap:** You fill the boxes without actually thinking deeply. You optimize for completion, not insight.

**The solution:** Think BEFORE you structure.

-----

## The Workflow

### Step 1: Braindump (No Structure)

**Before you start:** Am I in product mode (why, goals, second-order, trade-offs) or project mode (when, who, completion)? If you're about to fill boxes, switch to product mode first.

When you have a product decision, problem, or opportunity:

1. **Consider what context to bring into the conversation:** company/vision/strategy, roadmap, research artifacts, active initiatives ([01-Company-Context/](01-Company-Context/README.md), [03-Research-Artifacts/](03-Research-Artifacts/README.md), [04-Initiatives/](04-Initiatives/README.md)). Add or @-mention key docs so the agent can use them; this speeds up product thinking.
1. **Don't open a template yet**
1. **Open a blank doc** (or voice memo, or whiteboard)
1. **Ask yourself the messy questions** (see `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md`)
1. **Write/speak your raw thinking** - don't edit, don't organize, don't worry about completeness
1. **Go where your thinking takes you** - even if it feels off-topic
1. **Write until you feel stuck or satisfied**

**Time box:** 10-30 minutes

**Output:** Messy, raw, honest thinking

### Is the braindump \"sufficient\"?

Before you (or the agent) leave braindump mode and move on to frameworks, check that **at least** these are true:

- You have **named your key assumptions** (not just your desired outcome).
- You have separated **what you know vs. what you are guessing**.
- You have touched at least one **risk, edge case, or second-order effect** (\"and then what?\").
- You have written something that feels a bit **uncomfortable or challenging** to your current plan.

If these aren’t true yet, you are still in **product_sense**; stay with the prompts and braindump a bit longer before moving to structure.

### Step 2: Pattern Recognition (Light Structure)

Review your braindump:

- What themes emerged?
- What assumptions am I making?
- What do I actually know vs. what am I guessing?
- What makes me uncomfortable?
- What am I avoiding?

**Time box:** 5-10 minutes

**Output:** Self-awareness about your thinking

### Step 3: NOW Use the Framework (Structured Thinking)

**Now** open the relevant framework/template from `02-Methods-and-Tools/`:

- PRD template
- Opportunity assessment
- Prioritization framework
- Research plan
- Whatever fits your need

**Use your braindump to inform the structure.** Copy insights, quotes, questions from your raw thinking.

**Time box:** Variable (depending on framework)

**Output:** Structured artifact informed by deep thinking

### Before Any Major Decision: 30-Second Pre-Flight

Right before you decide or open a framework, run the **full checklist** (quick checks, red flags STOP, green lights PROCEED) in [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) at the top of the file.

**Minimum:** Can I articulate WHY? Have I asked "and then what?" at least twice? Do I know who loses from this?

### Confidence-Based Decision Rules

Use your confidence level + reversibility to choose how to proceed. For full calibration (forecast log, Brier score, review), see [00-Meta/0.3-Product-Judgment-Test](00-Meta/0.3-Product-Judgment-Test/).

| Confidence | Reversibility | Action |
|------------|----------------|--------|
| **>80%** | Reversible | Decide now. Set review date. |
| **>80%** | Irreversible | Double-check with 2–3 others first, then decide. |
| **50–80%** | Can learn quickly (&lt;1 day) | Gather specific info that would increase confidence, then decide. |
| **50–80%** | Slow to learn | Decide with current info + set clear review point to adjust. |
| **&lt;50%** | — | Don't decide yet. Either learn more or reframe the decision. |

-----

## Why This Works

### Braindump First = Better Thinking

**Traditional approach:**
1. Open PRD template
1. Fill in boxes
1. Ship it
Result: Shallow, checkbox thinking

**Braindump-first approach:**
1. Think deeply about the problem
1. Discover what you don't know
1. Use framework to organize insights
Result: Deep thinking captured in structure

### Frameworks Are Tools, Not Substitutes for Thought

**Good use:** "I've thought deeply about this. Now I'll use the PRD template to organize my thinking for stakeholders."

**Bad use:** "I need to write a PRD. Let me fill in the boxes."

**The difference:** Frameworks organize good thinking. They don't create it.

-----

## When to Braindump

### Before Writing a PRD

**Don't open the PRD template yet.**

First, braindump:
- Who is this really for?
- What job are they hiring this feature to do?
- What am I assuming about how they'll use this?
- What could go catastrophically wrong?
- Why this, why now?

**Then** use the PRD template.

### Before Prioritizing Features

**Don't open the prioritization framework yet.**

First, braindump:
- What evidence do I have this matters?
- What's the opportunity cost?
- Am I falling in love with my solution vs. the problem?
- What would make me 10x more confident?

**Then** use the prioritization framework.

### Before User Research

**Don't open the research plan template yet.**

First, braindump:
- What assumption, if wrong, would completely change our plans?
- What am I hoping NOT to hear? (Red flag - investigate this)
- What did we learn last time that we ignored?

**Then** use the research plan template.

### Before Strategy Sessions

**Don't open the strategy framework yet.**

First, braindump:
- What's actually working vs. not working? (Be brutally honest)
- What are we deluding ourselves about?
- Where is the market going that we're not ready for?

**Then** use the strategy framework.

### When You're Stuck on a Decision

**Don't jump to a decision framework yet.**

First, braindump:
- What am I actually afraid of?
- Is this reversible?
- What's the ONE thing that, if I knew it, would make this easy?

**Then** use the decision diagnostic: `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/3-product-sense-evaluation.md`

-----

## How to Actually Do This

### Option 1: Written Braindump

1. Open blank doc or text file
1. Set timer for 15 minutes
1. Write continuously - don't stop to edit
1. Answer the prompts that feel relevant
1. Follow tangents - they're usually important
1. Stop when timer ends or you feel complete

### Option 2: Voice Memo Braindump

1. Open voice recorder on phone
1. Walk and talk
1. Ask yourself the prompts out loud
1. Answer like you're explaining to a friend
1. Ramble - that's the point
1. Transcribe later (or just listen back)

### Option 3: Whiteboard Braindump

1. Stand at whiteboard
1. Write messy, draw connections
1. Use different colors for different types of thinking
1. Take photo when done
1. Clean it up later if needed

### Option 4: Conversation Braindump

1. Find a sparring partner
1. Explain your thinking out loud
1. Let them ask questions
1. Don't defend - just explore
1. Write down insights after

**Pick the method that matches your thinking style.**

-----

## The Prompts to Use

See `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md` for detailed prompts for:

- Before writing a PRD
- Before prioritization decisions
- Before product strategy sessions
- Before user research
- When stuck on decisions
- Before product teardowns
- Before talking to stakeholders
- For AI product decisions

**Don't use all the prompts.** Pick the 3-5 that make you uncomfortable. Those are the important ones.

-----

## What This Looks Like

### Bad Example: Template-First Thinking

```
PRD: New Feature X

Problem: Users need feature X
Solution: Build feature X
Success metrics: Usage of feature X
Timeline: 6 weeks

[Boxes filled. Thinking? Minimal.]
```

### Good Example: Braindump-First Thinking

```
BRAINDUMP:

Who is this really for? Not "users" - be specific. It's Sarah, the ops manager who's drowning in manual work. She's been asking for automation for 6 months. But wait - is she asking for the right thing? What job is she actually trying to do?

She says she wants automation. But when I watched her work, she doesn't trust automation - she manually checks everything anyway. So the real job isn't "automate" - it's "confidence that nothing breaks."

What if instead of building automation (which she won't trust), we build transparency? Show her exactly what's happening so she can spot issues fast?

Wait, that's different from what we specced. The current spec is "automate manual tasks" but maybe it should be "make manual checking faster and more reliable."

What am I assuming? I'm assuming she wants to eliminate work. But maybe she wants to do her work better, not eliminate it. Her job security might depend on being the person who catches issues.

[... continues for another page ...]

---

NOW I'll fill out the PRD template, with all these insights.
```

**See the difference?**

The braindump uncovered:
- The real user (Sarah, not "users")
- The real job (confidence, not automation)
- A hidden assumption (she wants to eliminate work vs. do it better)
- A completely different solution direction

**The template alone would never surface this.**

-----

## Common Objections

### "I don't have time for this"

You don't have time NOT to do this.

15 minutes of braindumping saves hours (or weeks) of building the wrong thing.

### "My thinking is too messy"

**Good.** Messy thinking is honest thinking.

If your thinking is neat and clean, you're probably not thinking deeply.

### "What if my braindump is wrong?"

Then you learned something valuable BEFORE you built it.

Wrong thinking in a braindump = discovery
Wrong thinking in production = disaster

### "My team wants structured docs, not messy braindumps"

**Give them both.**

Braindump for YOU (to think deeply)
Structured doc for THEM (to communicate clearly)

The braindump is the recipe. The doc is the meal.

### "I already know what to build"

**Dangerous.**

The times you're most confident are when you most need to braindump.

Ask yourself: What am I not questioning that I should be?

-----

## Integration with PM Brain

This braindump-first approach works WITH the PM Brain framework library, not against it.

**The frameworks in `02-Methods-and-Tools/` are still valuable.** They help you:
- Organize your thinking
- Communicate with stakeholders
- Ensure you've considered key dimensions
- Create artifacts for decision-making

**But frameworks are the SECOND step, not the first.**

1. **First:** Braindump (this file)
1. **Second:** Framework (`02-Methods-and-Tools/`)
1. **Third:** Execution (`04-Initiatives/`)

-----

## Daily Practice

Make this a habit:

**Morning:** Before jumping into work, braindump for 10 minutes
- What's the most important thing today?
- What am I avoiding?
- What assumption should I test?

**Before any major decision:** 15-minute braindump first

**End of day:** 5-minute reflection braindump
- What did I learn today?
- What surprised me?
- What would I do differently?

**Weekly:** 30-minute braindump on the week
- What patterns am I seeing?
- What's working vs. not working?
- What do I need to change?

-----

## AI Assistance for Braindumping

AI tools (like this assistant) can help you braindump:

**Good uses:**
- "Help me think through [problem] before I write the PRD"
- "Challenge my assumptions about [opportunity]"
- "Ask me questions that surface blind spots"
- "Play devil's advocate on [decision]"

**Bad uses:**
- "Write a PRD for [feature]" (skips the thinking)
- "Fill out this framework for me" (checkbox thinking)
- "What should I build?" (outsourcing judgment)

**The AI should help you think better, not think FOR you.**

-----

## Remember

**Frameworks don't think. You do.**

Templates organize thinking. They don't create it.

The best product decisions come from deep, honest thinking that gets structured later.

**Braindump first. Structure second. Execute third.**

**Your raw thinking is more valuable than your polished templates.**

-----

## Quick Reference

**When you're about to open a template, STOP.**

Ask yourself:

1. Have I thought deeply about this yet?
1. What do I believe that I shouldn't?
1. What makes me uncomfortable about this?
1. What am I avoiding?

If you haven't braindumped, **don't open the template yet**.

Think first. Structure later.

**That's the golden rule.**

-----

## Links to Key Resources

- **Braindump prompts:** `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md`
- **Decision diagnostic:** `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/3-product-sense-evaluation.md`
- **Daily practice exercises:** `02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/templates/1-daily-practice-exercises.md`
- **Framework library:** `02-Methods-and-Tools/`

Start with braindumping. Always.
