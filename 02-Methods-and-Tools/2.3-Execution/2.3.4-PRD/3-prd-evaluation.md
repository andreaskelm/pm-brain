# PRD Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-prd-framework.md`. This comprehensive evaluation framework is for peer review, quality gates, or deep learning.

## Usage Instructions

This framework provides a systematic approach to evaluate PRDs against evidence-based, outcome-focused methodology.

**When to use this comprehensive evaluation:**
- Peer review of coworkers' PRDs
- Quality gates before engineering execution
- Deep learning about what makes good PRDs
- After creation, when you want comprehensive feedback

**For creation-time checks:** Use the lightweight "Quick Quality Checks" in `1-prd-framework.md` (agent uses these automatically during creation).

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `PRD_QUALITY_CHECK` for immediate flag assessment
2. Apply `PRD_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `PRD_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `PRD_IMPROVEMENT_GENERATOR`

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

5. **Reference framework:** When suggesting improvements, reference specific sections from `1-prd-framework.md` for context.

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about this PRD? What feels right? What feels off?
- If you had to explain this PRD to a skeptical engineer in 2 minutes, what would you say?
- What would make you say "this PRD is obviously wrong"?
- What would make you say "this PRD is obviously right"?
- What does your product sense tell you about the requirements? Do they feel meaningful?
- Does this PRD feel like it will lead to the right outcome? What outcome might it drive instead?
- Who is this really for? Does the PRD make that clear?

**Bias Check:**
- What biases might be affecting your view? (Solution bias? Feature bias? Confirmation bias?)
- Are you seeing what you want to see, or what's actually there?
- What would someone with different product sense say about this PRD?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising
- List what surprised you or confirmed your assumptions

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: PRD_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ **Missing success metrics** - No clear definition of how success will be measured
❌ **Vague requirements** - Requirements are unclear or ambiguous ("improve UX", "make it better")
❌ **No user context** - Missing JTBD, user stories, or clear understanding of who this is for
❌ **Unclear success criteria** - No baselines, targets, or thresholds defined
❌ **Solution-first thinking** - Focuses on features before problems ("Build a dashboard")
❌ **Missing assumptions** - Assumptions not identified or documented
❌ **No traceability** - Missing links to opportunity doc, JTBD, or validation results
❌ **Unclear scope boundaries** - What's in/out of scope not explicitly stated

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Clear problem statement backed by evidence (user quotes, data)
✅ Success metrics with baselines and targets defined
✅ User context clearly articulated (JTBD, user stories, personas)
✅ Requirements have clear acceptance criteria (Given/When/Then)
✅ Traceability to discovery (links to opportunity, JTBD, validation)
✅ Dependencies identified with owners and timelines
✅ Risks identified with mitigation plans
✅ Scope boundaries clearly defined (in/out)

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

## STEP 2: PRD_EVALUATOR_PROMPT

You are a PRD expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
   - Ask: "Before we run the structured evaluation, what's your gut feeling about this PRD? What feels right? What feels off?"
   - Ask: "If you had to explain this PRD to a skeptical engineer in 2 minutes, what would you say?"
   - Ask: "What would make you say 'this PRD is obviously wrong'? What would make you say 'it's obviously right'?"
   - Ask: "What does your product sense tell you about the requirements? Do they feel meaningful?"
   - Ask: "Who is this really for? Does the PRD make that clear?"
   - Ask: "What biases might be affecting your view?" (Solution bias? Feature bias? Confirmation bias?)

2) **THEN: Run Structured Evaluation**
   - After capturing their product sense, run the structured evaluation below
   - Compare the structured evaluation results to their initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Flag where there are discrepancies and explore why

3) **END: Reflection**
   - "How did your initial product sense compare to the structured evaluation?"
   - "What did the structured evaluation reveal that your gut didn't catch?"
   - "What did your gut catch that the structured evaluation validated?"
   - "How can you develop better product sense for PRDs?"

Now evaluate provided PRD using these 6 weighted criteria:

## Scoring Framework (1-10 scale)

### 1. PROBLEM & USER CLARITY (Weight: 25%)

**Score 9-10:** Problem statement is clear, backed by evidence (user quotes, data), and user context (JTBD, user stories) is well-articulated. Easy to understand who this is for and why it matters.

**Score 7-8:** Problem and user context mostly clear with minor gaps in evidence or articulation.

**Score 4-6:** Problem or user context present but vague, requires domain knowledge to understand value.

**Score 1-3:** No clear problem statement or user context; focuses on features without understanding user needs.

**Examples:**
- ✅ Good: "Operations teams spend 30 min/day manually triaging alerts; 80% are false positives. JTBD: 'When I see an alert, help me quickly determine if it requires action.'"
- ❌ Poor: "Build a dashboard to show alerts"

---

### 2. SUCCESS METRICS (Weight: 25%)

**Score 9-10:** Success metrics clearly defined with baselines, targets, thresholds, and measurement plan. Mix of leading and lagging indicators. Guardrails defined.

**Score 7-8:** Success metrics defined with minor gaps in baselines, targets, or measurement plan.

**Score 4-6:** Some success metrics defined but vague or missing baselines/targets.

**Score 1-3:** No clear success metrics or purely output-based (features shipped).

**Examples:**
- ✅ Good: "Reduce alert triage time from 30min → 5min (baseline: 30min avg, target: 5min, threshold: 10min). Measure via time-to-resolution event."
- ❌ Poor: "Improve alert handling"

---

### 3. REQUIREMENTS CLARITY (Weight: 20%)

**Score 9-10:** All P0 requirements have clear acceptance criteria (Given/When/Then format). Requirements are specific, testable, and unambiguous. Edge cases considered.

**Score 7-8:** Most requirements have acceptance criteria with minor gaps in specificity or edge cases.

**Score 4-6:** Some requirements have acceptance criteria, others vague or missing.

**Score 1-3:** Requirements are vague, ambiguous, or missing acceptance criteria entirely.

**Examples:**
- ✅ Good: "Given a user views an alert, When the alert confidence score is <0.3, Then the alert is automatically dismissed and logged"
- ❌ Poor: "Make alerts smarter"

---

### 4. TRACEABILITY & EVIDENCE (Weight: 15%)

**Score 9-10:** Clear links to opportunity doc, JTBD, validation results. Evidence supports problem statement and solution approach. Assumptions documented with confidence levels.

**Score 7-8:** Good traceability with minor gaps in links or evidence.

**Score 4-6:** Some traceability but missing key links or evidence.

**Score 1-3:** No traceability to discovery work or evidence; assumptions not documented.

---

### 5. SCOPE & FEASIBILITY (Weight: 10%)

**Score 9-10:** Scope boundaries clearly defined (in/out), dependencies identified with owners and timelines, technical feasibility validated, risks identified with mitigation plans.

**Score 7-8:** Good scope definition with minor gaps in dependencies or risk mitigation.

**Score 4-6:** Some scope definition but unclear boundaries or missing dependencies.

**Score 1-3:** Unclear scope, missing dependencies, or unfeasible requirements.

---

### 6. STAKEHOLDER ALIGNMENT (Weight: 5%)

**Score 9-10:** All stakeholders reviewed and approved, cross-functional alignment confirmed, open questions documented with owners.

**Score 7-8:** Good alignment with minor gaps in stakeholder review or open questions.

**Score 4-6:** Some alignment but missing stakeholder reviews or unclear ownership.

**Score 1-3:** No stakeholder alignment or missing key approvals.

---

## Scoring Calculation

### Step 1: Calculate Raw Score
```
Raw Score = (Problem_User_Clarity × 0.25) + 
            (Success_Metrics × 0.25) + 
            (Requirements_Clarity × 0.20) + 
            (Traceability × 0.15) + 
            (Scope_Feasibility × 0.10) + 
            (Stakeholder_Alignment × 0.05)
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
- **Primary Strengths:** [2-3 key strengths]
- **Critical Issues:** [2-3 main problems]

### DETAILED SCORES

For each criterion provide:

**[Criterion Name] Score: X/10 (Weight: X%)**
- **Justification:** [2-3 sentences explaining the score]
- **Evidence:** [Specific quote or example from the PRD]
- **Improvement:** [One concrete, actionable suggestion]

### PRD QUALITY ASSESSMENT

**Problem-First Focus: X/10**
[How well does this PRD focus on problems and user needs vs features?]

**Execution Readiness: X/10**
[How ready is this PRD for engineering execution?]

**Evidence-Based Approach: X/10**
[How well is this PRD grounded in discovery and validation?]

### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

## STEP 3: PRD_ANTIPATTERN_DETECTOR

Scan for these common PRD mistakes and note specific instances:

### PROBLEM & USER ANTIPATTERNS

❌ **Solution-first thinking**
- PRD starts with features/solutions before problems
- Impact: -2.0 from Problem & User Clarity (critical)

❌ **Missing user context**
- No JTBD, user stories, or clear understanding of who this is for
- Impact: -2.0 from Problem & User Clarity (critical)

❌ **Vague problem statement**
- Problem not backed by evidence or too generic
- Impact: -1.5 from Problem & User Clarity

❌ **No evidence backing problem**
- Problem statement lacks user quotes, data, or validation
- Impact: -1.0 from Traceability & Evidence

### SUCCESS METRICS ANTIPATTERNS

❌ **Missing success metrics**
- No clear definition of how success will be measured
- Impact: -2.0 from Success Metrics (critical)

❌ **No baselines or targets**
- Success metrics lack current state or target state
- Impact: -1.5 from Success Metrics (critical)

❌ **Output-based metrics only**
- Metrics focus on features shipped, not outcomes achieved
- Impact: -1.5 from Success Metrics

❌ **Missing guardrails**
- No definition of what NOT to break
- Impact: -0.5 from Success Metrics

### REQUIREMENTS ANTIPATTERNS

❌ **Vague requirements**
- Requirements are unclear or ambiguous
- Impact: -2.0 from Requirements Clarity (critical)

❌ **Missing acceptance criteria**
- Requirements lack Given/When/Then format or testable criteria
- Impact: -1.5 from Requirements Clarity (critical)

❌ **Ignoring edge cases**
- Only happy-path flows documented, no error handling
- Impact: -1.0 from Requirements Clarity

❌ **Over-specification**
- Too much detail before validation
- Impact: -0.5 from Requirements Clarity

### TRACEABILITY ANTIPATTERNS

❌ **No links to discovery**
- Missing links to opportunity doc, JTBD, or validation results
- Impact: -1.5 from Traceability & Evidence (critical)

❌ **Assumptions not documented**
- Assumptions not identified or marked with confidence levels
- Impact: -1.0 from Traceability & Evidence

❌ **No validation evidence**
- Solution approach not backed by validation results
- Impact: -1.0 from Traceability & Evidence

### SCOPE ANTIPATTERNS

❌ **Unclear scope boundaries**
- What's in/out of scope not explicitly stated
- Impact: -1.5 from Scope & Feasibility (critical)

❌ **Missing dependencies**
- Dependencies not identified with owners and timelines
- Impact: -1.0 from Scope & Feasibility

❌ **Unfeasible requirements**
- Requirements not validated for technical feasibility
- Impact: -1.5 from Scope & Feasibility

❌ **Risks not identified**
- No risk assessment or mitigation plans
- Impact: -0.5 from Scope & Feasibility

### PROCESS ANTIPATTERNS

❌ **Missing stakeholder alignment**
- No evidence of stakeholder review or approval
- Impact: -1.0 from Stakeholder Alignment

❌ **Open questions not documented**
- Questions that need answers not tracked with owners
- Impact: -0.5 from Stakeholder Alignment

## Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Problem & User Issues: [count] ([list])
- Success Metrics Issues: [count] ([list])
- Requirements Issues: [count] ([list])
- Traceability Issues: [count] ([list])
- Scope Issues: [count] ([list])
- Process Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: PRD_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### Problem Statement Transformation Template

```
Current: [Original problem statement or feature description]
Issues: [What's wrong with it]
Improved: "[Clear problem statement backed by evidence]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Build a dashboard to show alerts"
Issues: Solution-first, no problem or user context
Improved: "Operations teams spend 30 min/day manually triaging alerts; 80% are false positives. JTBD: 'When I see an alert, help me quickly determine if it requires action.'"
Rationale: Focuses on problem (time waste, false positives) and user need (JTBD) vs feature delivery
```

#### Success Metrics Transformation Template

```
Current: [Original metrics or lack thereof]
Issues: [What's wrong with it]
Improved: "[Metric] from [baseline] to [target] (threshold: [minimum]) measured via [method]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Improve alert handling"
Issues: No baseline, target, threshold, or measurement plan
Improved: "Reduce alert triage time from 30min → 5min (baseline: 30min avg, target: 5min, threshold: 10min). Measure via time-to-resolution event tracked in analytics dashboard."
Rationale: Specific, measurable, with clear success criteria and measurement approach
```

#### Requirement Transformation Template

```
Current: [Original requirement]
Issues: [What's wrong with it]
Improved: "Given [context], When [trigger], Then [outcome]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Make alerts smarter"
Issues: Vague, no acceptance criteria, not testable
Improved: "Given a user views an alert, When the alert confidence score is <0.3, Then the alert is automatically dismissed and logged to audit trail"
Rationale: Specific, testable, with clear acceptance criteria
```

### METRICS ENHANCEMENT

For each weak or missing success metric, specify:

#### [Metric Name] Success Metric Framework

**Metric Definition:**
[Precise definition of what you're measuring]

**Baseline:**
[Current state - what's the current value?]

**Target:**
[Aspirational goal - what do we want to achieve?]

**Threshold:**
[Minimum for success - what's the minimum acceptable value?]

**Measurement Plan:**
- Event/Metric: [What event or metric will you track?]
- Data Source: [Where will the data come from?]
- Collection Method: [How will it be captured?]
- Frequency: [How often will it be measured?]
- Dashboard: [Link or location of dashboard]

**Guardrails:**
[What metrics must NOT degrade?]

**Example:**
```
Alert Triage Time Success Metric Framework

Metric Definition:
Average time from alert creation to resolution decision (dismiss or escalate)

Baseline:
Current average: 30 minutes per alert

Target:
Reduce to 5 minutes per alert (83% reduction)

Threshold:
10 minutes (minimum improvement to consider success)

Measurement Plan:
- Event/Metric: alert_triage_time (time_to_resolution event)
- Data Source: Alert management system analytics
- Collection Method: Automated tracking via event IDs
- Frequency: Daily aggregation, weekly reporting
- Dashboard: Operations Dashboard > Alert Performance tab

Guardrails:
- Alert accuracy must not degrade (false positive rate must stay <20%)
- Critical alert detection rate must stay >95%
```

### TRACEABILITY ENHANCEMENT

For each missing link or evidence gap, specify:

#### Missing Link: [Link Type]

**What's Missing:**
[What link or evidence is missing?]

**Where to Find It:**
[Where should this link/evidence be?]

**How to Add:**
[Specific steps to add the link/evidence]

**Example:**
```
Missing Link: Opportunity Assessment

What's Missing:
No link to opportunity assessment document that informed this PRD

Where to Find It:
Should be in PRD header or "Traceability" section

How to Add:
Add link: "Informed by: [link to opportunity-assessment.md]"
Include key insights: "Key insight from opportunity assessment: [quote or summary]"
```

### SCOPE CLARITY ENHANCEMENT

For each unclear scope boundary, specify:

#### Scope Boundary: [Area]

**Current State:**
[What's currently unclear about scope?]

**Clarification Needed:**
[What needs to be clarified?]

**Improved Scope Statement:**
[Clear in/out statement]

**Example:**
```
Scope Boundary: Alert Filtering

Current State:
PRD mentions "alert filtering" but unclear what's included/excluded

Clarification Needed:
- What types of alerts are filtered?
- What filtering criteria are included?
- What's explicitly out of scope?

Improved Scope Statement:
IN SCOPE:
- ML-based confidence scoring for alerts
- Auto-dismiss for low-confidence alerts (<0.3)
- Audit log for dismissed alerts

OUT OF SCOPE (for this PRD):
- Manual alert filtering UI
- Alert routing to different teams
- Alert escalation workflows
```

### 4-WEEK IMPROVEMENT PLAN

#### Week 1: Problem & Metrics Clarity Sprint
**Focus:** Rewrite problem statements and define success metrics

**Activities:**
- Workshop to identify clear problem statements backed by evidence
- Define success metrics with baselines, targets, and thresholds
- Add user context (JTBD, user stories) where missing
- Validate problem statements with stakeholders

**Deliverable:** Revised problem statements and success metrics

**Success Criteria:** Each problem statement backed by evidence, all success metrics have baselines/targets

---

#### Week 2: Requirements & Traceability Enhancement
**Focus:** Add acceptance criteria and improve traceability

**Activities:**
- Add Given/When/Then acceptance criteria for all P0 requirements
- Link PRD to opportunity doc, JTBD, and validation results
- Document assumptions with confidence levels
- Add evidence supporting solution approach

**Deliverable:** PRD with clear requirements and traceability

**Success Criteria:** All P0 requirements have acceptance criteria, all discovery links added

---

#### Week 3: Scope & Feasibility Validation
**Focus:** Clarify scope boundaries and validate feasibility

**Activities:**
- Explicitly define in/out of scope with rationale
- Identify dependencies with owners and timelines
- Validate technical feasibility with engineering
- Document risks with mitigation plans

**Deliverable:** PRD with clear scope and validated feasibility

**Success Criteria:** Scope boundaries clear, dependencies identified, feasibility validated

---

#### Week 4: Stakeholder Alignment & Finalization
**Focus:** Get stakeholder alignment and finalize PRD

**Activities:**
- Present revised PRD to stakeholders (PM, Eng, Design, Ops)
- Gather feedback and incorporate changes
- Document open questions with owners
- Get final approvals and publish

**Deliverable:** Approved PRD ready for execution

**Success Criteria:** Stakeholder sign-off, open questions tracked, PRD published

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

- PRD Framework: `1-prd-framework.md` - Complete methodology
- PRD Template: `2-prd-template.md` - Fill-in-the-blanks template
- PRD JTBD Template: `3-prd-jtbd-template.md` - Jobs-to-Be-Done focused template
- Related Frameworks:
  - Strategy: `../../2.1-Strategy/README.md` (Strategic Foundations, OKR Framework)
  - Discovery: `../../2.2-Discovery/README.md` (Opportunity Assessment, Idea Validation, Jobs to Be Done)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
