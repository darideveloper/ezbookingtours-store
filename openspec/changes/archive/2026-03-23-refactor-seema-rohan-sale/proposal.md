# Proposal: Refactor Seema Rohan Sale Model

## Why
Refactor the `seema_rohan` `Sale` model to move from storing all booking details in a single JSON field (`stripe_data`) to using structured database columns and ForeignKeys to existing `Hotel` and `Transport` models. This improvement will enhance data integrity, make the database searchable, and allow for better reporting and management through the Django Admin.

## What Changes
Refactor the `seema_rohan` `Sale` model to move from storing all booking details in a single JSON field (`stripe_data`) to using structured database columns and ForeignKeys to existing `Hotel` and `Transport` models. This improvement will enhance data integrity, make the database searchable, and allow for better reporting and management through the Django Admin.

## Impact
Currently, the `seema_rohan` app stores critical booking information like passengers, hotel, and flight details inside a JSON blob. This makes it impossible to query or filter sales by hotel, date, or other key attributes without manual inspection or custom scripts.

## Solution
1. **Model Update**: Add structured fields to the `Sale` model in `seema_rohan/models.py`.
2. **Relationships**: Link `Sale` to `Hotel` and `Transport` via ForeignKeys.
3. **View Update**: Update `BuyView.post` in `seema_rohan/views.py` to parse the incoming `description` string and populate the new database fields.
4. **Data Migration**: Provide a strategy for populating these fields for existing sales (if required).

## Success Criteria
- Sales are stored with individual columns for all booking details.
- ForeignKeys correctly link sales to hotels and transportation types.
- The Django Admin interface displays the new fields, allowing for easy filtering and searching.
- The confirm email functionality remains intact and uses the same logic.
