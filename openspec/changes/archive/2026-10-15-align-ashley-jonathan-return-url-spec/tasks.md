## 1. Spec Alignment

- [x] 1.1 Confirm `openspec/changes/align-ashley-jonathan-return-url-spec/specs/ashley-jonathan-airport-transfers/spec.md` matches shipped behavior for `from-host` and legacy `url`
- [x] 1.2 Re-read the Free Arrival Transfer Booking and Frontend Return URL Handling requirements from the main spec and verify precedence wording is exact

## 2. Verification

- [x] 2.1 Cross-check the delta against `ashley_jonathan/views.py` (`resolve_return_base` call sites for free and paid flows)
- [x] 2.2 Confirm `ashley_jonathan/tests.py` covers the alias and precedence via `test_free_arrival_with_url_fallback`, `test_free_arrival_from_host_beats_url`, and `test_paid_booking_propagates_url_fallback`
- [x] 2.3 Run `./venv/bin/python manage.py test ashley_jonathan --keepdb` and confirm the suite passes
- [x] 2.4 Run `openspec validate align-ashley-jonathan-return-url-spec --strict`
