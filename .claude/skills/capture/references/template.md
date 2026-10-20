# Capture shapes

This is the only shape. Folder READMEs point here. Do not copy this file into `3-Work/`.

## Signal bullet

One file per day you actually file something: `3-Work/signals/YYYY-MM-DD.md`. Append. Do not open a new file per sentence.

```markdown
# Signals YYYY-MM-DD

- **type:** info | alignment | nudge | small-decision
  **bit:** [their words — what changed]
  **know:** [what is actually known]
  **guess:** [what is still a guess]
  **provenance:** documented | verbal | hunch | industry
  **link:** [external raw source, or "none"]
  **landed:** [path to hypothesis, initiative note, avatar, 4-Research note, decisions.md row, or dropped]
```

`landed: dropped` is a finished bit. A missing `landed:` is not.

## Hypothesis page

One file per belief you are testing: `3-Work/hypotheses/<slug>.md`. Open one only after the braindump floor. Promote the bet into `3-Work/[initiative]/` when it needs an opportunity assessment or a PRD. An observation does not get a page here.

```markdown
# [Belief, specific enough to be wrong]

**Status:** active | resolved | killed
**Confidence:** High | Med | Low
**Cheapest test:** [one move that would teach you something]
**Decision trigger:** [observable signal that means you should make the call]

## Evidence for

- YYYY-MM-DD — [claim] — provenance: documented | verbal | hunch | industry — [link to signal bullet or note]

## Evidence against

- YYYY-MM-DD — [claim] — provenance: … — [link]

## What would change my mind

[Same bar as the decision trigger, in a sentence.]
```
