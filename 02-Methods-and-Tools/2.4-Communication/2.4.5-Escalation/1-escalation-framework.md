# Escalation Framework

## Overview

This framework helps PMs navigate when to escalate issues in large organizations. Escalation is a critical skill that junior PMs often struggle with—knowing when to handle something yourself vs. involve leadership.

-----

## When to Escalate Guide

### The Escalation Decision Framework

**Core Principle:** Escalate when you lack authority, information, or resources to resolve—not when it’s just hard or uncomfortable.

-----

### STEP 1: Before Escalating, Try These First

**Self-Checklist:**

```
Have I...
☐ Fully understood the problem?
☐ Talked to all relevant people?
☐ Explored multiple solutions?
☐ Attempted to resolve myself?
☐ Considered the trade-offs?
☐ Documented the situation?

If NO to most → Work on these first
If YES to most → Escalation may be appropriate
```

-----

### STEP 2: The Escalation Decision Tree

```
Issue Identified
│
▼
┌─────────────────────────┐
│ Do I have authority │
│ to make this decision? │
└─────────┬───────────────┘
│
┌─────────────┴─────────────┐
│ │
YES NO
│ │
▼ ▼
┌─────────────┐ ┌──────────────┐
│ Do I have │ │ ESCALATE │
│ information │ │ (Decision │
│ to decide? │ │ Authority) │
└──────┬──────┘ └──────────────┘
│
┌─────┴─────┐
YES NO
│ │
▼ ▼
┌────────┐ ┌──────────┐
│ Do I │ │ ESCALATE │
│ have │ │(Need Info)│
│resources│ └──────────┘
│ to │
│execute?│
└───┬────┘
│
┌───┴───┐
YES NO
│ │
▼ ▼
HANDLE ESCALATE
MYSELF (Resources)
```

-----

### STEP 3: Escalation Scenarios & Responses

#### Scenario 1: Cross-Team Conflict

**ESCALATE when:**

- Teams fundamentally disagree on direction
- Both teams have valid but incompatible positions
- Conflict affects roadmap or commitments
- You’ve tried to mediate unsuccessfully

**DON’T escalate when:**

- Minor disagreement on implementation
- Can be resolved with more conversation
- Just need clearer requirements

**How to escalate:**

```markdown
Subject: [ESCALATION NEEDED] Cross-Team Alignment Issue - [Topic]

Hi [Manager],

I need your help resolving a cross-team disagreement that's blocking progress.

**SITUATION:**
[Product Team] and [Engineering Team] disagree on [specific issue].

**POSITIONS:**
- Product perspective: [Position and rationale]
- Engineering perspective: [Position and rationale]

**WHAT I'VE TRIED:**
- [Action 1]: [Outcome]
- [Action 2]: [Outcome]
- [Action 3]: [Outcome]

**IMPACT OF NOT RESOLVING:**
- Timeline: [Impact]
- Scope: [Impact]
- Team morale: [Impact]

**MY RECOMMENDATION:**
[What you think should happen and why]

**WHAT I NEED:**
- Decision between [Option A] and [Option B]
- OR facilitation of conversation with [stakeholders]
- By when: [Date] (because [reason])

Happy to provide more context.
```

-----

#### Scenario 2: Technical Feasibility Questions

**ESCALATE when:**

- Engineering says something is impossible but business critically needs it
- Massive technical effort required (6+ months)
- Architectural decisions with long-term implications
- Involves platform or infrastructure teams

**DON’T escalate when:**

- Normal engineering complexity
- Just need more conversation with tech lead
- Can be scoped down or phased

**How to escalate:**

```markdown
Subject: [INPUT NEEDED] Technical Feasibility Assessment - [Feature]

Hi [Engineering Manager / CTO],

I need technical guidance on a business-critical feature that's raising feasibility concerns.

**BUSINESS NEED:**
[Customer problem, revenue impact, strategic importance]

**PROPOSED SOLUTION:**
[What we want to build]

**TECHNICAL CONCERN:**
Engineering team indicates this would require:
- [Technical constraint 1]
- [Technical constraint 2]
- Estimated effort: [X months]

**QUESTION:**
- Is this technically feasible within [timeframe]?
- If not as specified, what alternative approaches exist?
- What would need to change to make this possible?

**TRADE-OFF SPACE:**
We're open to:
- Phased approach
- Reduced scope
- Alternative technical approach
- Extended timeline (if justified)

**NEXT STEP:**
Could we schedule 30 minutes to discuss options?
Target decision: [Date]
```

-----

#### Scenario 3: Resource/Budget Needs

**ESCALATE when:**

- Need additional headcount
- Need budget for vendors/tools
- Current resources insufficient for commitments
- Competing priorities need arbitration

**DON’T escalate when:**

- Can reprioritize existing work
- Can use existing resources differently
- Haven’t fully utilized current resources

**How to escalate:**

```markdown
Subject: [RESOURCE REQUEST] Additional [Headcount/Budget] for [Initiative]

Hi [Manager],

I need [resource] to deliver [commitment].

**CURRENT SITUATION:**
- Commitment: [What we committed to]
- Current resources: [What we have]
- Gap: [What we're short]

**IMPACT OF GAP:**
Without additional resources:
- [Commitment] delays by [timeframe]
- [Stakeholder] expectations not met
- [Business impact]

**REQUEST:**
[Specific resource needed]:
- [Headcount]: [Role, when needed, duration]
- [Budget]: [Amount, what for, ROI]

**ALTERNATIVES CONSIDERED:**
- Reduce scope: [Would require cutting [features]]
- Extend timeline: [Would mean [date] instead of [date]]
- Deprioritize other work: [Would affect [initiative]]

**BUSINESS CASE:**
- Customer impact: [Quantify]
- Revenue impact: [Quantify]
- Strategic importance: [Explain]

**DECISION NEEDED:**
- Approve resource request
- OR accept [alternative]
By: [Date]
```

-----

#### Scenario 4: Scope/Priority Changes

**ESCALATE when:**

- Executive requests conflict with roadmap
- Customer commitment conflicts with strategy
- Major scope change mid-development
- Conflicting priorities from multiple executives

**DON’T escalate when:**

- Minor scope adjustments
- Can absorb within current plan
- Trade-offs are clear and within your authority

**How to escalate:**

```markdown
Subject: [DECISION NEEDED] Priority Conflict - [Initiative A] vs [Initiative B]

Hi [Manager],

I need help prioritizing conflicting requests from [Stakeholder A] and [Stakeholder B].

**REQUEST A (from [Stakeholder A]):**
- What: [Description]
- Why: [Business justification]
- When: [Deadline]
- Effort: [Estimate]

**REQUEST B (from [Stakeholder B]):**
- What: [Description]
- Why: [Business justification]
- When: [Deadline]
- Effort: [Estimate]

**THE CONFLICT:**
Both require [same resource / same timeframe / mutually exclusive approaches]

**IMPACT OF CHOOSING A:**
- Delivers: [Benefit]
- Delays: [What B stakeholder loses]
- Risk: [Potential downside]

**IMPACT OF CHOOSING B:**
- Delivers: [Benefit]
- Delays: [What A stakeholder loses]
- Risk: [Potential downside]

**MY RECOMMENDATION:**
[Your suggested priority and reasoning]

**WHAT I NEED:**
- Priority decision between A and B
- OR revised timeline/scope for one
- OR additional resources to do both

I can communicate the decision to both stakeholders once made.
```

-----

### STEP 4: How to Communicate Escalations

**Framework: Situation-Impact-Options-Recommendation (SIOR)**

```markdown
## Escalation: [Clear, specific title]

**SITUATION** (What's happening)
[2-3 sentences, facts only]

**IMPACT** (Why it matters)
- Customer impact: [Specific]
- Business impact: [Specific]
- Timeline impact: [Specific]

**OPTIONS** (Paths forward)
1. [Option A]: [Pros/Cons]
2. [Option B]: [Pros/Cons]
3. [Option C]: [Pros/Cons]

**RECOMMENDATION** (What you think should happen)
[Your suggested path and reasoning]

**REQUEST** (What you need)
☐ [Specific decision or resource]
☐ By when: [Date and why]
```

-----

### STEP 5: After Escalating

**Once escalated:**

```
☐ Follow up if no response within 24-48 hours
☐ Document the decision made
☐ Communicate outcome to affected parties
☐ Execute on the decision (don't relitigate)
☐ Thank the person who helped resolve
```

-----

## References

- Saying No: `../2.4.6-Saying-No/README.md`
- Stakeholder Management: `../2.4.7-Stakeholder-Management/README.md`
- Crisis Management: `../2.4.4-Crisis-Management/README.md`
- Self-Reflection: `../../2.0-Foundations/2.0.3-Self-Reflection/README.md`