# Proposal: Fix Hotel Name Saving

## Problem
In the `seema_rohan` app, the custom hotel name (`hotel_name` field) is not correctly saved in the database when the hotel provided by the frontend is not found in the `Hotel` model.

This typically happens when the payload contains both `Hotel: other` and `Hotel name: [custom hotel]`.

## Solution
The fix involves refining the parsing logic in `Sale.from_payload()` in `seema_rohan/models.py`.

Specifically, we need to ensure that:
1. `Hotel name` is always captured if present, and it SHOULD NOT be overwritten by `Hotel: other`.
2. The logic for looking up a `Hotel` model record and deciding whether to keep the `hotel_name` field is robust.

## Strategy
1. **Reproduction:** Add a new test case to `seema_rohan/tests.py` that specifically mimics the problematic frontend payload.
2. **Analysis:** Confirm why the current parsing logic fails.
3. **Fix:** Update `Sale.from_payload()` to correctly capture and prioritize the custom hotel name when the hotel is "other".
4. **Verification:** Ensure all tests pass, including the new reproduction case.

## Impact
- **Database:** No schema changes.
- **API:** No changes to API endpoints or frontend payloads.
- **Models:** Updated `Sale.from_payload()` class method.
