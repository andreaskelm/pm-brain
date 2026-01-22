# Opportunity Solution Tree Guide

## Disclaimer

The Opportunity Solution Tree is a living document. It evolves as you conduct continuous discovery and learn more about your customers and opportunities.

**Last Updated:** [Date]
**Next Review:** [Date]
**Product Trio:** [PM, Designer, Engineer]
**Interview Cadence:** [Weekly / Bi-weekly]

-----

## 🌳 Opportunity Solution Tree Structure

```
Desired Outcome
│
┌───────────────┼───────────────┐
│ │ │
Opportunity 1 Opportunity 2 Opportunity 3
│ │ │
┌────┼────┐ ┌────┼────┐ ┌────┼────┐
│ │ │ │ │ │ │ │ │
S1 S2 S3 S4 S5 S6 S7 S8 S9
│ │ │ │ │ │ │ │ │
E1 E2 E3 E4 E5 E6 E7 E8 E9

Legend:
Outcome = Desired business/product outcome
Opportunity = Customer need, pain point, desire
S = Solution (multiple per opportunity)
E = Experiment/Assumption Test
```

-----

## 🎯 Step 1: Define Your Desired Outcome

**Purpose:** Establish the North Star for this work—what business and customer value you're trying to create.

**Characteristics of Good Outcomes:**

- Measurable and specific
- Balances business and customer value
- Within team's control to influence
- Time-bound (usually quarterly)
- Motivating and clear

**Outcome Template:**

```
[Verb] [Metric] [by X%] [by date]

Examples:
- Increase trial-to-paid conversion rate by 25% by Q2
- Reduce time-to-first-value from 8 min to 5 min by Q3
- Improve 30-day retention from 45% to 60% by year-end
```

**Bad Outcomes (Outputs, not outcomes):**

- ❌ Ship 5 new features this quarter
- ❌ Improve the onboarding experience
- ❌ Make users happy

**Good Outcomes (Impact-focused):**

- ✅ Increase activation rate from 42% to 60% by Q2
- ✅ Reduce support tickets by 30% by Q3
- ✅ Grow weekly active users by 20% by year-end

**Your Desired Outcome:**

```
Outcome: [Write your specific, measurable outcome]

Why this matters to business: [Business value]

Why this matters to customers: [Customer value]

How we'll measure success: [Specific metrics and targets]

Timeframe: [When we expect to achieve this]
```

-----

## 🔍 Step 2: Map the Opportunity Space

**Purpose:** Identify customer needs, pain points, and desires that, if addressed, would drive your desired outcome.

**Where Opportunities Come From:**

- User interviews (primary source)
- Support tickets and feedback
- Analytics and data analysis
- Sales conversations
- User research studies

**⚠️ Critical Rule:** Opportunities must come primarily from actual customer interviews (target: 1 interview per week minimum).

**Interview Questions to Uncover Opportunities:**

- Tell me about the last time you tried to [accomplish goal]
- What were you trying to achieve?
- What made that difficult?
- How did you work around it?
- What would make that easier?

**Opportunity Mapping Process:**

1. **Conduct 6-8 interviews** to start
1. **Identify customer stories** where they struggled or had needs
1. **Extract opportunities** from stories
1. **Group related opportunities** into categories
1. **Structure hierarchically** (parent opportunities → sub-opportunities)

**Opportunity Characteristics:**

**Good Opportunities:**

- ✅ Expressed in customer language
- ✅ Focused on needs, not solutions
- ✅ Clearly connected to outcome
- ✅ Multiple people experience it
- ✅ Specific and concrete

**Bad Opportunities (Actually solutions):**

- ❌ "Need a better UI"
- ❌ "Want AI recommendations"
- ❌ "Need faster performance"

**Opportunity Template:**

```
Opportunity: [Customer need/pain point/desire in their words]

Customer Evidence:
- Interview quote 1: "[Quote from customer]" - [Customer ID/Name]
- Interview quote 2: "[Quote from customer]" - [Customer ID/Name]
- Data point: [Quantitative evidence]

Connection to Outcome: [How addressing this would drive the outcome]

Scope:
- How many customers affected: [Estimate]
- How often they experience this: [Frequency]
- Current satisfaction level: [1-5 scale]

Priority: [High / Medium / Low] based on [Criteria]
```

**Example Opportunity Map:**

```
Outcome: Increase activation rate from 42% to 60%

Opportunities (from 12 user interviews):

1. QUICKLY UNDERSTAND WHAT THE PRODUCT DOES
- See relevant examples for my use case
- Know if this will solve my problem
- Understand value before committing time

2. EXPERIENCE VALUE WITHOUT SETUP FRICTION
- Try core features immediately
- Not blocked by account creation
- Skip unnecessary information collection

3. FEEL CONFIDENT I'M DOING IT RIGHT
- Know if I'm on the right track
- Understand next steps
- Get validation of progress

4. CELEBRATE EARLY WINS
- See tangible results quickly
- Feel sense of achievement
- Build momentum to continue
```

**Opportunity Evaluation Criteria:**

Before selecting which opportunity to focus on, evaluate using:

**Opportunity Sizing:**

- How many customers affected?
- How often do they experience this?

**Market Factors:**

- How does this position us competitively?
- Is this a differentiator?

**Company Factors:**

- Alignment with company strategy?
- Resources available?

**Customer Factors:**

- How important to customers?
- Current satisfaction level?

-----

## 💡 Step 3: Generate Multiple Solutions

**Purpose:** For your target opportunity, generate 3+ different ways to address it.

**Critical Rule:** Resist falling in love with your first idea. Always ask "What else could we build?"

**Solution Generation Principles:**

- Generate 3-5 solutions per opportunity minimum
- Make solutions diverse (not minor variations)
- Keep solution descriptions brief (1-2 sentences)
- Don't commit to building yet—just exploring options

**Solution Template:**

```
Solution Name: [Brief, memorable name]

Description: [1-2 sentence explanation]

Key Assumption: [What needs to be true for this to work?]

Effort Estimate: [Small / Medium / Large]
```

**Example: Solutions for "Experience Value Without Setup Friction"**

**Solution 1: Guest Mode**

- Allow full product exploration without account
- Create account only when saving work
- Assumption: Users will create account after experiencing value

**Solution 2: Social Login + Smart Defaults**

- One-click signup with Google/LinkedIn
- Pre-populate profile from social data
- Assumption: Reducing clicks removes friction

**Solution 3: Progressive Information Collection**

- Collect info just-in-time, not upfront
- Each feature asks for what it needs
- Assumption: Spreading requests feels less overwhelming

**Solution 4: Sample Project Pre-loaded**

- New users start with example project
- Can explore and modify immediately
- Assumption: Hands-on learning > empty state

**Solution 5: Wizard with Skip Options**

- Guided setup with ability to skip any step
- Return to skipped items later
- Assumption: Flexibility reduces abandonment

**Compare & Contrast Questions:**

- Which solution addresses the opportunity most directly?
- Which has the lowest risk/highest confidence?
- Which can we test fastest/cheapest?
- Which aligns with our product strategy?
- What would we lose by not choosing each option?

-----

## 🧪 Step 4: Design Assumption Tests

**Purpose:** Validate solutions before fully building them.

**Key Principle:** Every solution has assumptions. Test the riskiest assumptions first.

**Types of Assumptions:**

**Desirability:** Do customers want this?
**Viability:** Does this support the business?
**Feasibility:** Can we build this?
**Usability:** Can customers use this?
**Ethical:** Should we build this?

**Assumption Mapping:**

For each solution, list key assumptions:

```
Solution: [Solution name]

Assumptions (in order of risk):
1. [Highest risk assumption]
2. [Medium risk assumption]
3. [Lower risk assumption]

Test Plan:
- Assumption: [What we believe]
- Test Method: [How we'll validate]
- Success Criteria: [What would prove us right]
- Timeline: [When we'll complete]
```

**Example: Assumption Tests for "Guest Mode"**

```
Solution: Guest Mode

Assumption 1: Users will explore features without account
- Test: Clickable prototype with analytics
- Success: 70%+ complete a core task in guest mode
- Timeline: 1 week

Assumption 2: Users will create account after experiencing value
- Test: Fake door test "Save your work"
- Success: 40%+ click "Create account" to save
- Timeline: 1 week

Assumption 3: Guest-to-paid conversion is comparable to regular signup
- Test: Build lightweight version, measure conversion
- Success: Conversion rate within 20% of regular flow
- Timeline: 3 weeks
```

**Test Method Options:**

**Cheap & Fast (Days):**

- Interviews with prototype
- Fake door test
- Landing page test
- Survey

**Medium (1-2 weeks):**

- Clickable prototype with users
- Wizard of Oz (manual backend)
- Concierge test
- Limited beta

**Expensive & Slow (2-6 weeks):**

- Full build with A/B test
- Pilot program
- Beta release

**Test Prioritization:**

- Test highest-risk assumptions first
- Test multiple solutions in parallel when possible
- Stop testing if assumptions invalidated
- Don't over-test—build when confidence is sufficient

-----

## 🔄 Continuous Discovery Process

**Weekly Cadence:**

**Monday/Tuesday:**

- Conduct 1-2 user interviews
- Focus on target opportunity area
- Record and note-take

**Wednesday:**

- Synthesize interview insights
- Update Opportunity Solution Tree
- Identify new opportunities or validate existing

**Thursday:**

- Review assumption test results
- Update solution options based on learning
- Plan next tests

**Friday:**

- Team synthesis session
- Decide which solutions to test next
- Update stakeholders on progress

-----

## 🔄 Tree Maintenance

### Monthly Tree Review

**Questions to Ask:**

**About Outcome:**

- [ ] Is this outcome still the right focus?
- [ ] Have we made progress? (Show data)
- [ ] Do we need to adjust target or timeframe?

**About Opportunities:**

- [ ] Are these still the right opportunities?
- [ ] Have we discovered new opportunities?
- [ ] Should we reprioritize based on learning?
- [ ] Are any opportunities validated/invalidated?

**About Solutions:**

- [ ] Do we have 3+ solutions per opportunity?
- [ ] Are solutions diverse enough?
- [ ] Have we tested enough assumptions?
- [ ] What should we build next?

**Tree Health Indicators:**

✅ **Healthy Tree:**

- Weekly customer interviews happening
- Multiple opportunities identified (5-10)
- 3+ solutions per target opportunity
- Active assumption testing
- Clear evidence trail
- Regular updates based on learning

⚠️ **Unhealthy Tree:**

- No recent customer interviews
- Single opportunity or solution fixation
- No experiments running
- Tree hasn't been updated in weeks
- Missing customer evidence
- Building without validating

-----

## 🎯 Combining Double Diamond + OST

### Use Together for Maximum Impact

**Opportunity Solution Tree = Continuous Practice**

- Ongoing customer discovery
- Always exploring opportunity space
- Multiple solutions always ready

**Double Diamond = Focused Sprint**

- When you need to converge and ship
- 6-12 week intensive exploration
- Deep dive on specific opportunity

### Integration Model

```
OST (Continuous)
────────────────────────────────────────────────►
│ │
▼ ▼
DD Sprint 1 DD Sprint 2
(8 weeks) (8 weeks)

│←Discover→│
│←Define→│
│←Develop→│
│←Deliver→│
```

**How They Work Together:**

**OST Feeds Double Diamond:**

- Use OST opportunities as DD starting point
- OST interviews provide research foundation
- OST solutions become DD ideation inputs

**Double Diamond Feeds OST:**

- DD learnings update OST
- Shipped solutions inform new opportunities
- DD experiments become OST evidence

**Example Workflow:**

**Weeks 1-12: Continuous OST**

- Weekly interviews
- Building opportunity map
- Generating multiple solutions
- Running small tests

**Weeks 13-20: Double Diamond Sprint**

- **Discover (2 weeks):** Deep dive on top opportunity from OST
- **Define (1 week):** Synthesize into clear problem
- **Develop (2 weeks):** Generate and prototype solutions
- **Deliver (3 weeks):** Test, build, ship

**Weeks 21+: Back to OST**

- Update tree with DD learnings
- Measure impact of shipped solution
- Explore next opportunity

-----

## References

- Main Framework: `../1-problem-solution-space-framework.md`
- Opportunity Solution Tree Template: `2-opportunity-solution-tree-template.md`
- Double Diamond Guide: `../1-Double-Diamond/1-double-diamond-guide.md`
- Supporting Frameworks: `../3-Supporting-Frameworks/1-supporting-frameworks.md`
