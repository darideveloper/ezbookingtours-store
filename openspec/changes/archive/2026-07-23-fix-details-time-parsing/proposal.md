## Why

The details parsing logic uses `line.split(":")` which splits on ALL colons, not just the first one. When a detail value contains a colon — such as times like "15:13" — the value is truncated to just "15". This affects customer confirmation emails showing "Arriving time: 15" instead of "Arriving time: 15:13".

## What Changes

- Fix detail parsing in `loris/views.py` to preserve values containing colons (e.g., times like "15:13")
- Update loris tests to verify time values with colons are preserved correctly

## Capabilities

### New Capabilities
- `fix-details-time-parsing`: Fix the colon-splitting logic in booking detail parsing to preserve time values containing colons (e.g., "15:13")

### Modified Capabilities
<!-- No existing specs are affected -->

## Impact

- `loris/views.py:108` — detail parsing logic to preserve full values containing colons
- `loris/tests.py` — add test verifying time values with colons are preserved in the email
