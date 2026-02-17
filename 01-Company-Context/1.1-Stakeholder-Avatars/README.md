# Stakeholder Avatars (Brainfeed Cast)

This folder holds your **global cast of recurring people** you work with (manager, Eng lead, designer, PM leadership, key cross-functional partners). One file per person. The agent uses these avatars with the [politics-coach skill](../../.cursor/skills/politics-coach/SKILL.md) to simulate "what would my manager say?" and to run politics checks on plans and communication when those people aren't in the room.

**To add or update avatars:** Use the guided quiz and methodology in [02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md). This folder is where the resulting data lives.

---

## For Agents

- **When to load:** User asks to set up/update their brainfeed cast, or asks "what would [Name] say?" / "how will [stakeholders] react?" or wants a politics check.
- **How to find an avatar:** List this folder's `.md` files. Match the requested name or role to the filename (e.g. "manager" → `1-jane-manager.md`) or to the "Name — Role" heading inside the file. Load the relevant file(s) and run the three-part simulation (out-loud, inner monologue, concerns + de-risking) per the politics-coach skill.
- **When creating a new avatar:** After running the 2.4.8 quiz, create a new file here with the naming convention below (e.g. `3-sam-design-lead.md`) and paste the filled structure from 2.4.8's [2-avatar-template.md](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/2-avatar-template.md).
- **Caution:** Avatars are approximations. Encourage the user to validate in real conversations; surface obvious biases.

---

## File naming convention

- **Pattern:** `N-name-role.md` — single digit (1–9), then **name of person**, then **role**; hyphen-separated. Optional **company/organization** at end if you work across multiple organizations: `N-name-role-org.md`.
- **Examples:** `1-jane-manager.md`, `2-alex-eng-lead.md`, `3-sam-design-lead.md`, `4-chris-vp-product.md`.
- **Optional organization:** `1-jane-manager-acme.md` (only if you need to disambiguate across organizations).
- **Example file:** `0-example-director-engineering.md` — single digit 0 keeps it at top and signals "example, not a real person." Do not delete; it shows the schema.

---

## How to add your first avatar

1. **Run the quiz** in [2.4.8-Stakeholder-Avatars](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md) (guided questions per person).
2. **Create a new file** in this folder with the naming convention: `N-name-role.md` (e.g. next number after existing files, e.g. `1-jane-manager.md`).
3. **Paste the template** from 2.4.8's [2-avatar-template.md](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/2-avatar-template.md) and fill it with the answers from the quiz.
4. **Update over time** — after important 1:1s or decisions, add a note to the relevant avatar file.

---

## Human workflow

- Pick 3–7 core people who materially impact your work.
- One file per person; keep content concrete (real phrases, real behaviors).
- Agents read these files when you ask for simulations or politics checks.

## See also

- **Setup method (guided quiz):** [02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/](../../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md)
- **Stakeholder directory (organization list):** [6-company-stakeholders.md](../6-company-stakeholders.md)
- **Company context setup:** [SETUP.md](../SETUP.md) → §3.5 Stakeholder avatars
- **Org survival (system-level politics):** [1.2-Org-Survival/](../1.2-Org-Survival/README.md)
