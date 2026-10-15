## Why

The ashley-jonathan post-payment redirect is currently hardcoded to the `ASHLEY_JONATHAN_PAGE` env var (`https://cancunconcierge.net/ashley-jonathan-airport-transfers?done=true`). Any clone, staging, or alternate landing page showing the same booking widget redirects users to the wrong page after payment. Allowing the frontend incoming page to supply the return URL (with `?done=true` appended) makes the widget reusable without backend/env changes.

## What Changes

- Accept an optional frontend-supplied return URL in `POST /ashley-jonathan/sale/` (`from-host` field, consistent with `seema_rohan` / `wedding` apps).
- Free arrival flow: return `{frontend_base}?done=true` when a valid frontend URL is supplied; otherwise fall back to `{ASHLEY_JONATHAN_PAGE}?done=true` (current behavior).
- Paid departure/round-trip flow: propagate the frontend base through the Stripe `url_success` callback as `?from=<frontend_base>` on `{HOST}/ashley-jonathan/sale/<id>`, so `SaleDoneView` can redirect to `{frontend_base}?done=true` after marking the sale done and sending emails.
- `GET /ashley-jonathan/sale/<sale_id>/`: honor validated `?from=` param for the final redirect; fall back to `ASHLEY_JONATHAN_PAGE` when absent or invalid.
- Validate the frontend-supplied URL (http/https only, host required, no credentials) to prevent open redirects; strip any existing query/fragment before appending `?done=true`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `ashley-jonathan-airport-transfers`: redirect targets for free-booking confirmation and paid payment-completion callback change from env-fixed to frontend-supplied-with-env-fallback.

## Impact

- Affected code: `ashley_jonathan/views.py` (`SaleView.post`, `SaleDoneView.get`), `ashley_jonathan/tests.py`.
- No DB migration; no change to `Sale` model or admin.
- Frontend widget contract: may optionally send `from-host`; existing clients sending no field keep current behavior (non-breaking).
- Systems: Stripe Flask API `url_success` payload gains a `?from=` query param; final user-facing redirect may vary per request.
