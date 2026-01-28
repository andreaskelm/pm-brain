# MoSCoW Prioritization Framework

## Overview

This framework helps product managers prioritize features, requirements, and initiatives using the MoSCoW method - a simple yet powerful categorization technique that brings clarity to complex prioritization decisions.

## Step 0: Braindump & Product Sense (Do this first!)

**Before using MoSCoW, braindump:**
- What features/initiatives are you considering? List everything - don't categorize yet.
- What does your product sense tell you? What truly makes or breaks this release?
- What assumptions are you making about must-haves? Are they actually must-haves?
- What biases might affect your categorization? (Stakeholder pressure? Latest customer complaint? Personal preferences?)
- What would great product sense look like here? What would an experienced PM absolutely insist on vs. be flexible about?

**Product sense exercise:**
- If you could ONLY ship 3 things, what would they be? Why?
- What would make you cancel this release entirely? (These are your true must-haves)
- What would be "nice to ship but we'd still succeed without"?
- What are you tempted to call a must-have that really isn't?

## Core Philosophy

### MoSCoW is About Strategic Trade-offs

MoSCoW prioritization helps teams determine what to focus on when resources are limited by categorizing work into four clear priorities: Must have, Should have, Could have, and Won't have (this time).

The method should:

- **Enable ruthless prioritization** - Not everything can be a must-have
- **Create built-in contingency** - Flexibility protects delivery commitments
- **Manage stakeholder expectations** - Clear communication prevents scope creep
- **Support time-boxed delivery** - Focus on what matters most within constraints

### The Critical Balance

No more than 60% effort for Must Have requirements on a project, and a sensible pool of Could Haves, usually around 20% effort. This creates the flexibility needed to deliver successfully.

**Recommended distribution:**
- Must Have: ≤60% of effort
- Should Have: ~20% of effort
- Could Have: ~20% of effort
- Won't Have: Excluded from timeframe calculations

## The Four Categories

### Must Have (Critical)

**Definition:** Requirements absolutely essential for project success. Without these, the project fails or has no value.

**Test question:** "If we don't deliver this, should we cancel the entire release?"

**Characteristics:**
- Legal/regulatory requirements
- Core functionality without which product is unusable
- Critical business objectives
- Non-negotiable stakeholder needs
- Features that define minimum viable product (MVP)

**Examples:**
- Login functionality for a banking app
- Payment processing for e-commerce
- Core API endpoints for platform integration
- GDPR compliance features
- Critical bug fixes blocking launch

### Should Have (Important)

**Definition:** Important requirements that add significant value but aren't critical. Project can succeed without them, though with workarounds.

**Test question:** "Would this absence hurt badly, but we could still launch with a reasonable workaround?"

**Characteristics:**
- Significantly improves user experience
- Important but not urgent
- Has workaround solutions available
- Reduces friction but doesn't block core value
- Valuable for competitive positioning

**Examples:**
- Advanced filtering in search
- Email notifications (when in-app notifications exist)
- Export to multiple formats (when one export format exists)
- Password reset via SMS (when email reset exists)
- Bulk edit operations

### Could Have (Nice-to-Have)

**Definition:** Desirable features with small impact if excluded. First to be deprioritized if capacity is constrained.

**Test question:** "Would users appreciate this, but hardly notice its absence?"

**Characteristics:**
- Minimal impact on outcome if omitted
- Enhances experience but not essential
- Easy to add in future release
- Low risk if delayed
- Often requested but not business-critical

**Examples:**
- Dark mode
- Custom themes
- Social sharing features
- Keyboard shortcuts
- Nice-to-have integrations

### Won't Have (Out of Scope)

**Definition:** Items explicitly excluded from current release. May be considered for future releases or dropped entirely.

**Test question:** "Is this a distraction from our core goals right now?"

**Characteristics:**
- Out of scope for current timeframe
- Low priority relative to other work
- Requires resources better spent elsewhere
- May be future consideration
- Helps prevent scope creep

**Examples:**
- Advanced AI features for MVP
- Mobile app when focusing on web
- Enterprise features for consumer launch
- Future platform integrations
- Experimental features needing more research

## When to Use MoSCoW

### MoSCoW Works Best For:

- **Time-boxed releases** with fixed deadlines
- **MVP development** requiring clear minimum feature set
- **Resource-constrained projects** needing focus
- **Sprint planning** to prioritize backlog items
- **Stakeholder alignment** when managing expectations
- **Feature negotiation** with competing demands

### MoSCoW May Not Be Ideal For:

- **Early discovery** before direction is clear
- **Continuous delivery** without release boundaries
- **Single-feature projects** too simple to need categorization
- **Complex dependencies** requiring more sophisticated sequencing
- **When need objective scoring** across many similar items

## Step-by-Step Process

### 1. Establish Context (Pre-Work)

**Align on objectives:**
- Define project goals and success metrics
- Identify key stakeholders
- Establish timeline and resource constraints
- Review business objectives and user needs

**Define category criteria:**
Document what qualifies for each category in your specific context. Be explicit about:
- What makes something "critical" vs "important"
- What trade-offs are acceptable
- What workarounds are viable
- How to handle disagreements

### 2. Generate Complete List

**Gather all items to prioritize:**
- Features from product backlog
- User stories from discovery
- Technical requirements
- Stakeholder requests
- Compliance needs
- Bug fixes and technical debt

**Ensure shared understanding:**
- Add clear descriptions to each item
- Document expected value/impact
- Note any dependencies
- List assumptions

### 3. Conduct Prioritization Session

**Set up collaborative session:**
- Include cross-functional stakeholders
- Provide pre-work materials
- Set time limit (90-120 minutes)
- Use visual tools (Miro, FigJam, physical board)

**Facilitate categorization:**
- Start with obvious must-haves
- Work through ambiguous items
- Encourage debate and discussion
- Use test questions for each category
- Document reasoning for decisions

**Watch for red flags:**
- Too many must-haves (>60% effort)
- Everything feels critical
- No could-haves or won't-haves
- Stakeholders unwilling to compromise
- Disagreement on basic definitions

### 4. Validate and Adjust

**Apply sanity checks:**
- Calculate effort distribution across categories
- Ensure must-haves truly pass the "cancel release" test
- Verify reasonable contingency exists
- Check alignment with business objectives

**Challenge must-haves:**
Review each must-have item:
- "Imagine we launch without this - what happens?"
- "Is there any viable workaround?"
- "Would we truly cancel the release?"
- "Are we confusing 'important' with 'critical'?"

**Rebalance if needed:**
- Move borderline must-haves to should-haves
- Ensure 20% could-have contingency
- Identify clear won't-haves
- Get explicit stakeholder buy-in

### 5. Document and Communicate

**Create clear documentation:**
- Use template (see `2-moscow-prioritization-template.md`)
- Include rationale for key decisions
- Note dependencies and risks
- Document assumptions

**Communicate to stakeholders:**
- Explain MoSCoW categories clearly
- Set expectations about flexibility
- Clarify won't-haves to prevent surprises
- Emphasize contingency plan

### 6. Review and Adapt

**Regular reviews:**
- **Sprint/weekly:** Progress on must-haves
- **Mid-release:** Reassess could-haves based on capacity
- **As scope changes:** Re-categorize affected items
- **At retrospectives:** Validate MoSCoW decisions

**Adapt to reality:**
- Adjust categories as you learn more
- Move items between categories as needed
- Add newly discovered requirements
- Update won't-haves based on feedback

## Common Pitfalls and Solutions

### Pitfall 1: Overloaded Must-Haves

The most common pitfall in MoSCoW prioritization is overloading the 'Must-Have' category, which becomes less effective when too many requirements are called essential, resulting in scope creep.

**Warning signs:**
- Must-haves exceed 60% of effort
- Team says "everything is critical"
- No clear MVP definition
- Stakeholders refuse compromises

**Solutions:**
- Apply strict "cancel release" test
- Use objective criteria (legal requirement, core functionality)
- Show trade-offs explicitly
- Create two-tier system: project MVP vs increment must-haves
- Get executive sponsorship for tough calls

### Pitfall 2: Lack of Objective Criteria

One common criticism against MoSCoW is that it does not include an objective methodology for ranking initiatives against each other.

**Warning signs:**
- Heated debates without resolution
- Personal opinions dominate
- Inconsistent categorization
- Different standards for different items

**Solutions:**
- Define criteria before categorizing
- Use complementary scoring (RICE, Value vs Effort)
- Anchor decisions to business objectives
- Document rationale for each item
- Validate with data where possible

### Pitfall 3: Insufficient Stakeholder Input

**Warning signs:**
- Product team deciding alone
- Sales/customer success surprised by priorities
- Missing critical requirements
- Lack of buy-in on decisions

**Solutions:**
- Include cross-functional team in session
- Get input from sales, CS, engineering, design
- Validate with actual users when possible
- Share draft categorization for feedback
- Make prioritization transparent and collaborative

### Pitfall 4: Treating MoSCoW as Static

**Warning signs:**
- No reviews after initial categorization
- Ignoring new information
- Rigid adherence despite changed conditions
- No mechanism for re-prioritization

**Solutions:**
- Schedule regular review cadence
- Create process for urgent re-categorization
- Track actual vs estimated effort
- Adjust based on delivery progress
- Maintain flexibility within structure

### Pitfall 5: Ignoring Dependencies

**Warning signs:**
- Could-haves blocking must-haves
- Technical prerequisites in wrong category
- Infrastructure needs not prioritized
- Integration dependencies missed

**Solutions:**
- Map dependencies explicitly
- Promote blockers to appropriate category
- Sequence within categories
- Coordinate with dependent teams
- Consider using additional prioritization method for sequencing

### Pitfall 6: Weak Won't-Have List

**Warning signs:**
- Nothing in won't-have category
- Vague "future consideration" items
- Stakeholder requests not explicitly addressed
- Scope creep during development

**Solutions:**
- Be explicit about what's excluded
- Document why items are won't-haves
- Use won't-haves to manage expectations
- Create backlog for future consideration
- Communicate won't-haves proactively

## Best Practices

### Do's

- **Start with business objectives** - Link priorities to strategic goals and OKRs
- **Define clear criteria** - Establish what qualifies for each category before categorizing
- **Engage stakeholders early** - Build consensus and manage expectations from the start
- **Be ruthless with must-haves** - Apply the "cancel release" test rigorously
- **Document reasoning** - Capture why items were categorized as they were
- **Balance the distribution** - Maintain ~60% must-have, ~20% should-have, ~20% could-have
- **Make dependencies visible** - Identify and map dependencies between items
- **Review regularly** - Revisit categorization as you learn more
- **Combine with other methods** - Use complementary frameworks (RICE, Kano) for deeper analysis
- **Communicate transparently** - Share prioritization decisions and rationale clearly

### Don'ts

- **Don't make everything a must-have** - This defeats the purpose of prioritization
- **Don't prioritize in isolation** - Involve cross-functional stakeholders
- **Don't ignore data** - Use analytics and user research to validate opinions
- **Don't treat it as permanent** - Be ready to adjust based on new information
- **Don't skip the won't-have** - Explicitly excluding items prevents confusion
- **Don't forget the 20% rule** - Must-haves shouldn't exceed 60% of effort
- **Don't confuse urgent with important** - Apply rigorous tests, not emotional reactions
- **Don't prioritize without context** - Understand user needs, technical constraints, business goals
- **Don't let one voice dominate** - Balance perspectives from multiple stakeholders
- **Don't apologize for tough calls** - Clear prioritization is your job as a PM

## Integration with Other Frameworks

### Combining MoSCoW with Other Methods

**MoSCoW + RICE:**
- Use RICE to score all items first
- Use scores to guide MoSCoW categorization
- Helps make categorization more objective

**MoSCoW + Kano:**
- Use Kano to understand user delight factors
- Map delighters to could-haves, basics to must-haves
- Ensures balanced feature mix

**MoSCoW + Value vs Effort:**
- Plot items on value/effort matrix
- High value + low effort = must-haves or should-haves
- High value + high effort = careful must-have consideration
- Low value items = could-haves or won't-haves

**MoSCoW + Roadmapping:**
- Use MoSCoW for specific releases within roadmap
- Must-haves and should-haves go in NOW section
- Could-haves may go in NEXT section
- Won't-haves inform LATER themes

### When to Use Each Method

- **Use MoSCoW primarily for:** Time-boxed releases, MVP definition, stakeholder alignment
- **Use RICE for:** Objective scoring across many similar features
- **Use Kano for:** Understanding user satisfaction and feature types
- **Use Value vs Effort for:** Quick visual prioritization, technical prioritization

## Metrics for Success

Track these metrics to evaluate your MoSCoW effectiveness:

### Process Metrics

- **Categorization time** - Session length and efficiency
- **Stakeholder participation** - Cross-functional involvement rate
- **Consensus level** - Disagreements resolved vs escalated
- **Documentation quality** - Rationale captured for key decisions

### Outcome Metrics

- **Must-have delivery rate** - Percentage of must-haves shipped on time
- **Scope creep** - Items added to must-haves mid-release
- **Reprioritization frequency** - How often categories change
- **Stakeholder satisfaction** - Alignment and expectation management

### Learning Metrics

- **Prediction accuracy** - Did must-haves match actual criticality?
- **Category distribution** - Did ratios match recommended guidelines?
- **Dependency issues** - Were dependencies properly identified?
- **Retrospective insights** - What would you categorize differently?

## Advanced Techniques

### Two-Tier MoSCoW

For large projects, apply MoSCoW at multiple levels:
- **Project level:** Overall project must-haves
- **Release/increment level:** Specific release must-haves

An item can be a project should-have but a release must-have.

### Minimum Viable Product (MVP) Focus

Use MoSCoW to define MVP:
- Must-haves = MVP features
- Should-haves = enhanced version
- Could-haves = future iterations

### Weighted MoSCoW

Add effort estimates within categories to sequence work:
- Prioritize small must-haves first for quick wins
- Balance effort across categories
- Identify quick could-haves that build momentum

### Risk-Based Adjustment

Adjust categories based on risk:
- High-risk must-haves may need should-have alternatives
- Low-risk should-haves might be promoted to must-haves
- Technical spikes may be must-haves to reduce uncertainty

---

## References

- MoSCoW Template: `2-moscow-prioritization-template.md`
- Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
- OKR Framework: `../1-OKR/README.md`
- Roadmap Framework: `../2-Roadmap/README.md`
- Prioritization: `../4-Prioritization/README.md`
- Kano Model: `../4-Kano-Model/README.md`
- Self-Reflection: `../../2.9-Other/2.9.2-Self-Reflection/README.md`
