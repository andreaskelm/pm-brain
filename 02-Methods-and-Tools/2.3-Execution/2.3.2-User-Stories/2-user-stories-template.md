# User Stories Template

Use this template for each user story. Copy once per story. For the format guide, splitting patterns, INVEST criteria, and examples, see `1-user-stories.md`.

```markdown
## Story: [Brief title]

**Type:** [Feature | Improvement | Bug | Tech Debt]
**Status:** [Backlog | Ready | In Progress | Done]
**Epic / Initiative:** [Link or name]
**Owner:** [Name]

**As a** [specific user type],
**I want** [specific action],
**So that** [specific benefit / outcome]

### Acceptance Criteria
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result] *(add / remove — aim for 3–5)*

### Context
- **Background:** [Why now? Related work or decision?]
- **Design:** [Link to mockups / Figma / wireframes]
- **Dependencies:** [What needs to happen first?]

### Out of Scope
- [What we are explicitly NOT doing in this story]

### Effort Estimate
- **Size:** [XS | S | M | L | XL]
- **Notes:** [Rough reasoning or unknowns]

### Definition of Done
- [ ] Code complete and reviewed
- [ ] Tests written and passing
- [ ] Acceptance criteria met
- [ ] Documentation updated (if needed)
```

## How to Use

1. Copy the block above for each story
2. Be specific on user type — not just "user" but e.g. "rådgiver preparing a budget review" or "new subscriber on mobile"
3. Write 3–5 acceptance criteria in Given/When/Then format — they should be testable
4. Keep one story to one action; if it spans multiple, split it (see `1-user-stories.md` → splitting patterns)
5. Validate against INVEST before marking Ready: Independent, Negotiable, Valuable, Estimable, Small, Testable
