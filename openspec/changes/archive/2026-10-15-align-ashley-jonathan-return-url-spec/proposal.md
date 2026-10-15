## Why

Commit `fab088c` made ashley-jonathan honor the frontend's legacy `url` field when `from-host` is absent, because the deployed dmc.com widget sends `url` rather than `from-host`. The merged specification at `openspec/specs/ashley-jonathan-airport-transfers/spec.md` still describes only `from-host`, so it now misstates shipped behavior for exactly the case that failed in production.

## What Changes

- Document `url` as an accepted legacy alias for the frontend-supplied return URL, with `from-host` taking precedence when both are present.
- Qualify the free-arrival fallback scenario: fall back to `ASHLEY_JONATHAN_PAGE` only when neither `from-host` nor `url` yields a valid URL.
- Add `url` to the set of inputs evaluated by the invalid-return-URL rejection scenario.
- Documentation only — no code, model, admin, template, or deployment changes.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `ashley-jonathan-airport-transfers`: the free-arrival and frontend-return-URL requirements are corrected to describe the accepted input fields (`from-host`, legacy `url`) and their precedence.

## Impact

- Affected artifacts: `openspec/specs/ashley-jonathan-airport-transfers/spec.md` (via delta at archive time).
- Affected code: none. Behavior already shipped in `ashley_jonathan/views.py` (`fab088c`).
- Excluded, having no spec-level behavior change: logging/observability work in `ashley_jonathan/views.py` and `ezbookingtours_store/settings.py`, Dockerfile env additions, and the `EMAIL_CLIENT` admin-recipient refinement.
