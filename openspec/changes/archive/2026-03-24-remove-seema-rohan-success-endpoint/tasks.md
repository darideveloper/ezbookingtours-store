# Tasks: Simplify Seema Rohan Redirection Flow

- [x] **Modify `seema_rohan/views.py`**:
    - [x] Update `BuyView.post` to ensure the sale is saved with `is_paid = False`.
    - [x] Clean `from_host` in `BuyView.post` by removing the last segment if a trailing slash is present (consistent with other apps).
    - [x] Update `success_url` in `BuyView.post` to point directly to the frontend with `?thanks=true`.
    - [x] Remove the `SuccessView` class entirely.
- [x] **Update `seema_rohan/urls.py`**:
    - [x] Remove the `success/` path definition.
- [x] **Validation**:
    - [x] Verify that the `buy` endpoint returns a JSON with a redirect directly to the frontend with `?thanks=true`.
    - [x] Ensure `is_paid` is set to `False` in the database for new bookings.
