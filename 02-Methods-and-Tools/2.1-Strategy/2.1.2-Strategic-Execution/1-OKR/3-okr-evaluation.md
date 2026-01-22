# OKR Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

## Usage Instructions

This framework provides a systematic approach to evaluate OKRs against evidence-based, outcome-focused methodology.

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `OKR_QUALITY_CHECK` for immediate flag assessment
2. Apply `OKR_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `OKR_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `OKR_IMPROVEMENT_GENERATOR`

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about these OKRs? What feels right? What feels off?
- If you had to explain these OKRs to a skeptical executive in 2 minutes, what would you say?
- What would make you say "these OKRs are obviously wrong"?
- What would make you say "these OKRs are obviously right"?
- What does your product sense tell you about the outcomes? Do they feel meaningful?
- Do these OKRs feel like they'll drive the right behavior? What behavior might they drive instead?

**Bias Check:**
- What biases might be affecting your view? (Activity bias? Vanity metrics? Output vs. outcome?)
- Are you seeing what you want to see, or what's actually there?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

# STEP 1: OKR_QUALITY_CHECK

Scan for these flags before detailed evaluation:

## RED FLAGS (each counts as -1 multiplier point)

❌ Objectives are project/feature names ("Build X", "Implement Y", "Deploy Z")
❌ KRs are milestones ("Complete Phase 1", "Launch feature", "Finish integration")
❌ No baselines or targets specified ("Improve conversion", "Increase quality")
❌ Missing time bounds ("Increase revenue", "Reduce costs")
❌ No measurement instrumentation mentioned (no dashboards, events, or tracking)
❌ More than 2 Objectives per team
❌ More than 5 KRs per Objective
❌ KRs focus on activities not outcomes ("Implement X", "Deploy Y")

## GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Clear business outcome objectives (not features or projects)
✅ Specific baseline → target with thresholds
✅ Event definitions and dashboard links provided
✅ Mix of leading and lagging indicators
✅ Clear strategic alignment documented
✅ Dependencies identified with owners and timelines
✅ Confidence scoring approach defined

## Multiplier Calculation

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

# STEP 2: OKR_EVALUATOR_PROMPT

You are an OKR expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
- Ask: "Before we run the structured evaluation, what's your gut feeling about these OKRs? What feels right? What feels off?"
- Ask: "If you had to explain these OKRs to a skeptical executive in 2 minutes, what would you say?"
- Ask: "What would make you say 'these OKRs are obviously wrong'? What would make you say 'they're obviously right'?"
- Ask: "What does your product sense tell you about the outcomes? Do they feel meaningful?"
- Ask: "Do these OKRs feel like they'll drive the right behavior? What behavior might they drive instead?"
- Ask: "What biases might be affecting your view?" (Activity bias? Vanity metrics? Output vs. outcome?)

2) **THEN: Run Structured Evaluation**
- After capturing their product sense, run the structured evaluation below
- Compare the structured evaluation results to their initial gut feeling
- Highlight where product sense aligned with structured evaluation
- Flag where there are discrepancies and explore why

3) **END: Reflection**
- "How did your initial product sense compare to the structured evaluation?"
- "What did the structured evaluation reveal that your gut didn't catch?"
- "What did your gut catch that the structured evaluation validated?"
- "How can you develop better product sense for OKRs?"

Now evaluate provided OKRs using these 6 weighted criteria:

## Scoring Framework (1-10 scale)

### 1. OUTCOME CLARITY (Weight: 30%)

**Score 9-10:** Objectives clearly state business outcomes, not activities. Easy to understand why this matters to the business without domain expertise.

**Score 7-8:** Mostly outcome-focused with minor activity language.

**Score 4-6:** Mix of outcomes and outputs, requires context to understand value.

**Score 1-3:** Activity/project-focused, no clear business outcome articulated.

**Examples:**
- ✅ Good: "Reduce time-to-signal from user insight to product changes by 30%"
- ❌ Poor: "Implement new dashboard"

---

### 2. KEY RESULT MEASURABILITY (Weight: 25%)

**Score 9-10:** All KRs are specific, measurable, time-bound with clear baselines and targets. Mix of leading/lagging indicators.

**Score 7-8:** Most KRs measurable with minor gaps in specificity.

**Score 4-6:** Some measurable KRs, others vague or milestone-based.

**Score 1-3:** Vague, unmeasurable, or purely milestone/project KRs.

**Examples:**
- ✅ Good: "API response time from 2.1s to <1.5s by Q3 (threshold: 1.8s)"
- ❌ Poor: "Improve system performance"

---

### 3. EVIDENCE-BASED APPROACH (Weight: 20%)

**Score 9-10:** KRs include clear instrumentation, event definitions, pass/fail thresholds, dashboard links.

**Score 7-8:** Good measurement approach with minor gaps in instrumentation.

**Score 4-6:** Some measurement defined, lacks clear thresholds or instrumentation.

**Score 1-3:** No clear measurement approach or evidence plan.

---

### 4. STRATEGIC ALIGNMENT (Weight: 10%)

**Score 9-10:** Clear connection to company/BU goals, JTBD, or business priorities with explicit linking.

**Score 7-8:** Good alignment with minor gaps in connection.

**Score 4-6:** Some alignment visible but not clearly articulated.

**Score 1-3:** No clear connection to broader strategy or business goals.

---

### 5. SCOPE APPROPRIATENESS (Weight: 10%)

**Score 9-10:** 1-2 Objectives with 2-4 KRs each, appropriate for team capacity and timeline.

**Score 7-8:** Good scope with minor concerns about feasibility.

**Score 4-6:** Scope issues - too many objectives or unrealistic KRs.

**Score 1-3:** Massive scope, too many objectives, or clearly unfeasible.

---

### 6. DEPENDENCY CLARITY (Weight: 5%)

**Score 9-10:** Dependencies clearly identified with owners, timelines, and risk mitigation.

**Score 7-8:** Dependencies identified with minor gaps.

**Score 4-6:** Some dependencies noted but lacks detail.

**Score 1-3:** Dependencies unclear or not identified.

---

## Scoring Calculation

### Step 1: Calculate Raw Score
```
Raw Score = (Outcome_Clarity × 0.30) + 
            (Measurability × 0.25) + 
            (Evidence × 0.20) + 
            (Alignment × 0.10) + 
            (Scope × 0.10) + 
            (Dependencies × 0.05)
```

### Step 2: Apply Quality Multiplier
```
Final Score = Raw Score × Quality Multiplier
```

### Step 3: Determine Rating
- 8.0-10.0: Excellent (ready for execution)
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
- **OKR Type:** [Impact/Enabler/Mixed]
- **Primary Strengths:** [2-3 key strengths]
- **Critical Issues:** [2-3 main problems]

### DETAILED SCORES

For each criterion provide:

**[Criterion Name] Score: X/10 (Weight: X%)**
- **Justification:** [2-3 sentences explaining the score]
- **Evidence:** [Specific quote or example from the OKRs]
- **Improvement:** [One concrete, actionable suggestion]

### OKR QUALITY ASSESSMENT

**Business Impact Focus: X/10**
[How well do these OKRs focus on business outcomes vs activities?]

**Measurement Rigor: X/10**
[How well are KRs instrumented and measurable?]

**Execution Clarity: X/10**
[How clear is it what success looks like and how to achieve it?]

### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

# STEP 3: OKR_ANTIPATTERN_DETECTOR

Scan for these common OKR mistakes and note specific instances:

## OBJECTIVE ANTIPATTERNS

❌ **Business-as-usual work disguised as objectives**
- Ongoing operational work presented as strategic initiative
- Impact: -0.5 from Outcome Clarity

❌ **Too many objectives (>2 per team)**
- Dilutes focus and reduces execution effectiveness
- Impact: -1.0 from Scope Appropriateness

❌ **Vague aspirations without clear outcomes**
- Generic goals like "improve quality" or "increase efficiency"
- Impact: -1.0 from Outcome Clarity

❌ **Project/feature delivery focus**
- Objectives describe what to build, not what to achieve
- Impact: -2.0 from Outcome Clarity (critical)

## KEY RESULT ANTIPATTERNS

❌ **Milestones masquerading as metrics**
- "Complete Phase 1", "Launch feature", "Finish migration"
- Impact: -2.0 from Measurability (critical)

❌ **No baseline established**
- Cannot measure progress without starting point
- Impact: -1.0 from Measurability

❌ **Targets without thresholds**
- No pass/fail criteria for quarterly scoring
- Impact: -0.5 from Evidence-Based Approach

❌ **Unmeasurable or subjective criteria**
- Cannot be objectively verified
- Impact: -2.0 from Measurability (critical)

❌ **Input metrics instead of outcome metrics**
- Measures activity (features shipped) vs impact (user value)
- Impact: -1.0 from Outcome Clarity

## PROCESS ANTIPATTERNS

❌ **No instrumentation plan**
- No dashboards, events, or tracking methodology
- Impact: -1.0 from Evidence-Based Approach

❌ **Missing confidence scoring approach**
- No weekly check-in methodology defined
- Impact: -0.5 from Evidence-Based Approach

❌ **Unclear ownership assignments**
- No clear owners for objectives or key results
- Impact: -0.5 from Scope Appropriateness

❌ **No connection to broader strategy**
- Cannot explain how this ladders to company goals
- Impact: -1.0 from Strategic Alignment

❌ **Dependencies not identified or owned**
- Cross-team needs unclear or without owners
- Impact: -1.0 from Dependency Clarity

## Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Objective Issues: [count] ([list])
- Key Result Issues: [count] ([list])
- Process Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

# STEP 4: OKR_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

## REWRITE EXAMPLES

### Objective Transformation Template
```
Current: [Original objective text]
Issues: [What's wrong with it]
Improved: "[Action verb] [business outcome] by [amount/percentage] [timeframe]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Implement customer portal"
Issues: Feature-focused, no business outcome
Improved: "Reduce customer support ticket volume by 40% through self-service"
Rationale: Focuses on business impact (support cost reduction) vs feature delivery
```

### Key Result Transformation Template
```
Current: [Original KR text]
Issues: [What's wrong with it]
Improved: "[Metric] from [baseline] to [target] by [date] (threshold: [minimum])"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Improve API performance"
Issues: No baseline, target, or threshold
Improved: "API response time from 2.1s to <1.5s by Q3 (threshold: 1.8s)"
Rationale: Specific, measurable, with clear success criteria
```

---

## MEASUREMENT PLAN

For each weak or unmeasured KR, specify:

### [KR Name] Measurement Framework

**Event/Metric Definition:**
[Precise definition of what you're measuring]

**Instrumentation:**
- Data Source: [Where the data comes from]
- Collection Method: [How it's captured]
- Frequency: [How often it's measured]

**Dashboard:**
- Location: [Link or description]
- Refresh Rate: [How often updated]
- Key Visualizations: [What charts/graphs to include]

**Thresholds:**
- Target: [Aspirational goal]
- Threshold: [Minimum for success]
- Red Line: [Unacceptable performance]

**Example:**
```
User Satisfaction Score Measurement Framework

Event/Metric Definition:
Monthly NPS score from internal users of settlement system

Instrumentation:
- Data Source: Monthly survey via email
- Collection Method: Automated Qualtrics survey
- Frequency: Last week of each month

Dashboard:
- Location: Operations Dashboard > User Experience tab
- Refresh Rate: Weekly (survey results + trend analysis)
- Key Visualizations: NPS trend line, satisfaction breakdown by function

Thresholds:
- Target: 70% promoters (NPS >8)
- Threshold: 65% promoters (minimum for pass)
- Red Line: <50% promoters (triggers intervention)
```

---

## STRATEGIC CONNECTIVITY

Demonstrate how OKRs connect to broader strategy:

### Company/BU Goals Connection
**Goal:** [Specific company objective]
**How This OKR Supports It:** [Clear explanation of linkage]

### JTBD/Opportunity Connection
**Job to Be Done:** [Customer or business need]
**Problem Being Solved:** [Specific pain point]
**Expected Impact:** [How solving this creates value]

### Success Metrics Ladder
```
OKR → Team Metric → Department Metric → Company Metric
Example: "Settlement time -60%" → "Ops efficiency +40%" → "Unit cost -25%" → "Margin +5%"
```

---

## 4-WEEK IMPROVEMENT PLAN

### Week 1: Outcome Clarity Sprint
**Focus:** Rewrite all objectives to focus on business outcomes

**Activities:**
- Workshop with stakeholders to identify business problems
- Transform activity-focused objectives into outcome statements
- Validate objectives pass "so what?" test

**Deliverable:** Revised objectives in outcome format

**Success Criteria:** Each objective clearly states business impact

---

### Week 2: Measurement Definition
**Focus:** Define measurement methodology and establish baselines

**Activities:**
- Identify data sources for each KR
- Establish current state baselines
- Define instrumentation approach
- Set up data collection if not already available

**Deliverable:** Measurement framework document

**Success Criteria:** Every KR has baseline, target, threshold, and instrumentation plan

---

### Week 3: Implementation & Dashboarding
**Focus:** Establish tracking infrastructure and thresholds

**Activities:**
- Build or configure dashboards
- Set up automated data collection
- Define pass/fail thresholds
- Create weekly check-in template

**Deliverable:** Live dashboards with baseline data

**Success Criteria:** Stakeholders can view real-time progress on all KRs

---

### Week 4: Validation & Alignment
**Focus:** Validate with stakeholders and align with company priorities

**Activities:**
- Present revised OKRs to leadership
- Confirm strategic alignment
- Clarify dependencies with partner teams
- Finalize confidence scoring methodology

**Deliverable:** Approved OKR set ready for execution

**Success Criteria:** Stakeholder sign-off and clear execution plan

---

## SUMMARY TEMPLATE

### Quick Wins (Implement Immediately)
1. [High-impact, low-effort improvement]
2. [High-impact, low-effort improvement]
3. [High-impact, low-effort improvement]

### Strategic Improvements (Next Cycle)
1. [Major change requiring planning]
2. [Major change requiring planning]

### Long-term Capability Building
1. [Foundational improvement for future cycles]
2. [Foundational improvement for future cycles]