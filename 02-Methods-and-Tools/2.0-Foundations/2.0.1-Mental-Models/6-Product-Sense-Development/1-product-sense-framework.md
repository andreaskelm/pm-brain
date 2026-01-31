# Product Sense Development Framework

**Purpose:** Systematic method for developing product intuition through deliberate practice.

Product sense—the ability to make good product decisions under uncertainty—is a skill. Like any skill, it improves with deliberate practice. This framework provides the structure, exercises, and tracking system to develop stronger product judgment over time.

-----

## What Is Product Sense?

Product sense is the combination of:

1. **Customer Insight** - Deep understanding of user needs, behaviors, and motivations
2. **Market & Opportunity Analysis** - Ability to see market dynamics, competitive positioning, and opportunities
3. **Solution Design** - Skill in crafting products that elegantly solve problems
4. **Strategic Judgment** - Capability to make good prioritization and tradeoff decisions

**It's not:**
- Memorizing frameworks
- Following checklists
- Copying what successful products do
- Having all the answers

**It is:**
- Pattern recognition
- Intuition built from experience
- Judgment calibrated through practice
- Ability to think deeply before structuring

### Second-Order Effects and Ambiguity Tolerance

Two abilities quietly sit underneath strong product sense:

- **Second-order effects** - Seeing not just the immediate impact of a decision, but the ripple effects on user behavior, the product surface area, the team, and future options. Great PMs ask: *\"If this works (or fails), what does that change later?\"*
- **Ambiguity tolerance** - Making thoughtful bets when information is incomplete, conflicting, or noisy. Instead of waiting for certainty, you identify what will likely remain unknown, decide what level of risk is acceptable, and move anyway with clear eyes.

-----

## Why Deliberate Practice Matters

**The problem:** Most PMs learn product sense through:
- Trial and error (slow, expensive mistakes)
- Copying others (works until context changes)
- Reading frameworks (knowledge without judgment)
- On-the-job experience (unstructured, inconsistent)

**The solution:** Deliberate practice:
- **Structured exercises** that target specific skills
- **Consistent practice** that builds habits
- **Reflection** that accelerates learning
- **Tracking** that proves growth

**The research:** Deliberate practice is how experts develop expertise (Ericsson, Dweck, Dweck). 10 minutes daily compounds faster than 2 hours monthly.

-----

## How This System Works

### The Practice Cycle

```
Daily Practice (10 min)
   ↓
Weekly Reflection (30 min)
   ↓
Monthly Synthesis (60 min)
   ↓
Growth Portfolio (evidence for reviews)
```

### Daily Practice (10 minutes)

**What:** Pick ONE exercise from the daily practice menu
- User observation
- Product teardown
- Cross-domain inspiration
- Pattern recognition
- Judgment training

**How:** Set timer, do it, log 1-2 sentence insight

**Why:** Builds product thinking into muscle memory

**Where:** Log in `00-Meta/1-daily-log-YYYY-QX.md`

### Weekly Reflection (30 minutes)

**What:** Synthesize week's practice and decisions

**How:** 
1. Review daily log
2. Copy weekly reflection template
3. Identify patterns, decisions, learnings
4. Set focus for next week

**Why:** Connects daily dots into weekly insights

**Where:** `00-Meta/0.1-Learning-Log/[Year]-Q[#]/week-##.md`

### Monthly Synthesis (60 minutes)

**What:** Review month's growth and patterns

**How:**
1. Review all weekly reflections
2. Update self-assessment (rate 4 dimensions)
3. Update growth portfolio
4. Identify trajectory and focus areas

**Why:** Tracks growth trajectory, calibrates judgment

**Where:** `00-Meta/0.1-Learning-Log/[Year]-Q[#]/monthly-[month].md`

### Growth Portfolio (Ongoing)

**What:** Evidence of product sense development

**How:** Document journey, decisions, and outcomes

**Why:** Proof for 1:1s, performance reviews, career growth

**Where:** `00-Meta/0.2-Growth-Portfolio/`

-----

## The Four Dimensions

Rate yourself monthly on these dimensions (1-5 scale):

### 1. Customer Insight

**1 - Surface Level:** I understand what users say they want
**2 - Feature Requests:** I can categorize user feedback and identify patterns
**3 - Underlying Needs:** I can distinguish between stated wants and actual needs
**4 - Predictive:** I can anticipate needs users haven't articulated
**5 - Transformative:** I see opportunities that reframe how users think about their problems

### 2. Market & Opportunity Analysis

**1 - Reactive:** I respond to what competitors do
**2 - Aware:** I track market trends and competitive moves
**3 - Analytical:** I can assess market size, timing, and positioning
**4 - Strategic:** I identify opportunities others miss and explain why they matter
**5 - Visionary:** I see where markets are heading before consensus forms

### 3. Solution Design

**1 - Feature Factory:** I translate requests into features
**2 - User-Centered:** I design based on observed user behavior
**3 - Balanced:** I balance user needs, technical constraints, business goals
**4 - Innovative:** I generate novel solutions that elegantly solve complex problems
**5 - Transformative:** I create solutions that change user behavior and market expectations

### 4. Strategic Judgment

**1 - Overwhelmed:** I struggle to choose between options
**2 - Framework-Driven:** I use scoring/prioritization methods mechanically
**3 - Context-Aware:** I adapt prioritization to situation and constraints
**4 - Principled:** I make clear tradeoffs aligned with strategy and can defend them
**5 - Masterful:** I see second-order effects (user behavior shifts, team/org consequences, future optionality) and make bets that compound over time, even when the information is messy or incomplete

**See:** `templates/2-self-assessment-template.md` for detailed assessment framework.

-----

## Core Prompts You Can Reuse Everywhere

You do not need every prompt in this system to think deeply. A small set of questions gets you most of the way there.

Use these **core prompts** before any framework, decision, or document:

- **Who is this really for, and what is their day like?**
- **What job is this doing for them?**
- **What assumptions am I making? What don’t I actually know yet?**
- **If this works, what second-order effects might it create later—for users, the product, the team, or the business?**
- **What could go wrong, and what would I do if it did?**

Everything else in the templates is optional depth layered on top of these few questions.

-----

## Integration with PM-Brain

### The Three-Layer System

**Layer 1: How to Think (This Framework)**
- Product sense development through practice
- **Output:** Better judgment, faster pattern recognition, stronger intuition

**Layer 2: How to Execute (02-Methods-and-Tools)**
- Framework library for doing PM work
- **Output:** PRDs, roadmaps, research plans, strategy docs

**Layer 3: What You're Building (04-Initiatives)**
- Your actual product work
- **Output:** Shipped features, user value, business impact

**The flow:**
```
1. Practice product thinking (00-Meta)
   ↓
2. Use frameworks to structure thinking (02-Methods-and-Tools)
   ↓
3. Execute on initiatives (04-Initiatives)
   ↓
4. Reflect on outcomes (00-Meta)
   ↓
[repeat]
```

**Key principle:** Product sense practice makes you better at using frameworks, which makes you better at executing initiatives.

### Before Using Any Framework

**The Golden Rule:** Braindump before structure.

**Never jump straight to templates.**

1. **First:** Braindump using `2-product-sense-prompts.md` (10-15 min)
   - Think deeply, ask uncomfortable questions
   - Don't worry about structure or completeness
   - Go where your thinking takes you

2. **Second:** Use framework from `02-Methods-and-Tools/` (variable)
   - Use your braindump to inform the structure
   - Copy insights, quotes, questions from raw thinking
   - Fill templates with deep thinking, not shallow answers

3. **Third:** Execute in `04-Initiatives/` (ongoing)
   - Build the thing
   - Ship it
   - Learn from outcomes

**Example:**

Before writing a PRD:
1. Braindump: Who is this really for? What job are they hiring it to do? What could go wrong? Why this, why now?
2. Then: Use `02-Methods-and-Tools/2.3-Execution/2.3.4-PRD/2-prd-template.md`
3. Execute: Build the thing in `04-Initiatives/4.1-Initiative-Codename/`

**This ensures deep thinking, not checkbox thinking.**

-----

## When to Use This Framework

### Use When:
- You want to systematically improve your product judgment
- You're new to product management and want to build intuition
- You're stuck on decisions and need better judgment
- You want evidence of growth for performance reviews
- You want to develop deeper product thinking before using templates
- You want to build a habit of deliberate practice

### Don't Use When:
- You need immediate tactical help (use specific frameworks instead)
- You're looking for a quick fix (this is a long-term practice system)
- You want to skip the thinking and just fill templates (defeats the purpose)
- You're already an expert and don't need practice (experts still practice)

-----

## Common Pitfalls

### ❌ Trying to do everything

**Don't:**
- Do all 10 daily exercises every day
- Do all weekly exercises every week
- Fill out every prompt in braindump

**Do:**
- Pick one daily exercise
- Pick one weekly exercise
- Answer the prompts that make you uncomfortable

**Quality > quantity.**

### ❌ Skipping the braindump

**Don't:**
- Jump straight to frameworks
- Fill templates without thinking first
- Optimize for completion over insight

**Do:**
- Always braindump first
- Think messy before thinking structured
- Use frameworks to organize, not create, thinking

Remember that you'll almost never have perfect information. The goal is not to remove ambiguity, but to **name it, think through second-order effects, and still make a deliberate bet.**

### ❌ Being too hard on yourself

**Don't:**
- Expect instant transformation
- Beat yourself up for skipping days
- Inflate self-assessment scores to feel better

**Do:**
- Expect gradual, compounding improvement
- Resume practice after breaks
- Be brutally honest in self-assessments

**Growth requires honest self-awareness.**

### ❌ Practicing in isolation

**Don't:**
- Never share your insights
- Avoid getting feedback
- Practice alone forever

**Do:**
- Discuss insights with teammates
- Request feedback quarterly
- Find a practice buddy

**Learning accelerates through conversation.**

-----

## Expected Outcomes

### After 1 Month
- You braindump before jumping to solutions
- You catch assumptions earlier
- Stakeholders notice your "why" answers are deeper
- Daily practice feels natural

### After 3 Months
- Pattern recognition speeds up
- You generate more diverse solutions faster
- Self-assessments show measurable improvement
- Weekly practice is a highlight of your week

### After 6 Months
- Product intuition is noticeably stronger
- Decision retrospectives prove better judgment
- Your product launches have better outcomes
- You can't imagine working without this system

### After 1 Year
- You're the person others come to for product thinking
- Your self-assessments show dramatic growth
- Your growth portfolio speaks for itself
- This system is part of who you are as a PM

-----

## Making This Stick

### Schedule It
- [ ] Block 10 min daily: "Product Practice"
- [ ] Block 60 min weekly: "Deep Product Work"
- [ ] Block 30 min monthly: "Self-Assessment"

### Start Small

**Week 1:**
- Just do 3 daily exercises
- Skip weekly deep work if it feels like too much
- Get the rhythm

**Week 2-4:**
- Add weekly deep work
- Find your preferred exercises
- Build the habit

**Month 2+:**
- Full system engaged
- Rhythm established
- Seeing benefits

**It's okay to start small. It's not okay to never start.**

-----

## Remember

**Product sense is a skill. Skills improve with practice.**

This framework gives you the practice system.

Use it consistently and honestly; your product sense will compound.

You will often be deciding in fog. Practicing with these prompts trains you to navigate ambiguity and second-order consequences, not to eliminate them.

-----

## Quick Links

- **Braindump prompts:** [`2-product-sense-prompts.md`](2-product-sense-prompts.md)
- **Decision diagnostic:** [`3-product-sense-evaluation.md`](3-product-sense-evaluation.md)
- **Daily exercises:** [`templates/1-daily-practice-exercises.md`](templates/1-daily-practice-exercises.md)
- **Self-assessment:** [`templates/2-self-assessment-template.md`](templates/2-self-assessment-template.md)
- **Golden Rule:** [`PRODUCT-SENSE-RULES.md`](../../../../../PRODUCT-SENSE-RULES.md)
- **Your practice space:** [`00-Meta/`](../../../../../00-Meta/)

**Start with daily practice. Everything else follows.**
