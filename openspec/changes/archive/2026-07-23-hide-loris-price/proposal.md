## Why

The loris app has no payment feature — no Stripe integration, no checkout flow, no payment processing. Despite this, the confirmation email unconditionally displays `Price: {{price}} USD`. In production the frontend sends a hardcoded dummy value of `1`, so customers receive a misleading email showing "Price: 1 USD". This is confusing and unprofessional for a booking that involves no payment.

## What Changes

- Remove the price display (`<h2>Price: {{price}} USD</h2>`) from the loris confirmation email template
- Remove `price` from the required field validation in the `SalesView.post()` view (it is a dummy field with no business meaning)

## Capabilities

### New Capabilities
- `hide-email-price`: Remove price display from the loris confirmation email and make price optional in the view

### Modified Capabilities
<!-- No existing specs are affected -->

## Impact

- `loris/templates/loris/mail.html` — remove the price `<h2>` block
- `loris/views.py` — remove `price` from required validation checks; use `.get("price", 0)` default
