# Proposal: Simplify Seema Rohan Payload Parsing

Replace the long `if-elif` chain in `Sale.from_payload` with a structured mapping dictionary and a more efficient processing loop.

## Why
The current `from_payload` implementation is hard to maintain due to its lengthy `elif` chain. It makes adding new fields cumbersome and prone to errors.

## What Changes
- Refactor the parsing loop in `seema_rohan/models.py` to use a `MAPPING` dictionary for simple fields.
- Use a `SEQUENCE_MAPPING` to handle duplicate labels (Airline, Flight) in a consistent way.
- Ensure all current functionality (date/time parsing, hotel logic) remains unchanged but is expressed more cleanly.

## Impact
- Affected specs: `seema-rohan-refactor`
- Affected code: `seema_rohan/models.py`
