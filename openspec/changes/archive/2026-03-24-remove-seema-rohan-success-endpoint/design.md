# Design: Remove Seema Rohan Success Endpoint

## Context
The `@seema_rohan/` app currently has a redundant intermediate backend success page. The user wants to simplify this flow by having the main `buy` endpoint return a direct redirect to the frontend with the success flag.

## Current Flow
1.  Frontend sends booking data to `/seema-rohan/buy/` (`BuyView.post`).
2.  `BuyView` saves the sale as `is_paid=False`.
3.  `BuyView` returns a JSON response with a redirect to `/seema-rohan/success/<sale_id>/?from=frontend-url`.
4.  User hits `/seema-rohan/success/<sale_id>/` (`SuccessView.get`).
5.  `SuccessView` updates the sale to `is_paid=True`.
6.  `SuccessView` redirects the user back to the frontend with `?thanks=true`.

## Proposed Flow
1.  Frontend sends booking data to `/seema-rohan/buy/` (`BuyView.post`).
2.  `BuyView` saves the sale (defaults to `is_paid=False`).
3.  `BuyView` cleans the `from-host` URL (removing trailing segments if needed) and appends `?thanks=true`.
4.  `BuyView` returns a JSON response with this direct frontend "thanks" URL.

## Changes

### 1. `seema_rohan/views.py`
-   **Remove** `SuccessView` class.
-   **Modify** `BuyView.post`:
    -   Keep `sale.is_paid = False` (default) to allow manual tracking of cash payments.
    -   Implement "clean from host" logic:
        ```python
        # Clean from host
        if "/" in from_host:
            from_host_end = from_host.rfind("/")
            from_host = from_host[:from_host_end]
        ```
    -   Construct the final redirect URL:
        ```python
        success_url = f"{from_host}/?thanks=true"
        ```

### 2. `seema_rohan/urls.py`
-   **Remove** the `success` path definition.

## Impact on Requirements
- **Automatic Sale Confirmation**: Modified to mark the sale as `is_paid=True` initially.
- **Direct Success Redirect**: Removed.
- **Frontend Redirect**: Added new requirement for direct frontend redirection with success flag.
