# 0.2 Growth Portfolio

**Purpose:** Evidence of your product sense development for 1:1s, performance reviews, and career growth.

This is where your practice becomes proof.

-----

## Mode & Visibility

**Your portfolio visibility depends on your PM-Brain mode:**

- **🌍 Public Mode:** Portfolio is tracked and visible (great for public portfolio/blog)
- **🔒 Private Mode:** Portfolio is private (files ignored by git)
- **👥 Team Mode:** Portfolio is private (files ignored by git)

**To check or change mode:** See `00-Meta/README.md`

**Note:** Even in private/team modes, you can selectively share portfolio content by:
- Copying to a separate public repo
- Sanitizing and sharing specific entries
- Using it locally for 1:1s and reviews

Your portfolio is valuable regardless of whether it's tracked in git.

-----

## What's in This Folder

### 1-product-sense-journey.md
Your product sense trajectory over time.

**Product Judgment Test:** Your [Overall Brier trend](../0.3-Product-Judgment-Test/dashboard.md) is evidence of calibration—reference it in your journey and in [3-metrics-dashboard.md](3-metrics-dashboard.md).

**Sections:**
- Timeline of key milestones
- Skills developed
- Frameworks mastered
- Challenges overcome
- Inflection points

**Update:** Monthly (after synthesis)

**Use for:** Performance reviews, promotions, job interviews

### 2-decision-showcase.md
Your best product decisions and what you learned.

**Sections:**
- High-impact decisions
- Difficult tradeoffs
- Learning from failures
- Reversals and pivots
- Decision quality metrics

**Update:** Quarterly (or after significant decisions)

**Use for:** 1:1s, case study interviews, demonstrating judgment

-----

## How to Use This

### Monthly: Keep It Current

After completing your monthly synthesis:

1. **Open growth portfolio files**

2. **Update 1-product-sense-journey.md:**
   - Add any milestone from the month
   - Note skills that leveled up
   - Document challenges overcome

3. **Update 2-decision-showcase.md:**
   - Add significant decisions from the month
   - Track outcomes

4. **Commit:**
   ```bash
   git add 0.2-Growth-Portfolio/
   git commit -m "docs: Update growth portfolio - January 2026"
   ```

**Time:** 15 minutes/month

**Why:** When review season comes, you won't remember what you did in Q1.

### Quarterly: Deep Update

Every 3 months:

1. **Review all monthly syntheses** from the quarter

2. **Update 2-decision-showcase.md:**
   - Add 2-3 best decisions from the quarter
   - Document what you learned
   - Note decision outcomes

3. **Review the whole portfolio:**
   - Is your narrative clear?
   - Does it show growth trajectory?
   - Would a stranger understand your impact?

**Time:** 45 minutes/quarter

### Performance Review: Pull It Together

Before your performance review:

1. **Read your entire portfolio** (30 min)

2. **Prepare your narrative:**
   - What was I working on?
   - How did I grow?
   - What impact did I deliver?
   - Why am I ready for the next level?

**Time:** 90 minutes (once or twice per year)

**Result:** You walk into the review with receipts.

-----

## What Good Portfolio Entries Look Like

### Product Sense Journey

**Bad:**
```
## Q1 2026
- Did some work
- Got better at PM
- Shipped features
```

**Good:**
```
## Q1 2026: Shipped 3 Features, Killed 2 Early, Established Weekly Practice

**Skills Developed:**
- User research: Conducted 8 observation sessions, 3 interviews
- Decision-making: Killed 2 low-impact features in week 1 (saved 8 weeks)
- Strategic thinking: Led Q2 planning, introduced ICE prioritization

**Inflection Point:**
Week 8 - stopped avoiding user research, watched users struggle with 
checkout flow, completely changed our Q2 roadmap. This one decision 
prevented us from building the wrong thing.

**Evidence:**
- Weekly reflections: 00-Meta/0.1-Learning-Log/2026-Q1/
- Self-assessment: Customer Insight 3.0 → 3.5, Strategic Judgment 3.5 → 4.0
```

### Decision Showcase

**Bad:**
```
## Feature X
- We built it
- Users liked it
- Good decision
```

**Good:**
```
## Feature X: Chose Fast Iteration Over Perfect Launch

**Context:** Pressure to launch "perfect" checkout flow. Engineering wanted 
2 more months. Sales wanted it yesterday.

**Decision:** Ship MVP in 2 weeks, iterate based on real usage.

**Why:** Checkout flow assumptions were untested. Better to learn fast than 
build perfectly wrong.

**Tradeoff:** Accepted some rough edges for faster learning.

**Outcome:**
- Week 1: 20% of users hit edge case we didn't anticipate
- Week 2: Fixed based on real data
- Month 1: 15% increase in conversion
- Avoided 6 weeks building features users didn't need

**Learning:** On reversible decisions with high uncertainty, bias toward 
shipping and learning. My instinct to wait for perfect was wrong.

**Confidence:** Was 60% confident. Turned out 90% right.

**Evidence:** Weekly reflection week-06.md, monthly synthesis January
```

### Framework Contributions

**Bad:**
```
- Shared some templates
- Helped the team
```

**Good:**
```
## Introduced "Braindump Before Structure" Practice

**Problem:** Team was filling out PRD templates without deep thinking.
PRDs looked complete but decisions were shallow.

**Solution:** Introduced braindump practice and prompts before any framework.

**Adoption:**
- 4 PMs now braindump before PRDs
- Average PRD quality feedback score: 3.2 → 4.1
- Stakeholders comment on "better why explanations"

**Artifacts Created:**
- Braindump prompts template: 02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-template.md
- Updated all major frameworks with "Before using this framework" section
- Presented at PM team meeting, created Slack channel

**Impact:** Team's product thinking depth improved measurably.
```

-----

## Tips for Building Your Portfolio

### Document as You Go

**Don't wait for performance reviews.**

5 minutes/month documenting > 5 hours before review trying to remember what you did.

### Be Specific

**Vague:**
- "Improved product sense"
- "Made good decisions"
- "Helped the team"

**Specific:**
- "Customer Insight rating increased 3.0 → 3.5 (evidence: 8 user observations)"
- "Killed 2 features early, saved 8 weeks (evidence: decision showcase)"
- "Introduced braindump practice, 4 PMs adopted, PRD scores 3.2 → 4.1"

**Specificity = credibility.**

### Link to Evidence

Every claim should link to evidence:
- Learning log entries
- Weekly reflections
- Self-assessments
- Decision retrospectives
- Shipped features
- User feedback
- Metrics dashboards

**"I got better" (unsubstantiated) vs. "I got better (see self-assessment, weekly reflections, decision outcomes)" (credible)**

### Show Growth, Not Perfection

**Don't hide failures. Show what you learned.**

**Bad:**
- Only list wins
- Ignore mistakes
- Pretend you're perfect

**Good:**
- "Feature Y failed because I didn't talk to users. Learned: now I do 2 observations/week"
- "Overestimated technical feasibility 3x this quarter. Learned: now I prototype before committing"
- "Avoided hard stakeholder conversation, project delayed 4 weeks. Learned: escalate early"

**Growth is more impressive than perfection.**

### Update Monthly, Not Yearly

**Yearly updates = you forget everything.**

**Monthly updates = 15 min/month = complete portfolio.**

Set calendar reminder: "Last Friday: Update growth portfolio"

-----

## Using This for Career Growth

### Performance Reviews

Pull from portfolio:
- Product sense journey → Shows trajectory
- Decision showcase → Demonstrates judgment
- Impact metrics → Proves delivery
- Framework contributions → Shows leadership

**You'll have specific examples with evidence. Your manager won't.**

### Promotion Conversations

Portfolio demonstrates:
- **Current level mastery:** Impact metrics, decision quality
- **Next level readiness:** Framework contributions, team influence
- **Growth trajectory:** Self-assessments over time

**Promotions go to people who can prove readiness. This is the proof.**

### Job Interviews

Decision showcase = ready-made case studies:
- "Tell me about a hard decision"
- "Tell me about a failure and what you learned"
- "How do you prioritize?"
- "Give me an example of product sense"

**You'll have polished, evidence-backed stories. Other candidates will improvise.**

### 1:1s with Manager

Monthly portfolio updates = monthly talking points:
- "Here's what I shipped this month"
- "Here's how I grew"
- "Here's where I need support"

**Structured 1:1s > rambling updates.**

-----

## Remember

**Your growth is happening. Document it.**

Without documentation:
- You forget what you did
- Your manager forgets what you did
- You can't prove growth
- You undersell yourself

With documentation:
- Clear trajectory
- Specific examples
- Measurable growth
- Confident self-advocacy

**15 minutes/month documenting = career insurance.**

-----

## Quick Links

- **Journey:** `1-product-sense-journey.md`
- **Decisions:** `2-decision-showcase.md`

**Update monthly. Use for reviews. Advance your career.**
