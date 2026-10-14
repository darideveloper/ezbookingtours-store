# Tasks

## 1. App Scaffolding & Configuration

- [x] 1.1 Scaffold `ashley_jonathan` app directory containing `__init__.py`, `apps.py`, and `models.py` defining the `Sale` model matching `rohan_karisma` conventions, and verify `python manage.py check` executes without error.
- [x] 1.2 Register `ashley_jonathan` in `ezbookingtours_store/settings.py` (`INSTALLED_APPS` and `UNFOLD["SIDEBAR"]`), mount `/ashley-jonathan/` in `ezbookingtours_store/urls.py`, and add `ASHLEY_JONATHAN_PAGE` to `.env` and `.env.example`.
- [x] 1.3 Create and apply the initial migration for `ashley_jonathan` via `python manage.py makemigrations ashley_jonathan` and `python manage.py migrate`, verifying the `ashley_jonathan_sale` table is created.

## 2. Admin & Email Template

- [x] 2.1 Register `Sale` in `ashley_jonathan/admin.py` using `ModelAdminUnfoldBase` with `list_display`, `search_fields`, and `list_filter` mirroring `rohan_karisma`, verifying admin loads cleanly.
- [x] 2.2 Create confirmation email template `ashley_jonathan/templates/ashley_jonathan/email.html` customized for Ashley & Jonathan wedding transfers, verifying template syntax.

## 3. Views & Booking Endpoints

- [x] 3.1 Implement `SaleView` in `ashley_jonathan/views.py` to handle booking requests:
  - For free arrival service ($0): save sale immediately with `sale_done=True`, trigger confirmation emails, and return confirmation redirect URL.
  - For paid departure and round-trip services: save sale with `sale_done=False`, request checkout URL from Stripe Flask API, and return Stripe URL.
- [x] 3.2 Implement `SaleDoneView` in `ashley_jonathan/views.py` to handle the post-Stripe callback: mark `sale_done=True`, send confirmation emails, and redirect to `f"{ASHLEY_JONATHAN_PAGE}?done=true"`.
- [x] 3.3 Register `SaleView` and `SaleDoneView` in `ashley_jonathan/urls.py` (`sale/` and `sale/<int:sale_id>/`), verifying route resolution.

## 4. Verification & Testing

- [x] 4.1 Implement unit and integration tests in `ashley_jonathan/tests.py` covering:
  - Free arrival booking with immediate confirmation and email dispatch.
  - Paid departure booking with Stripe API interaction.
  - Paid round-trip booking charging the departure rate.
  - `SaleDoneView` marking the sale done, sending emails, and redirecting.
  - Verify all tests pass with `python manage.py test ashley_jonathan`.
- [x] 4.2 Update frontend configuration in `../cancun-concierge/code/ashley-jonathan-airport-transfers.js` and `../cancun-concierge/ashley-jonathan-airport-transfers/index.html` to point to `/ashley-jonathan/sale/` and configure arrival as $0 and round trip matching departure price.
