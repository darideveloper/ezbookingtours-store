## Context

The ashley-jonathan booking widget deployed at `cancunconciergedmc.com` posts its payload with a top-level `url` field set to `window.location.href`; it does not send `from-host`. Commit `f236555` implemented the return-URL feature reading only `from-host`, so in production the request fell back to the hardcoded `ASHLEY_JONATHAN_PAGE` default. Commit `fab088c` resolved this by reading `from-host` first and falling back to the legacy `url`. The specification merged from the `ashley-jonathan-dynamic-redirect` change still documents `from-host` only, so it no longer describes the shipped system.

## Goals / Non-Goals

**Goals:**
- Make the specification describe the accepted input fields (`from-host`, legacy `url`) and their precedence.
- Keep the documented fallback and validation rules consistent with shipped behavior.
- Close the drift with no code change, since the behavior already ships.

**Non-Goals:**
- No changes to `ashley_jonathan/views.py` logic, tests, models, admin, or templates.
- No documentation of observability, Dockerfile, or email-recipient refinements — those carry no spec-level behavior change.
- No requirement that the frontend stop sending `url`; backwards compatibility is retained deliberately.

## Decisions

- **Document `url` as a legacy alias rather than replacing it.** Rationale: the widget is deployed outside this repository and cannot be atomically updated; the backend must keep accepting both. Alternative of requiring a frontend change was rejected because it would leave production broken until the WordPress site is redeployed.
- **State precedence explicitly (`from-host` wins).** Rationale: both fields may be present (`url` is always sent by the current widget), so the resolution order is observable behavior and must be specified, not implied.
- **Qualify the fallback scenario by outcome ("neither yields a valid URL") rather than by field presence.** Rationale: the previous wording keyed off `from-host` alone, which became false once `url` was honored.
- **No code tasks.** The delta is documentation-only; verification is limited to confirming the spec matches `ashley_jonathan/views.py` and the existing tests.

## Risks / Trade-offs

- [Risk] Recording a legacy alias in the spec could be mistaken for a permanent contract → Mitigation: label it explicitly as legacy and note the frontend may migrate to `from-host` later.
- [Risk] Spec-only change could drift again if the frontend changes → Mitigation: the alias behavior is covered by tests `test_free_arrival_with_url_fallback`, `test_free_arrival_from_host_beats_url`, and `test_paid_booking_propagates_url_fallback`.
- [Trade-off] Accepting two field names adds a small amount of ambiguity to the request contract → Mitigation: precedence is deterministic and documented.
