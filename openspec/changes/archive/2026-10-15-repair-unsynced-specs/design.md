## Context

The repository archives completed changes into `openspec/changes/archive/` and merges their delta specs into `openspec/specs/`. Three defects from that step remain visible in `openspec validate --strict --specs` (14 passed, 2 failed):

- `2026-07-16-create-loris-app` declared capability `loris-app` with six requirements, but `openspec/specs/loris-app/` was never created. The `loris` Django app is fully implemented (`loris/models.py`, `views.py`, `urls.py`, `admin.py`, `tests.py`, `templates/`), so this is a missing spec, not missing code.
- `openspec/specs/hide-email-price/spec.md` is a byte-identical copy of its delta and begins with `## ADDED Requirements`.
- `openspec/specs/fix-details-time-parsing/spec.md` is its delta with the `## ADDED Requirements` line stripped, leaving no top-level `## Purpose`/`## Requirements` sections.

`openspec validate` cannot re-check archived changes (`openspec validate 2026-07-16-create-loris-app` returns `Unknown item`), so these defects are only detectable by inspecting main specs.

## Goals / Non-Goals

**Goals:**
- Recover the `loris-app` capability into `openspec/specs/loris-app/spec.md` exactly as declared by the archived change.
- Restore the standard document structure for the two malformed specs without altering requirement wording.
- Reach 16/16 on `openspec validate --strict --specs`.

**Non-Goals:**
- No changes to `loris/` or any application code, models, URLs, admin, or templates.
- No requirement rewording, addition, or removal in `fix-details-time-parsing` or `hide-email-price`.
- No renaming of the `hide-email-price` capability directory.
- No capability specs created for the eight apps that currently have none; that is a separate coverage decision.

## Decisions

- **Recover `loris-app` content verbatim from the archived delta rather than re-authoring it.** Rationale: the archived change is the authoritative record of what was approved; inventing wording would create undocumented requirements. The only addition is the standard `# loris-app Specification` / `## Purpose` / `## Requirements` wrapper.
- **Repair the two malformed specs by adding the missing wrapper sections only.** Rationale: their requirement text already exists and was already approved; the failure is purely structural, so touching requirement wording would misrepresent the repair as a behaviour change.
- **Model the two repairs as implementation tasks rather than delta requirements.** Rationale: `MODIFIED` deltas require restating full requirement content, which would risk re-introducing drift and would falsely imply the requirements changed. Only `loris-app` is a genuine spec addition and therefore carries a delta.
- **Leave the `hide-email-price` capability name unchanged.** Rationale: capability names and change names are independent in this schema, so the difference from change `hide-loris-price` is not a defect; renaming would add churn and break the archived reference.
- **Regenerate `## Purpose` text as `TBD - created by archiving change ...`, matching the existing convention** used by specs such as `loris-confirmation-email`.

## Risks / Trade-offs

- [Risk] Recovered `loris-app` content could describe behaviour that has since drifted → Mitigation: the six requirements are verified against `loris/` during the tasks phase before archiving.
- [Risk] A future archive could repeat the malformed-copy defect → Mitigation: the strict validation gate now covers all 16 specs, so a repeat surfaces immediately; the root cause is a manual sync step, not tooling.
- [Trade-off] Repairing main specs directly rather than through `MODIFIED` deltas is a deliberate deviation from the normal sync-only path → Mitigation: justified because the content is unchanged and the defect originated in the sync step itself; the change record documents it.
