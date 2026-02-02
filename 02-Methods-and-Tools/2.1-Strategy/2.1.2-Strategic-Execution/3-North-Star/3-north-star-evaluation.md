# North Star Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-north-star-framework.md`. This comprehensive evaluation framework is for peer review, quality gates, or deep learning.

## Usage Instructions

This framework provides a systematic approach to evaluate North Star frameworks against evidence-based, outcome-focused methodology.

**When to use this comprehensive evaluation:**
- Peer review of coworkers' North Star frameworks
- Quality gates before execution
- Deep learning about what makes good North Star metrics
- After creation, when you want comprehensive feedback

**For creation-time checks:** Use the lightweight "Quick Quality Checks" in `1-north-star-framework.md` (agent uses these automatically during creation).

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `NORTH_STAR_QUALITY_CHECK` for immediate flag assessment
2. Apply `NORTH_STAR_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `NORTH_STAR_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `NORTH_STAR_IMPROVEMENT_GENERATOR`

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

5. **Reference framework:** When suggesting improvements, reference specific sections from `1-north-star-framework.md` for context.

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about this North Star? What feels right? What feels off?
- If you had to explain this North Star to a skeptical executive in 2 minutes, what would you say?
- What would make you say "this North Star is obviously wrong"?
- What would make you say "this North Star is obviously right"?
- What does your product sense tell you about the metric? Does it feel like it captures real customer value?
- Does this North Star feel actionable? Can teams see how their work connects to it?
- What biases might be affecting your metric choice? (Vanity metrics? Activity bias?)

**Bias Check:**
- What biases might be affecting your view? (Vanity metrics? Activity bias? Output vs. outcome?)
- Are you seeing what you want to see, or what's actually there?
- What would someone with different product sense say about this North Star?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising
- List what surprised you or confirmed your assumptions

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: NORTH_STAR_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ **Vanity metrics** - Metric looks good but doesn't drive value (page views, registered users)
❌ **Unclear input/output relationships** - How inputs influence North Star is not clear
❌ **Not actionable** - Teams can't see how their work connects to the North Star
❌ **Misaligned with strategy** - North Star doesn't connect to strategic priorities
❌ **Too many inputs** - More than 5 input metrics (dilutes focus)
❌ **No work connections** - Initiatives don't map to input metrics
❌ **Unclear measurement** - No clear definition of how North Star is measured
❌ **Wrong product game** - Metric doesn't match ATTENTION/TRANSACTION/PRODUCTIVITY game

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Customer value-focused metric (not vanity metrics)
✅ Clear input/output relationships documented
✅ Actionable inputs (teams can directly influence them)
✅ Strategic alignment documented
✅ 3-5 input metrics (focused, not overwhelming)
✅ Work connections mapped (initiatives link to inputs)
✅ Clear measurement definition with baseline
✅ Product game correctly identified (ATTENTION/TRANSACTION/PRODUCTIVITY)

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

## STEP 2: NORTH_STAR_EVALUATOR_PROMPT

You are a North Star Framework expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
   - Ask: "Before we run the structured evaluation, what's your gut feeling about this North Star? What feels right? What feels off?"
   - Ask: "If you had to explain this North Star to a skeptical executive in 2 minutes, what would you say?"
   - Ask: "What would make you say 'this North Star is obviously wrong'? What would make you say 'it's obviously right'?"
   - Ask: "What does your product sense tell you about the metric? Does it feel like it captures real customer value?"
   - Ask: "Does this North Star feel actionable? Can teams see how their work connects to it?"
   - Ask: "What biases might be affecting your metric choice?" (Vanity metrics? Activity bias? Output vs. outcome?)

2) **THEN: Run Structured Evaluation**
   - After capturing their product sense, run the structured evaluation below
   - Compare the structured evaluation results to their initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Flag where there are discrepancies and explore why

3) **END: Reflection**
   - "How did your initial product sense compare to the structured evaluation?"
   - "What did the structured evaluation reveal that your gut didn't catch?"
   - "What did your gut catch that the structured evaluation validated?"
   - "How can you develop better product sense for North Star metrics?"

Now evaluate provided North Star framework using these 6 weighted criteria:

## Scoring Framework (1-10 scale)

### 1. METRIC QUALITY (Weight: 30%)

**Score 9-10:** North Star metric captures customer value, predicts business outcomes, and avoids vanity metrics. Clear why this metric matters.

**Score 7-8:** Good metric with minor concerns about value capture or vanity metric risk.

**Score 4-6:** Metric has some value but may be vanity-focused or unclear connection to customer value.

**Score 1-3:** Vanity metric or no clear customer value connection.

**Examples:**
- ✅ Good: "Weekly Learning Users" (Amplitude) - captures value delivered
- ❌ Poor: "Total registered users" - vanity metric, doesn't capture value

---

### 2. INPUT/OUTPUT CLARITY (Weight: 25%)

**Score 9-10:** Clear, documented relationships between input metrics and North Star. Teams understand how inputs drive the North Star.

**Score 7-8:** Good input/output relationships with minor gaps in documentation or clarity.

**Score 4-6:** Some input/output relationships but unclear or undocumented.

**Score 1-3:** No clear input/output relationships or inputs don't connect to North Star.

**Examples:**
- ✅ Good: "Input: New user activation rate → Influences North Star: Weekly active users (activation drives retention)"
- ❌ Poor: "Input: Feature adoption" (unclear how it influences North Star)

---

### 3. ACTIONABILITY (Weight: 20%)

**Score 9-10:** Input metrics are actionable (teams can directly influence them). Work connections clearly mapped. Teams can explain how their work impacts inputs.

**Score 7-8:** Mostly actionable with minor gaps in work connections or team understanding.

**Score 4-6:** Some actionable inputs but unclear work connections or team mapping.

**Score 1-3:** Inputs not actionable or teams can't see how their work connects.

---

### 4. STRATEGIC ALIGNMENT (Weight: 10%)

**Score 9-10:** Clear connection to strategic priorities and business goals. North Star aligns with product strategy and company direction.

**Score 7-8:** Good alignment with minor gaps in connection to strategy.

**Score 4-6:** Some alignment but not clearly articulated or documented.

**Score 1-3:** No clear connection to strategic priorities or misaligned with strategy.

---

### 5. SCOPE APPROPRIATENESS (Weight: 10%)

**Score 9-10:** 3-5 input metrics (focused, not overwhelming). Product game correctly identified (ATTENTION/TRANSACTION/PRODUCTIVITY). Appropriate for team capacity.

**Score 7-8:** Good scope with minor concerns about number of inputs or game identification.

**Score 4-6:** Scope issues - too many inputs (>5) or unclear product game.

**Score 1-3:** Too many inputs (>7) or wrong product game, clearly inappropriate scope.

---

### 6. MEASUREMENT & OPERATIONALIZATION (Weight: 5%)

**Score 9-10:** Clear measurement definition with baseline, target, and dashboard links. Operationalized into planning processes (OKRs, roadmaps).

**Score 7-8:** Good measurement approach with minor gaps in operationalization.

**Score 4-6:** Some measurement defined but lacks baseline or operational integration.

**Score 1-3:** No clear measurement approach or not operationalized.

---

## Scoring Calculation

### Step 1: Calculate Raw Score
```
Raw Score = (Metric_Quality × 0.30) + 
            (Input_Output_Clarity × 0.25) + 
            (Actionability × 0.20) + 
            (Strategic_Alignment × 0.10) + 
            (Scope_Appropriateness × 0.10) + 
            (Measurement × 0.05)
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
- **Product Game:** [ATTENTION/TRANSACTION/PRODUCTIVITY]
- **Primary Strengths:** [2-3 key strengths]
- **Critical Issues:** [2-3 main problems]

### DETAILED SCORES

For each criterion provide:

**[Criterion Name] Score: X/10 (Weight: X%)**
- **Justification:** [2-3 sentences explaining the score]
- **Evidence:** [Specific quote or example from the North Star framework]
- **Improvement:** [One concrete, actionable suggestion]

### NORTH STAR QUALITY ASSESSMENT

**Customer Value Focus: X/10**
[How well does this North Star capture customer value vs vanity metrics?]

**Team Actionability: X/10**
[How actionable is this North Star for teams? Can they see how their work connects?]

**Strategic Alignment: X/10**
[How well does this North Star align with strategic priorities?]

### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

## STEP 3: NORTH_STAR_ANTIPATTERN_DETECTOR

Scan for these common North Star mistakes and note specific instances:

### METRIC ANTIPATTERNS

❌ **Vanity metrics as North Star**
- Metrics like "total registered users" or "page views" that look good but don't drive value
- Impact: -2.0 from Metric Quality (critical)

❌ **Output vs. outcome confusion**
- Focuses on activity (features shipped) vs customer value delivered
- Impact: -2.0 from Metric Quality (critical)

❌ **Unclear customer value connection**
- Metric doesn't clearly capture customer value or predict business outcomes
- Impact: -1.5 from Metric Quality

❌ **Wrong product game**
- Metric doesn't match ATTENTION/TRANSACTION/PRODUCTIVITY game
- Impact: -1.0 from Scope Appropriateness

### INPUT/OUTPUT ANTIPATTERNS

❌ **Unclear input/output relationships**
- How inputs influence North Star is not documented or unclear
- Impact: -2.0 from Input/Output Clarity (critical)

❌ **Inputs don't connect to North Star**
- Input metrics don't clearly influence the North Star
- Impact: -1.5 from Input/Output Clarity (critical)

❌ **Missing input metrics**
- No input metrics defined or too few (<3)
- Impact: -1.0 from Input/Output Clarity

### ACTIONABILITY ANTIPATTERNS

❌ **Not actionable**
- Teams can't see how their work connects to inputs or North Star
- Impact: -2.0 from Actionability (critical)

❌ **No work connections**
- Initiatives don't map to input metrics
- Impact: -1.5 from Actionability (critical)

❌ **Inputs not influenceable**
- Input metrics are not things teams can directly influence
- Impact: -1.0 from Actionability

### SCOPE ANTIPATTERNS

❌ **Too many inputs**
- More than 5 input metrics (dilutes focus)
- Impact: -1.0 from Scope Appropriateness

❌ **Too few inputs**
- Less than 3 input metrics (may not capture full picture)
- Impact: -0.5 from Scope Appropriateness

### STRATEGIC ANTIPATTERNS

❌ **Misaligned with strategy**
- North Star doesn't connect to strategic priorities or business goals
- Impact: -1.5 from Strategic Alignment (critical)

❌ **No strategic connection documented**
- Strategic alignment not articulated or documented
- Impact: -1.0 from Strategic Alignment

### MEASUREMENT ANTIPATTERNS

❌ **Unclear measurement**
- No clear definition of how North Star is measured
- Impact: -1.0 from Measurement & Operationalization

❌ **No baseline or target**
- Missing current state or target state for North Star
- Impact: -0.5 from Measurement & Operationalization

❌ **Not operationalized**
- North Star not integrated into planning processes (OKRs, roadmaps)
- Impact: -0.5 from Measurement & Operationalization

## Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Metric Issues: [count] ([list])
- Input/Output Issues: [count] ([list])
- Actionability Issues: [count] ([list])
- Scope Issues: [count] ([list])
- Strategic Issues: [count] ([list])
- Measurement Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: NORTH_STAR_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### North Star Metric Transformation Template

```
Current: [Original metric]
Issues: [What's wrong with it]
Improved: "[Customer value-focused metric]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Total registered users"
Issues: Vanity metric, doesn't capture value delivered
Improved: "Weekly Learning Users" (users who complete a learning activity each week)
Rationale: Focuses on value delivered (learning) vs activity (registration)
```

#### Input Metric Transformation Template

```
Current: [Original input metric]
Issues: [What's wrong with it]
Improved: "[Actionable input metric] - [How it influences North Star]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Feature adoption"
Issues: Unclear how it influences North Star, not actionable
Improved: "New user activation rate within first session" - Influences North Star by driving first-time value delivery, which predicts weekly return
Rationale: Specific, actionable (teams can improve onboarding), clear connection to North Star
```

### METRIC ENHANCEMENT

For each weak or vanity metric, specify:

#### [Metric Name] North Star Metric Framework

**Current Metric:**
[What metric is currently used?]

**Issues:**
[What's wrong with it? Vanity? No customer value?]

**Improved Metric:**
[Customer value-focused metric]

**Definition:**
[Precise definition of what you're measuring]

**Why This Metric:**
[Why this metric captures customer value and predicts business outcomes]

**Measurement Plan:**
- Baseline: [Current value]
- Target: [Aspirational goal]
- Dashboard: [Link or location]
- Frequency: [How often measured]

**Example:**
```
Weekly Active Users North Star Metric Framework

Current Metric:
Total registered users

Issues:
Vanity metric - doesn't capture value delivered, easy to game

Improved Metric:
Weekly Learning Users (users who complete a learning activity each week)

Definition:
Count of unique users who complete at least one learning activity (course completion, quiz passed, skill demonstrated) in a given week

Why This Metric:
- Captures value delivered (learning) vs activity (registration)
- Predicts retention (users who learn are more likely to return)
- Connects to business outcomes (engaged learners drive revenue)

Measurement Plan:
- Baseline: 5,000 weekly learning users (current)
- Target: 10,000 weekly learning users (6 months)
- Dashboard: Product Analytics > Engagement > Weekly Learning Users
- Frequency: Weekly aggregation, monthly reporting
```

### INPUT/OUTPUT RELATIONSHIP ENHANCEMENT

For each unclear input/output relationship, specify:

#### [Input Metric] Input/Output Relationship Framework

**Input Metric:**
[Name of input metric]

**How It Influences North Star:**
[Clear explanation of how this input drives the North Star]

**Evidence:**
[What evidence supports this relationship? Data? Correlation?]

**Team Ownership:**
[Which team(s) can influence this input?]

**Work Connections:**
[What initiatives/work connect to this input?]

**Example:**
```
New User Activation Rate Input/Output Relationship Framework

Input Metric:
New user activation rate within first session (percentage of new users who complete first learning activity in first session)

How It Influences North Star:
Drives first-time value delivery, which is the strongest predictor of weekly return. Users who activate in first session are 3x more likely to become weekly learning users.

Evidence:
- Correlation analysis: 0.75 correlation between first-session activation and weekly return
- Cohort analysis: Users who activate in first session have 60% weekly return rate vs 20% for non-activators

Team Ownership:
- Product: Onboarding flow design
- Engineering: Onboarding flow implementation
- Design: First-session experience

Work Connections:
- Initiative: "Simplify onboarding flow" → Moves activation rate from 40% to 60%
- Initiative: "Personalized first-session recommendations" → Moves activation rate from 40% to 55%
```

### ACTIONABILITY ENHANCEMENT

For each non-actionable input, specify:

#### [Input Metric] Actionability Framework

**Current State:**
[What's currently not actionable about this input?]

**Improved Input:**
[Actionable version]

**How Teams Can Influence:**
[Specific ways teams can move this input]

**Work Mapping:**
[How current initiatives/work map to this input]

**Example:**
```
User Engagement Actionability Framework

Current State:
Input: "User engagement" (too vague, not actionable)

Improved Input:
"Percentage of users discovering personalized content" (specific, actionable)

How Teams Can Influence:
- Product: Improve content discovery UI
- Engineering: Build recommendation engine
- Design: Design personalized content feed
- Data: Improve recommendation algorithms

Work Mapping:
- Initiative: "Build recommendation engine" → Moves personalized content discovery from 30% to 50%
- Initiative: "Redesign content feed" → Moves personalized content discovery from 30% to 45%
```

### 4-WEEK IMPROVEMENT PLAN

#### Week 1: Metric Quality Sprint
**Focus:** Refine North Star metric to focus on customer value

**Activities:**
- Workshop to evaluate current metric against customer value criteria
- Identify vanity metric risks
- Refine or replace metric to focus on customer value
- Validate metric with stakeholders

**Deliverable:** Customer value-focused North Star metric

**Success Criteria:** Metric clearly captures customer value, avoids vanity metrics

---

#### Week 2: Input/Output Clarity Enhancement
**Focus:** Define clear input/output relationships

**Activities:**
- Identify 3-5 input metrics that influence North Star
- Document how each input influences the North Star
- Map inputs to team capabilities
- Validate relationships with data or evidence

**Deliverable:** Clear input/output relationships documented

**Success Criteria:** All inputs have clear documented relationships to North Star

---

#### Week 3: Actionability & Work Connections
**Focus:** Make inputs actionable and map work connections

**Activities:**
- Ensure inputs are things teams can directly influence
- Map current initiatives to input metrics
- Create work connections section
- Validate teams can see how their work connects

**Deliverable:** Actionable inputs with work connections mapped

**Success Criteria:** Teams can explain how their work impacts inputs

---

#### Week 4: Operationalization & Alignment
**Focus:** Operationalize North Star and validate strategic alignment

**Activities:**
- Integrate North Star into planning processes (OKRs, roadmaps)
- Set up dashboards and tracking
- Validate strategic alignment
- Communicate to all teams

**Deliverable:** Operationalized North Star framework

**Success Criteria:** North Star integrated into processes, teams understand it

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

- North Star Framework: `1-north-star-framework.md` - Complete methodology
- North Star Template: `2-north-star-template.md` - Fill-in-the-blanks template
- Related Frameworks:
  - Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
  - OKR Framework: `../1-OKR/README.md`
  - Roadmap: `../2-Roadmap/README.md`
  - Prioritization: `../4-Prioritization/README.md`
  - Execution: `../../2.3-Execution/README.md` (Metrics Framework)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
