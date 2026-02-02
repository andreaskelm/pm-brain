# OKR Framework

## Overview

This framework helps you create and manage Objectives and Key Results (OKRs) that align teams around measurable outcomes. OKRs operationalize strategy into actionable, measurable goals that connect daily work to business results.

## Step 0: Braindump & Product Sense (Do this first!)

**Use prompts from:** [2-product-sense-prompts.md](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → [Before a Product Strategy Session](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#before-a-product-strategy-session).

**Quick start:** What outcomes are you trying to achieve? What feels like the right outcome? What assumptions? What biases might affect your OKRs? If you had to pick ONE outcome that matters most, what would it be? **See prompts file for full list.**

**When to use OKRs:**
- Operationalizing strategic priorities into measurable outcomes
- Aligning teams around shared objectives
- Tracking progress on key initiatives
- Connecting product work to business metrics

**When OKRs might not be needed:**
- Very small teams (<5 people) where alignment is already strong
- Exploratory research phases before clear objectives emerge
- One-off projects with clear, single success criteria

---

## Core Philosophy

### OKRs are NOT Project Plans or Task Lists

OKRs should:

- **Enable outcome focus over output tracking** - Measure what matters, not just activity
- **Drive alignment over individual goals** - Connect team work to shared objectives
- **Encourage ambition over safety** - Stretch goals that inspire, not just achievable targets
- **Support learning over perfection** - It's okay to miss ambitious goals if you learn

### Core Principles

**Outcome over output:**
- Tie to business results and job outcomes, not just deliverables
- Focus on customer value and business impact
- Avoid activity-based metrics (e.g., "Launch feature" → "Increase engagement by 20%")

**Evidence before investment:**
- Use RAT-style Key Results with thresholds
- Test assumptions before committing resources
- Use leading indicators to predict lagging outcomes

**Small docs, fast loops:**
- Keep OKR documents to 1-2 pages
- Weekly confidence checks (not just quarterly reviews)
- Iterate based on learnings

**Traceability:**
- Link OKRs to JTBD → Opportunity → RAT → PRD → Decision Log
- Connect daily work to Key Results
- Show how initiatives contribute to outcomes

### The OKR Philosophy

OKRs operationalize strategy by translating high-level direction into measurable outcomes. They create a shared language for what success looks like and enable teams to align around common objectives while maintaining autonomy in how they achieve them.

The framework balances ambition with realism—OKRs should be stretch goals that inspire teams, but also grounded in evidence and achievable with focused effort. Missing an ambitious goal is acceptable if you learn and adjust; hitting an easy goal teaches you nothing.

---

## Framework Structure

### 1. Objectives

**What to capture:**
- 1-2 Objectives per team per cycle
- Qualitative, inspirational statements
- Strategic focus areas
- Clear "what" you're trying to achieve

**Why it matters:** Objectives provide direction and alignment. They answer "where are we going?" and create shared purpose.

**Example:**
```
Objective: "Enable teams to discover and adopt advanced features"
```

**Common mistakes:**
- ❌ Too many Objectives (3+) - dilutes focus
- ❌ Activity-based ("Launch new dashboard") - should be outcome-focused
- ❌ Too vague ("Improve product") - needs specificity

### 2. Key Results

**What to capture:**
- 2-4 Key Results per Objective
- Specific, measurable, time-bound outcomes
- Mix of leading and lagging indicators
- Pass/fail thresholds defined

**Why it matters:** Key Results make Objectives measurable. They answer "how will we know we succeeded?" and enable progress tracking.

**Example:**
```
Key Result: "Increase weekly active users of advanced features from 5,000 to 8,000 by end of Q2"
```

**Common mistakes:**
- ❌ Milestone/project KRs ("Complete Phase 1") - should be outcomes
- ❌ No baselines or targets ("Improve conversion") - needs specific numbers
- ❌ Too many KRs (5+) - dilutes focus

### 3. KR IDs and Linking

**What to capture:**
- Stable KR IDs (e.g., `O1-KR1`, `O1-KR2`)
- Link initiatives and PRDs to KR IDs
- Track contributions to each KR
- Document evidence and progress

**Why it matters:** KR IDs enable traceability. They connect daily work to outcomes and show how initiatives contribute to Key Results.

**Example:**
```
Initiative: "Redesign feature discovery flow"
Contributes to: O1-KR1, O1-KR2
Evidence: User research showing discovery pain points
```

### 4. Confidence Scoring

**What to capture:**
- Weekly confidence levels: 0 (off-track), 1 (at-risk), 2 (on-track)
- Evidence for confidence level
- Risks and blockers
- Next actions

**Why it matters:** Confidence scoring enables early course correction. It answers "are we on track?" and helps teams adjust before it's too late.

**Example:**
```
KR1 Confidence: 1 (at-risk)
Evidence: Adoption rate 30% below target, user feedback indicates confusion
Risks: Onboarding flow needs improvement
Next: Test simplified onboarding flow next week
```

## How to Use This Framework

### Step 1: Prepare Inputs (Week 1, Async)

**Purpose:** Gather context and inputs needed for OKR setting

**Activities:**
- Review company/BU priorities and constraints
- Review team mission and core metrics (SLAs, latency, cost-to-serve)
- Review opportunity backlog tied to JTBD and ODI outcomes
- Review last cycle's decision log and post-mortems
- Compile candidate problem spaces and metrics

**Deliverables:**
- Inputs document with priorities, constraints, and opportunities
- Candidate Objectives and Key Results list

**Time estimate:** 4-6 hours (async, distributed across team)

### Step 2: Framing Workshop (Week 1-2, 2-3 hours)

**Purpose:** Align on "why now" and select Objectives

**Activities:**
- Discuss "why now" - what's changed that requires new OKRs?
- Review candidate Objectives from prep
- Select 1-2 Objectives per team
- Brainstorm potential Key Results for each Objective
- Align on strategic focus

**Deliverables:**
- 1-2 Objectives selected
- Initial list of candidate Key Results

**Time estimate:** 2-3 hours (workshop)

**Common challenges:**
- **Too many Objectives:** Force ranking to top 1-2
- **Vague Objectives:** Push for specificity and clarity
- **Solution:** Use "so that" statements to clarify value

### Step 3: Define Key Results (Week 2, 2-3 hours)

**Purpose:** Convert Objectives into measurable Key Results

**Activities:**
- Convert top assumptions into RAT-style KRs with thresholds
- Define baselines and targets for each KR
- Specify measurement instrumentation (events, IDs, dashboards)
- Mix leading and lagging indicators
- Ensure 2-4 KRs per Objective

**Deliverables:**
- Complete Key Results with baselines, targets, and thresholds
- Measurement plan for each KR

**Time estimate:** 2-3 hours

**Common challenges:**
- **Milestone KRs:** Push to convert to outcome-based
- **Missing baselines:** Research historical data or set initial baseline
- **Solution:** Use outcome proxies when direct metrics aren't available

### Step 4: Stakeholder Review (Week 2, 1-2 hours)

**Purpose:** Validate OKRs with stakeholders

**Activities:**
- Share draft OKRs with stakeholders (leadership, adjacent teams)
- Validate metrics and measurement approach
- Review guardrails and dependencies
- Get alignment on priorities

**Deliverables:**
- Validated OKRs
- Stakeholder alignment confirmed

**Time estimate:** 1-2 hours (meetings)

### Step 5: Publish and Link (Week 2, 1 hour)

**Purpose:** Make OKRs operational

**Activities:**
- Assign stable KR IDs (O1-KR1, O1-KR2, etc.)
- Publish to company OKR system
- Assign owners for each KR
- Link dashboards and tracking
- Connect initiatives and PRDs to KR IDs

**Deliverables:**
- Published OKRs with KR IDs
- Dashboards linked
- Work connected to KRs

**Time estimate:** 1 hour

## When to Use OKRs

### OKRs Work Best For:

- **Operationalizing strategy** - When you need to translate strategic priorities into measurable outcomes
  - **Example:** Company strategy says "expand enterprise market" → OKRs define specific enterprise metrics to move
- **Team alignment** - When multiple teams need to align around shared objectives
  - **Example:** Product, Engineering, and Design teams align on user engagement goals
- **Outcome tracking** - When you need to measure progress on key initiatives
  - **Example:** Tracking whether new features actually drive the intended business outcomes
- **Connecting work to metrics** - When daily work needs clear connection to business results
  - **Example:** Linking feature development to user engagement and revenue metrics

### OKRs May Not Be Ideal For:

- **Very small teams (<5 people)** - Overhead may not be worth it if alignment is already strong
  - **Alternative:** Simple goal-setting or task tracking
- **Exploratory research phases** - When objectives aren't clear yet
  - **Alternative:** Discovery frameworks, opportunity assessment
- **One-off projects** - When success criteria are clear and single
  - **Alternative:** Project plan with success criteria
- **Tactical execution** - When work is clearly defined and just needs to be done
  - **Alternative:** Task lists, sprint planning

### Decision Criteria

Use OKRs when:
- ✅ You have strategic priorities to operationalize
- ✅ You need team alignment around outcomes
- ✅ You want to connect work to business metrics
- ✅ You have capacity for weekly tracking
- ✅ You're ready to commit to quarterly cycles

Consider alternatives when:
- ❌ Team is very small and already aligned
- ❌ Still in discovery/exploration phase
- ❌ Work is purely tactical execution
- ❌ No capacity for regular tracking

## Common Pitfalls and Solutions

### Pitfall 1: Activity-Based Key Results

**What it looks like:**
- KRs like "Launch new feature" or "Complete Phase 1"
- Focus on deliverables, not outcomes
- No connection to business metrics
- Can't measure impact

**Why it's a problem:**
- Doesn't measure value delivered
- Teams optimize for completion, not impact
- No learning about what works
- Can't connect work to business results

**How to avoid it:**
- Always ask "so that" - what outcome does this enable?
- Convert activities to outcomes (e.g., "Launch feature" → "Increase engagement by 20%")
- Use outcome proxies when direct metrics aren't available
- Focus on customer value and business impact

**Example:**
```
Before: "Launch new dashboard feature"
After: "Increase weekly active users of analytics features from 2,000 to 5,000"
Result: Measures adoption and value, not just completion
```

### Pitfall 2: Too Many Objectives or Key Results

**What it looks like:**
- 3+ Objectives per team
- 5+ Key Results per Objective
- Everything feels like a priority
- Team can't focus

**Why it's a problem:**
- Dilutes focus and effort
- Nothing gets done well
- Team loses clarity on priorities
- OKRs become checklist, not strategic guide

**How to avoid it:**
- Limit to 1-2 Objectives per team
- Limit to 2-4 Key Results per Objective
- Force ranking: if everything is priority, nothing is
- Use "not now" list for lower priorities

**Example:**
```
Before: 3 Objectives, 12 total Key Results
After: 1 Objective, 3 Key Results
Result: Clear focus, team knows what matters most
```

### Pitfall 3: Missing Baselines or Targets

**What it looks like:**
- KRs like "Improve conversion" (no baseline or target)
- "Increase engagement" (how much? from what?)
- No way to measure progress
- Can't tell if you're succeeding

**Why it's a problem:**
- Can't track progress
- No clear definition of success
- Team doesn't know if they're on track
- Can't grade at end of cycle

**How to avoid it:**
- Always include baseline (current state)
- Always include target (desired state)
- Use specific numbers, not vague improvements
- Research historical data to set baselines

**Example:**
```
Before: "Improve user engagement"
After: "Increase weekly active users from 10,000 to 15,000"
Result: Clear baseline, clear target, measurable progress
```

### Pitfall 4: Set-and-Forget OKRs

**What it looks like:**
- OKRs set at start of quarter, never reviewed
- No weekly confidence checks
- No mid-cycle adjustments
- Learnings don't inform next cycle

**Why it's a problem:**
- OKRs become irrelevant as context changes
- Team works on outdated priorities
- Miss opportunities to course-correct
- Don't learn from what worked/didn't work

**How to avoid it:**
- Weekly confidence checks (0/1/2)
- Mid-cycle assessment and adjustment
- Document learnings in decision log
- Use learnings to inform next cycle

**Example:**
```
Week 1: KR1 confidence = 2 (on-track)
Week 4: KR1 confidence = 1 (at-risk) - adoption slower than expected
Week 6: Adjusted strategy based on learnings, KR1 confidence = 2
Result: Course-corrected before it was too late
```

### Pitfall 5: Vanity Metrics

**What it looks like:**
- KRs that look good but don't drive value
- Metrics that are easy to move but don't matter
- Focus on activity, not outcomes
- No connection to business results

**Why it's a problem:**
- Teams optimize for wrong things
- Looks like progress but no real impact
- Wastes resources on low-value work
- Doesn't drive business outcomes

**How to avoid it:**
- Connect every KR to business value
- Ask "why does this matter?" for each KR
- Use North Star or input metrics when possible
- Avoid metrics that are easy to game

**Example:**
```
Before: "Increase page views by 50%" (vanity - easy to game, doesn't drive value)
After: "Increase weekly active users from 10,000 to 15,000" (outcome - drives value)
Result: Team focuses on meaningful engagement, not just traffic
```

## Quick Quality Checks (Use During Creation)

**Purpose:** Catch common issues early while creating OKRs. The agent will automatically scan for these red flags during creation conversations.

### Top Red Flags to Watch For

❌ **Objectives are project/feature names** - "Build X", "Implement Y", "Deploy Z"  
→ **Fix:** Reframe as business outcomes. Ask: "What outcome does this enable?"

❌ **KRs are milestones** - "Complete Phase 1", "Launch feature", "Finish integration"  
→ **Fix:** Convert to measurable outcomes. Ask: "How will we measure success?"

❌ **No baselines or targets** - "Improve conversion", "Increase quality"  
→ **Fix:** Add specific numbers. Ask: "What's the current state? What's the target?"

❌ **Missing time bounds** - "Increase revenue", "Reduce costs"  
→ **Fix:** Add timeframe. Ask: "By when do we want to achieve this?"

❌ **No measurement plan** - No dashboards, events, or tracking mentioned  
→ **Fix:** Define instrumentation. Ask: "How will we measure this? What events/dashboards?"

❌ **Too many Objectives** - More than 2 per team  
→ **Fix:** Force rank to top 1-2. Ask: "If you could only focus on ONE outcome, what would it be?"

❌ **Too many KRs** - More than 5 per Objective  
→ **Fix:** Limit to 2-4. Ask: "Which KRs matter most for this Objective?"

❌ **Activity-focused KRs** - "Implement X", "Deploy Y"  
→ **Fix:** Focus on outcomes. Ask: "What outcome does this activity enable?"

### Quick Product Sense Questions (Ask Yourself)

- What's your gut feeling about these OKRs? What feels right? What feels off?
- If you had to explain these OKRs to a skeptical executive in 2 minutes, what would you say?
- What would make you say "these OKRs are obviously wrong"?
- What would make you say "these OKRs are obviously right"?
- Do these OKRs feel like they'll drive the right behavior? What behavior might they drive instead?
- What biases might be affecting your view? (Activity bias? Vanity metrics? Output vs. outcome?)

### Green Flags (What Good OKRs Look Like)

✅ Clear business outcome objectives (not features or projects)  
✅ Specific baseline → target with thresholds  
✅ Event definitions and dashboard links provided  
✅ Mix of leading and lagging indicators  
✅ Clear strategic alignment documented  
✅ Dependencies identified with owners and timelines  
✅ Confidence scoring approach defined

**Note:** For comprehensive evaluation (peer review, quality gates), see `3-okr-evaluation.md`.

---

## Best Practices

### Do's

- ✅ **Start with outcomes** - Always ask "what outcome are we trying to achieve?"
- ✅ **Keep it simple** - 1-2 Objectives, 2-4 Key Results per Objective
- ✅ **Mix leading and lagging** - Use leading indicators to predict lagging outcomes
- ✅ **Set ambitious goals** - Stretch goals inspire teams; it's okay to miss if you learn
- ✅ **Track weekly** - Weekly confidence checks enable early course correction
- ✅ **Link to work** - Connect initiatives and PRDs to KR IDs for traceability
- ✅ **Document learnings** - Capture what worked and what didn't in decision log
- ✅ **Use RAT-style KRs** - Test assumptions before committing resources

### Don'ts

- ❌ **Don't use activities as KRs** - Focus on outcomes, not deliverables
- ❌ **Don't set too many OKRs** - 1-2 Objectives max per team
- ❌ **Don't forget baselines** - Always include current state and target state
- ❌ **Don't set-and-forget** - Review weekly, adjust mid-cycle
- ❌ **Don't use vanity metrics** - Connect every KR to business value
- ❌ **Don't make OKRs too easy** - Stretch goals drive learning and growth
- ❌ **Don't ignore confidence signals** - Low confidence means adjust, not ignore
- ❌ **Don't duplicate metrics** - Each KR should measure something unique

## Integration with Other Frameworks

### Combining OKRs with Strategy Blocks

**When to combine:** When operationalizing strategic pillars into measurable outcomes

**How they work together:**
- Strategy Blocks provide strategic pillars and direction
- OKRs translate pillars into measurable Objectives and Key Results
- Strategic pillars inform OKR Objectives
- OKR progress validates strategic choices

**Example workflow:**
```
Step 1: Use Strategy Blocks to identify strategic pillars (e.g., "Enable discovery of advanced features")
Step 2: Create OKR Objective aligned to pillar (e.g., "Enable teams to discover and adopt advanced features")
Step 3: Define Key Results that measure pillar success (e.g., "Increase advanced feature adoption by 60%")
Step 4: Track OKR progress to validate strategic pillar
```

### Combining OKRs with Roadmaps

**When to combine:** When building roadmaps that support OKR Key Results

**How they work together:**
- OKRs define what outcomes to achieve
- Roadmaps define what initiatives will achieve those outcomes
- Initiatives link to KR IDs they support
- Roadmap prioritization informed by OKR priorities

**Example workflow:**
```
Step 1: Set OKRs with Key Results (e.g., O1-KR1: "Increase engagement by 20%")
Step 2: Identify initiatives that could support each KR
Step 3: Prioritize initiatives using RICE/ICE
Step 4: Build roadmap with initiatives linked to KR IDs
Step 5: Track initiative progress toward KR targets
```

### Combining OKRs with North Star

**When to combine:** When OKRs should move the North Star metric

**How they work together:**
- North Star defines the ultimate metric
- OKRs define how to move the North Star
- Key Results should connect to North Star or input metrics
- OKR progress should move North Star

**Example workflow:**
```
Step 1: Define North Star metric (e.g., "Weekly active users")
Step 2: Identify input metrics that influence North Star
Step 3: Create OKR Key Results that move input metrics
Step 4: Track how OKR progress moves North Star
```

### Combining OKRs with Prioritization Frameworks

**When to combine:** When prioritizing initiatives that support OKRs

**How they work together:**
- OKRs define strategic priorities
- Prioritization frameworks (RICE/ICE) score initiatives
- Initiatives that support high-priority KRs get higher scores
- Prioritization informed by OKR alignment

**Example workflow:**
```
Step 1: Set OKRs with Key Results
Step 2: List initiatives that could support each KR
Step 3: Score initiatives using RICE/ICE
Step 4: Boost scores for initiatives aligned to OKRs
Step 5: Prioritize top-scoring, OKR-aligned initiatives
```

### Typical Integration Patterns

**Pattern 1: Strategy → OKRs → Roadmap**
- Strategy Blocks → OKRs → Roadmap → PRDs
- **Use when:** Building quarterly roadmap from strategy

**Pattern 2: OKRs → Prioritization → Roadmap**
- OKRs → RICE/ICE Prioritization → Roadmap
- **Use when:** Prioritizing initiatives to achieve OKRs

**Pattern 3: North Star → OKRs → Initiatives**
- North Star → OKRs → Prioritized Initiatives
- **Use when:** Connecting work to North Star metric

## Advanced Techniques

### RAT-Style Key Results

**When to use:** When testing assumptions before committing resources

**How it works:**
- Define Key Results as tests of assumptions
- Set thresholds for pass/fail
- Run tests (RATs) to validate assumptions
- Adjust OKRs based on test results

**Example:**
```
Assumption: "Users want advanced filtering"
KR: "Test advanced filtering with 100 users; 70%+ find it valuable"
Threshold: 70% positive feedback = pass, proceed with full feature
Result: Test validates assumption before building full feature
```

### Cascading OKRs

**When to use:** When multiple levels need alignment (company → team → individual)

**How it works:**
- Company sets high-level OKRs
- Teams create OKRs that support company OKRs
- Individuals create OKRs that support team OKRs
- Maintain traceability through KR IDs

**Example:**
```
Company O1: "Expand enterprise market"
  → Team O1: "Enable enterprise teams to discover advanced features"
    → Individual O1: "Design enterprise feature discovery flow"
```

### Confidence-Based OKR Adjustment

**When to use:** When confidence signals indicate need for change

**How it works:**
- Track confidence weekly (0/1/2)
- Low confidence (0) triggers investigation
- At-risk confidence (1) triggers adjustment planning
- Adjust OKRs mid-cycle if needed (document in decision log)

**Example:**
```
Week 1-4: KR1 confidence = 2 (on-track)
Week 5: KR1 confidence = 1 (at-risk) - adoption slower than expected
Week 6: Adjusted strategy, KR1 confidence = 2
Result: Course-corrected before end of cycle
```

### Outcome Proxy Metrics

**When to use:** When direct outcome metrics aren't available yet

**How it works:**
- Use leading indicators as proxies for lagging outcomes
- Validate proxies correlate with outcomes over time
- Replace proxies with direct metrics when available

**Example:**
```
Ultimate outcome: "Increase revenue by 20%"
Proxy KR: "Increase enterprise signups by 30%" (leading indicator)
Rationale: Enterprise customers drive revenue; signups predict revenue
```

## Metrics for Success

Track these to know if your OKR framework is working:

- **OKR completion rate** - What % of KRs achieve their targets?
  - **Target:** 60-70% (stretch goals mean some misses are expected)
- **Confidence accuracy** - How well does confidence predict final results?
  - **Target:** Confidence trends match final grades
- **Team alignment** - Can everyone explain current OKRs?
  - **Target:** 90%+ of team can articulate OKRs
- **Work linkage** - What % of initiatives link to KR IDs?
  - **Target:** 80%+ of initiatives link to KRs
- **Learning capture** - Are learnings documented in decision log?
  - **Target:** Every cycle has documented learnings
- **Stakeholder satisfaction** - Do stakeholders understand OKRs?
  - **Target:** Stakeholders can explain team OKRs

## Review Schedule

### Weekly Reviews (20-30 minutes)

**Focus:** Track progress and confidence

**Activities:**
- Review KR status and progress
- Update confidence levels (0/1/2)
- Identify risks and blockers
- Plan next RAT tests or actions

**Deliverables:**
- Updated confidence scores
- Risk log
- Next actions

### Mid-Cycle Reviews (1-2 hours)

**Focus:** Assess if adjustments needed

**Activities:**
- Review progress vs. targets
- Assess if Objectives still relevant
- Decide: double-down, pivot, or stop
- Document material changes in decision log

**Deliverables:**
- Adjustment decisions
- Updated OKRs (if changed)
- Decision log entries

### End-of-Cycle Reviews (2-3 hours)

**Focus:** Grade results and capture learnings

**Activities:**
- Grade each KR (0.0-1.0 scale)
- Calculate Objective scores (average of KRs)
- Document what worked and what didn't
- Roll learnings into decision log
- Archive completed OKRs

**Deliverables:**
- Graded OKRs
- Learnings document
- Decision log updates

### Quarterly Planning (4-6 hours)

**Focus:** Set next cycle OKRs

**Activities:**
- Review last cycle's learnings
- Gather inputs (strategy, opportunities, constraints)
- Set new OKRs for next quarter
- Align with stakeholders

**Deliverables:**
- New OKRs for next cycle
- Stakeholder alignment

## Stakeholder Communication

### For Leadership

**Focus on:**
- Strategic alignment and business impact
- Progress toward key outcomes
- Risks and blockers requiring support
- Resource needs

**Key messages:**
- How OKRs support company strategy
- Progress on key business metrics
- What help is needed to succeed

### For Product Teams

**Focus on:**
- How work connects to outcomes
- Progress tracking and confidence
- Initiative prioritization
- Learning and iteration

**Key messages:**
- How initiatives contribute to KRs
- Current progress and confidence
- What's working and what's not

### For Engineering Teams

**Focus on:**
- Technical outcomes and quality metrics
- Effort estimates and capacity
- Dependencies and blockers
- Technical debt considerations

**Key messages:**
- How technical work supports KRs
- Capacity and effort estimates
- Dependencies and risks

### For Cross-Functional Teams

**Focus on:**
- Shared objectives and alignment
- Dependencies and handoffs
- Collaborative outcomes
- Integration points

**Key messages:**
- How teams work together on shared OKRs
- Dependencies and coordination needs
- Success criteria for collaboration

## Inputs (each cycle)
- Company/BU priorities and constraints.
- Team mission and core metrics (SLAs, latency, cost-to-serve).
- Opportunity backlog tied to JTBD and ODI outcomes.
- Last cycle’s decision log and post-mortems.

## OKR Types
- Impact OKRs: move a core business metric.
- Enabler OKRs: unlock future impact (platform, data quality, compliance).
Keep 1–2 Objectives per team; 2–4 KRs per Objective.

## KR Quality
- Specific, measurable, time-bound; mix lagging/leading.
- Instrumented with event/ID definitions and pass/fail thresholds.
- Avoid milestone/project KRs; use outcome proxies when needed.

## Process (2-week spin-up; rolling thereafter)
1) Prep (async): compile inputs; propose problem spaces and candidate metrics.
2) Framing workshop: align on “why now,” pick 1–2 Objectives, brainstorm KRs.
3) Convert top assumptions into RAT-style KRs with thresholds.
4) Stakeholder review: validate metrics, guardrails, dependencies.
5) Publish to company OKRs; assign owners; link dashboards.

## Cadence
- Weekly 20–30 min: KR status, confidence (0/1/2), risks, next RAT test.
- Mid-cycle: decide to double-down, pivot, or stop; snapshot if materially changed.
- End-cycle: grade KRs (0.0–1.0); roll learnings into decision log.

## Scoring & Confidence
- Scoring at cycle end: 0.0–1.0 per KR; average → Objective score.
- Weekly confidence: 0 (off-track), 1 (at-risk), 2 (on-track); cite evidence.

## Linking Rules
- Assign stable KR IDs `O#-KR#`. Use everywhere (initiatives, PRDs, dashboards).
- Initiatives list KR IDs they contribute to and link evidence; do not duplicate metrics.
- Material changes recorded in `decision-log.md`; archive snapshots on change.

## Example Objectives (illustrative)
- Reduce time-to-signal from insight to product changes by 30%.
- Improve post-release operational reliability.
- Strengthen governance and compliance for key product decisions.

-----

## References

- OKR Template: `2-okr-template.md`
- OKR Evaluation: `3-okr-evaluation.md`
- Company Context: `../../01-Company-Context/README.md`
- Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
- Roadmap: `../2-Roadmap/README.md`
- North Star: `../3-North-Star/README.md`
- Prioritization: `../4-Prioritization/README.md`
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)


