# Tasks: Fix Hotel Name Saving

## Phase 1: Reproduction & Analysis
- [ ] Add reproduction test case to `seema_rohan/tests.py` using the payload provided by the user.
- [ ] Run tests and confirm the failure.
- [ ] Analyze the parsing logic during the failing test.

## Phase 2: Implementation
- [ ] Refine the hotel parsing logic in `Sale.from_payload()` in `seema_rohan/models.py` to ensure it correctly captures the custom hotel name.
- [ ] Add a more robust lookup for the `Hotel` model record that does not accidentally clear a valid custom name.

## Phase 3: Validation
- [ ] Run the reproduction test and confirm it passes.
- [ ] Run all tests in `seema_rohan/tests.py` and confirm no regressions.
- [ ] Run all project tests if applicable.
