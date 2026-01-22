# Template Structure Guide

This guide provides comprehensive documentation for the reusable template system used across all frameworks, templates, playbooks, and guides in the PM Brain repository.

## Part 1: System Overview

### Purpose: Why Standardized Templates Matter

Standardized templates serve multiple critical functions:

**For Junior PMs:**
- **Clarity** - Clear structure reduces cognitive load and confusion
- **Learning** - Consistent patterns help build mental models
- **Confidence** - Examples and guidance reduce fear of "doing it wrong"
- **Efficiency** - Less time figuring out structure, more time thinking

**For Senior PMs:**
- **Efficiency** - Familiar patterns reduce overhead
- **Quality** - Ensures important elements aren't missed
- **Consistency** - Makes frameworks easier to navigate and maintain
- **Speed** - Faster to create new frameworks when structure is clear

**For AI/LLM Collaboration:**
- **Structured prompts** - Clear section markers enable better AI parsing
- **Context provision** - Braindump sections provide rich context for AI
- **Consistent interaction** - Predictable structure improves AI responses
- **Scalability** - Templates enable AI to help across many frameworks

### Target Audience Considerations

**Junior PMs need:**
- More examples and explanations
- Step-by-step guidance
- Clear "what" and "how" before "why"
- Explicit connections to other frameworks
- Common mistakes highlighted upfront

**Senior PMs need:**
- Principles and philosophy
- Edge cases and nuances
- Integration with other frameworks
- Quick reference for key decisions
- Flexibility to adapt as needed

**Both need:**
- Clear structure
- Product sense development
- Bias awareness
- Reflection prompts
- Cross-references

### AI/LLM Optimization

Templates are designed to work seamlessly with AI/LLM models:

**Structured Prompts:**
- Clear section markers (`##`, `###`) for parsing
- Explicit prompt templates embedded in evaluation frameworks
- "Help me think" vs "think for me" guidance

**Context Provision:**
- Braindump sections provide rich context before structuring
- Product sense exercises give AI insight into user thinking
- Examples show expected output format

**Consistent Interaction:**
- Predictable structure improves AI responses
- Reusable prompt patterns across frameworks
- Clear instructions for AI role (coach vs executor)

**Scalability:**
- Templates enable AI to help across many frameworks
- Consistent patterns reduce training needed
- Structured evaluation enables automated quality checks

---

## Part 2: Template Variants Analysis

### Quickstart Template

**Purpose:** Rapid introduction, first-time users, time-constrained situations

**Structure Characteristics:**
- Minimal sections (5-7 main sections)
- Focus on "what" and "how" with brief "why"
- Examples embedded throughout
- Quick decision frameworks
- Prerequisites checklist
- Success indicators

**Pros:**
- ✅ Fast to consume (5-10 minutes)
- ✅ Low cognitive load
- ✅ Gets people started quickly
- ✅ Reduces barrier to entry
- ✅ Good for onboarding

**Cons:**
- ❌ May oversimplify complex topics
- ❌ Lacks depth for nuanced decisions
- ❌ Doesn't cover edge cases
- ❌ May need to reference full framework later
- ❌ Less suitable for strategic decisions

**When to Use:**
- Simple or well-understood frameworks
- Onboarding materials
- Quick references
- Time-constrained situations
- When users need to start immediately

**Example Frameworks:**
- Strategy Blocks Quickstart (`2.1-Strategy/2.1.1-Strategic-Foundations/1-Strategy-Blocks/2-quickstart.md`)

---

### Full Framework Template

**Purpose:** Comprehensive understanding, complex decisions, teaching tool

**Structure Characteristics:**
- All standard sections (9+ sections)
- Detailed explanations with rationale
- Edge cases and nuances
- Integration guidance
- Multiple examples
- Common pitfalls with solutions
- Best practices
- Metrics for success

**Pros:**
- ✅ Complete coverage
- ✅ Addresses edge cases
- ✅ Builds deep understanding
- ✅ Enables independent use
- ✅ Suitable for complex decisions
- ✅ Good for teaching

**Cons:**
- ❌ Longer to read (20-30 minutes)
- ❌ May overwhelm beginners
- ❌ Requires more maintenance
- ❌ Higher cognitive load
- ❌ May include unnecessary detail for simple cases

**When to Use:**
- Strategic frameworks
- Complex methodologies
- Foundational knowledge
- Teaching/onboarding contexts
- When deep understanding is required
- When edge cases matter

**Example Frameworks:**
- OKR Framework (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/1-okr-framework.md`)
- MoSCoW Prioritization (`2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/3-MoSCoW/1-moscow-prioritization-framework.md`)
- North Star Framework (`2.1-Strategy/2.1.2-Strategic-Execution/3-North-Star/1-north-star-framework.md`)

---

### Evaluation Template

**Purpose:** Structured assessment, quality checks, reflection

**Structure Characteristics:**
- Product sense check first (Step 0)
- Quality flag system (red/green flags)
- Weighted scoring framework
- Antipattern detection
- Improvement generation
- Reflection prompts

**Pros:**
- ✅ Objective assessment
- ✅ Reduces bias
- ✅ Enables comparison over time
- ✅ Provides actionable improvements
- ✅ Quality gates for frameworks
- ✅ Structured reflection

**Cons:**
- ❌ Can feel mechanical
- ❌ Requires calibration
- ❌ May miss nuance
- ❌ Additional overhead
- ❌ Not needed for all frameworks

**When to Use:**
- When frameworks need quality gates
- Peer review contexts
- Improvement tracking
- When objective assessment adds value
- When comparing multiple outputs
- Teaching quality standards

**Example Frameworks:**
- OKR Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/3-okr-evaluation.md`)
- Roadmap Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/3-roadmap-evaluation.md`)

---

## Part 3: Universal Elements (All Templates)

Every framework template should include these elements, adapted to the template variant:

### 1. Step 0: Braindump & Product Sense (Universal Pattern)

**Why it's universal:**
- Prevents premature structuring
- Develops product intuition
- Provides context for AI
- Reduces bias
- Captures initial thinking

**Structure:**
```
## Step 0: Braindump & Product Sense (Do this first!)

**Before using [framework], braindump:**
- [Braindump prompt 1 - e.g., "What outcomes are you trying to achieve? Dump everything - don't structure yet."]
- [Braindump prompt 2 - e.g., "What does your product sense tell you? What feels right or wrong?"]
- [Braindump prompt 3 - e.g., "What assumptions are you making? List them explicitly."]

**Product sense exercise:**
- [Question 1 - e.g., "If you had to pick ONE outcome that matters most, what would it be? Why?"]
- [Question 2 - e.g., "What would make you say 'this is obviously wrong'?"]

**Bias check:**
- [Bias awareness prompt - e.g., "What biases might affect your view? (Vanity metrics? Activity vs. outcome?)"]
```

**AI Optimization:**
- Provides rich context before structuring
- Shows user's thinking process
- Enables AI to challenge assumptions
- Helps AI understand user's product sense level

### 2. Overview

**Purpose:** Quick understanding of what the framework is and why it matters

**Structure:**
- What it is (one sentence)
- Why it matters (one sentence)
- When to use it (brief list)

**Quickstart variant:** Very brief (2-3 sentences)
**Full Framework variant:** 2-3 paragraphs with context

### 3. Core Philosophy

**Purpose:** Understand principles and beliefs underlying the framework

**Structure:**
- What the framework is NOT (to set boundaries)
- Core principles (what it should do)
- Key concepts/philosophy

**Quickstart variant:** Brief principles list
**Full Framework variant:** Detailed explanation with rationale

### 4. Framework Structure

**Purpose:** Understand how the framework is organized

**Structure:**
- Key components
- How components relate
- What to capture in each component
- Why each component matters

**Quickstart variant:** Simple list of components
**Full Framework variant:** Detailed explanation of each component

### 5. How to Use

**Purpose:** Step-by-step practical guidance

**Structure:**
- Numbered steps
- Activities for each step
- Deliverables
- Time estimates (if applicable)

**Quickstart variant:** Brief steps (2-3 sentences each)
**Full Framework variant:** Detailed steps with examples and edge cases

### 6. When to Use / When Not to Use

**Purpose:** Decision criteria for using the framework

**Structure:**
- Works best for (use cases)
- May not be ideal for (anti-patterns)
- Alternatives to consider

**Quickstart variant:** Simple list
**Full Framework variant:** Detailed scenarios with examples

### 7. Common Pitfalls

**Purpose:** Learn from common mistakes

**Structure:**
- Pitfall name
- Warning signs
- Why it's a problem
- Solutions

**Quickstart variant:** Brief list with solutions
**Full Framework variant:** Detailed explanations with examples

### 8. Best Practices

**Purpose:** Do's and Don'ts

**Structure:**
- Do's (what to do)
- Don'ts (what to avoid)
- Rationale for each

**Quickstart variant:** Brief list
**Full Framework variant:** Detailed with examples

### 9. References

**Purpose:** Connect to related frameworks

**Structure:**
- Links to templates
- Links to evaluations (if applicable)
- Links to related frameworks
- Cross-references

**All variants:** Consistent link format

---

## Part 4: Template Customization Guide

### For Different Domains

**Strategy Frameworks:**
- Emphasize: Alignment, trade-offs, decision criteria, strategic thinking
- Add sections: Strategic context, alignment with company goals, decision frameworks
- Examples: OKRs, Roadmaps, North Star, Prioritization

**Discovery Frameworks:**
- Emphasize: Bias awareness, evidence gathering, validation, customer focus
- Add sections: Research methods, validation approaches, bias checks
- Examples: Research Interviews, Opportunity Assessment, Idea Validation

**Communication Frameworks:**
- Emphasize: Audience, clarity, stakeholder management, message framing
- Add sections: Audience analysis, communication channels, stakeholder mapping
- Examples: Newsletters, One-Pagers, Stakeholder Management

**Execution Frameworks:**
- Emphasize: Measurement, iteration, outcomes, delivery
- Add sections: Success metrics, iteration cycles, outcome tracking
- Examples: PRDs, Daily Rituals, Metrics

### For Different Audiences

**Junior PMs:**
- More examples throughout
- Clearer explanations with rationale
- Step-by-step guidance
- "What" and "how" before "why"
- Explicit connections to other frameworks
- Common mistakes highlighted upfront
- More structure and scaffolding

**Senior PMs:**
- Focus on principles and philosophy
- Edge cases and nuances
- Integration with other frameworks
- Quick reference for key decisions
- Flexibility to adapt
- Less scaffolding, more principles

**Both:**
- Clear structure (universal)
- Product sense development (universal)
- Bias awareness (universal)
- Reflection prompts (universal)
- Cross-references (universal)

### For AI Collaboration

**Structured Prompts:**
- Use clear section markers (`##`, `###`)
- Embed explicit prompt templates in evaluation frameworks
- Include "help me think" vs "think for me" guidance
- Provide example prompts

**Context Provision:**
- Braindump sections provide rich context
- Product sense exercises give AI insight
- Examples show expected output format
- Include user's thinking process

**Consistent Interaction:**
- Predictable structure improves responses
- Reusable prompt patterns
- Clear instructions for AI role
- Consistent formatting

**Scalability:**
- Templates enable AI to help across frameworks
- Consistent patterns reduce training
- Structured evaluation enables automation
- Reusable components

### Template Adaptation Checklist

When adapting a template for a new framework:

- [ ] Choose appropriate template variant (Quickstart vs Full Framework)
- [ ] Include all universal elements
- [ ] Adapt for domain (Strategy/Discovery/Communication/Execution)
- [ ] Consider audience (Junior vs Senior PMs)
- [ ] Add domain-specific sections
- [ ] Include AI collaboration prompts
- [ ] Add examples relevant to domain
- [ ] Cross-reference related frameworks
- [ ] Include reflection prompts
- [ ] Test with target audience

---

## Design Decisions & Rationale

### Decision 1: Three Template Variants

**Rationale:** Different use cases need different levels of detail

**Pros:**
- Flexibility for different contexts
- Appropriate level of detail
- Avoids one-size-fits-all
- Respects user time constraints

**Cons:**
- More files to maintain
- Requires decision-making
- May create confusion about which to use

**Mitigation:** Clear decision guide (`5-template-decision-guide.md`)

### Decision 2: Universal "Step 0: Braindump & Product Sense"

**Rationale:** Consistent pattern prevents premature structuring and develops intuition

**Pros:**
- Develops product sense
- Provides context for AI
- Reduces bias
- Captures initial thinking

**Cons:**
- Adds overhead
- May feel repetitive
- Requires discipline

**Mitigation:** Make it brief but meaningful, show value clearly

### Decision 3: Embedded AI Collaboration Prompts

**Rationale:** Templates optimized for AI/LLM use as thought partners

**Pros:**
- Better AI interactions
- Structured thinking
- Scalable assistance
- Consistent patterns

**Cons:**
- Requires AI access
- May not work for all users
- Requires AI literacy

**Mitigation:** Templates work without AI, but optimized for AI use

### Decision 4: Pros/Cons in Documentation

**Rationale:** Transparency about trade-offs helps decision-making

**Pros:**
- Informed choices
- Sets expectations
- Builds trust
- Helps users understand trade-offs

**Cons:**
- May create analysis paralysis
- Adds length to documentation
- May discourage use

**Mitigation:** Keep pros/cons concise, focus on actionable guidance

### Decision 5: Separate Evaluation Template

**Rationale:** Not all frameworks need evaluation, but when they do, structure helps

**Pros:**
- Quality gates
- Objective assessment
- Improvement guidance
- Comparison over time

**Cons:**
- Additional complexity
- May feel mechanical
- Requires calibration
- Not needed for all frameworks

**Mitigation:** Make evaluation optional, use only when it adds value

### Decision 6: Playbook Variants (Special Case)

**Rationale:** Some frameworks need detailed process/playbook documentation beyond standard framework structure

**When to use:** When framework requires:
- Detailed week-by-week process documentation
- Role assignments and RACI matrices
- Specific deliverables and timelines
- Operational execution guidance

**Example:** Strategy Blocks Full Guide (`2.1-Strategy/2.1.1-Strategic-Foundations/1-Strategy-Blocks/1-full-guide.md`)

**Characteristics:**
- More process-focused than framework-focused
- Includes detailed roles, responsibilities, timelines
- Week-by-week activities and deliverables
- Operational execution guidance

**Acceptable variant:** Playbook variants are acceptable when they serve a different purpose than framework guides. They complement Quickstart/Full Framework templates rather than replace them.

**Guidelines:**
- Playbook should still include universal elements where applicable (Overview, Step 0, etc.)
- Should complement Quickstart or Full Framework guide
- Focus on execution process rather than framework structure
- Can be more detailed and prescriptive than standard frameworks

### Decision 7: README Templates (Domain & Initiative)

**Rationale:** README files need consistent patterns for navigation and onboarding at both domain and initiative levels.

**Pros:**
- Clear orientation for new users
- Faster navigation for experienced users
- Encourages flows and cross-linking

**Cons:**
- Another template to maintain
- Needs refresh when structure changes

**Usage guidance:**
- Use **Domain README Template** for Strategy/Discovery/Communication/Execution/Foundations directories
- Use **Initiative README Template** for `04-Initiatives/4.x-*` folders
- Adapt “Before using…” and flows per domain context

---

## References

- Quickstart Template: `2-quickstart-template.md`
- Full Framework Template: `3-full-framework-template.md`
- Evaluation Template: `4-evaluation-template.md`
- Template Decision Guide: `5-template-decision-guide.md`
- Domain README Template: `6-readme-template-domain.md`
- Initiative README Template: `7-readme-template-initiative.md`
- Main README: `README.md`
