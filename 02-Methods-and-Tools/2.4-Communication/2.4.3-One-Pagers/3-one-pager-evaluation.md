# One-Pager Evaluation Framework

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-one-pager-framework.md`. This comprehensive evaluation framework is for peer review, quality gates, or deep learning.

## Usage Instructions

This framework provides a systematic approach to evaluate one-pagers against evidence-based, decision-driving methodology.

**When to use this comprehensive evaluation:**
- Peer review of coworkers' one-pagers
- Quality gates before sharing with executives
- Deep learning about what makes effective one-pagers
- After creation, when you want comprehensive feedback

**For creation-time checks:** Use the lightweight "Quick Quality Checks" in `1-one-pager-framework.md` (agent uses these automatically during creation).

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `ONE_PAGER_QUALITY_CHECK` for immediate flag assessment
2. Apply `ONE_PAGER_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `ONE_PAGER_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `ONE_PAGER_IMPROVEMENT_GENERATOR`

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

5. **Reference framework:** When suggesting improvements, reference specific sections from `1-one-pager-framework.md` for context.

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- What's your gut feeling about this one-pager? What feels right? What feels off?
- If you had to explain this one-pager to a skeptical executive in 2 minutes, what would you say?
- What would make you say "this one-pager is obviously wrong"?
- What would make you say "this one-pager is obviously right"?
- What does your product sense tell you about the ask? Is it clear what decision is needed?
- Does this one-pager feel like it will drive action? What action might it drive instead?
- Who is this really for? Does the one-pager make that clear?

**Bias Check:**
- What biases might be affecting your view? (Information overload? Unclear ask? Wrong audience?)
- Are you seeing what you want to see, or what's actually there?
- What would someone with different product sense say about this one-pager?

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising
- List what surprised you or confirmed your assumptions

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: ONE_PAGER_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ **Unclear ask** - Decision/action needed is not clear
❌ **Missing context** - Reader lacks context to understand the problem
❌ **Jargon-heavy** - Uses jargon or acronyms without defining them
❌ **No clear decision/action** - Doesn't specify what decision is needed or what action to take
❌ **Buries the lead** - Key information buried in middle or end
❌ **Missing data** - Claims not supported by numbers or evidence
❌ **Vague language** - Uses vague terms like "improve significantly" instead of specific numbers
❌ **Wrong audience** - Written for wrong audience or assumes too much prior knowledge

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ Clear ask/decision specified upfront
✅ Problem clearly stated with context
✅ Specific numbers and data support claims
✅ TL;DR/executive summary leads with punchline
✅ Decision/action is crystal clear
✅ Written for target audience (appropriate level of detail)
✅ Trade-offs and risks addressed
✅ Scannable format (headings, bullets, whitespace)

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

## STEP 2: ONE_PAGER_EVALUATOR_PROMPT

You are a one-pager expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
   - Ask: "Before we run the structured evaluation, what's your gut feeling about this one-pager? What feels right? What feels off?"
   - Ask: "If you had to explain this one-pager to a skeptical executive in 2 minutes, what would you say?"
   - Ask: "What would make you say 'this one-pager is obviously wrong'? What would make you say 'it's obviously right'?"
   - Ask: "What does your product sense tell you about the ask? Is it clear what decision is needed?"
   - Ask: "Does this one-pager feel like it will drive action? What action might it drive instead?"
   - Ask: "What biases might be affecting your view?" (Information overload? Unclear ask? Wrong audience?)

2) **THEN: Run Structured Evaluation**
   - After capturing their product sense, run the structured evaluation below
   - Compare the structured evaluation results to their initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Flag where there are discrepancies and explore why

3) **END: Reflection**
   - "How did your initial product sense compare to the structured evaluation?"
   - "What did the structured evaluation reveal that your gut didn't catch?"
   - "What did your gut catch that the structured evaluation validated?"
   - "How can you develop better product sense for one-pagers?"

Now evaluate provided one-pager using these 6 weighted criteria:

## Scoring Framework (1-10 scale)

### 1. CLARITY (Weight: 25%)

**Score 9-10:** One-pager is crystal clear. Can be understood in 3 minutes. No jargon without definitions. Easy to scan.

**Score 7-8:** Mostly clear with minor gaps in clarity or scannability.

**Score 4-6:** Some clarity but requires effort to understand or has jargon issues.

**Score 1-3:** Unclear, jargon-heavy, or difficult to understand.

**Examples:**
- ✅ Good: "Reduce alert triage time from 30min → 5min (83% reduction)"
- ❌ Poor: "Improve alert handling significantly"

---

### 2. DECISION-DRIVING (Weight: 25%)

**Score 9-10:** Clear ask/decision specified upfront. Reader knows exactly what decision is needed and what action to take.

**Score 7-8:** Good decision clarity with minor gaps in ask or action specification.

**Score 4-6:** Some decision clarity but ask is vague or buried.

**Score 1-3:** No clear ask or decision needed; unclear what action to take.

**Examples:**
- ✅ Good: "ASK: Approve $500K budget for Q2 to build ML-based alert prioritization"
- ❌ Poor: "We need to improve alerts"

---

### 3. STAKEHOLDER FOCUS (Weight: 20%)

**Score 9-10:** Written for target audience with appropriate level of detail. Assumes right amount of prior knowledge. Addresses stakeholder concerns.

**Score 7-8:** Good stakeholder focus with minor gaps in audience alignment.

**Score 4-6:** Some stakeholder focus but wrong level of detail or assumes too much/little knowledge.

**Score 1-3:** Wrong audience or inappropriate level of detail.

---

### 4. COMPLETENESS (Weight: 15%)

**Score 9-10:** All key sections present (problem, solution, why now, impact, approach, trade-offs, ask). Nothing critical missing.

**Score 7-8:** Good completeness with minor gaps in sections or details.

**Score 4-6:** Some sections missing or incomplete.

**Score 1-3:** Missing critical sections or incomplete.

---

### 5. DATA & EVIDENCE (Weight: 10%)

**Score 9-10:** Claims supported by specific numbers and data. No vague language. Evidence clearly presented.

**Score 7-8:** Good data support with minor gaps in specificity or evidence.

**Score 4-6:** Some data but vague language or missing evidence.

**Score 1-3:** No data or evidence; purely qualitative or vague.

---

### 6. ACCESSIBILITY (Weight: 5%)

**Score 9-10:** Highly scannable (headings, bullets, whitespace). Visual hierarchy clear. Can be read quickly.

**Score 7-8:** Good accessibility with minor gaps in formatting or scannability.

**Score 4-6:** Some accessibility but formatting issues or hard to scan.

**Score 1-3:** Poor formatting, hard to scan, or dense text.

---

## Scoring Calculation

### Step 1: Calculate Raw Score
```
Raw Score = (Clarity × 0.25) + 
            (Decision_Driving × 0.25) + 
            (Stakeholder_Focus × 0.20) + 
            (Completeness × 0.15) + 
            (Data_Evidence × 0.10) + 
            (Accessibility × 0.05)
```

### Step 2: Apply Quality Multiplier
```
Final Score = Raw Score × Quality Multiplier
```

### Step 3: Determine Rating
- 8.0-10.0: Excellent (ready to share)
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
- **Evidence:** [Specific quote or example from the one-pager]
- **Improvement:** [One concrete, actionable suggestion]

### ONE-PAGER QUALITY ASSESSMENT

**Decision Readiness: X/10**
[How ready is this one-pager to drive a decision?]

**Stakeholder Alignment: X/10**
[How well does this one-pager align with stakeholder needs?]

**Actionability: X/10**
[How actionable is this one-pager? Will it drive the intended action?]

### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

## STEP 3: ONE_PAGER_ANTIPATTERN_DETECTOR

Scan for these common one-pager mistakes and note specific instances:

### CLARITY ANTIPATTERNS

❌ **Unclear ask**
- Decision/action needed is not clear
- Impact: -2.0 from Decision-Driving (critical)

❌ **Missing context**
- Reader lacks context to understand the problem
- Impact: -1.5 from Completeness (critical)

❌ **Jargon-heavy**
- Uses jargon or acronyms without defining them
- Impact: -1.5 from Clarity (critical)

❌ **Buries the lead**
- Key information buried in middle or end
- Impact: -1.0 from Clarity

### DECISION ANTIPATTERNS

❌ **No clear decision/action**
- Doesn't specify what decision is needed or what action to take
- Impact: -2.0 from Decision-Driving (critical)

❌ **Vague ask**
- Ask is present but vague or unclear
- Impact: -1.5 from Decision-Driving (critical)

❌ **Multiple asks**
- Too many decisions/asks (dilutes focus)
- Impact: -1.0 from Decision-Driving

### STAKEHOLDER ANTIPATTERNS

❌ **Wrong audience**
- Written for wrong audience or assumes too much prior knowledge
- Impact: -1.5 from Stakeholder Focus (critical)

❌ **Assumes prior knowledge**
- Assumes reader knows context they don't
- Impact: -1.0 from Stakeholder Focus

❌ **Too much detail**
- Includes unnecessary detail for target audience
- Impact: -0.5 from Stakeholder Focus

### DATA ANTIPATTERNS

❌ **Missing data**
- Claims not supported by numbers or evidence
- Impact: -1.5 from Data & Evidence (critical)

❌ **Vague language**
- Uses vague terms like "improve significantly" instead of specific numbers
- Impact: -1.0 from Data & Evidence

❌ **No evidence**
- Purely qualitative with no supporting data
- Impact: -1.0 from Data & Evidence

### COMPLETENESS ANTIPATTERNS

❌ **Missing problem statement**
- Problem not clearly stated
- Impact: -1.5 from Completeness (critical)

❌ **Missing trade-offs**
- Trade-offs and risks not addressed
- Impact: -1.0 from Completeness

❌ **Missing why now**
- Timing/urgency not explained
- Impact: -0.5 from Completeness

### ACCESSIBILITY ANTIPATTERNS

❌ **Poor formatting**
- Hard to scan, dense text, no visual hierarchy
- Impact: -1.0 from Accessibility

❌ **Too long**
- Longer than necessary (should be concise)
- Impact: -0.5 from Accessibility

## Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- Clarity Issues: [count] ([list])
- Decision Issues: [count] ([list])
- Stakeholder Issues: [count] ([list])
- Data Issues: [count] ([list])
- Completeness Issues: [count] ([list])
- Accessibility Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: ONE_PAGER_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### Ask/Decision Transformation Template

```
Current: [Original ask or lack thereof]
Issues: [What's wrong with it]
Improved: "ASK: [Specific decision/action needed] by [deadline]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "We need to improve alerts"
Issues: Vague, no clear decision, no deadline
Improved: "ASK: Approve $500K budget for Q2 to build ML-based alert prioritization. Decision needed by March 15."
Rationale: Specific ask (budget approval), clear decision (yes/no), deadline for decision
```

#### Problem Statement Transformation Template

```
Current: [Original problem statement or lack thereof]
Issues: [What's wrong with it]
Improved: "[Clear problem statement with context and data]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "Alerts are a problem"
Issues: No context, no data, too vague
Improved: "Operations teams waste 30 min/day manually triaging alerts; 80% are false positives. Survey of 50 teams shows 70% spend >20 min/day on triage."
Rationale: Specific problem (time waste, false positives), context (operations teams), data (survey results)
```

#### TL;DR Transformation Template

```
Current: [Original TL;DR or lack thereof]
Issues: [What's wrong with it]
Improved: "[2-3 sentence TL;DR that leads with punchline]"
Rationale: [Why this is better]
```

**Example:**
```
Current: "This one-pager discusses alert improvements"
Issues: Doesn't lead with punchline, vague, no decision
Improved: "We propose building ML-based alert prioritization to reduce triage time by 83% (30min → 5min). ASK: Approve $500K budget for Q2. Decision needed by March 15."
Rationale: Leads with punchline (proposal + impact), includes ask upfront, deadline specified
```

### ASK ENHANCEMENT

For each weak or missing ask, specify:

#### [One-Pager Type] Ask Framework

**Current Ask:**
[What's currently the ask or lack thereof?]

**Issues:**
[What's wrong with it?]

**Improved Ask:**
[Specific decision/action needed]

**Decision Needed:**
[What specific decision is needed?]

**Deadline:**
[When is the decision needed?]

**Context:**
[Why is this decision needed now?]

**Example:**
```
Product One-Pager Ask Framework

Current Ask:
"We need to improve alerts"

Issues:
Vague, no clear decision, no deadline, no context

Improved Ask:
"Approve $500K budget for Q2 to build ML-based alert prioritization"

Decision Needed:
Yes/No on $500K budget approval for Q2

Deadline:
March 15 (2 weeks before Q2 planning)

Context:
- Q2 planning starts March 22
- Need budget approval before committing engineering resources
- Opportunity to reduce triage time by 83% (30min → 5min)
```

### CLARITY ENHANCEMENT

For each unclear section, specify:

#### [Section Name] Clarity Framework

**Current State:**
[What's currently unclear?]

**Issues:**
[What's wrong with it?]

**Improved Version:**
[Clear, specific version]

**Rationale:**
[Why this is clearer]

**Example:**
```
Impact Section Clarity Framework

Current State:
"This will improve alert handling significantly"

Issues:
Vague ("significantly"), no specific numbers, no baseline

Improved Version:
"Reduce alert triage time from 30min → 5min (83% reduction). Save 2.5 hours/week per team member. Enable teams to focus on high-value alerts."

Rationale:
Specific numbers (30min → 5min), percentage (83%), time savings quantified, outcome clear
```

### STAKEHOLDER ALIGNMENT ENHANCEMENT

For each stakeholder misalignment, specify:

#### [Stakeholder Type] Alignment Framework

**Current State:**
[What's currently misaligned?]

**Issues:**
[What's wrong with it?]

**Improved Version:**
[Stakeholder-aligned version]

**Rationale:**
[Why this is better aligned]

**Example:**
```
Executive Alignment Framework

Current State:
"Technical details about ML model architecture..."

Issues:
Too technical for executives, wrong level of detail

Improved Version:
"ML-based scoring automatically prioritizes alerts by confidence. High-confidence alerts (<0.3) auto-dismissed. Expected impact: 83% reduction in triage time."

Rationale:
High-level explanation (not technical details), focuses on business impact, appropriate for executives
```

### 4-WEEK IMPROVEMENT PLAN

#### Week 1: Clarity & Ask Sprint
**Focus:** Clarify ask and improve overall clarity

**Activities:**
- Workshop to refine ask/decision
- Rewrite TL;DR to lead with punchline
- Remove jargon and define acronyms
- Ensure problem statement is clear

**Deliverable:** Clear ask and improved clarity

**Success Criteria:** Ask is specific with deadline, TL;DR leads with punchline, no jargon

---

#### Week 2: Stakeholder Focus & Completeness
**Focus:** Align with target audience and ensure completeness

**Activities:**
- Identify target audience and adjust level of detail
- Ensure all key sections present (problem, solution, why now, impact, approach, trade-offs, ask)
- Add missing context where needed
- Address stakeholder concerns

**Deliverable:** Stakeholder-aligned and complete one-pager

**Success Criteria:** Written for target audience, all key sections present

---

#### Week 3: Data & Evidence Enhancement
**Focus:** Add specific numbers and evidence

**Activities:**
- Replace vague language with specific numbers
- Add data to support claims
- Include baselines and targets
- Add evidence from research or analysis

**Deliverable:** Data-supported one-pager

**Success Criteria:** All claims supported by specific numbers, no vague language

---

#### Week 4: Accessibility & Finalization
**Focus:** Improve formatting and finalize

**Activities:**
- Improve formatting (headings, bullets, whitespace)
- Ensure visual hierarchy is clear
- Make it scannable (can be read in 3 minutes)
- Peer review and incorporate feedback

**Deliverable:** Finalized, accessible one-pager ready to share

**Success Criteria:** Highly scannable, clear visual hierarchy, ready to share

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

- One-Pager Framework: `1-one-pager-framework.md` - Complete methodology
- One-Pager Templates: `2-one-pager-templates.md` - Ready-to-use templates
- Related Frameworks:
  - Meeting Agendas: `../2.4.2-Meeting-Agendas/README.md`
  - Stakeholder Management: `../2.4.7-Stakeholder-Management/README.md`
  - Newsletter: `../2.4.1-Newsletter/README.md`
  - Strategy: `../../2.1-Strategy/README.md` (Strategic Foundations)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)
