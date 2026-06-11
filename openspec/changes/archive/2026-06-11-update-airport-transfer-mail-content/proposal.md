## Why

The confirmation email sent to guests after submitting airport transfer details needs updated copy to better reflect the current workflow, including mention of payment, Cancun travel information, and to match the correct business sign-off. The current message references a wedding date and uses generic language that does not apply to all bookings.

## What Changes

- Replace the body text of `rhea_peeyush_airport_transfers/templates/rhea_peeyush_airport_transfers/mail.html` with the new copy provided by the client.
- New copy: acknowledges payment and Cancun travel info submission, promises a detailed confirmation email with arrival process and hotel departure time, and closes with "Warm Regards. The Cancun Concierge DMC team."

## Capabilities

### New Capabilities
<!-- None introduced -->

### Modified Capabilities
- `rhea-peeyush-airport-transfers`: The email body content (confirmation message text) displayed to guests is being updated with new approved copy.

## Impact

- **Template file**: `rhea_peeyush_airport_transfers/templates/rhea_peeyush_airport_transfers/mail.html` — only the paragraph body text changes; HTML structure, logo, styling, and Django template tags remain intact.
- No backend logic, views, or models are affected.
- No API or dependency changes.
