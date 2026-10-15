## Context

`ashley_jonathan/views.py` currently hardcodes the post-booking redirect to `ASHLEY_JONATHAN_PAGE` (`SaleView.post` free flow `:147`, `SaleDoneView.get` `:206`). Paid flow uses an intermediate backend callback (`{HOST}/ashley-jonathan/sale/<id>` as Stripe `url_success` `:164`) so the sale can be marked done and emails sent before the final 302. `seema_rohan` and `wedding` apps already solve the multi-page problem with a frontend-supplied `from-host` field (`seema_rohan/views.py:33,56`, `wedding/views.py:64,95,287`). This change ports that proven pattern to ashley-jonathan in a backward-compatible way.

## Goals / Non-Goals

**Goals:**
- Allow the booking widget on any landing page to get users back to that same page + `?done=true` after free or paid confirmation.
- Keep zero-config fallback to `ASHLEY_JONATHAN_PAGE` for existing integrations.
- Preserve sale-completion guarantees (mark done + emails before final redirect) and block open redirects.

**Non-Goals:**
- No Stripe webhook replacement; keep the backend `SaleDoneView` callback.
- No change to `Sale` model, admin, email templates, or price logic.
- No change to `rohan_karisma` / `digitalrealty` behavior.

## Decisions

- **Field name `from-host` (top-level JSON, optional).** Rationale: consistent with `seema_rohan` / `wedding` frontend contract; no new naming to document. Alternative `return_url` rejected to avoid diverging contracts.
- **Sanitize + validate, then strip to origin+path.** Trim whitespace, strip trailing `/`, drop existing query/fragment, require `http(s)://` with a network host. Invalid or missing value → fall back to `ASHLEY_JONATHAN_PAGE`. Alternative allowlist-env-var considered but deferred; initial rule (scheme + host present, no credentials) blocks the dangerous cases while staying config-free.
- **Propagate via `?from=` on the intermediate callback.** `url_success = {HOST}/ashley-jonathan/sale/<id>?from=<urlencoded frontend_base>`. `SaleDoneView` reads `request.GET.get("from")`, re-validates, redirects to `{base}?done=true`. Alternative of pointing Stripe directly at the frontend rejected — would skip `sale_done` update and emails.
- **Email `cta` stays `ASHLEY_JONATHAN_PAGE`.** Receipt link should point at the canonical page, not a potentially ephemeral clone URL.
- **Append exactly `?done=true`.** Matches current frontend expectation and existing tests (`tests.py:81,175`).

## Risks / Trade-offs

- [Risk] Open redirect via crafted `from-host` → Mitigation: strict validation (http/https, host required, strip query/fragment); fallback to env default on failure.
- [Risk] Stripe `url_success` length/encoding issues with long `?from=` → Mitigation: pass only origin+path (no query), URL-encode once; existing `wedding` app already ships this shape.
- [Risk] Frontend never sends the field → Mitigation: behavior identical to today; covered by existing tests.
- [Trade-off] Two sources of truth (env + per-request) → Mitigation: clear precedence (valid `from-host` wins, else env), documented in spec and tasks.

## Migration Plan

1. Deploy backend (backward compatible, no env change required).
2. Document the optional contract: frontend may send `from-host: window.location.origin + window.location.pathname` in the sale POST (no widget code change in this repo; backend-only change).
3. Rollback: revert backend or stop sending the field — both restore env-fixed behavior.
