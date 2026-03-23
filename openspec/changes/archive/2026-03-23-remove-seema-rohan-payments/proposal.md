# Proposal: Remove payment-related logic from seema_rohan app

Currently, the `seema_rohan` app has features for VIP codes, free dates, and Stripe redirection. These are no longer required. The goal is to simplify the sale flow so that every sale is treated as if a VIP code was used (no payment to Stripe).

## Why

Payments are no longer required for this specific store (seema_rohan). The client wants to simplify the booking process by removing VIP code validation and free dates logic, allowing all bookings to be confirmed immediately without Stripe redirection.

## Capabilities

- **Refactor `seema_rohan` app**: Remove models and views related to VIP codes, free dates, and Stripe. Update `BuyView` to skip payment logic.

## What Changes

- Remove `VipCode`, `FreeDays`, `FreeDaysCategory` models.
- Update `Sale` model to simplify it (remove `vip_code`).
- Update `BuyView` to skip Stripe link generation and always redirect to success.
- Remove `ValidateVipCodeView` and `FreeDatesView`.
- Clean up `admin.py` and `urls.py`.
