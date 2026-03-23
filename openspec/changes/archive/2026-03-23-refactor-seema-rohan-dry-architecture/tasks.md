# Tasks: Seema Rohan DRY and Architectural Refactor

Ordered tasks to implement the DRY and architectural improvements.

## 1. Implementation
- [x] 1.1 Add `parse_dt` utility to `ezbookingtours_store/tools.py`
    - #### Validation
    - Verify that `parse_dt("2026-03-23", ["%Y-%m-%d"])` returns a date object.
    - Verify that `parse_dt("invalid", ["%Y-%m-%d"])` returns `None`.
- [x] 1.2 Update `Transport.price` to `DecimalField` in `seema_rohan/models.py`
    - #### Validation
    - Run `python manage.py makemigrations seema_rohan`
    - Run `python manage.py migrate seema_rohan`
- [x] 1.3 Add `from_payload` class method to `Sale` model in `seema_rohan/models.py`
    - #### Validation
    - Move logic from `BuyView.post` and use `parse_dt` where possible.
    - [Validation]: Test this method in the Django shell with a sample payload.
- [x] 1.4 Refactor `BuyView.post` in `seema_rohan/views.py` to use `Sale.from_payload`
    - #### Validation
    - Verify that the view is now significantly cleaner.
    - Verify that the `details_objs` are still correctly extracted for email confirmation.
- [x] 1.5 Final verification of Admin and Emails
    - #### Validation
    - Confirm all fields are correctly populated in the Admin after a test sale.
    - Confirm the email still contains all booking details.
