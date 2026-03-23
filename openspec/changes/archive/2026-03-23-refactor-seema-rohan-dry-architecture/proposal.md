# Proposal: Seema Rohan DRY and Architectural Refactor

Refine the `seema_rohan` application by applying the DRY (Don't Repeat Yourself) principle, centralizing data parsing logic into the models, and ensuring data type consistency for pricing fields.

## Why
The current implementation of the `Sale` model's field population logic is entirely within the `BuyView`, which makes it difficult to maintain and non-reusable. Additionally, the `Transport` model uses `FloatField` for prices while `Sale` uses `DecimalField`, which can lead to precision issues and inconsistencies.

## What Changes
- **DRY Logic**: Move payload parsing from `BuyView.post` to a static method `Sale.from_payload` in `seema_rohan/models.py`.
- **Price Consistency**: Convert `Transport.price` from `FloatField` to `DecimalField` in `seema_rohan/models.py`.
- **Shared Utilities**: Add a robust date/time parsing helper to `ezbookingtours_store/tools.py` for use across all transfer apps.
- **Admin Layout**: Refactor the `SaleAdmin` to use fieldsets more effectively for better UX.

## Impact
- **Affected specs**: `seema-rohan-refactor`
- **Affected code**: `seema_rohan/models.py`, `seema_rohan/views.py`, `seema_rohan/admin.py`, `ezbookingtours_store/tools.py`.
