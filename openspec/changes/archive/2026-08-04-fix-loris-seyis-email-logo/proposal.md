## Why

The confirmation emails for the `loris` and `seyis` apps are missing their branding logo. The `loris` template references `https://cancunconciergedmc.com/loris/imgs/logo.png`, which returns **404** (the file was never uploaded to the WordPress frontend host), so email clients render a broken image. The `seyis` template (cloned from `loris`) omits the logo entirely. Both apps should use the site-wide logo at `https://cancunconciergedmc.com/imgs/logo.png`, which is confirmed to serve with HTTP 200.

## What Changes

- Change the logo `src` in `loris/templates/loris/mail.html` from `https://cancunconciergedmc.com/loris/imgs/logo.png` to `https://cancunconciergedmc.com/imgs/logo.png`.
- Add the same `<img>` logo element to `seyis/templates/seyis/mail.html` using `https://cancunconciergedmc.com/imgs/logo.png`.
- No other apps' email templates are modified; this is scoped to `loris` and `seyis` only.

## Capabilities

### New Capabilities
- `loris-confirmation-email`: Spec for the loris confirmation email template, including the brand logo requirement.
- `seyis-confirmation-email`: Spec for the seyis confirmation email template, including the brand logo requirement.

### Modified Capabilities
- None. The brand-logo requirement for seyis is fully covered by the new `seyis-confirmation-email` capability.

## Impact

- `loris/templates/loris/mail.html` — logo URL updated.
- `seyis/templates/seyis/mail.html` — logo element added.
- No model, view, or API changes. `tools.send_sucess_mail` is untouched.
- Requires network access to `cancunconciergedmc.com` for email clients to fetch the logo (already the established pattern across other apps).
