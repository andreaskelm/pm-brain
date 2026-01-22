# Double Diamond Process Guide

## Disclaimer

The Double Diamond is iterative, not linear. You may cycle back to earlier phases as you learn. The goal is progress, not perfection.

**Current Phase:** [Discover / Define / Develop / Deliver]
**Exploration Started:** [Date]
**Phase Target Completion:** [Date]
**Team:** [Product Manager, Designer, Engineer(s), Others]
**Desired Outcome:** [What we're trying to achieve]

-----

## 💎 Diamond 1: Problem Space

### Phase 1: DISCOVER (Diverge) - Explore the Problem

**Objective:** Understand the problem space thoroughly without jumping to solutions.

**Mindset:** Be curious, not certain. Explore widely. Question assumptions.

**Duration:** 2-4 weeks (depending on scope)

**Key Activities:**

|Activity |Purpose |Methods |Output |
|--------------------------|-----------------------------------|--------------------------------------------------|-------------------------------|
|**User Research** |Understand customer needs & context|Interviews, shadowing, diary studies |User insights, pain points |
|**Data Analysis** |Quantify the problem |Analytics review, cohort analysis, funnel analysis|Usage patterns, drop-off points|
|**Competitive Analysis** |Understand market landscape |Competitor review, feature comparison |Market gaps, opportunities |
|**Stakeholder Interviews**|Gather internal perspectives |Leadership, sales, support interviews |Business constraints, goals |
|**Journey Mapping** |Visualize current experience |Customer journey maps, service blueprints |Pain point identification |

**Research Methods Toolkit:**

**Qualitative Methods:**

- **User Interviews:** 1-on-1 conversations (30-60 min)
- Tip: Ask about last time they experienced the problem, not hypotheticals
- **Contextual Inquiry:** Observe users in their environment
- Tip: Watch what they do, not just what they say
- **Diary Studies:** Users log experiences over time
- Tip: Good for understanding patterns and context
- **Jobs to Be Done Interviews:** Understand what users are trying to accomplish
- Tip: Focus on the "job," not the product

**Quantitative Methods:**

- **Analytics Review:** Understand current behavior patterns
- **Surveys:** Gather data from larger sample
- **A/B Test Results:** Learn from past experiments
- **Cohort Analysis:** How behavior differs by segment

**Outputs from Discover:**

- [ ] 8-15 user interviews completed
- [ ] Key insights synthesized (3-5 major themes)
- [ ] Journey map or service blueprint created
- [ ] Data analysis completed (usage patterns, pain points)
- [ ] Initial opportunity areas identified (5-10)

**Example: Discover Phase Output**

**Project:** Improving new user activation

**Key Insights from 12 user interviews:**

1. New users unclear what to do first (8/12 mentioned)
1. Core value not experienced in first session (10/12)
1. Setup feels overwhelming (7/12)
1. Users don't understand why they need account (6/12)
1. Success isn't celebrated/visible (9/12)

**Quantitative validation:**

- 42% activation rate (industry benchmark: 60%)
- 65% drop-off during setup flow
- Users who complete setup are 3.2x more likely to return

-----

### Phase 2: DEFINE (Converge) - Frame the Problem

**Objective:** Synthesize insights into a clear, actionable problem statement.

**Mindset:** Be decisive, not exhaustive. Converge on focus area.

**Duration:** 1-2 weeks

**Key Activities:**

|Activity |Purpose |Methods |Output |
|-------------------------|-------------------------------|-----------------------------------|------------------------|
|**Insight Synthesis** |Find patterns in research |Affinity mapping, thematic analysis|Key themes, patterns |
|**Problem Framing** |Define the core issue |Five Whys, root cause analysis |Problem statement |
|**Opportunity Selection**|Choose what to focus on |Prioritization matrix, voting |Target opportunity |
|**Success Criteria** |Define what "solved" looks like|Metric definition, target setting |Success metrics |
|**HMW Questions** |Reframe as opportunities |How Might We workshop |Solution-neutral prompts|

**Synthesis Techniques:**

**Affinity Mapping:**

1. Write each insight on sticky note
1. Group related insights together
1. Label each group (themes)
1. Look for larger patterns across groups

**Five Whys:**

```
Problem: Low activation rate
Why? Users don't complete setup
Why? Setup feels overwhelming
Why? Too many steps required upfront
Why? We ask for information we don't need immediately
Why? We haven't prioritized which data is essential
Root cause: Poor information architecture in onboarding
```

**Root Cause Analysis (Fishbone):**
Explore six categories: People, Process, Tools, Environment, Methods, Materials

**Problem Statement Template:**

```
[User type] needs a way to [need/goal]
because [insight]
which leads to [impact]

Currently, [current state/pain point]
resulting in [negative outcome]

We will know we've succeeded when [measurable outcome]
```

**Example:**

```
New users need a way to experience core product value within their first session
because they don't understand what the product can do for them
which leads to abandonment before value realization.

Currently, 42% of signups never complete setup and 65% drop off during the process
resulting in lost customers and missed revenue.

We will know we've succeeded when activation rate increases from 42% to 60%
and time-to-first-value decreases from 8 minutes to under 5 minutes.
```

**How Might We Questions:**

Generate 10-15 HMW questions from your problem statement:

- ✅ HMW help new users discover core value in under 5 minutes?
- ✅ HMW make setup feel effortless rather than overwhelming?
- ✅ HMW celebrate early wins to build momentum?
- ✅ HMW reduce required information during signup?
- ✅ HMW show value before asking for commitment?

**Outputs from Define:**

- [ ] Clear problem statement documented
- [ ] Success metrics defined
- [ ] 10-15 How Might We questions generated
- [ ] Target opportunity selected
- [ ] Constraints and requirements documented

-----

## 💎 Diamond 2: Solution Space

### Phase 3: DEVELOP (Diverge) - Generate Solutions

**Objective:** Generate multiple diverse solutions for the defined problem.

**Mindset:** Be generative, not evaluative. Defer judgment. Think "What else?"

**Duration:** 2-3 weeks

**Key Activities:**

|Activity |Purpose |Methods |Output |
|-----------------------|-----------------------|-------------------------------------|----------------------|
|**Ideation** |Generate many solutions|Brainstorming, Crazy 8s, SCAMPER |20-50 solution ideas |
|**Solution Sketching** |Visualize concepts |Storyboards, wireframes, concept maps|Low-fi prototypes |
|**Feasibility Check** |Technical reality check|Engineering spikes, tech research |Feasibility assessment|
|**Concept Development**|Refine top ideas |Detailed wireframes, user flows |3-5 developed concepts|
|**Assumption Mapping** |Identify risks |Assumption listing, risk assessment |Test plan |

**Ideation Techniques:**

**Crazy 8s:**

1. Take one HMW question
1. Fold paper into 8 sections
1. Set timer for 8 minutes
1. Sketch one idea per section (1 min each)
1. Forces rapid, diverse thinking

**SCAMPER:**

- **S**ubstitute: What can we replace?
- **C**ombine: What can we merge?
- **A**dapt: What can we adjust?
- **M**odify: What can we change?
- **P**ut to other use: New way to use existing?
- **E**liminate: What can we remove?
- **R**everse: What if we did opposite?

**Round-Robin Brainstorming:**

1. Each person writes 3 ideas silently (5 min)
1. Pass papers clockwise
1. Build on previous ideas (5 min)
1. Repeat 3-4 times
1. Generates diverse, built-upon ideas

**Solution Generation Rules:**

During ideation:

- ✅ Quantity over quality
- ✅ Build on others' ideas ("Yes, and…")
- ✅ Encourage wild ideas
- ✅ Defer judgment
- ❌ No critiquing
- ❌ No "that won't work"
- ❌ No solution fixation

**From Ideas to Concepts:**

1. Generate 20-50 raw ideas
1. Cluster similar ideas (affinity grouping)
1. Identify 8-10 distinct concepts
1. Develop top 3-5 concepts with details
1. Create low-fidelity prototypes

**Concept Development Template:**

For each of top 3-5 solutions:

```
Concept Name: [Brief, memorable name]

Description: [2-3 sentences explaining the solution]

Key Features:
- Feature 1
- Feature 2
- Feature 3

How It Addresses the Problem:
[Explain connection to problem statement]

Key Assumptions:
- Assumption 1
- Assumption 2
- Assumption 3

Feasibility Assessment:
- Technical: [Easy / Medium / Hard]
- Design: [Easy / Medium / Hard]
- Effort: [Small / Medium / Large]

Risks:
- Risk 1
- Risk 2
```

**Example: Three Concepts for Activation Problem**

**Concept A: Progressive Setup**

- Show value first, collect info later
- Break setup into micro-steps
- Allow exploration before account creation

**Concept B: Guided First Experience**

- Interactive tutorial with sample data
- Celebrate each completed action
- Personalize based on use case

**Concept C: Social Proof Onboarding**

- Show what others accomplished
- Pre-populated templates to start
- Quick wins in first 2 minutes

**Outputs from Develop:**

- [ ] 20+ solution ideas generated
- [ ] 3-5 detailed solution concepts
- [ ] Low-fidelity prototypes or wireframes
- [ ] Assumptions documented for each concept
- [ ] Feasibility assessments completed

-----

### Phase 4: DELIVER (Converge) - Test & Implement

**Objective:** Validate solutions with users and implement the best option.

**Mindset:** Be evidence-driven, not opinion-driven. Test, learn, iterate.

**Duration:** 2-6 weeks (depending on build complexity)

**Key Activities:**

|Activity |Purpose |Methods |Output |
|----------------------|-----------------------|------------------------------|---------------------------------|
|**Prototype Testing** |Validate with users |Usability tests, concept tests|User feedback, insights |
|**Assumption Testing**|De-risk before building|Smoke tests, concierge tests |Validated/invalidated assumptions|
|**Solution Selection**|Choose best option |Scoring, evidence review |Final solution |
|**Build MVP** |Create minimal version |Agile development |Working MVP |
|**Measure & Learn** |Validate impact |A/B tests, analytics |Impact data |

**Testing Methods:**

**Low-Fidelity Testing:**

- **Paper Prototypes:** Hand-drawn interfaces
- Fast, cheap, great for early feedback
- **Clickable Wireframes:** Basic interactive flows
- Tools: Figma, Balsamiq, Sketch
- **Wizard of Oz:** Human simulates system
- Great for AI/automation features

**Medium-Fidelity Testing:**

- **Interactive Prototypes:** Looks real, limited functionality
- Tools: Figma, Adobe XD, InVision
- **Concierge Testing:** Manually deliver the service
- Validate demand before automating

**High-Fidelity Testing:**

- **Fake Door Test:** Button/page for non-existent feature
- Measures interest before building
- **Limited Beta:** Small user group gets real feature
- Validates in production environment
- **A/B Test:** Compare new vs. old
- Gold standard for validation

**Usability Testing Protocol:**

**Preparation:**

1. Define what you want to learn
1. Create testing script with tasks
1. Recruit 5-8 users per concept
1. Prepare prototype

**During Test (30-45 min):**

1. Intro & context (5 min)
1. Task completion (20-30 min)
- Think aloud protocol
- Observe, don't help
1. Retrospective questions (5-10 min)
- What worked? What confused?
- Would you use this?

**After Test:**

1. Synthesize findings across users
1. Identify patterns (3+ users = pattern)
1. Rate severity: Critical / Major / Minor
1. Iterate or select solution

**Solution Selection Framework:**

Score each concept on:

|Criterion |Weight|Concept A|Concept B|Concept C|
|----------------------------------------------------------|------|---------|---------|---------|
|**User Desirability** (Does solving the problem matter?) |30% |Score |Score |Score |
|**Solution Usability** (Can users use this effectively?) |25% |Score |Score |Score |
|**Technical Feasibility** (Can we build this?) |20% |Score |Score |Score |
|**Business Viability** (Does this support business goals?)|15% |Score |Score |Score |
|**Time to Value** (How fast can we ship and learn?) |10% |Score |Score |Score |
|**Total Weighted Score** |100% |Total |Total |Total |

Use 1-5 scale for each criterion.

**Build-Measure-Learn Loop:**

1. **Build:** Create minimum viable version
- Include instrumentation
- Ship to small % of users
1. **Measure:** Track key metrics
- Success metrics defined in Define phase
- User behavior data
- Qualitative feedback
1. **Learn:** Analyze results
- Did it move the metric?
- What surprised us?
- What should we change?

**Outputs from Deliver:**

- [ ] 5-8 usability tests completed per concept
- [ ] Key assumptions validated or invalidated
- [ ] Solution selected with evidence
- [ ] MVP built and shipped
- [ ] Impact measured against success criteria
- [ ] Learnings documented for future

-----

## References

- Main Framework: `../1-problem-solution-space-framework.md`
- Double Diamond Template: `2-double-diamond-template.md`
- Supporting Frameworks: `../3-Supporting-Frameworks/1-supporting-frameworks.md`
- Opportunity Solution Tree: `../2-Opportunity-Solution-Tree/1-opportunity-solution-tree-guide.md`
