## Context

The loris app's confirmation email template (`loris/templates/loris/mail.html`) unconditionally renders a price section (`<h2>Price: {{price}} USD</h2>`). The app has no payment integration — price is a dummy value hardcoded to `1` by the frontend. The `SalesView.post()` currently requires price via `if not (... price is not None ...)`, forcing the frontend to always send it even though it's meaningless.

Similar apps in the project (e.g. `seema_rohan`, `tony_thoa`) either omit price from their email templates or disable its display entirely. This change brings loris in line with that pattern.

## Goals / Non-Goals

**Goals:**
- Remove price display from the loris confirmation email
- Make `price` optional in the `SalesView.post()` validation so the frontend is not required to send a dummy value
- Keep `price` on the model (no migration) to avoid schema changes

**Non-Goals:**
- Removing the `price` field from the database model (separate change if desired later)
- Changing the `will_ryan_airport_transfers` app (same bug; scoped separately)
- Changing `tools.send_sucess_mail()` signature (price param stays but is simply unused by this template)

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Template approach | Remove price block entirely instead of `{% if price %}` | Price has no business meaning here — no scenario where it should be shown. Conditional would imply it's sometimes valid. |
| Validation change | Switch from `price is not None` to not checking price at all | Price is vestigial. No reason to require a field that does nothing. Backend should accept `price=0` (default) gracefully. |
| Model field | Keep `Sale.price` as-is (no migration) | Removing a DB field is a breaking schema change with zero benefit. The field does no harm and avoids an unnecessary migration. |
| tools.send_sucess_mail | Keep passing price, template ignores it | Changing the shared function signature would ripple to 5+ other apps. Minimal change principle: only touch what's broken. |

## Risks / Trade-offs

- **Frontend still sends price** → No breakage; the POST body is backward compatible. Price is accepted and stored but simply not displayed.
- **Admin panel still shows price** → The Django admin (if used) still displays the `price` column. No change planned — this is a customer-facing email issue only.
- **No migration** → Risk-free. The `price` column stays in the DB with `default=0`.
