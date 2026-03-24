# Proposal: Simplify Seema Rohan Redirection Flow

## Problem
The `seema_rohan` app currently has a `/seema-rohan/success/<sale_id>/` endpoint (`SuccessView`) that marks a sale as paid and redirects the user back to the frontend with `?thanks=true`. However, since this app doesn't involve any payment logic on the backend (bookings are just saved), this intermediate step is unnecessary. The frontend should receive a direct redirect to the final "thanks" page upon successful booking submission.

## Proposed Change
1.  **Remove `SuccessView`**: Delete the `SuccessView` from `seema_rohan/views.py`.
2.  **Remove success path**: Delete the `success/` path from `seema_rohan/urls.py`.
3.  **Update `BuyView`**:
    - Ensure the `post` method in `BuyView` keeps the sale as `is_paid = False` (default), as payments are managed manually in cash outside the app.
    - Update the `redirect` URL returned in the JSON response to point directly to the frontend host with the `thanks=true` flag.
    - Implement the "clean from host" logic to ensure the redirect points to the base frontend URL.

## Impact
- **Backend**: Reduced complexity and fewer endpoints.
- **Frontend**: Simplified flow as it no longer needs to hit a backend "success" page before returning to its own "thanks" state.
- **Data**: Bookings will be marked as paid immediately upon successful submission.

## Capability/Spec Changes
- **Modified**: `seema-rohan-refactor` specification.
    - **Remove** `Requirement: Direct Success Redirect`.
    - **Add/Modify** requirements for immediate confirmation and direct frontend redirect.
