# [Framework Name] Evaluation Framework

> **Template Instructions:** Replace `[Framework Name]` with your actual framework name. Fill in all `[placeholders]` with relevant content. Remove this instruction block when done.

> **Before running structured evaluation:** Senior PMs are often busy, but it's critical to first tap into your product sense and gut feeling. Use your intuition to identify what feels right or wrong, then use the structured framework to validate and deepen your insights.

## Usage Instructions

This framework provides a systematic approach to evaluate [framework outputs - e.g., "OKRs", "roadmaps", "PRDs"] against evidence-based methodology.

**Evaluation Process:**
0. **Product Sense & Gut Check** (Do this first! 5-10 minutes)
1. Run `[FRAMEWORK]_QUALITY_CHECK` for immediate flag assessment
2. Apply `[FRAMEWORK]_EVALUATOR_PROMPT` for comprehensive scoring
3. Use `[FRAMEWORK]_ANTIPATTERN_DETECTOR` for specific methodology issues
4. Generate improvements with `[FRAMEWORK]_IMPROVEMENT_GENERATOR`

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

Before running the structured evaluation, take 5-10 minutes to review with your product sense:

**Product Sense Questions:**
- [Question 1 - e.g., "What's your gut feeling about this [output]? What feels right? What feels off?"]
- [Question 2 - e.g., "If you had to explain this to a skeptical executive in 2 minutes, what would you say?"]
- [Question 3 - e.g., "What would make you say 'this is obviously wrong'?"]
- [Question 4 - e.g., "What would make you say 'this is obviously right'?"]
- [Question 5 - e.g., "What does your product sense tell you about [key aspect]? Do they feel meaningful?"]

**Bias Check:**
- [Bias check 1 - e.g., "What biases might be affecting your view? (Activity bias? Vanity metrics? Output vs. outcome?)"]
- [Bias check 2 - e.g., "Are you seeing what you want to see, or what's actually there?"]
- [Bias check 3 - e.g., "What would someone with different product sense say?"]

**Capture Your Initial Thoughts:**
- Write down your gut reactions before running the structured evaluation
- Note what feels strong vs. weak
- Identify any red flags your intuition is raising
- List what surprised you or confirmed your assumptions

**Then proceed to structured evaluation** to validate, deepen, and quantify your initial product sense.

---

## STEP 1: [FRAMEWORK]_QUALITY_CHECK

Scan for these flags before detailed evaluation:

### RED FLAGS (each counts as -1 multiplier point)

❌ **[Red flag 1]** - [Description of what this looks like]
❌ **[Red flag 2]** - [Description]
❌ **[Red flag 3]** - [Description]
❌ **[Red flag 4]** - [Description]
❌ **[Red flag 5]** - [Description]

**Example red flags:**
- ❌ [Example 1]
- ❌ [Example 2]

### GREEN FLAGS (each counts as +0.5 multiplier point, max +2)

✅ **[Green flag 1]** - [Description of what this looks like]
✅ **[Green flag 2]** - [Description]
✅ **[Green flag 3]** - [Description]
✅ **[Green flag 4]** - [Description]

**Example green flags:**
- ✅ [Example 1]
- ✅ [Example 2]

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

## STEP 2: [FRAMEWORK]_EVALUATOR_PROMPT

You are a [framework] expert conducting a peer review. **Your role is to help the user think, not to think for them.**

**IMPORTANT:** Before running the structured evaluation, first help the user tap into their product sense:

1) **FIRST: Product Sense & Gut Check**
   - Ask: "Before we run the structured evaluation, what's your gut feeling about this [output]? What feels right? What feels off?"
   - Ask: "If you had to explain this to a skeptical executive in 2 minutes, what would you say?"
   - Ask: "What would make you say 'this is obviously wrong'? What would make you say 'it's obviously right'?"
   - Ask: "What does your product sense tell you about [key aspect]? Do they feel meaningful?"
   - Ask: "What biases might be affecting your view?" ([specific biases relevant to framework])

2) **THEN: Run Structured Evaluation**
   - After capturing their product sense, run the structured evaluation below
   - Compare the structured evaluation results to their initial gut feeling
   - Highlight where product sense aligned with structured evaluation
   - Flag where there are discrepancies and explore why

3) **END: Reflection**
   - "How did your initial product sense compare to the structured evaluation?"
   - "What did the structured evaluation reveal that your gut didn't catch?"
   - "What did your gut catch that the structured evaluation validated?"
   - "How can you develop better product sense for [framework outputs]?"

Now evaluate provided [framework outputs] using these [N] weighted criteria:

### Scoring Framework (1-10 scale)

### 1. [CRITERION 1] (Weight: X%)

**Score 9-10:** [Excellent description - what this looks like at the highest level]

**Score 7-8:** [Good description - what this looks like at a good level]

**Score 4-6:** [Fair description - what this looks like at an acceptable level]

**Score 1-3:** [Poor description - what this looks like when it's failing]

**Examples:**
- ✅ **Good:** [Example of good criterion]
- ❌ **Poor:** [Example of poor criterion]

**How to assess:**
- [Guidance on how to evaluate this criterion]
- [What to look for]
- [Common indicators]

### 2. [CRITERION 2] (Weight: X%)

[Similar structure to Criterion 1]

### 3. [CRITERION 3] (Weight: X%)

[Similar structure]

[Continue with additional criteria - typically 4-6 criteria total]

### Scoring Calculation

**Step 1: Calculate Raw Score**
```
Raw Score = (Criterion_1 × Weight_1) + 
            (Criterion_2 × Weight_2) + 
            (Criterion_3 × Weight_3) + 
            ...
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

### Output Format

#### EXECUTIVE SUMMARY
- **Final Score:** [Score]/10 ([Rating])
- **Raw Score:** [Score]/10
- **Quality Multiplier:** [Multiplier]× (Red flags: [count], Green flags: [count])
- **Primary Strengths:** [2-3 key strengths]
- **Critical Issues:** [2-3 main problems]

#### DETAILED SCORES

For each criterion provide:

**[Criterion Name] Score: X/10 (Weight: X%)**
- **Justification:** [2-3 sentences explaining the score]
- **Evidence:** [Specific quote or example from the [output]]
- **Improvement:** [One concrete, actionable suggestion]

#### [FRAMEWORK] QUALITY ASSESSMENT

**[Aspect 1]: X/10**
[How well does this [output] demonstrate [aspect]?]

**[Aspect 2]: X/10**
[How well does this [output] demonstrate [aspect]?]

#### TOP 3 IMPROVEMENTS
1. **[Most impactful change]** - [Why this matters and expected impact]
2. **[Second priority]** - [Why this matters and expected impact]
3. **[Third priority]** - [Why this matters and expected impact]

---

## STEP 3: [FRAMEWORK]_ANTIPATTERN_DETECTOR

Scan for these common [framework] mistakes and note specific instances:

### [CATEGORY 1] ANTIPATTERNS

❌ **[Antipattern Name]**
- [Description of what this looks like]
- **Impact:** [Scoring impact - e.g., "-2.0 from [Criterion] (critical)"]
- **Example:** [Concrete example]

❌ **[Antipattern Name]**
- [Description]
- **Impact:** [Scoring impact]
- **Example:** [Example]

### [CATEGORY 2] ANTIPATTERNS

❌ **[Antipattern Name]**
- [Description]
- **Impact:** [Scoring impact]
- **Example:** [Example]

[Continue with additional categories as needed]

### Antipattern Summary Format

**Total Antipatterns Found: [count]**

By Category:
- [Category 1] Issues: [count] ([list])
- [Category 2] Issues: [count] ([list])
- [Category 3] Issues: [count] ([list])

**Severity Assessment:**
- Critical (>5 antipatterns): Fundamental methodology failure
- High (3-5 antipatterns): Major rewrite required
- Medium (1-2 antipatterns): Targeted improvements needed
- Low (0 antipatterns): Minor refinements only

---

## STEP 4: [FRAMEWORK]_IMPROVEMENT_GENERATOR

Based on evaluation results, provide actionable improvements:

### REWRITE EXAMPLES

#### [Component Type] Transformation Template

```
Current: [Original text]
Issues: [What's wrong with it]
Improved: "[Improved version]"
Rationale: [Why this is better]
```

**Example:**
```
Current: [Example of poor component]
Issues: [What's wrong]
Improved: [Example of improved component]
Rationale: [Why improvement is better]
```

### MEASUREMENT PLAN

For each weak or unmeasured [component], specify:

#### [Component Name] Measurement Framework

**Definition:**
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

### STRATEGIC CONNECTIVITY

Demonstrate how [output] connects to broader strategy:

#### Company/BU Goals Connection
**Goal:** [Specific company objective]
**How This [Output] Supports It:** [Clear explanation of linkage]

#### [Related Framework] Connection
**[Related Framework Element]:** [Description]
**Problem Being Solved:** [Specific pain point]
**Expected Impact:** [How solving this creates value]

### [N]-WEEK IMPROVEMENT PLAN

#### Week 1: [Focus Area] Sprint
**Focus:** [What to improve this week]

**Activities:**
- [Activity 1]
- [Activity 2]
- [Activity 3]

**Deliverable:** [What you'll have after this week]

**Success Criteria:** [How you'll know you succeeded]

---

#### Week 2: [Focus Area]
[Similar structure to Week 1]

[Continue with additional weeks as needed - typically 2-4 weeks]

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

- **Framework:** `1-[framework-name]-framework.md` - Complete methodology
- **Template:** `2-[framework-name]-template.md` - Fill-in-the-blanks template
- **Related Frameworks:**
  - [Related Framework 1]: `[path]`
  - [Related Framework 2]: `[path]`
- **Foundations:** `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

---

## Template Notes

**When to use Evaluation Framework:**
- Framework needs quality gates
- Peer review is required
- Improvement tracking is needed
- Objective assessment adds value

**Pros of Evaluation Framework:**
- ✅ Objective assessment
- ✅ Reduces bias
- ✅ Enables comparison over time
- ✅ Provides actionable improvements

**Cons of Evaluation Framework:**
- ❌ Can feel mechanical
- ❌ Requires calibration
- ❌ May miss nuance

See `1-template-structure-guide.md` for more details on template customization.
