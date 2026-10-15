## 1. Recover loris-app Capability

- [x] 1.1 Add `openspec/specs/loris-app/spec.md` with the standard wrapper (`# loris-app Specification`, `## Purpose`, `## Requirements`) and the six requirements from the archived `2026-07-16-create-loris-app` delta
- [x] 1.2 Verify the recovered requirements against `loris/` (models.py, urls.py, views.py, admin.py, apps.py) and confirm none describe behaviour that no longer exists

## 2. Repair Malformed Specs

- [x] 2.1 Repair `openspec/specs/fix-details-time-parsing/spec.md` by adding the standard wrapper sections, leaving requirement wording byte-identical
- [x] 2.2 Repair `openspec/specs/hide-email-price/spec.md` the same way, removing the leftover `## ADDED Requirements` heading

## 3. Verification

- [x] 3.1 Run `openspec validate --strict --specs` and confirm 16 passed / 0 failed
- [x] 3.2 Confirm no requirement text changed in the two repaired specs by diffing against their archived deltas (only wrapper lines should differ)
- [x] 3.3 Run `./venv/bin/python manage.py test loris --keepdb` to confirm the recovered `loris-app` spec still matches reality
