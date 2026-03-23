# Design: Refactor seema_rohan app to remove payment logic

## Architecture

The `seema_rohan` app will transition from a payment-based system to a simple booking system.

### Model Changes
- **Remove**: `VipCode`, `FreeDays`, `FreeDaysCategory`.
- **Simplify**: `Sale`. We can keep `is_paid` and `stripe_data` if needed for database compatibility or historical data, but for new sales, they will be set to `True` and `None` respectively. The user explicitly mentioned "all related to vip code and free dates should be removed", so `vip_code` should be removed from `Sale` as well.

### View Changes
- **BuyView**:
    - Receives sale data.
    - Saves the `Sale` object (always marked as paid/no VIP code required).
    - Sends the confirmation email immediately.
    - Returns a JSON response with a redirect to the `SuccessView`.
- **SuccessView**:
    - Continues to redirect to the original host with `thanks=true`.

### URL Changes
- Remove `validate-vip-code/` and `free-dates/`.

## Data Migration
Since this involves model removal, a Django migration will be necessary. Existing data for `VipCode` and `FreeDays` will be lost.
The `Sale` model's `vip_code` field will be removed.

## Success Flow
1. User submits the booking form (frontend).
2. Frontend calls `/seema-rohan/buy/`.
3. Backend saves the sale, sends email, and returns `/seema-rohan/success/<id>?from=<host>`.
4. Frontend redirects the user.
5. `SuccessView` redirects the user back to the website with `?thanks=true`.
