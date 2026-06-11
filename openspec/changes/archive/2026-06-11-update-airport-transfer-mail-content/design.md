## Context

The `mail.html` template is rendered and sent as a confirmation email to guests after they submit their airport transfer booking. The current body text references a "wedding date" and uses a generic tone that does not match all booking contexts. The client has provided updated approved copy that acknowledges payment, references Cancun travel info submission, and uses the correct closing.

## Goals / Non-Goals

**Goals:**
- Replace the email body paragraph text in `mail.html` with the client-approved copy.
- Preserve the existing HTML structure, logo image, Google Fonts link, and Django template tags.

**Non-Goals:**
- Changes to email styling, layout, or the logo.
- Changes to backend views, models, or URL configuration.
- Localization or multi-language support.
- Changes to any other template or email.

## Decisions

**Direct in-place text edit** — The change is purely a copy update to a single `<p>` block. No new files, components, or abstractions are needed. Editing the template directly is the simplest and lowest-risk approach.

## Risks / Trade-offs

- **Typo in source copy** → The user-provided text contains "inclufing" (likely "including") and "Regads" (likely "Regards"). These will be corrected to their intended spellings in the implementation. → *Mitigation*: Confirm corrections with the team before deploy if needed.
- No rollback complexity — change is a single-file text edit, easily reverted via git.
