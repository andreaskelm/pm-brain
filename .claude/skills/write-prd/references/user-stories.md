# User Stories

For breaking PRD requirements into buildable work. A story is a conversation starter with a definition of done, not a mini-spec.

```markdown
## Story: [Brief title]

**As a** [specific user — "new subscriber on mobile", not "user"],
**I want** [one action],
**So that** [the outcome they actually care about]

### Acceptance criteria (3–5, testable)
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

### Context
- Why now / related decision:
- Design:
- Dependencies:

### Out of scope
- [What this story deliberately doesn't do]
```

## What goes wrong

- **Feature, not story:** "Implement new search algorithm" → "As a returning shopper, I want relevant results so I can find what I bought before in one search."
- **Too technical:** "As a developer, I want to refactor the codebase." If the real benefit is speed, say the user-facing benefit.
- **No real benefit:** "So that there's a blue button." If you can't write the "so that", question whether it's worth building.
- **UI spec instead of need:** "A dropdown in the top right" → "Quick access to account settings." Let design solve it.
- **Too many things:** search + filters + sorting + pagination is four stories.

## Splitting (when a story is bigger than ~5 days)

By user type (free vs. premium) · by workflow step (cart → shipping → payment) · happy path vs. edge cases · by operation (create / delete / organize).

## Ready check (INVEST)

Independent · Negotiable (not prescribing *how*) · Valuable to a user · Estimable · Small (fits a sprint) · Testable (criteria exist).

Further reading: Mike Cohn, *User Stories Applied*; Jeff Patton, *User Story Mapping*.
