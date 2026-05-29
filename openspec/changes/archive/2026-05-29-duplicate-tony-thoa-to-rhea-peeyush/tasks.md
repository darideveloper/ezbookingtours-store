## 1. Directory Structure & Renaming

- [x] 1.1 Duplicate `tony_thoa_airport_transfers/` to `rhea_peeyush_airport_transfers/`
- [x] 1.2 Rename `templates/tony_thoa_airport_transfers/` to `templates/rhea_peeyush_airport_transfers/`

## 2. Module-Level Updates

- [x] 2.1 Update `apps.py`: Change `TonyThoaAirportTransfersConfig` to `RheaPeeyushAirportTransfersConfig` and update `name`
- [x] 2.2 Update `models.py`, `admin.py`, `urls.py`: Update internal imports from `tony_thoa_airport_transfers` to `rhea_peeyush_airport_transfers`
- [x] 2.3 Update `views.py`:
    - [x] 2.3.1 Update imports: `from rhea_peeyush_airport_transfers import models`
    - [x] 2.3.2 Update `IndexView` message to "Rhea Peeyush App Running"
    - [x] 2.3.3 Update `success_url` path from `/tony-thoa/` to `/rhea-peeyush/`
    - [x] 2.3.4 Update `tools.send_sucess_mail` subjects to "Rhea & Peeyush Airport Transfer"
    - [x] 2.3.5 Update `template_path` to use `rhea_peeyush_airport_transfers`
    - [x] 2.3.6 Update Stripe `user` identifier to "rhea-peeyush"
- [x] 2.4 Update `mail.html`:
    - [x] 2.4.1 Update logo URL to `https://cancunconciergedmc.com/logo.webp`
    - [x] 2.4.2 Update logo alt text to "Cancun Concierge DMC Logo" or "Rhea & Peeyush Airport Transfers Logo"
    - [x] 2.4.3 Verify "Dear guest" text and other branding elements

## 3. Global Project Updates

- [x] 3.1 Add `rhea_peeyush_airport_transfers` to `INSTALLED_APPS` in `ezbookingtours_store/settings.py`
- [x] 3.2 Add Rhea Peeyush section to `UNFOLD` (sidebar) configuration in `ezbookingtours_store/settings.py` (including Ventas, Hoteles, Transportes, Códigos VIP, and Días Gratis)
- [x] 3.3 Add route to `ezbookingtours_store/urls.py`: `path("rhea-peeyush/", include("rhea_peeyush_airport_transfers.urls"))`

## 4. Database & Migrations

- [x] 4.1 Delete existing migrations in `rhea_peeyush_airport_transfers/migrations/` (except `__init__.py`)
- [x] 4.2 Generate initial migrations: `python manage.py makemigrations rhea_peeyush_airport_transfers`
- [x] 4.3 Apply migrations: `python manage.py migrate`

## 5. Verification

- [x] 5.1 Verify admin sidebar displays Rhea Peeyush and links to sale list
- [x] 5.2 Verify `/rhea-peeyush/` endpoint renders and processes bookings
- [x] 5.3 Verify confirmation email rendering via `?preview=true`
