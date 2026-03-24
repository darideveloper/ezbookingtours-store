# Tasks: Fix Hotel Name Saving

## Phase 1: Reproduction & Analysis
- [x] Add reproduction test case to `seema_rohan/tests.py` using the payload provided by the user.
- [x] Run tests and confirm the failure.
- [x] Analyze the parsing logic during the failing test.

## Phase 2: Implementation
- [x] Refine the hotel parsing logic in `Sale.from_payload()` in `seema_rohan/models.py` to ensure it correctly captures the custom hotel name.
- [x] Add a more robust lookup for the `Hotel` model record that does not accidentally clear a valid custom name.

## Phase 3: Validation
- [x] Run the reproduction test and confirm it passes.
- [x] Run all tests in `seema_rohan/tests.py` and confirm no regressions.
- [x] Run all project tests if applicable.
