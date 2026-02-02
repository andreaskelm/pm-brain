# Roadmap Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-roadmap-framework.md`. This comprehensive evaluation framework is for peer review, quality gates, or deep learning.

## Usage Instructions

This framework provides a systematic approach to evaluate roadmaps against evidence-based, outcome-focused methodology.

**When to use this comprehensive evaluation:**
- Peer review of coworkers' roadmaps
- Quality gates before finalizing/sharing
- Deep learning about what makes good roadmaps
- After creation, when you want comprehensive feedback

**For creation-time checks:** Use the lightweight "Quick Quality Checks" in `1-roadmap-framework.md` (agent uses these automatically during creation).

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `ROADMAP_QUALITY_CHECK` for immediate flag assessment
2. Apply `ROADMAP_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `ROADMAP_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `ROADMAP_IMPROVEMENT_GENERATOR`

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

5. **Reference framework:** When suggesting improvements, reference specific sections from `1-roadmap-framework.md` for context.

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about this roadmap? What feels right? What feels off?
- If you had to explain this roadmap to a skeptical executive in 2 minutes, what would you say?
- What would make you say "this roadmap is obviously wrong"?
- What would make you say "this roadmap is obviously right"?
- What does your product sense tell you about the priorities? Do they feel right?
- What initiatives feel like they might be missing? What feels like it shouldn't be there?

**Bias Check:**
- What biases might be affecting your view? (Recency bias? Squeaky wheel? Status quo?)
- Are you seeing what you want to see, or what's actually there?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: ROADMAP_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ Initiative names are system/application names ("Implement X", "Deploy Y")
❌ Outcomes focus on migration percentages ("100% users migrated")
❌ Dependencies are just team names ("Marketing, IT")
❌ Success metrics are binary done/not-done only
❌ Heavy unexplained acronyms/jargon throughout
❌ No clear business problems articulated
❌ Time horizons don't match confidence levels

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Problems clearly stated in business terms
✅ Plain language throughout
✅ Quantified business impact metrics
✅ Specific, actionable dependencies
✅ Clear scope boundaries
✅ Confidence levels align with time horizons

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

## STEP 2: ROADMAP_EVALUATOR_PROMPT

You are a product roadmap expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
- Ask: "Before we run the structured evaluation, what's your gut feeling about this roadmap? What feels right? What feels off?"
- Ask: "If you had to explain this roadmap to a skeptical executive in 2 minutes, what would you say?"
- Ask: "What would make you say 'this roadmap is obviously wrong'? What would make you say 'it's obviously right'?"
- Ask: "What does your product sense tell you about the priorities? Do they feel right?"
- Ask: "What initiatives feel like they might be missing? What feels like it shouldn't be there?"
- Ask: "What biases might be affecting your view?" (Recency bias? Squeaky wheel? Status quo?)

2) **THEN: Run Structured Evaluation**
- After capturing their product sense, run the structured evaluation below
- Compare the structured evaluation results to their initial gut feeling
- Highlight where product sense aligned with structured evaluation
- Flag where there are discrepancies and explore why

3) **END: Reflection**
- "How did your initial product sense compare to the structured evaluation?"
- "What did the structured evaluation reveal that your gut didn't catch?"
- "What did your gut catch that the structured evaluation validated?"
- "How can you develop better product sense for roadmaps?"

Now evaluate the provided roadmap using these 6 weighted criteria:

## Scoring Framework (1-10 scale):

### 1. PROBLEM CLARITY (Weight: 25%)
**Score 9-10:** Each initiative clearly states the business problem, why it matters, and impact of not solving it. Outsiders easily understand the value.
**Score 7-8:** Problems are stated but could be clearer or more business-focused.
**Score 4-6:** Vague problem statements requiring domain knowledge to understand.
**Score 1-3:** No clear problem articulation; focuses on features/implementations.

### 2. LANGUAGE ACCESSIBILITY (Weight: 20%) 
**Score 9-10:** Written in plain language, passes "mom test," minimal unexplained jargon.
**Score 7-8:** Mostly accessible with minor technical terms.
**Score 4-6:** Requires significant domain knowledge to understand.
**Score 1-3:** Heavy jargon, insider language only.

### 3. OUTCOME DEFINITION (Weight: 20%)
**Score 9-10:** Clear business outcomes with measurable impact, not feature delivery.
**Score 7-8:** Good outcomes with minor implementation focus.
**Score 4-6:** Mix of business outcomes and technical outputs.
**Score 1-3:** Focuses on delivery/migration rather than business value.

### 4. SUCCESS METRICS (Weight: 15%)
**Score 9-10:** Specific, measurable, business-impact focused with leading/lagging indicators.
**Score 7-8:** Good metrics needing stronger business connection.
**Score 4-6:** Some specific metrics, many binary/completion-based.
**Score 1-3:** Vague or purely completion-based metrics.

### 5. SCOPE BOUNDARIES (Weight: 10%)
**Score 9-10:** Clear start/end points, stakeholders understand inclusion/exclusion.
**Score 7-8:** Generally clear scope with minor ambiguity.
**Score 4-6:** Some clarity with areas of confusion.
**Score 1-3:** Vague boundaries, unclear deliverables.

### 6. DEPENDENCY SPECIFICITY (Weight: 10%)
**Score 9-10:** Dependencies specify what's needed, from whom, by when, and impact of delays.
**Score 7-8:** Clear dependencies with minor gaps.
**Score 4-6:** Some specificity, many vague references.
**Score 1-3:** Team/system names only, no context.

## Output Format:

### EXECUTIVE SUMMARY
- Overall Score: [Weighted average]/10
- Primary Strengths: [2-3 key strengths]
- Critical Issues: [2-3 main problems]

### DETAILED SCORES
For each criterion:
- **[Criterion] Score: X/10**
- Justification: [Brief explanation]
- Example: [Specific quote showing strength/weakness]
- Improvement: [One concrete suggestion]

### STAKEHOLDER READINESS
Rate how well this roadmap would serve:
- **Executive Leadership:** [Score + reason]
- **Cross-functional Teams:** [Score + reason]
- **External Stakeholders:** [Score + reason]

### TOP 3 IMPROVEMENTS
1. [Most impactful change]
2. [Second priority]
3. [Third priority]

### Scoring Calculation

**Step 1: Calculate Raw Score**
```
Raw Score = (Problem_Clarity × 0.25) + 
            (Language_Accessibility × 0.20) + 
            (Outcome_Definition × 0.20) + 
            (Success_Metrics × 0.15) + 
            (Scope_Boundaries × 0.10) + 
            (Dependency_Specificity × 0.10)
```

**Step 2: Apply Quality Multiplier**
```
Final Score = Raw Score × Quality Multiplier
```

**Step 3: Determine Rating**
- 8.0-10.0: Excellent (ready for execution)
- 6.0-7.9: Good (minor refinements needed)
- 4.0-5.9: Fair (significant improvements required)
- 2.0-3.9: Poor (major rewrite needed)
- 0.0-1.9: Failing (complete restart recommended)

---

## STEP 3: ROADMAP_ANTIPATTERN_DETECTOR

Scan for these common roadmap mistakes and note specific instances:

### INITIATIVE ANTIPATTERNS

❌ **System/application names instead of problems**
- Initiative names like "Implement X", "Deploy Y" focus on solutions, not problems
- Impact: -2.0 from Problem Clarity (critical)

❌ **Migration percentages as outcomes**
- Outcomes like "100% users migrated" focus on completion, not business value
- Impact: -1.5 from Outcome Definition (critical)

❌ **Binary success metrics only**
- Metrics are done/not-done without measurable business impact
- Impact: -2.0 from Success Metrics (critical)

### LANGUAGE ANTIPATTERNS

❌ **Heavy unexplained jargon**
- Acronyms and technical terms without context
- Impact: -1.5 from Language Accessibility (critical)

❌ **Insider language only**
- Requires domain expertise to understand
- Impact: -1.0 from Language Accessibility

### OUTCOME ANTIPATTERNS

❌ **No clear business problems**
- Focuses on features/implementations without stating problems
- Impact: -2.0 from Problem Clarity (critical)

❌ **Delivery/migration focus**
- Outcomes focus on completion rather than business value
- Impact: -1.5 from Outcome Definition

### DEPENDENCY ANTIPATTERNS

❌ **Vague dependencies**
- Just team names ("Marketing, IT") without specifics
- Impact: -1.5 from Dependency Specificity (critical)

❌ **Missing dependency details**
- No "what", "from whom", "by when", or "impact of delays"
- Impact: -1.0 from Dependency Specificity

### SCOPE ANTIPATTERNS

❌ **Unclear boundaries**
- Stakeholders don't understand what's included/excluded
- Impact: -1.0 from Scope Boundaries

❌ **Confidence mismatch**
- High confidence for LATER, low confidence for NOW
- Impact: -1.0 from Scope Boundaries

### Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Initiative Issues: [count] ([list])
- Language Issues: [count] ([list])
- Outcome Issues: [count] ([list])
- Dependency Issues: [count] ([list])
- Scope Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: ROADMAP_IMPROVEMENT_GENERATOR

Based on the evaluation, provide:

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### Initiative Transformation Template

```
Current: [Original initiative text]
Issues: [What's wrong with it]
Improved: "[Problem-first or outcome-focused version]"
Rationale: [Why this is better]
```

**Problem-First Template:**
"Eliminate [specific problem] that currently causes [business impact] for [stakeholder group]"

**Business Outcome Template:**
"Achieve [business result] by [method] resulting in [measurable benefit]"

**Example:**
```
Current: "Implement new dashboard"
Issues: System name, no problem or outcome stated
Improved: "Eliminate manual reporting that currently takes 10 hours/week for operations teams"
Rationale: Focuses on problem (manual reporting) and impact (time waste) vs feature delivery
```

### METRICS ENHANCEMENT

For each initiative with weak or binary metrics, specify:

#### [Initiative Name] Success Metrics Framework

**Business Impact Metric:**
[Specific, measurable metric that shows business value]

**Baseline:**
[Current state]

**Target:**
[Aspirational goal]

**Threshold:**
[Minimum for success]

**Measurement Plan:**
- Data Source: [Where the data comes from]
- Collection Method: [How it's captured]
- Frequency: [How often measured]
- Dashboard: [Link or location]

**Example:**
```
Onboarding Flow Improvement Success Metrics Framework

Business Impact Metric:
Time-to-first-value for new teams (days from signup to completing first workflow)

Baseline:
Current average: 14 days

Target:
Reduce to 7 days (50% reduction)

Threshold:
10 days (minimum improvement to consider success)

Measurement Plan:
- Data Source: User activity events in analytics system
- Collection Method: Automated tracking via event IDs
- Frequency: Weekly aggregation
- Dashboard: Product Analytics > Onboarding tab
```

### DEPENDENCY SPECIFICATION

For each vague dependency, specify:

#### [Dependency Name] Dependency Framework

**What's Needed:**
[Specific deliverable or capability]

**From Whom:**
[Specific team/person]

**By When:**
[Specific date or milestone]

**Impact of Delay:**
[What happens if this dependency is delayed]

**Mitigation Plan:**
[How to reduce risk if dependency fails]

**Example:**
```
API Performance Dependency Framework

What's Needed:
Infrastructure team to provision new database cluster

From Whom:
Infrastructure Team (lead: Jane Doe)

By When:
End of Q2 (June 30)

Impact of Delay:
Initiative delayed by 2 weeks, cannot achieve target outcome on time

Mitigation Plan:
- Alternative: Use existing cluster with performance tuning (80% of benefit)
- Escalation path: CTO if delay exceeds 1 week
```

### STAKEHOLDER COMMUNICATION PLAN

For each stakeholder group, specify:

#### For Executives
**Key Messages:**
- [Message 1 focusing on business impact]
- [Message 2 focusing on strategic alignment]
- [Message 3 focusing on risks/dependencies]

**Format:**
- [Preferred format: one-pager, presentation, email]

#### For Cross-Functional Teams
**Key Messages:**
- [Message 1 focusing on operational implications]
- [Message 2 focusing on dependencies]
- [Message 3 focusing on collaboration needs]

**Format:**
- [Preferred format: meeting, shared doc, async update]

#### For External Stakeholders
**Key Messages:**
- [Message 1 focusing on customer value]
- [Message 2 focusing on timeline expectations]
- [Message 3 focusing on confidence levels]

**Format:**
- [Preferred format: newsletter, roadmap page, direct communication]

### 4-WEEK IMPROVEMENT PLAN

#### Week 1: Problem Clarity Sprint
**Focus:** Rewrite all initiatives to focus on problems and outcomes

**Activities:**
- Workshop to identify business problems for each initiative
- Transform system names into problem statements
- Validate initiatives pass "so what?" test

**Deliverable:** Revised initiatives with clear problem statements

**Success Criteria:** Each initiative clearly states the problem it solves

---

#### Week 2: Language & Metrics Enhancement
**Focus:** Improve accessibility and measurement

**Activities:**
- Rewrite jargon-heavy sections in plain language
- Define specific, measurable success metrics for each initiative
- Establish baselines and targets

**Deliverable:** Plain language roadmap with measurable metrics

**Success Criteria:** Roadmap passes "mom test" and has specific metrics

---

#### Week 3: Dependency & Scope Clarity
**Focus:** Specify dependencies and clarify scope boundaries

**Activities:**
- Document specific dependencies (what, from whom, by when)
- Clarify scope boundaries for each initiative
- Align confidence levels with time horizons

**Deliverable:** Roadmap with clear dependencies and scope

**Success Criteria:** All dependencies have owners and timelines

---

#### Week 4: Stakeholder Validation
**Focus:** Validate improvements with stakeholders

**Activities:**
- Present revised roadmap to stakeholders
- Gather feedback on clarity and alignment
- Finalize roadmap based on input

**Deliverable:** Validated roadmap ready for execution

**Success Criteria:** Stakeholder sign-off and clear execution plan

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

- Roadmap Framework: `1-roadmap-framework.md` - Complete methodology
- Roadmap Template: `2-roadmap-template.md` - Fill-in-the-blanks template
- Related Frameworks:
  - Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
  - OKR Framework: `../1-OKR/README.md`
  - North Star: `../3-North-Star/README.md`
  - Prioritization: `../4-Prioritization/README.md`
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
