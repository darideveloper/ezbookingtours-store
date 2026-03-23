# Tasks: Remove payment-related logic from seema_rohan app

1. **[x]** Update `seema_rohan/models.py`: Remove `VipCode`, `FreeDays`, `FreeDaysCategory` models and remove `vip_code` field from `Sale`.
2. **[x]** Run `python manage.py makemigrations seema_rohan` to create the migration for model changes.
3. **[x]** Update `seema_rohan/views.py`:
    - Remove `ValidateVipCodeView`.
    - Remove `FreeDatesView`.
    - Refactor `BuyView` to skip VIP validation and Stripe redirection. Always send email and redirect to success.
4. **[x]** Update `seema_rohan/urls.py`: Remove paths for `validate-vip-code/` and `free-dates/`.
5. **[x]** Update `seema_rohan/admin.py`: Remove `VipCodeAdmin`, `FreeDaysAdmin`, and `FreeDaysCategoryAdmin`. Update `SaleAdmin` to remove `vip_code` and `stripe_data` from `list_display`, `search_fields`, etc. (if they were removed from the model).
6. **[x]** Verify that `seema_rohan` app still works (manual check of `transports/` and `hotels/` endpoints, and a mock `buy/` POST).
