## Why

Three archive-time sync defects left the specification set out of sync with the archived changes. The `loris-app` capability declared by `2026-07-16-create-loris-app` was never materialised into `openspec/specs/`, and two specs were copied from their deltas verbatim instead of being rewritten into the standard spec structure. As a result `openspec validate --strict --specs` reports 14 passed / 2 failed, and the loris app has no capability spec despite being fully implemented.

## What Changes

- Add the missing `loris-app` capability specification, recovering its six requirements from the archived `2026-07-16-create-loris-app` delta.
- Repair `openspec/specs/fix-details-time-parsing/spec.md` to carry the standard `# <name> Specification`, `## Purpose`, and `## Requirements` structure. Requirement wording is preserved unchanged.
- Repair `openspec/specs/hide-email-price/spec.md` the same way, removing the leftover `## ADDED Requirements` delta heading. Requirement wording is preserved unchanged.
- No requirement semantics change anywhere: this is structural repair plus one recovered capability.

## Capabilities

### New Capabilities

- `loris-app`: Django app packaging, HTTP endpoints, email dispatch, models, admin registration, and test coverage for the Lori's Birthday transfer app.

### Modified Capabilities

None. `fix-details-time-parsing` and `hide-email-price` keep their existing requirements; only the surrounding document structure is corrected, which is not a spec-level behaviour change.

## Impact

- Affected artifacts: new `openspec/specs/loris-app/spec.md`; structural repair of `openspec/specs/fix-details-time-parsing/spec.md` and `openspec/specs/hide-email-price/spec.md`.
- Affected code: none.
- Validation target: `openspec validate --strict --specs` passes 16/16.
- Out of scope: the capability-name/change-name difference (`hide-email-price` vs. change `hide-loris-price`) is intentional and left as-is, since change names and capability names are independent; and the eight first-party apps that have no capability spec are a separate coverage decision.
