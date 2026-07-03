# Evidence Strength — Vocabulary (Not Workflow)

**For Agents:** When a load-bearing claim appears in conversation or artifacts, name its evidence-strength tier in passing — one sentence, not a lecture. This is a **vocabulary**, not a workflow: real PM work is messy; the point is to make claims wear their actual strength instead of laundering guesses as facts. Do not require tags on every sentence. Optional inline tags below are for logs and decision records when helpful.

**Load when:** Assumptions vs facts lens fires and the user needs shared language; filling forecast-log, prioritization-decision-log, or research-insight-log; Friday drift sweep flags weak evidence on a stale belief.

---

## The four tiers (strongest to weakest)

| Tier | Meaning | Examples |
|------|---------|----------|
| **documented** | Artifact-backed — went through synthesis or is directly citable | Interview transcript, research note, metric dashboard, decision memo, `4-Research/` file |
| **verbal** | Heard from a person, no durable artifact | Stakeholder comment in a meeting, off-the-record exec signal, customer call you didn't record |
| **hunch** | Your intuition or judgment, not yet validated | "My read is…", pattern you've seen before but haven't tested on this product |
| **industry** | Accepted background knowledge, no product-specific evidence | "Best practice says…", benchmark from another company, framework default |

**Hierarchy:** documented outweighs verbal; verbal outweighs hunch; hunch outweighs industry. When two tiers conflict, name the stronger one and flag the gap.

---

## How the coach uses this

In conversation, name the tier naturally:

- "That's verbal — useful, but you don't have it documented yet."
- "You're leaning on industry knowledge there; what's *your* evidence for this product?"
- "Three documented interviews saying the same thing — that's worth treating as real."

Do **not** turn every exchange into tagging exercise. The lens fires when a claim is doing real work (driving a decision, blocking progress, or sitting in a log).

---

## Optional inline tags (logs and artifacts)

When writing to growth logs or decision records, you may tag load-bearing claims:

- `[documented]` — link to source when possible
- `[verbal]` — name who/when if known
- `[hunch]` — yours or named stakeholder's
- `[industry]` — flag for replacement with product-specific evidence

Example in a prioritization log: "Mid-market ops batch weekly, not daily `[documented]` — see 2026-04-22 interview."

---

## Related

- Assumptions vs facts lens: [AGENTS.md](../../../../AGENTS.md)
- [Assumptions Framework](3-assumptions-framework.md) — align on beliefs before solutions
- Reopen triggers (what would change your mind): [forecast-log.md](../../../../5-Growth/3-Product-Judgment-Test/forecast-log.md), [2-prioritization-decision-log.md](../../../../5-Growth/2-prioritization-decision-log.md)
- Friday drift sweep: `/week` Friday + [2-weekly-cadence.md](../../../4-Execution/1-Daily-Execution-And-Rituals/2-weekly-cadence.md)
- Bias when evidence is thin: [2-Bias/1-bias-framework.md](../../2-Bias/1-bias-framework.md)
