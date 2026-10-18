## Context

All outgoing mail flows through `django.core.mail.backends.smtp.EmailBackend` configured from env vars (see `ezbookingtours_store/settings.py:172-183`). There are three sending patterns in the codebase:

1. **Shared util** `ezbookingtours_store/tools.py::send_sucess_mail()` — used by 7 apps, sends a client copy and an admin copy (`EMAIL_CLIENT`) over one connection.
2. **Direct `EmailMultiAlternatives`** in `digitalrealty/views.py`, `rohan_karisma/views.py`, `ashley_jonathan/views.py`, and legacy `store/tools.py`.
3. **`send_mail` test endpoint** in `store/views.py` (`test-email/`).

No send site currently sets `reply_to`, so replies land in the SMTP account inbox. Deliverability constraints mean the `From` address cannot change (SPF/DKIM of `EMAIL_HOST_USER`).

## Goals / Non-Goals

**Goals:**
- Buyer "Reply" targets the admin inbox (`EMAIL_CLIENT`) on every email, including admin copies and the test endpoint.
- Future send sites are covered automatically without developer discipline.
- No new environment variables; reuse `EMAIL_CLIENT`.
- Local/dev runs without email config must not crash.

**Non-Goals:**
- Per-brand or per-event Reply-To routing (explicitly rejected during exploration — single address for all).
- Changing `From`, `EMAIL_HOST_USER`, or SMTP authentication.
- New env var (`EMAIL_REPLY_TO`) — rejected; `EMAIL_CLIENT` hardcoded as the source.
- Delivery logging/reporting changes.

## Decisions

**D1. Two-layer enforcement: explicit + backend.**
- *Alternative considered: explicit only* — visible and greppable, but the `test-email/` endpoint, legacy `store/tools.py`, and future apps could silently miss it (the codebase already shows drift: 7 apps share a util, others copy-paste).
- *Alternative considered: backend only* — one place, but a reader of `views.py` sees no header; obscures intent.
- Decision: pass `reply_to=[settings.EMAIL_CLIENT]` explicitly at each current send site, AND add a custom backend as a safety net.

**D2. Backend implementation: subclass `django.core.mail.backends.smtp.EmailBackend`.**
```python
# ezbookingtours_store/email_backend.py
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend

class ReplyToEmailBackend(EmailBackend):
    def send_messages(self, email_messages):
        reply_to = settings.EMAIL_REPLY_TO or None
        if reply_to:
            for message in email_messages:
                if not message.reply_to:
                    message.reply_to = [reply_to]
        return super().send_messages(email_messages)
```
- `EMAIL_BACKEND = "ezbookingtours_store.email_backend.ReplyToEmailBackend"` in settings.
- `EMAIL_REPLY_TO = os.getenv("EMAIL_CLIENT")` as the single derived setting — no new env var, central reference point.
- Locmem backend used in tests does not inherit this; injection is exercised via unit tests on the backend itself.

**D3. Empty-config guard.** In `send_sucess_mail()` (already tolerant) and in the backend: if `EMAIL_REPLY_TO` is falsy, skip injection rather than crash — protects local dev where `EMAIL_CLIENT` is unset. Explicit `reply_to=[settings.EMAIL_CLIENT]` at call sites likewise degrades to an empty list.

**D4. Apply to both client and admin copies.** Consistent header everywhere (user decision: both). No special-casing in `tools.py`.

## Risks / Trade-offs

- [Implicit magic: developer reading `views.py` doesn't see backend injection] → explicit `reply_to=` at current sites; document the backend in README notes/design.
- [Some receivers display `Reply-To` prominently and may confuse it with `From`] → acceptable; keeps `From` intact for deliverability.
- [Admin copy also gets `Reply-To` pointing to itself — replying to your own admin mail sends back to admin] → accepted per user decision (D4); behavior consistent, not harmful.
- [Tests mocking `EmailMultiAlternatives` don't exercise the backend] → backend gets its own unit test; existing tests keep locmem backend.
- [Whitenoise/anyio-style settings change could break deployment if module import fails] → no external imports; only `django.core.mail.backends.smtp`.

## Migration Plan

1. Add `email_backend.py` + settings change; deploy (no data migration, no env change).
2. Update util and direct send sites.
3. Rollback: revert `EMAIL_BACKEND` to `django.core.mail.backends.smtp.EmailBackend` — instant, because the header is the only behavioral difference.

## Open Questions

- None outstanding — scope/address/source/coverage were decided during exploration (single address = `EMAIL_CLIENT`, both copies, hardcoded, explicit + backend).
