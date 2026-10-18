## Why

Outgoing emails are sent with `From = EMAIL_HOST_USER` and no `Reply-To` header, so when buyers hit "Reply" their answer goes to the SMTP account inbox instead of the monitored admin inbox (`EMAIL_CLIENT`). The business needs customer replies routed to the admin inbox without risking deliverability by changing the `From` address.

## What Changes

- Add a `Reply-To: EMAIL_CLIENT` header to every outgoing email (client confirmation and admin copy alike).
- Update the shared `send_sucess_mail()` util in `ezbookingtours_store/tools.py` to pass `reply_to=[settings.EMAIL_CLIENT]` on both sends.
- Update the apps that bypass the shared util and construct `EmailMultiAlternatives` directly: `digitalrealty.views`, `rohan_karisma.views`, `ashley_jonathan.views`, `store/tools.py`, and the `send_mail` call in `store/views.py` (`test-email/` endpoint).
- Add a custom SMTP backend (`ReplyToEmailBackend`) that injects `Reply-To = EMAIL_CLIENT` into any message that does not already define one, and point `EMAIL_BACKEND` at it — a safety net that keeps future apps and edge-case sends covered.
- Guard against an empty/unset `EMAIL_CLIENT` so local development without email config does not crash.

Explicitly NOT changing: the `From` address (stays `EMAIL_HOST_USER`), no new env vars (config value is reused `EMAIL_CLIENT`), single Reply-To for all apps (no per-brand routing).

## Capabilities

### New Capabilities
- `email-reply-to`: Reply-To header behavior on all outgoing emails — explicit passing in send call sites and backend-level injection as a safety net, including the empty-config guard.

### Modified Capabilities

## Impact

- **Code**: `ezbookingtours_store/settings.py` (EMAIL_BACKEND path), new `ezbookingtours_store/email_backend.py`, `ezbookingtours_store/tools.py`, `digitalrealty/views.py`, `rohan_karisma/views.py`, `ashley_jonathan/views.py`, `store/tools.py`, `store/views.py`.
- **Behavior**: Every email gains a `Reply-To` header pointing at `EMAIL_CLIENT`; replies from buyers land in the admin inbox instead of the SMTP account.
- **Risk**: Low — header-only change, no `From`/auth changes, no schema or API changes. Existing tests that mock `EmailMultiAlternatives` may need assertions updated.
- **Dependencies**: None new; stock Django `EMAIL_BACKEND` subclass only.
