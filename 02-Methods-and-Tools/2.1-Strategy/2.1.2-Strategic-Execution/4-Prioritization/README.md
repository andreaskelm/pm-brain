# Prioritization

## For Agents: When to Suggest Prioritization Frameworks

**Trigger conditions:**
- User mentions: "prioritize", "what should I build first", "backlog", "roadmap sequencing", "MVP scope", "what's most important"
- User is in: `execution_mode` (after braindump) or when user asks to prioritize features/initiatives
- Prerequisites: User has multiple options/initiatives to prioritize (not just one thing)
- User has: Some understanding of the options (may need discovery first if options are unclear)

**How to introduce:**
- "You have multiple initiatives to prioritize. Let's use a prioritization framework to make a defensible decision. First, which method fits your situation?"
- "Based on your thinking about [initiatives/features], let's structure this prioritization decision using [method from decision-tree]."

**Method selection (use `decision-tree.md`):**
- **ICE** - Quick call, little data, early ideas
- **RICE** - Bigger bets with data, feature/initiative scoring
- **Impact-Effort (Value-Effort)** - Workshop/alignment, visual, stakeholder sessions
- **MoSCoW** - Scope negotiation, timeboxed release, MVP definition
- **Kano** - Balance hygiene vs. delight, ensure table stakes covered

**Common mistakes to avoid:**
- Don't suggest prioritization if user only has one option (help them explore more options first)
- Don't skip braindump - prioritization frameworks organize judgment, they don't create it
- Don't suggest RICE if user has no data (suggest ICE or Impact-Effort instead)
- Don't suggest prioritization if user is still exploring opportunities (use Opportunity Assessment first)
- Don't create activity-based priorities (focus on outcomes, not just outputs)

**When NOT to use prioritization frameworks:**
- User is exploring opportunities (use Opportunity Assessment)
- User needs to define strategy first (use Strategic Foundations)
- User has only one clear option (help them validate it or explore alternatives)
- User is doing discovery (use Discovery frameworks first)

**Cross-reference:** If user needs to prioritize between validated opportunities, they should have completed Opportunity Assessments first. Link to Discovery frameworks if user hasn't validated options yet.

---

Systematic methods to decide what to do first. Use these to make defensible, transparent calls that align to strategy.

## Before Using This Framework

⚠️ **Don't jump straight to scoring frameworks.**

### 1. Read the Golden Rule

**See:** [`/PRODUCT-SENSE-RULES.md`](../../../../../PRODUCT-SENSE-RULES.md)

### 2. Braindump First (15 min)

**Use prompts from:** [`2-product-sense-prompts.md`](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → "Before Making a Prioritization Decision" section.

**Quick start (top 3-4 questions):**
- What evidence do I have this matters? (Real data, not vibes)
- What's the opportunity cost?
- Am I falling in love with my solution vs. the problem?
- What would make me 10x more confident?

**See prompts file for full list.** Prioritization frameworks can't create judgment—they organize it.

### 3. Log the Decision (Optional but Recommended)

Before or after you score, capture the decision in your **prioritization decision log**:

- **Log file:** `00-Meta/prioritization-decision-log.md`
- **What to capture:** who this is for, the real job/pain, evidence, opportunity cost, and “what could catastrophically go wrong if we’re wrong?”

This gives you a reusable trail of **why** you prioritized what you did, and lets you revisit the quality of your calls later.

### 4. Then Use This Framework

After your braindump (and optional log entry), use prioritization methods to structure your decision.

## Files
-`1-RICE-ICE/`
  - `1-RICE-ICE-scoring-framework.md`
  - `2-RICE-ICE-scoring-template.md`
- `2-Value-Effort-Matrix/2-Impact-Effort.md` — Lightweight Impact–Effort (Value–Effort) workshop method for visual alignment
- `3-MoSCoW/` — Categorical prioritization for scope/timeboxing
- `4-Kano-Model/` — Balance hygiene vs. delight
- `decision-tree.md` — Which method should I use? (quick chooser)

## How to use
1) **Braindump & product sense** – capture initiatives, assumptions, and biases first.  
2) **Pick a method** – use `decision-tree.md` to choose (RICE/ICE, Impact-Effort, MoSCoW, Kano).  
3) **Apply the framework** – use the relevant framework/template pair.  
4) **Review balance** – check mix of quick wins vs. big bets; hygiene vs. delight.  
5) **Decide & document** – record rationale and next review date.  
6) **Reflect** – what changed, what biases you caught, what you’d do differently.

## When to use
- Backlog or quarterly planning
- Sequencing roadmap items (Now/Next/Later)
- MVP scoping or release negotiation (MoSCoW)
- Balancing delighters vs. table stakes (Kano)
- Workshop alignment (Impact-Effort)

## How to maintain
- **Weekly**: Revisit top items for progress/changes.  
- **Bi-weekly**: Groom backlog, score new ideas.  
- **Monthly**: Portfolio balance check.  
- **Quarterly**: Full re-prioritization aligned to strategy/OKRs.

## Links
- Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
- OKR Framework: `../1-OKR/README.md`
- Roadmap: `../2-Roadmap/README.md`
- North Star: `../3-North-Star/README.md`
- Discovery: `../../2.2-Discovery/README.md` (Opportunity Assessment)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
