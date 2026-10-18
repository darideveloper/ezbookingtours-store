## 1. Settings and Backend

- [x] 1.1 Add `EMAIL_REPLY_TO = os.getenv("EMAIL_CLIENT")` to `ezbookingtours_store/settings.py` next to the other email settings (line ~172-178), with a short comment explaining it is the Reply-To source (reuses `EMAIL_CLIENT`, no new env var).
- [x] 1.2 Create `ezbookingtours_store/email_backend.py` with `ReplyToEmailBackend(EmailBackend)` that overrides `send_messages` to inject `reply_to = [settings.EMAIL_REPLY_TO]` on any message with an empty `reply_to`, skipping injection entirely when `EMAIL_REPLY_TO` is falsy (per design.md D2/D3).
- [x] 1.3 Change `EMAIL_BACKEND` in `settings.py` to `"ezbookingtours_store.email_backend.ReplyToEmailBackend"`.
- [x] 1.4 Add a short note to the README email/SMTP section: outgoing emails carry `Reply-To = EMAIL_CLIENT` via `ReplyToEmailBackend`, which auto-injects it (no new env var).

## 2. Shared Util

- [x] 2.1 In `ezbookingtours_store/tools.py::send_sucess_mail`, add `reply_to=[settings.EMAIL_CLIENT] if settings.EMAIL_CLIENT else []` to both `EmailMultiAlternatives` calls (client at ~line 103, admin at ~line 116).

## 3. Direct Send Sites

- [x] 3.1 `digitalrealty/views.py` (~line 150): add `reply_to` to the `EmailMultiAlternatives` loop, guarded for empty `EMAIL_CLIENT`.
- [x] 3.2 `rohan_karisma/views.py` (~line 150): same change as 3.1.
- [x] 3.3 `ashley_jonathan/views.py` (~line 125): add `reply_to=[EMAIL_CLIENT]` (file already computes `EMAIL_ADMIN = settings.EMAIL_CLIENT or EMAIL_USER` — reuse value if cleaner).
- [x] 3.4 Legacy `store/tools.py` (~line 23): add `reply_to` to the admin-notification `EmailMultiAlternatives`.
- [x] 3.5 `store/views.py` test endpoint (~line 289): use `EmailMessage(..., reply_to=[EMAIL_CLIENT])` (the original `send_mail` call could not accept `reply_to`).

## 4. Tests

- [x] 4.1 Add unit test for `ReplyToEmailBackend`: message without `reply_to` gets `EMAIL_CLIENT` injected; message that already has `reply_to` is not overwritten; empty `EMAIL_REPLY_TO` sends without injection (mock SMTP or use `console.EmailBackend` subclass basis).
- [x] 4.2 Update/extend existing mocked tests (`digitalrealty/tests.py:86,101`, `ashley_jonathan/tests.py:300`) to assert the mock receives/sets `reply_to = [EMAIL_CLIENT]`.
- [x] 4.3 Verify local dev without `EMAIL_CLIENT` doesn't fail: run existing test suite (`manage.py test`) with `EMAIL_CLIENT` removed from test env/fallback.

## 5. Validation

- [x] 5.1 Run `manage.py check` and the full test suite locally; all green.
- [x] 5.2 Exercise `/store/test-email/` and confirm the sent email carries `Reply-To: <EMAIL_CLIENT>`; covered by regression test `store/tests.py::test_test_email_sets_reply_to`.
- [x] 5.3 Confirm a sale flow sends both buyer and admin copies with the header; covered by `ashley_jonathan/tests.py::test_admin_copy_uses_email_client`.
