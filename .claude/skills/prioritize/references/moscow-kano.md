# MoSCoW and Kano

Two categorical methods for different questions. MoSCoW is about **what makes the cut** for a fixed timebox. Kano is about **how features affect satisfaction**: what's table stakes, what's a differentiator, what's a delighter.

## MoSCoW — scope negotiation, timeboxed releases, MVP definition

| Category | Test | Effort budget |
|---|---|---|
| **Must have** | If it's missing, the release fails, is illegal, or is unsafe. Not "really important". | ≤ 60% |
| **Should have** | Important and painful to leave out, but there's a workaround | ~20% |
| **Could have** | Nice to have. This is the contingency pool you drop when things slip. | ~20% |
| **Won't have (this time)** | Explicitly out, written down, with a reason | — |

**The 60% rule is the whole point.** If Musts exceed 60% of effort, you have no slack, and the first estimate miss blows the deadline. When stakeholders push more into Must, ask: "If we shipped without this, would we cancel the release?" If not, it's a Should.

**The Won't list is the most valuable output.** A weak one ("future enhancements") means the argument is just postponed to sprint 4. Name the items, the requester, and the reason.

Pitfalls: everything is Must (apply the cancel-the-release test); no objective criteria (agree the criteria *before* the session); treating it as static (re-run when scope or dates change); ignoring dependencies (a Could that a Must depends on is really a Must).

Combining: score with RICE first, then let scores inform (not dictate) categories, then sanity-check strategically.

## Kano — balance table stakes vs. delight

| Category | Present | Absent | What to do |
|---|---|---|---|
| **Must-be (basic)** | Not noticed | Very dissatisfied | Make it good enough; don't over-invest |
| **Performance** | More is better | Less is worse | Compete here where rivals are weak |
| **Attractive (delighter)** | Delighted | Not missed | Pick 1–3 that fit the brand |
| **Indifferent** | Don't care | Don't care | Drop or defer |
| **Reverse** | Some dislike it | Some prefer it absent | Make optional, or understand why |

**The questionnaire.** Two questions per feature, same wording except the negation:
- Functional: "If the product *had* [feature], how would you feel?"
- Dysfunctional: "If the product did *not* have [feature], how would you feel?"
- Answers: I like it · I expect it · I'm neutral · I can live with it · I dislike it

**Evaluation table** (rows = functional answer, columns = dysfunctional answer)

| | Like | Expect | Neutral | Live with | Dislike |
|---|---|---|---|---|---|
| **Like** | Questionable | Attractive | Attractive | Attractive | Performance |
| **Expect** | Reverse | Indifferent | Indifferent | Indifferent | Must-be |
| **Neutral** | Reverse | Indifferent | Indifferent | Indifferent | Must-be |
| **Live with** | Reverse | Indifferent | Indifferent | Indifferent | Must-be |
| **Dislike** | Reverse | Reverse | Reverse | Reverse | Questionable |

Classify each response, take the most frequent category per feature, and note close splits. A split usually means two segments, so segment before concluding.

**Optional coefficients** (A, P, M, I = response counts):
- Satisfaction CS+ = (A + P) ÷ (A + P + M + I), from 0 to 1
- Dissatisfaction CS− = −(P + M) ÷ (A + P + M + I), from 0 to −1

**Sample:** 20–30 responses per feature minimum, 100+ for confidence; pilot with 10–15 first; keep it under 20 features.

**Category drift is real.** Today's delighter is next year's expectation (think dark mode, SSO, mobile apps). Re-survey annually in stable markets, quarterly in fast ones, and after a major competitor launch.

Where Kano breaks down: B2B products where the buyer isn't the user (survey both, separately); brand-new categories where customers can't imagine the feature; and teams that treat the survey output as a roadmap instead of an input.

Credit: Noriaki Kano (1984).
