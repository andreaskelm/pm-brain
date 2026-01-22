# Creating Interview Snapshots (Continuous Discovery Habits)

## Goal
Create structured snapshots that capture **ALL** specific customer stories, behaviors, and needs from qualitative interviews or user research sessions, following the Continuous Discovery Habits methodology.

**If using with AI:** The AI's role is to help you think and structure your thoughts, not to think for you. Always braindump first (see section below).

> **Important:** Capture **ALL** stories and insights from the interview, not just 2-3. Every story matters. The "2-3" in quality checklists refers to a minimum, not a limit.

## Before You Start: Braindump & Product Sense

**STOP. Don't just copy-paste this into AI. Think first.**

Before creating the interview snapshot, take 5-10 minutes to braindump your thoughts:

**Braindumping prompts:**
- What do you remember from this interview? Dump everything - don't structure yet.
- What stories stood out? What felt important?
- What surprised you? What confirmed your assumptions?
- What does your product sense tell you? What feels significant?
- What biases might affect how you interpret this? (Confirmation bias? Recency bias?)

**Product sense exercise:**
- If you had to explain this interview in 2 minutes, what would you say?
- What would make you say "this interview revealed something important"?
- What would make you say "this interview didn't reveal much"?
- What does your gut tell you about the key insights?

**Then proceed** to create the structured snapshot using the framework below.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `03-Research-Artifacts/3.1-User-Interviews/snapshots/`
- **Filename:** `snapshot-[participant-identifier]-[YYYY-MM-DD].md`

## Process

**IMPORTANT:** If you're using this with an AI assistant, your role is to help the user think, not to think for them.

**Step 0: Help User Braindump First**
- Ask the user to braindump their thoughts about the interview (see "Before You Start" section above)
- Quiz them: "What do you remember? What stood out? What surprised you?"
- Help them use their product sense: "What does your gut tell you? What feels important?"
- Only after they've thought through it, proceed to process the interview data

0. **Follow the rules:** Start by telling me your plan for approaching this task in a way that is optimized to uphold these guidelines above all, and eliminates any chance of violating them. Make sure it includes a final phase of verifying every single quote, and fixing any violations, repeating this until there are no violations. 

1. **Parse Interview Data:** Process transcript, notes, or session recordings
2. **Identify Session Type:** Categorize as discovery interview, usability test, feedback session, etc.
3. **Extract Customer Stories:** Focus on specific behavioral instances, not generalizations
4. **Map Customer Journey:** Document the participant's experience flow
5. **Identify Needs & Pain Points:** Extract underlying customer needs from stories
6. **Capture Behavioral Insights:** Note interesting patterns or unexpected behaviors
7. **Create Structured Snapshot:** Compile findings using standard template
8. **Tag for Retrieval:** Add relevant tags for future synthesis

## Story Extraction Principles
**DO capture:**
- **Specific instances:** "The last time I..." or "Yesterday when I..."
- **Actual behavior:** What they did step-by-step, in sequence
- **Contextual details:** Environment, timing, tools used, people involved
- **Emotional reactions:** Moments of frustration, delight, confusion, surprise
- **Current workarounds:** How they solve problems today with existing tools
- **Failed attempts:** What they've tried that didn't work and why

**AVOID capturing:**
- **Generalizations:** "I always..." "I never..." without specific examples
- **Hypothetical scenarios:** "I would probably..." or "If I could..."
- **Feature requests:** Unless you probe for the underlying need/problem
- **Opinions about competitors:** Focus on their actual experience, not comparisons
- **Wishful thinking:** What they think they want vs. what they actually do

## Interview Snapshot Template
```markdown
# Interview Snapshot: [Participant Role/ID] - [Date]

## Participant Context
- **Role/Position:** [Their job function or user type]
- **Experience Level:** [Novice/Intermediate/Expert in relevant domain]
- **Usage Context:** [How/when they use the product/service]
- **Interview Type:** [Discovery/Usability/Feedback/etc.]

## Key Stories Captured

### Story 1: [Brief descriptive title]
**Situation:** [Context and trigger]
**Actions:** [Step-by-step what they did]
**Outcome:** [What happened as a result]
**Emotion:** [How they felt about the experience]

### Story 2: [Brief descriptive title]
**Situation:** [Context and trigger]
**Actions:** [Step-by-step what they did]
**Outcome:** [What happened as a result]
**Emotion:** [How they felt about the experience]

## Customer Journey Moments
- **Trigger:** What initiated their process
- **Key Steps:** Major phases of their workflow
- **Decision Points:** Where they had to make choices
- **Pain Points:** Friction or frustration moments
- **Success Moments:** When things worked well

## Needs Identified
- **Explicit Needs:** What they directly said they needed
- **Implicit Needs:** Underlying needs inferred from their stories
- **Unmet Needs:** Problems they're solving with workarounds

## Behavioral Insights
- **Surprising Behaviors:** Actions that differed from expectations
- **Workaround Patterns:** How they adapt when primary solution fails
- **Mental Models:** How they think about the problem space
- **Success Patterns:** What conditions lead to positive outcomes

## Quotes & Evidence
> "[Exact quote that illustrates key insight]"
> 
> "[Another relevant quote with context]"

## Opportunities Suggested
- [Potential opportunity based on unmet needs]
- [Another opportunity from behavioral patterns]

## Follow-up Questions
- [Questions to explore in future interviews]
- [Assumptions to test based on this conversation]

## Tags
#[customer-segment] #[use-case] #[product-area] #[priority-level]
```

## Quality Checklist
Before saving, verify:
- [ ] **ALL** specific stories captured with full context (not just 2-3 - capture everything)
- [ ] Clear distinction between what they said vs. what they did
- [ ] Underlying needs identified, not just surface complaints
- [ ] Direct quotes captured to support insights
- [ ] Behavioral patterns noted, not just preferences
- [ ] Tagged appropriately for future synthesis
- [ ] No stories or insights left out - completeness is key
```