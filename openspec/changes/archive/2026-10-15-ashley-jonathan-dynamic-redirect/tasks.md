## 1. Redirect Helper

- [x] 1.1 Add `resolve_return_base(from_host)` helper in `ashley_jonathan/views.py` to trim, strip trailing slash, drop query/fragment, validate http/https with host, and fall back to `ASHLEY_JONATHAN_PAGE`
- [x] 1.2 Unit-cover helper edge cases (missing, non-http, no host, credentials, query/fragment stripping)

## 2. Sale Booking Flow

- [x] 2.1 Update `SaleView.post` free arrival branch to return `{resolved_base}?done=true` in `stripe_url`/`url` response
- [x] 2.2 Update `SaleView.post` paid branch to set Stripe `url_success` to `{HOST}/ashley-jonathan/sale/<id>?from=<encoded base>` when valid, plain callback otherwise
- [x] 2.3 Keep email `cta` on `ASHLEY_JONATHAN_PAGE` and preserve `user` remap + Stripe error handling

## 3. Payment Callback

- [x] 3.1 Update `SaleDoneView.get` to honor validated `?from=` for the final `?done=true` redirect with env fallback
- [x] 3.2 Preserve preview mode, 404 for unknown sale, and mark-done + email ordering

## 4. Tests and Verification

- [x] 4.1 Extend `ashley_jonathan/tests.py`: free with `from-host`, free fallback, paid `url_success` with `?from=`, callback redirect to `from` and to env fallback, invalid-URL rejection
- [x] 4.2 Run `python manage.py test ashley_jonathan` and existing suite for regressions
