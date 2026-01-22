# Template Decision Guide

Quick reference for choosing which template to use when creating a new framework.

## Quick Decision Matrix

| Scenario | Use This Template | Why |
|----------|------------------|-----|
| New to framework, need quick start | **Quickstart** | Fast, low cognitive load, gets you started immediately |
| Complex strategic decision | **Full Framework** | Comprehensive, addresses edge cases, builds deep understanding |
| Need to assess quality | **Evaluation** | Objective scoring, improvement guidance, quality gates |
| Simple, well-understood framework | **Quickstart** | Avoids over-engineering, faster to create and maintain |
| Teaching/onboarding context | **Full Framework** | Complete understanding, addresses questions, builds knowledge |
| Time-constrained situation | **Quickstart** | Gets you started fast, can reference full framework later |
| Need to improve existing work | **Evaluation** | Structured improvement process, identifies specific issues |
| Framework has many edge cases | **Full Framework** | Covers nuances, prevents mistakes |
| Framework is foundational knowledge | **Full Framework** | Deep understanding required, referenced frequently |
| Need rapid introduction | **Quickstart** | Low barrier to entry, quick to consume |
| Framework needs quality gates | **Evaluation** | Objective assessment, peer review support |
| Framework is experimental/new | **Quickstart** | Lower investment, can evolve to full framework later |

## Decision Flow

```
Start: Creating a new framework

Is this framework simple or well-understood?
├─ YES → Use Quickstart Template
└─ NO → Continue

Does this framework need quality assessment/evaluation?
├─ YES → Use Evaluation Template (in addition to Quickstart or Full Framework)
└─ NO → Continue

Is deep understanding required?
├─ YES → Use Full Framework Template
└─ NO → Use Quickstart Template
```

## Template Comparison

### Quickstart Template

**Best for:**
- Simple frameworks
- Rapid introduction
- Time-constrained situations
- Onboarding materials
- Quick references

**Characteristics:**
- 5-10 minute read
- Minimal sections (5-7)
- Focus on "what" and "how"
- Examples embedded
- Quick decision frameworks

**When NOT to use:**
- Complex strategic frameworks
- When edge cases matter
- Teaching contexts requiring depth
- Foundational knowledge

### Full Framework Template

**Best for:**
- Complex frameworks
- Strategic decisions
- Teaching/onboarding
- Foundational knowledge
- When depth is required

**Characteristics:**
- 20-30 minute read
- Comprehensive sections (9+)
- Detailed explanations
- Edge cases covered
- Integration guidance

**When NOT to use:**
- Simple, well-understood frameworks
- Time-constrained situations
- When quick start is sufficient

### Evaluation Template

**Best for:**
- Quality gates
- Peer review
- Improvement tracking
- Objective assessment
- Comparing outputs over time

**Characteristics:**
- Structured scoring
- Product sense check first
- Red/green flag system
- Improvement generation
- Reflection prompts

**When NOT to use:**
- Simple frameworks without quality needs
- When subjective assessment is sufficient
- One-time use cases

## Domain-Specific Guidance

### Strategy Frameworks

**Typical choice:** Full Framework Template
- Strategic decisions require depth
- Edge cases matter
- Integration with other frameworks is important

**Quickstart when:**
- Framework is well-established
- Used for quick reference
- Time-constrained planning

**Evaluation when:**
- Quality gates needed (e.g., OKRs, Roadmaps)
- Peer review required
- Improvement tracking valuable

### Discovery Frameworks

**Typical choice:** Full Framework Template
- Bias awareness requires depth
- Validation methods need explanation
- Research quality matters

**Quickstart when:**
- Simple research methods
- Quick reference needed
- Team already familiar

**Evaluation when:**
- Research quality assessment needed
- Interview guide evaluation
- Opportunity assessment review

### Communication Frameworks

**Typical choice:** Quickstart Template
- Often straightforward
- Focus on execution
- Time-sensitive

**Full Framework when:**
- Complex stakeholder management
- Crisis communication
- Strategic communication planning

**Evaluation when:**
- Message quality assessment
- Stakeholder alignment check
- Communication effectiveness review

### Execution Frameworks

**Typical choice:** Quickstart or Full Framework (depends on complexity)
- PRDs: Full Framework (complex)
- Daily rituals: Quickstart (simple)
- Metrics: Full Framework (nuanced)

**Evaluation when:**
- PRD quality gates
- Metrics framework assessment
- Delivery quality review

## Audience Considerations

### Junior PMs

**Prefer:** Full Framework Template
- Need more examples and explanations
- Benefit from step-by-step guidance
- Require deeper understanding

**Quickstart acceptable when:**
- Framework is simple
- Used with mentor support
- Quick reference needed

### Senior PMs

**Prefer:** Quickstart Template
- Familiar with patterns
- Need efficiency
- Can adapt as needed

**Full Framework when:**
- Framework is new to them
- Complex strategic context
- Teaching others

## Combination Patterns

### Quickstart + Evaluation

**Use when:**
- Framework is simple but needs quality gates
- Quick introduction with assessment
- Rapid iteration cycles

**Example:** Simple prioritization framework with quality check

### Full Framework + Evaluation

**Use when:**
- Complex framework requiring quality gates
- Strategic decisions with assessment
- Teaching with quality standards

**Example:** OKR framework with evaluation

### Quickstart → Full Framework Evolution

**Use when:**
- Framework is experimental
- Starting simple, evolving to comprehensive
- Learning what's needed over time

**Example:** New discovery method starting simple, evolving based on usage

## Decision Checklist

Before choosing a template, consider:

- [ ] **Complexity:** Is this framework simple or complex?
- [ ] **Audience:** Who will use this? (Junior vs Senior PMs)
- [ ] **Time:** How much time do users have?
- [ ] **Depth:** Is deep understanding required?
- [ ] **Quality:** Are quality gates needed?
- [ ] **Context:** Teaching vs reference vs execution?
- [ ] **Edge cases:** Do edge cases matter?
- [ ] **Integration:** Does it integrate with other frameworks?
- [ ] **Maintenance:** How often will this be updated?

## Examples from Repository

**Quickstart Examples:**
- Strategy Blocks Quickstart (`2.1-Strategy/2.1.1-Strategic-Foundations/1-Strategy-Blocks/2-quickstart.md`)

**Full Framework Examples:**
- OKR Framework (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/1-okr-framework.md`)
- MoSCoW Prioritization (`2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/3-MoSCoW/1-moscow-prioritization-framework.md`)
- North Star Framework (`2.1-Strategy/2.1.2-Strategic-Execution/3-North-Star/1-north-star-framework.md`)

**Evaluation Examples:**
- OKR Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/3-okr-evaluation.md`)
- Roadmap Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/3-roadmap-evaluation.md`)

## Still Unsure?

**Default recommendation:** Start with **Quickstart Template**
- Faster to create
- Easier to iterate
- Can evolve to Full Framework if needed
- Less maintenance overhead

**Upgrade to Full Framework when:**
- Users ask for more detail
- Edge cases emerge
- Framework becomes foundational
- Teaching context requires depth

**Add Evaluation when:**
- Quality becomes an issue
- Peer review is needed
- Improvement tracking is valuable
- Objective assessment adds value

## References

- **Template Structure Guide:** `1-template-structure-guide.md` - Comprehensive documentation
- **Quickstart Template:** `2-quickstart-template.md` - Template file
- **Full Framework Template:** `3-full-framework-template.md` - Template file
- **Evaluation Template:** `4-evaluation-template.md` - Template file
- **Main README:** `README.md` - Overview
