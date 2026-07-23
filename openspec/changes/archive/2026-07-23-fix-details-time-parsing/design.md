## Context

The loris app uses `line.split(":")` to split each comma-separated booking detail segment into a name/value pair. This splits on ALL colons, so any value containing a colon — such as times in HH:MM format (e.g., "15:13") — gets truncated: the value becomes just the part before the second colon ("15"), and the minutes are lost. This is visible in customer confirmation emails showing "Arriving time: 15" instead of "Arriving time: 15:13".

## Goals / Non-Goals

**Goals:**
- Fix the parsing logic in loris to preserve values containing colons
- Strip leading/trailing whitespace from parsed name and value parts
- Add/update loris tests to prevent regression

**Non-Goals:**
- Changing the email templates
- Changing the data format sent by the frontend
<!-- no additional non-goals -->

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Split limit | `split(":", 1)` (maxsplit=1) | Default `split(":")` breaks on every colon. Limiting to the first split is the minimal fix with zero risk — the name never contains colons. |
| Whitespace cleanup | `.strip()` on both name and value | The comma-split leaves leading spaces on all lines after the first. `.strip()` makes rendered output clean. |
| Test approach | Add test with time value | Time values with colons need regression coverage. Existing tests don't cover this edge case. |

## Risks / Trade-offs

- **No data migration needed** → The bug is in display/parsing only. Raw `details` is stored in `full_data` on the Sale model. Only the parsed `details_objs` used for email rendering is affected. Fixing the parser fixes future renders; historical emails are already sent.
- **Backward compatibility** → No change to POST body format or database schema. Zero risk.
