# Generating Solutions for Customer Opportunities (Continuous Discovery Habits)

## Goal
Generate multiple, diverse solution concepts for validated customer opportunities, ensuring solutions address underlying needs rather than symptoms, and can be tested with minimal investment.

## Before You Start: Braindump & Product Sense

**STOP. Don't just copy-paste this into AI. Think first.**

Before generating solutions, take 10-15 minutes to braindump your thoughts:

**Braindumping prompts:**
- What solutions come to mind? Dump everything - don't judge yet.
- What does your product sense tell you? What feels like the right approach?
- What biases might affect your thinking? (Solution bias? Feature bias? Status quo bias?)
- What would make you say "this solution is obviously wrong"?
- What would make you say "this solution is obviously right"?

**Product sense exercise:**
- If you had to solve this in 1 week with no budget, what would you do?
- What's the smallest thing that could work?
- What would great product sense notice about this opportunity?
- What does your gut tell you about the best solution approach?

**Then proceed** to generate solutions using the framework below.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `03-Research-Artifacts/3.1-User-Interviews/solutions/`
- **Filename:** `solutions-[opportunity-name]-[YYYY-MM-DD].md`

## Process

**IMPORTANT:** If you're using this with an AI assistant, your role is to help the user think, not to think for them.

**Step 0: Help User Braindump First**
- Ask the user to braindump their thoughts about solutions (see "Before You Start" section above)
- Quiz them: "What solutions come to mind? What feels like the right approach?"
- Help them use their product sense: "What does your gut tell you? What's the smallest thing that could work?"
- Only after they've thought through it, proceed to generate solutions

1. **Review Opportunity:** Deeply understand the customer need and context
2. **Divergent Brainstorming:** Generate many solution ideas without judgment
3. **Solution Categorization:** Group similar concepts and identify themes
4. **Convergent Selection:** Choose 3-5 most promising concepts for development
5. **Detail Selected Solutions:** Flesh out chosen concepts with specifics
6. **Identify Assumptions:** List key assumptions underlying each solution
7. **Design Quick Tests:** Plan how to validate solutions with minimal effort
8. **Document Solution Set:** Create comprehensive solution documentation

## Solution Generation Principles

### Divergent Phase (Quantity over Quality)
- **Generate 15-20+ initial ideas:** Push beyond obvious solutions
- **No criticism allowed:** Capture all ideas, even seemingly bad ones
- **Build on others' ideas:** Use "Yes, and..." thinking
- **Think across solution types:** Digital, process, service, integration, etc.
- **Consider different interaction models:** Self-service, assisted, automated, hybrid

### Solution Categories to Explore
- **Digital solutions:** Apps, websites, dashboards, tools
- **Process improvements:** Workflow changes, new procedures
- **Service enhancements:** Human-assisted solutions, support changes
- **Integration approaches:** Connecting existing systems/tools
- **Education/training:** Helping customers solve problems themselves
- **Automation:** Removing manual steps from customer workflows

### Convergent Phase (Quality and Feasibility)
- **Customer value first:** Does this truly solve the customer need?
- **Feasibility second:** Can we realistically build/deliver this?
- **Differentiation third:** How does this compare to existing solutions?

## Solution Document Template
```markdown
# Solutions for: [Opportunity Title]

## Opportunity Recap
**Need Statement:** [Brief restatement of customer opportunity]
**Evidence:** [Key supporting stories/data]
**Success Criteria:** [How we'll know if solutions work]

## Solution Generation Process
**Date:** [When brainstorming occurred]
**Participants:** [Who was involved]
**Method:** [Brainstorming technique used]

## All Ideas Generated
*[Include full list of initial ideas, even ones not selected]*
1. [Idea 1]
2. [Idea 2]
3. [Idea 3]
...

## Selected Solution Concepts

### Solution 1: [Descriptive Name]

#### Concept Overview
**Core Idea:** [One-sentence description]
**Customer Experience:** [How customer would interact with this solution]
**Value Proposition:** [Why this solves the customer need]

#### Detailed Description
**How it works:**
- [Step 1 of customer experience]
- [Step 2 of customer experience]
- [Step 3 of customer experience]

**Key Features:**
- [Essential capability 1]
- [Essential capability 2]
- [Essential capability 3]

#### Implementation Approach
**Build vs. Buy vs. Partner:**
- [Assessment of development approach]

**Technical Requirements:**
- [Key technical needs/constraints]
- [Integration requirements]
- [Performance/scale considerations]

**Resource Needs:**
- [Team composition required]
- [Estimated timeline]
- [Budget considerations]

#### Key Assumptions
- **Customer Behavior:** [Assumptions about how customers will use this]
- **Technical:** [Assumptions about feasibility/performance]
- **Business:** [Assumptions about market/business model]
- **Adoption:** [Assumptions about customer acceptance]

#### Testable Hypotheses
- [Assumption 1] → Test: [How to validate this assumption]
- [Assumption 2] → Test: [How to validate this assumption]
- [Assumption 3] → Test: [How to validate this assumption]

#### Success Metrics
- **Customer behavior:** [How usage would change]
- **Business impact:** [Expected business results]
- **Leading indicators:** [Early signals of success]

---

### Solution 2: [Descriptive Name]
*[Same structure as Solution 1]*

---

### Solution 3: [Descriptive Name]
*[Same structure as Solution 1]*

## Solution Comparison

| Criterion | Solution 1 | Solution 2 | Solution 3 |
|-----------|------------|------------|------------|
| **Customer Value** | [High/Med/Low + reasoning] | [High/Med/Low + reasoning] | [High/Med/Low + reasoning] |
| **Technical Feasibility** | [High/Med/Low + reasoning] | [High/Med/Low + reasoning] | [High/Med/Low + reasoning] |
| **Implementation Speed** | [Fast/Med/Slow + timeline] | [Fast/Med/Slow + timeline] | [Fast/Med/Slow + timeline] |
| **Resource Requirements** | [Low/Med/High + details] | [Low/Med/High + details] | [Low/Med/High + details] |
| **Risk Level** | [Low/Med/High + risks] | [Low/Med/High + risks] | [Low/Med/High + risks] |
| **Competitive Advantage** | [Low/Med/High + reasoning] | [Low/Med/High + reasoning] | [Low/Med/High + reasoning] |

## Testing Strategy

### Recommended Testing Order
1. **[Solution name]** - [Reasoning for testing first]
2. **[Solution name]** - [Reasoning for testing second]
3. **[Solution name]** - [Reasoning for testing third]

### Quick Test Plans

#### Solution 1 Tests
**Test 1: [Assumption being tested]**
- **Method:** [How to test - interview, prototype, survey, etc.]
- **Success criteria:** [What results would validate the assumption]
- **Timeline:** [How long this test takes]
- **Resources needed:** [What's required to run this test]

**Test 2: [Another assumption]**
- **Method:** [Testing approach]
- **Success criteria:** [Validation criteria]
- **Timeline:** [Duration]
- **Resources needed:** [Requirements]

## Next Steps
- [ ] Review solutions with technical team for feasibility assessment
- [ ] Create lo-fi prototypes for top 2 solutions
- [ ] Design and run assumption tests
- [ ] Schedule customer validation sessions
- [ ] Update opportunity document with solution learning

## Decision Framework
**When to build:** [Criteria for moving forward with development]
**When to iterate:** [Criteria for refining the solution]
**When to pivot:** [Criteria for trying a different solution]
**When to park:** [Criteria for deprioritizing this opportunity]

## Tags
#solutions #[opportunity-theme] #[customer-segment] #[product-area]

## Related Documents
- **Opportunity:** [Link to opportunity document]
- **Interview snapshots:** [Supporting customer evidence]
- **Test results:** [Link to assumption test results when available]
```

## Solution Quality Checklist
Before saving, verify:
- [ ] Multiple diverse solution approaches generated
- [ ] Solutions address customer need, not just symptoms
- [ ] Key assumptions clearly identified
- [ ] Test plans designed for riskiest assumptions
- [ ] Implementation feasibility considered
- [ ] Success metrics defined for each solution
```
