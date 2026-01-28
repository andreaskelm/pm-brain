# User Story Creation Framework

**What it is:** Structured method for writing user stories that capture user needs and define acceptance criteria

## Overview
User stories translate customer needs into actionable development work. A well-written story captures WHO, WHAT, and WHY in a format that guides development and testing.

## Step 0: Braindump & Product Sense (Do this first!)
**Before writing stories, braindump:**
- What problem are we solving? For whom?
- What does your product sense tell you about this feature?
- Are we solving the right problem or just adding features?

**Product sense exercise:**
- If this story takes 2 weeks to build, will it create 2 weeks' worth of value?
- What would make you say "this story is obviously wrong"?

## When to Use
- Breaking down features into development tasks
- Communicating requirements to engineering
- Planning sprints and estimating work
- Creating shared understanding of what to build

## How to Write User Stories

### The Standard Format
As a [user type],
I want [action/feature],
So that [benefit/outcome]
### Step-by-Step Process

**1. Identify the User**
- Not just "user" - be specific
- Example: "busy parent", "new subscriber", "power user"
- Consider different user types with different needs

**2. Define the Action**
- What does the user want to do?
- Keep it focused (one story = one action)
- Use active verbs

**3. Explain the Benefit**
- Why does the user want this?
- What outcome does it enable?
- Connect to user job or goal

**4. Add Acceptance Criteria**
- Define "done" clearly
- Usually 3-5 criteria
- Should be testable

**5. Include Context (optional)**
- Background information
- Dependencies
- Design/technical notes

## Template
```markdown
## Story: [Brief title]

**As a** [specific user type],
**I want** [specific action],
**So that** [specific benefit/outcome]

### Acceptance Criteria
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

### Context
- Background: [Why now? Related work?]
- Design: [Link to designs/mockups]
- Dependencies: [What needs to happen first?]

### Out of Scope
- [What we're explicitly NOT doing]

### Definition of Done
- [ ] Code complete and reviewed
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Acceptance criteria met
```

## Examples

### Bad Examples

❌ **Too vague:**
As a user,
I want better search,
So that I can find things
*Problems: Who is "user"? What's "better"? What "things"?*

❌ **No benefit:**
As a user,
I want a blue button,
So that there's a blue button
*Problem: No actual user benefit*

❌ **Too technical:**
As a user,
I want the API to return JSON,
So that the database is normalized
*Problem: Technical implementation, not user need*

### Good Examples

✅ **Well-written:**
As a busy parent,
I want to save recipes I find while browsing,
So that I can quickly access them when planning meals later
Acceptance Criteria:

 Given I'm viewing a recipe, when I click "Save", then it's added to My Recipes
 Given I've saved a recipe, when I visit My Recipes, then I see it in the list
 Given I'm viewing a saved recipe, when I click "Remove", then it's removed from My Recipes
 ✅ **Complex feature:**
 As a new subscriber,
I want guided onboarding that learns my preferences,
So that I get relevant content recommendations from day one
Acceptance Criteria:

 Given I'm a new user, when I sign up, then I see onboarding flow
 Given I'm in onboarding, when I select preferences, then they're saved to my profile
 Given I complete onboarding, when I view home, then I see personalized recommendations
 Given I skip a step, when I continue, then I can complete it later from settings
 Context:

Users who complete onboarding have 3x higher retention (data link)
Design: [Figma link]
Dependencies: Recommendation engine must be deployed first

Out of Scope:

Social media sign-in (separate story)
Email preference settings (covered in settings story)

## Story Splitting Patterns

When stories are too large (>5 days), split them:

### Pattern 1: By User Type
**Original:** "As a user, I want to edit my profile"
**Split:**
- "As a free user, I want to edit basic profile info"
- "As a premium user, I want to edit advanced profile settings"

### Pattern 2: By Workflow Step
**Original:** "As a user, I want to checkout"
**Split:**
- "As a user, I want to add items to cart"
- "As a user, I want to enter shipping info"
- "As a user, I want to complete payment"

### Pattern 3: By Happy Path vs. Edge Cases
**Original:** "As a user, I want to upload photos"
**Split:**
- "As a user, I want to upload photos (happy path)"
- "As a user, I want error handling for invalid files"

### Pattern 4: By CRUD Operations
**Original:** "As a user, I want to manage bookmarks"
**Split:**
- "As a user, I want to create bookmarks"
- "As a user, I want to delete bookmarks"
- "As a user, I want to organize bookmarks"

## INVEST Criteria

Good stories follow INVEST:

| Criteria | Meaning | Example |
|----------|---------|---------|
| **Independent** | Can be developed separately | Not dependent on other unfinished stories |
| **Negotiable** | Details can be discussed | Not overly prescriptive about HOW |
| **Valuable** | Delivers user value | User can accomplish something |
| **Estimable** | Team can estimate size | Clear enough to estimate |
| **Small** | Can complete in one sprint | Usually 1-5 days of work |
| **Testable** | Can verify it's done | Clear acceptance criteria |

## Common Mistakes

**1. Feature, Not Story**
❌ "Implement new search algorithm"
✅ "As a user, I want relevant search results, so I can find what I'm looking for quickly"

**2. Too Technical**
❌ "As a developer, I want to refactor the codebase"
✅ "As a user, I want faster page loads, so I don't wait for content" (if that's the real benefit)

**3. Too Many Things**
❌ One story covering: search + filters + sorting + pagination
✅ Split into separate stories

**4. No Acceptance Criteria**
❌ Just the story, no criteria
✅ Always include clear, testable criteria

**5. UI Specifications, Not Needs**
❌ "As a user, I want a dropdown in the top right"
✅ "As a user, I want quick access to account settings"

## Checklist

Before calling a story "ready":
- [ ] Follows "As a/I want/So that" format
- [ ] Identifies specific user type
- [ ] Describes clear action
- [ ] Explains user benefit
- [ ] Has 3-5 acceptance criteria
- [ ] Passes INVEST criteria
- [ ] Can be completed in one sprint
- [ ] No technical jargon in user-facing parts
- [ ] Team understands and can estimate

## Further Reading
- Mike Cohn: "User Stories Applied"
- Jeff Patton: "User Story Mapping"
- Roman Pichler: "Agile Product Management with Scrum"

## References
- OKR Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md`
- PRD Framework: `../2.3.4-PRD/README.md`
- Jobs-to-be-Done: `../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md`
