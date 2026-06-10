## Context

Currently, the confirmation email template in `rhea_peeyush_airport_transfers` has a generic message about Cancun Travel Flight Information. The customer wants a specific message tailored to the wedding context.

## Goals / Non-Goals

**Goals:**
- Update the HTML email template `rhea_peeyush_airport_transfers/templates/rhea_peeyush_airport_transfers/mail.html` with the new content.

**Non-Goals:**
- Modify views, models, or any email dispatching logic (which remains unchanged).
- Change confirmation emails for other apps.

## Decisions

- **Direct template modification**: We will edit `mail.html` directly since Django's templating engine renders this exact file.
- **Sign-off Spacing**: We will use HTML non-breaking spaces (`&nbsp; &nbsp;`) to place "Warm regards" and "The Cancun Concierge DMC team" on the same line with spacing, per the user's requirement.

## Risks / Trade-offs

*(None)*
