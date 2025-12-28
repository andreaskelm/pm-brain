# Creating Opportunities from Customer Insights (Continuous Discovery Habits)

## Goal
Transform customer insights from interview snapshots into clear, evidence-based opportunities that represent unmet customer needs and can guide product development decisions.

> **Important:** Include **ALL** supporting customer stories and evidence for each opportunity. Don't limit to 2-3 examples - more evidence makes opportunities stronger.

## Before You Start: Braindump & Product Sense

**STOP. Don't just copy-paste this into AI. Think first.**

Before creating opportunities, take 10-15 minutes to braindump your thoughts:

**Braindumping prompts:**
- What opportunities do you think exist? Dump everything - don't structure yet.
- What customer needs feel real? What feels like noise?
- What does your product sense tell you? What feels like a real opportunity?
- What biases might affect your view? (Solution bias? Feature bias? Confirmation bias?)
- What would make you say "this is obviously not an opportunity"?

**Product sense exercise:**
- If you had to pick ONE opportunity to pursue, what would it be? Why?
- What would make you say "this opportunity is obviously worth pursuing"?
- What would make you say "this opportunity is obviously not worth it"?
- What does your gut tell you about the most promising opportunities?

**Then proceed** to create opportunities using the framework below.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `03-Research-Artifacts/3.1-User-Interviews/opportunities/`
- **Filename:** `opportunity-[brief-description]-[YYYY-MM-DD].md`

## Process

**IMPORTANT:** If you're using this with an AI assistant, your role is to help the user think, not to think for them.

**Step 0: Help User Braindump First**
- Ask the user to braindump their thoughts about opportunities (see "Before You Start" section above)
- Quiz them: "What opportunities do you think exist? What feels like a real opportunity?"
- Help them use their product sense: "What does your gut tell you? What feels worth pursuing?"
- Only after they've thought through it, proceed to create opportunities

1. **Review Interview Evidence:** Analyze multiple interview snapshots for patterns
2. **Identify Customer Need Patterns:** Look for recurring themes across different customers
3. **Frame as Opportunities:** Express patterns as "How might we..." statements
4. **Validate with Evidence:** Ensure each opportunity is backed by specific customer stories
5. **Assess Opportunity Size:** Estimate breadth and depth of customer impact
6. **Connect to Business Outcomes:** Link opportunities to measurable business results
7. **Document Opportunity:** Create structured opportunity document
8. **Share for Feedback:** Circulate with team for validation and prioritization

## Opportunity Identification Principles
**Strong opportunities have:**
- **Multiple customer evidence:** Supported by stories from 3+ different customers
- **Clear unmet need:** Specific problem customers are trying to solve
- **Current workarounds:** Customers are cobbling together solutions
- **Measurable impact:** Can connect to business metrics or customer success
- **Actionable scope:** Specific enough to generate targeted solutions

**Weak opportunities:**
- **Single source:** Only one customer mentioned this
- **Feature requests:** Customers asking for specific features vs. expressing needs
- **Edge cases:** Problems only affecting very specific, uncommon scenarios
- **Vague statements:** Too broad or abstract to act upon
- **Already solved:** Existing solutions adequately address the need

## Opportunity Validation Framework
Before documenting, ask:
- **Evidence:** What specific customer stories support this opportunity?
- **Frequency:** How many customers experience this need?
- **Intensity:** How painful is this problem for customers?
- **Workarounds:** What are customers doing today to solve this?
- **Business Impact:** How does solving this connect to business outcomes?

## Opportunity Document Template
```markdown
# Opportunity: [Clear, customer-focused title]

## Opportunity Statement
**How might we** [specific customer need or desired outcome] **so that** [customer value/benefit]?

## Customer Evidence

### Supporting Stories
**Customer A:** [Brief story showing this need]
**Customer B:** [Different customer, same underlying need]
**Customer C:** [Third example with additional context]
**Customer D:** [Additional example]
*[Include ALL stories that support this opportunity - don't limit to 2-3]*

### Customer Quotes
> "[Direct quote illustrating the need]" - Customer A
> 
> "[Another quote showing impact]" - Customer B
> 
> "[Additional quote]" - Customer C
*[Include ALL relevant quotes - more evidence strengthens the opportunity]*

## Current State Analysis

### How Customers Solve This Today
- **Primary workaround:** [Most common current solution]
- **Alternative approaches:** [Other ways customers handle this]
- **Failure modes:** [When current solutions break down]

### Pain Points
- **Friction:** [Where current solutions create extra work]
- **Risk:** [What goes wrong with current approaches]
- **Inefficiency:** [Time/resource waste in current state]

### Success Indicators
- **When it works:** [Conditions where customers succeed today]
- **Positive outcomes:** [What good results look like]

## Opportunity Scope

### Customer Segments Affected
- **Primary:** [Main customer type experiencing this need]
- **Secondary:** [Other segments with similar but different needs]
- **Not affected:** [Who doesn't have this problem]

### Frequency & Context
- **How often:** [Daily/weekly/monthly/situational]
- **Trigger conditions:** [What circumstances create this need]
- **Seasonal/temporal patterns:** [Time-based variations]

## Business Impact Potential

### Customer Value
- **Time savings:** [Estimated efficiency gains]
- **Quality improvement:** [Better outcomes for customers]
- **Risk reduction:** [Problems prevented]
- **Satisfaction:** [Emotional/experience benefits]

### Business Metrics Connection
- **Revenue impact:** [How this could affect revenue]
- **Cost reduction:** [Operational efficiencies gained]
- **Customer retention:** [Impact on churn or satisfaction]
- **Competitive advantage:** [Market positioning benefits]

## Prioritization Factors

### Opportunity Size
- **Breadth:** How many customers are affected? [High/Medium/Low]
- **Depth:** How significant is the impact per customer? [High/Medium/Low]
- **Growth:** Is this need increasing over time? [Yes/No/Unknown]

### Strategic Alignment
- **Business objectives:** How does this support company goals?
- **Product strategy:** Alignment with product roadmap direction
- **Competitive positioning:** Impact on market differentiation

### Implementation Considerations
- **Technical complexity:** [Estimated difficulty]
- **Resource requirements:** [Team/time investment needed]
- **Dependencies:** [What else needs to happen first]

## Success Metrics
If we address this opportunity, we would expect to see:
- **Leading indicators:** [Early signals of progress]
- **Customer behavior changes:** [How usage patterns would shift]
- **Business metric improvements:** [Quantifiable business impact]

## Next Steps
- [ ] Validate opportunity sizing with additional customer research
- [ ] Generate multiple solution approaches
- [ ] Estimate implementation effort with technical team
- [ ] Prioritize against other opportunities

## Tags
#customer-need #[customer-segment] #[product-area] #[priority] #opportunity

## Related Documents
- **Interview snapshots:** [Links to supporting interviews]
- **Previous research:** [Related findings]
- **Solutions explored:** [Any solution brainstorming done]
```

## Quality Checklist
Before saving, verify:
- [ ] Backed by evidence from multiple customers - include **ALL** supporting stories (not just 3+)
- [ ] Framed as customer need, not solution
- [ ] Clear connection to business outcomes
- [ ] Specific enough to guide solution generation
- [ ] Current customer workarounds documented
- [ ] Success metrics identified
- [ ] All relevant customer evidence included - completeness is key