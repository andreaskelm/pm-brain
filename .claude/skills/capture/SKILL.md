---
name: capture
description: File a sharp bit after the user has thought — an alignment, a nudge, a picked-up fact, or a small call. Use when the user says "file this bit", "where does this go", "log this alignment", "I just picked this up", or "this isn't a task but it should stick". Do not use for dumping a transcript, ingesting a paste, or opening a new bet before the braindump floor.
---

# Capture (file a bit)

A bit is something that changed an alignment, a belief, or a small call. It is not a task, a standup line, or a transcript to process. The failure mode is filing a paste before the user has said what they believe. Refuse that write.

The shape of a signal bullet and a hypothesis page lives only in [references/template.md](references/template.md). Do not invent a second schema beside the notes.

## Is this the right thing?

**Use capture when** they already have a sharp bit and want it filed: a hallway alignment, a nudge that moved someone, a fact they picked up, a small call.

**Do not use capture when**

- The problem is still forming, they are stuck, or they said "help me think" → `braindump`.
- They are about to **open a new hypothesis** or put a **confidence percent** on a call → `braindump` until the floor is met (named assumption that decides it, know vs guess, one risk, one uncomfortable thought). Fig-leaf answers do not pass. Then return here to write.
- They want an opportunity assessment, PRD, or interview synthesis → `opportunity-assessment` or `discovery-synthesis`.
- The line is a task ("email Sara", "update the ticket") → it stays in their task tool. Do not write it.

**Skip the thinking:** acknowledge, offer a 2-minute version of the gate, proceed only if they insist, and name the risk in one sentence. Do not silently file.

## Gate — ask, then wait

No file until they have answered. You may offer a read. You do not pick the type and proceed. One batch, then stop.

1. **What is this?** Info, alignment, nudge, or small decision.
2. **What do you know, and what are you guessing?**
3. **Where does it land?** Today's signal file, an existing hypothesis, an initiative note, one line on an avatar that already exists, `4-Research/`, or drop it.

If they cannot name the landing spot, drop it or park one line in `4-Research/`. Do not invent a hypothesis to give the note a home.

Check the repo before asking them to re-explain a person, initiative, or bet that already has a file: `3-Work/hypotheses/`, `3-Work/[initiative]/`, `1-Context/1.1-Stakeholder-Avatars/`.

## Write

Only after the gate, and only in their words.

**Day file.** Append one bullet to `3-Work/signals/YYYY-MM-DD.md` (create the file if this is the first bit today). Use the signal shape in the template. `landed:` is required before you call the bit done: a hypothesis path, an initiative research note, an avatar, a `4-Research/` note, a `5-Growth/decisions.md` row, or `dropped`. An open bullet is a failed capture, not a todo.

**Durable touches.** Offer them. Do not write them silently. Cap at **three** besides the day file (hypothesis evidence, avatar last-signal line, initiative or research note, or a scored decision). Say what you skipped.

- **Existing hypothesis** — add an evidence row (date, for/against, provenance, link back to the signal bullet). Confidence stays High / Med / Low.
- **New hypothesis** — only after the braindump floor. Page shape is in the template. Status starts at `active`.
- **Avatar** — one "last signal" line on a file that already exists. Do not invent a person. Do not rewrite `1-Context/`.
- **Scored decision** — only when they state a confidence percent they are willing to score later, and only after the floor. Offer a row in `5-Growth/decisions.md`. A hallway call without a percent stays on the signal (and on the hypothesis or avatar it touches). Never mark it decided for them.
- **Unplaced insight** — one short note in `4-Research/` when nothing in `3-Work/` should change.

Provenance on every bullet and evidence row: `documented` (with a link), `verbal`, `hunch`, or `industry`.

## Before calling it done

2–4 bullets: what they decided, what was written, what you refused. If a durable write is still waiting on a yes, say so and stop.

Red flags: [references/criteria.md](references/criteria.md).

## Org reality

- **The paste is not the thinking.** A transcript in the chat is raw material. Filing starts when they answer the gate.
- **Busy Tuesday.** One sharp bit beats a cleaned-up meeting dump.
- **Politics in the bullet.** An alignment names who moved and what they now expect. A vibe ("stakeholder seemed fine") does not get a file.
- **Calibration pollution.** Small calls do not become Brier rows just because they were written down.

## References

- [references/template.md](references/template.md) — signal bullet and hypothesis page
- [references/criteria.md](references/criteria.md) — flags
