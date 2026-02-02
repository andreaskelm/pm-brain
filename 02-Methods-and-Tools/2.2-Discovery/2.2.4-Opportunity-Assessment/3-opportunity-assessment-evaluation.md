# Opportunity Assessment Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-opportunity-assessment-framework.md`. This comprehensive evaluation framework is for peer review, quality gates, or deep learning.

## Usage Instructions

This framework provides a systematic approach to evaluate opportunity assessments against evidence-based methodology.

**When to use this comprehensive evaluation:**
- Peer review of coworkers' opportunity assessments
- Quality gates before discovery work
- Deep learning about what makes good opportunity assessments
- After creation, when you want comprehensive feedback

**For creation-time checks:** Use the lightweight "Quick Quality Checks" in `1-opportunity-assessment-framework.md` (agent uses these automatically during creation).

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `OPPORTUNITY_ASSESSMENT_QUALITY_CHECK` for immediate flag assessment
2. Apply `OPPORTUNITY_ASSESSMENT_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `OPPORTUNITY_ASSESSMENT_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `OPPORTUNITY_ASSESSMENT_IMPROVEMENT_GENERATOR`

---

## AI Agent Instructions

**For LLMs/AI agents using this framework:**

1. **Follow the step sequence:** Always start with STEP 0 (Product Sense), then proceed through STEP 1-4 in order.

2. **Help user think, don't think for them:**
   - Ask the product sense questions from STEP 0 before running structured evaluation
   - Compare structured results to user's initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Explore discrepancies together

3. **Use structured sections:**
   - STEP 1: Scan for red/green flags, calculate multiplier
   - STEP 2: Score each criterion (1-10), calculate raw score, apply multiplier
   - STEP 3: Scan for antipatterns, categorize by type
   - STEP 4: Generate specific improvements using templates

4. **Output format:** Use the "Output Format" section in STEP 2 as a template for presenting results.

5. **Reference framework:** When suggesting improvements, reference specific sections from `1-opportunity-assessment-framework.md` for context.

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about this opportunity assessment? What feels right? What feels off?
- If you had to explain this opportunity to a skeptical executive in 2 minutes, what would you say?
- What would make you say "this opportunity is obviously wrong"?
- What would make you say "this opportunity is obviously right"?
- What does your product sense tell you about the hypothesis? Does it feel meaningful?
- Does this opportunity feel like it's worth pursuing? What would make you kill it?
- What assumptions feel risky? Which ones feel solid?

**Bias Check:**
- What biases might be affecting your view? (Solution bias? Confirmation bias? Opportunity bias?)
- Are you seeing what you want to see, or what's actually there?
- What would someone with different product sense say about this opportunity?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising
- List what surprised you or confirmed your assumptions

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: OPPORTUNITY_ASSESSMENT_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ **No clear hypothesis** - Opportunity statement is vague or missing
❌ **Assumptions not identified** - Assumptions not documented with confidence levels
❌ **Missing evidence plan** - No research plan or validation approach defined
❌ **Vague opportunity** - Opportunity not clearly articulated or too broad
❌ **Solution bias** - Focuses on solutions before understanding the problem
❌ **Missing decision criteria** - No kill/pivot/commit thresholds defined
❌ **No customer context** - Missing target customer or JTBD understanding
❌ **Missing success metrics** - No clear definition of how success will be measured

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Clear hypothesis with opportunity statement
✅ Assumptions documented with confidence levels (High/Med/Low)
✅ Evidence plan with research methods and decision criteria
✅ Target customer clearly defined with JTBD context
✅ Success metrics with baselines and targets
✅ Decision criteria defined (kill/pivot/commit thresholds)
✅ Risks identified across desirability/viability/feasibility/usability
✅ Solution ideas kept high-level until validated

### Multiplier Calculation

**Red Flag Count → Multiplier:**
- 0-1 red flags: 1.0× (no penalty)
- 2-3 red flags: 0.8× (minor issues)
- 4-5 red flags: 0.5× (significant issues)
- 6+ red flags: 0.2× (fundamental failure)

**Green Flag Bonus:**
Add 0.5 multiplier points for each green flag (maximum +2.0 to multiplier)

**Final Multiplier Formula:**
```
Base Multiplier = [1.0, 0.8, 0.5, 0.2] based on red flag count
Green Bonus = min(green_flag_count × 0.5, 2.0)
Quality Multiplier = max(0.1, Base Multiplier + Green Bonus)
```

---

## STEP 2: OPPORTUNITY_ASSESSMENT_EVALUATOR_PROMPT

You are an opportunity assessment expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
   - Ask: "Before we run the structured evaluation, what's your gut feeling about this opportunity assessment? What feels right? What feels off?"
   - Ask: "If you had to explain this opportunity to a skeptical executive in 2 minutes, what would you say?"
   - Ask: "What would make you say 'this opportunity is obviously wrong'? What would make you say 'it's obviously right'?"
   - Ask: "What does your product sense tell you about the hypothesis? Does it feel meaningful?"
   - Ask: "What assumptions feel risky? Which ones feel solid?"
   - Ask: "What biases might be affecting your view?" (Solution bias? Confirmation bias? Opportunity bias?)

2) **THEN: Run Structured Evaluation**
   - After capturing their product sense, run the structured evaluation below
   - Compare the structured evaluation results to their initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Flag where there are discrepancies and explore why

3) **END: Reflection**
   - "How did your initial product sense compare to the structured evaluation?"
   - "What did the structured evaluation reveal that your gut didn't catch?"
   - "What did your gut catch that the structured evaluation validated?"
   - "How can you develop better product sense for opportunity assessments?"

Now evaluate provided opportunity assessment using these 6 weighted criteria:

## Scoring Framework (1-10 scale)

### 1. HYPOTHESIS CLARITY (Weight: 25%)

**Score 9-10:** Clear, specific hypothesis with well-articulated opportunity statement. Easy to understand what problem/opportunity is being addressed and why it matters.

**Score 7-8:** Hypothesis mostly clear with minor gaps in specificity or articulation.

**Score 4-6:** Hypothesis present but vague or requires domain knowledge to understand value.

**Score 1-3:** No clear hypothesis or opportunity statement; too vague or solution-focused.

**Examples:**
- ✅ Good: "Operations teams waste 30 min/day manually triaging alerts; 80% are false positives. Opportunity: Reduce triage time by 75% through automated prioritization."
- ❌ Poor: "Build an alert system"

---

### 2. ASSUMPTION IDENTIFICATION (Weight: 20%)

**Score 9-10:** All key assumptions explicitly identified with confidence levels (High/Med/Low). Clear distinction between facts and hypotheses. What would change your mind is documented.

**Score 7-8:** Most assumptions identified with minor gaps in confidence levels or clarity.

**Score 4-6:** Some assumptions identified but missing confidence levels or key assumptions.

**Score 1-3:** Assumptions not identified or documented; unclear what's assumed vs. known.

**Examples:**
- ✅ Good: "Assumption: 70% of operations teams spend >20 min/day on alert triage (Confidence: High - backed by survey data). Assumption: ML can accurately prioritize alerts (Confidence: Low - needs validation)."
- ❌ Poor: "We assume teams want better alerts"

---

### 3. EVIDENCE PLAN (Weight: 20%)

**Score 9-10:** Clear research plan with specific methods, participants, sample sizes, and timelines. Decision criteria (kill/pivot/commit thresholds) well-defined. Links to discovery methods.

**Score 7-8:** Good evidence plan with minor gaps in methods or decision criteria.

**Score 4-6:** Some research plan but vague methods or missing decision criteria.

**Score 1-3:** No clear evidence plan or validation approach; missing decision criteria.

**Examples:**
- ✅ Good: "Research: Interview 10 operations team members (sample: 2 per team, 5 teams). Method: 30-min interviews focusing on alert triage pain points. Decision criteria: If <30% report >20 min/day triage time, kill opportunity."
- ❌ Poor: "Talk to some users"

---

### 4. CUSTOMER & STRATEGIC FIT (Weight: 15%)

**Score 9-10:** Target customer clearly defined with JTBD context. Clear connection to strategic priorities. Stakeholder impact well-understood.

**Score 7-8:** Good customer definition with minor gaps in JTBD or strategic fit.

**Score 4-6:** Some customer context but vague or missing JTBD/strategic connection.

**Score 1-3:** No clear target customer or strategic fit; missing JTBD understanding.

---

### 5. SUCCESS METRICS & OPPORTUNITY SIZE (Weight: 15%)

**Score 9-10:** Success metrics clearly defined with baselines and targets. Opportunity size estimated (revenue, time saved, risk reduced). Guardrails defined.

**Score 7-8:** Good metrics with minor gaps in baselines, targets, or opportunity size.

**Score 4-6:** Some metrics defined but vague or missing baselines/targets.

**Score 1-3:** No clear success metrics or opportunity size; purely qualitative.

---

### 6. RISK ASSESSMENT (Weight: 5%)

**Score 9-10:** Risks identified across desirability, viability, feasibility, usability, compliance. Mitigation plans or validation approaches for each risk.

**Score 7-8:** Good risk assessment with minor gaps in coverage or mitigation.

**Score 4-6:** Some risks identified but incomplete coverage or missing mitigation.

**Score 1-3:** Risks not identified or assessed; no mitigation planning.

---

## Scoring Calculation

### Step 1: Calculate Raw Score
```
Raw Score = (Hypothesis_Clarity × 0.25) + 
            (Assumption_Identification × 0.20) + 
            (Evidence_Plan × 0.20) + 
            (Customer_Strategic_Fit × 0.15) + 
            (Success_Metrics × 0.15) + 
            (Risk_Assessment × 0.05)
```

### Step 2: Apply Quality Multiplier
```
Final Score = Raw Score × Quality Multiplier
```

### Step 3: Determine Rating
- 8.0-10.0: Excellent (ready for discovery)
- 6.0-7.9: Good (minor refinements needed)
- 4.0-5.9: Fair (significant improvements required)
- 2.0-3.9: Poor (major rewrite needed)
- 0.0-1.9: Failing (complete restart recommended)

---

## Output Format

### EXECUTIVE SUMMARY
- **Final Score:** [Score]/10 ([Rating])
- **Raw Score:** [Score]/10
- **Quality Multiplier:** [Multiplier]× (Red flags: [count], Green flags: [count])
- **Primary Strengths:** [2-3 key strengths]
- **Critical Issues:** [2-3 main problems]

### DETAILED SCORES

For each criterion provide:

**[Criterion Name] Score: X/10 (Weight: X%)**
- **Justification:** [2-3 sentences explaining the score]
- **Evidence:** [Specific quote or example from the opportunity assessment]
- **Improvement:** [One concrete, actionable suggestion]

### OPPORTUNITY ASSESSMENT QUALITY ASSESSMENT

**Hypothesis Quality: X/10**
[How clear and well-articulated is the opportunity hypothesis?]

**Validation Readiness: X/10**
[How ready is this opportunity assessment for discovery work?]

**Strategic Alignment: X/10**
[How well does this opportunity align with strategic priorities?]

### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

## STEP 3: OPPORTUNITY_ASSESSMENT_ANTIPATTERN_DETECTOR

Scan for these common opportunity assessment mistakes and note specific instances:

### HYPOTHESIS ANTIPATTERNS

❌ **No clear hypothesis**
- Opportunity statement is vague or missing
- Impact: -2.0 from Hypothesis Clarity (critical)

❌ **Solution bias**
- Focuses on solutions before understanding the problem
- Impact: -2.0 from Hypothesis Clarity (critical)

❌ **Vague opportunity**
- Opportunity not clearly articulated or too broad
- Impact: -1.5 from Hypothesis Clarity

❌ **Outcome vs. output confusion**
- Focuses on features/solutions instead of outcomes
- Impact: -1.0 from Hypothesis Clarity

### ASSUMPTION ANTIPATTERNS

❌ **Assumptions not identified**
- Assumptions not documented or marked
- Impact: -2.0 from Assumption Identification (critical)

❌ **Missing confidence levels**
- Assumptions not marked with High/Med/Low confidence
- Impact: -1.5 from Assumption Identification (critical)

❌ **Facts vs. hypotheses confusion**
- Can't distinguish what's known vs. assumed
- Impact: -1.0 from Assumption Identification

❌ **No "what would change your mind"**
- Missing documentation of what evidence would change the assessment
- Impact: -0.5 from Assumption Identification

### EVIDENCE PLAN ANTIPATTERNS

❌ **Missing evidence plan**
- No research plan or validation approach defined
- Impact: -2.0 from Evidence Plan (critical)

❌ **No decision criteria**
- Missing kill/pivot/commit thresholds
- Impact: -1.5 from Evidence Plan (critical)

❌ **Vague research methods**
- Research plan lacks specificity (methods, participants, sample sizes)
- Impact: -1.0 from Evidence Plan

❌ **No timeline**
- Research plan missing timeline or milestones
- Impact: -0.5 from Evidence Plan

### CUSTOMER ANTIPATTERNS

❌ **No customer context**
- Missing target customer or JTBD understanding
- Impact: -1.5 from Customer & Strategic Fit (critical)

❌ **Vague customer definition**
- Customer segment too broad or unclear
- Impact: -1.0 from Customer & Strategic Fit

❌ **Missing strategic fit**
- No connection to strategic priorities or business goals
- Impact: -1.0 from Customer & Strategic Fit

### METRICS ANTIPATTERNS

❌ **Missing success metrics**
- No clear definition of how success will be measured
- Impact: -1.5 from Success Metrics & Opportunity Size (critical)

❌ **No baselines or targets**
- Success metrics lack current state or target state
- Impact: -1.0 from Success Metrics & Opportunity Size

❌ **Missing opportunity size**
- No estimate of opportunity value (revenue, time, risk)
- Impact: -1.0 from Success Metrics & Opportunity Size

### RISK ANTIPATTERNS

❌ **Risks not identified**
- No risk assessment across desirability/viability/feasibility/usability
- Impact: -1.0 from Risk Assessment

❌ **Incomplete risk coverage**
- Missing risks in key areas (e.g., only technical risks, no customer risks)
- Impact: -0.5 from Risk Assessment

❌ **No mitigation plans**
- Risks identified but no validation or mitigation approaches
- Impact: -0.5 from Risk Assessment

## Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Hypothesis Issues: [count] ([list])
- Assumption Issues: [count] ([list])
- Evidence Plan Issues: [count] ([list])
- Customer Issues: [count] ([list])
- Metrics Issues: [count] ([list])
- Risk Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: OPPORTUNITY_ASSESSMENT_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### Hypothesis Transformation Template

```
Current: [Original opportunity statement or solution description]
Issues: [What's wrong with it]
Improved: "[Clear hypothesis with opportunity statement]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Build an alert system"
Issues: Solution-focused, no problem or opportunity stated
Improved: "Operations teams waste 30 min/day manually triaging alerts; 80% are false positives. Opportunity: Reduce triage time by 75% through automated prioritization, saving 2.5 hours/week per team member."
Rationale: Focuses on problem (time waste, false positives) and opportunity (time savings) vs solution delivery
```

#### Assumption Documentation Template

```
Current: [Original assumption or lack thereof]
Issues: [What's wrong with it]
Improved: "[Assumption] (Confidence: High/Med/Low) - [Evidence or rationale]. What would change our mind: [Specific evidence threshold]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "We assume teams want better alerts"
Issues: Vague, no confidence level, no evidence threshold
Improved: "Assumption: 70% of operations teams spend >20 min/day on alert triage (Confidence: High - backed by survey of 50 teams). What would change our mind: If <30% report >20 min/day triage time in interviews."
Rationale: Specific, confidence-marked, with clear evidence threshold for validation
```

#### Evidence Plan Template

```
Current: [Original research plan or lack thereof]
Issues: [What's wrong with it]
Improved: "Research: [Method] with [Participants] ([Sample size]). Timeline: [Duration]. Decision criteria: [Kill/Pivot/Commit thresholds]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Talk to some users"
Issues: Vague method, no participants, no sample size, no decision criteria
Improved: "Research: 30-min interviews with 10 operations team members (sample: 2 per team, 5 teams). Timeline: 2 weeks. Decision criteria: If <30% report >20 min/day triage time, kill opportunity. If >70% report need, commit to PRD."
Rationale: Specific method, participants, sample size, timeline, and clear decision thresholds
```

### HYPOTHESIS ENHANCEMENT

For each weak or missing hypothesis, specify:

#### [Opportunity Name] Hypothesis Framework

**Problem Statement:**
[Clear problem statement backed by evidence]

**Opportunity Statement:**
[What opportunity exists? What value could be created?]

**Why Now:**
[What's changed that makes this opportunity relevant now?]

**Expected Impact:**
[What outcome are we trying to achieve? Quantify if possible.]

**Example:**
```
Alert Triage Automation Hypothesis Framework

Problem Statement:
Operations teams waste 30 min/day manually triaging alerts; 80% are false positives. Survey of 50 teams shows 70% spend >20 min/day on triage.

Opportunity Statement:
Reduce alert triage time by 75% through automated prioritization, saving 2.5 hours/week per team member. Enable teams to focus on high-value alerts.

Why Now:
- ML capabilities matured (can now accurately score alerts)
- Alert volume increased 3x in past year (makes manual triage unsustainable)
- Operations teams reporting burnout from alert fatigue

Expected Impact:
- Time savings: 2.5 hours/week per team member × 50 teams = 125 hours/week saved
- Reduced false positive rate: From 80% to <20%
- Improved team satisfaction: Reduce alert-related burnout
```

### ASSUMPTION DOCUMENTATION ENHANCEMENT

For each missing or vague assumption, specify:

#### [Assumption Category] Assumptions Framework

**Assumption:**
[Specific assumption statement]

**Confidence Level:**
[High/Med/Low] - [Rationale for confidence level]

**Evidence Supporting:**
[What evidence supports this assumption?]

**What Would Change Our Mind:**
[Specific evidence threshold that would invalidate assumption]

**Validation Approach:**
[How will we validate this assumption?]

**Example:**
```
Customer Need Assumptions Framework

Assumption:
70% of operations teams spend >20 min/day manually triaging alerts

Confidence Level:
High - Backed by survey data from 50 teams (72% reported >20 min/day)

Evidence Supporting:
- Survey of 50 operations teams (Q2 2024)
- 72% reported spending >20 min/day on alert triage
- Average reported time: 35 min/day

What Would Change Our Mind:
If <30% of interviewed teams report >20 min/day triage time, assumption is wrong

Validation Approach:
- Conduct 10 interviews with operations team members
- Ask: "How much time do you spend per day triaging alerts?"
- If <30% report >20 min/day, kill opportunity
```

### EVIDENCE PLAN ENHANCEMENT

For each weak or missing evidence plan, specify:

#### [Research Area] Evidence Plan Framework

**Key Questions:**
[What specific questions need to be answered?]

**Research Methods:**
- Method: [Interviews, surveys, data analysis, experiments, prototypes]
- Participants: [Who will participate?]
- Sample Size: [How many?]
- Timeline: [How long will this take?]

**Decision Criteria:**
- Kill Threshold: [What evidence would cause us to kill this opportunity?]
- Pivot Threshold: [What evidence would cause us to pivot?]
- Commit Threshold: [What evidence would cause us to commit to PRD?]

**Example:**
```
Alert Triage Pain Points Evidence Plan Framework

Key Questions:
1. How much time do teams spend triaging alerts?
2. What percentage of alerts are false positives?
3. What's the biggest pain point in alert triage?
4. Would automated prioritization help?

Research Methods:
- Method: 30-min semi-structured interviews
- Participants: Operations team members (2 per team, 5 teams = 10 total)
- Sample Size: 10 interviews
- Timeline: 2 weeks (5 interviews per week)

Decision Criteria:
- Kill Threshold: If <30% report >20 min/day triage time, kill opportunity
- Pivot Threshold: If teams report different pain point (not time), pivot hypothesis
- Commit Threshold: If >70% report >20 min/day AND want automated prioritization, commit to PRD
```

### 4-WEEK IMPROVEMENT PLAN

#### Week 1: Hypothesis & Assumption Clarity Sprint
**Focus:** Clarify hypothesis and document assumptions

**Activities:**
- Workshop to refine opportunity hypothesis
- Document all assumptions with confidence levels
- Identify what would change your mind for each assumption
- Validate hypothesis with stakeholders

**Deliverable:** Clear hypothesis with documented assumptions

**Success Criteria:** Hypothesis is clear and specific, all key assumptions documented with confidence levels

---

#### Week 2: Evidence Plan Development
**Focus:** Create comprehensive research plan

**Activities:**
- Define specific research questions
- Select research methods (interviews, surveys, data analysis)
- Define participants and sample sizes
- Set decision criteria (kill/pivot/commit thresholds)
- Create research timeline

**Deliverable:** Complete evidence plan with methods and decision criteria

**Success Criteria:** Research plan has specific methods, participants, sample sizes, and decision thresholds

---

#### Week 3: Customer Context & Metrics Enhancement
**Focus:** Define customer context and success metrics

**Activities:**
- Define target customer with JTBD context
- Identify success metrics with baselines and targets
- Estimate opportunity size (revenue, time, risk)
- Define guardrails
- Assess strategic fit

**Deliverable:** Opportunity assessment with clear customer context and metrics

**Success Criteria:** Target customer clearly defined, success metrics have baselines/targets, opportunity size estimated

---

#### Week 4: Risk Assessment & Validation
**Focus:** Complete risk assessment and validate readiness

**Activities:**
- Identify risks across desirability, viability, feasibility, usability, compliance
- Define mitigation or validation approaches for each risk
- Review complete opportunity assessment
- Validate readiness for discovery work

**Deliverable:** Complete opportunity assessment ready for discovery

**Success Criteria:** All risks identified with mitigation plans, assessment ready for discovery work

---

### SUMMARY TEMPLATE

#### Quick Wins (Implement Immediately)
1. [High-impact, low-effort improvement]
2. [High-impact, low-effort improvement]
3. [High-impact, low-effort improvement]

#### Strategic Improvements (Next Cycle)
1. [Major change requiring planning]
2. [Major change requiring planning]

#### Long-term Capability Building
1. [Foundational improvement for future cycles]
2. [Foundational improvement for future cycles]

---

## References

- Opportunity Assessment Framework: `1-opportunity-assessment-framework.md` - Complete methodology
- Opportunity Assessment Template: `2-opportunity-assessment-template.md` - Fill-in-the-blanks template
- Related Frameworks:
  - Research Interviews: `../2.2.1-Research-Interviews/README.md`
  - Continuous Discovery: `../2.2.2-Continuous-Discovery-Habits/README.md`
  - Jobs To Be Done: `../2.2.3-Jobs-To-Be-Done/README.md`
  - Idea Validation: `../2.2.5-Idea-Validation/README.md`
  - Execution: `../../2.3-Execution/README.md` (PRD Framework)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
