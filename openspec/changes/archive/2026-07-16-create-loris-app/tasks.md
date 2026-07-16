## 1. Scaffold the loris app

- [x] 1.1 Copy the entire `will_ryan_airport_transfers/` directory to `loris/`
- [x] 1.2 Rename `loris/templates/will_ryan_airport_transfers/` to `loris/templates/loris/`
- [x] 1.3 Rename `loris/static/will_ryan_airport_transfers/` to `loris/static/loris/`
- [x] 1.4 Delete all old migration `.py` files from `loris/migrations/` (keep `__init__.py`)
- [x] 1.5 Delete `loris/__pycache__/` and `loris/migrations/__pycache__/` directories entirely

## 2. Update Python imports and references

- [x] 2.1 `loris/apps.py`: Rename class to `LorisConfig`, set `name = 'loris'`
- [x] 2.2 `loris/views.py`: Change import to `from loris import models` (line 6)
- [x] 2.3 `loris/views.py`: Change template path from `"will_ryan_airport_transfers"` to `"loris"` (line 119)
- [x] 2.4 `loris/views.py`: Update email subjects to `"Voucher Lori's Birthday Celebration Airport Transfer"` and `"(#{sale.id}) Lori's Birthday Celebration Airport Transfer"` (lines 123-124)
- [x] 2.5 `loris/tests.py`: Change import to `from loris import models` (line 3)
- [x] 2.6 `loris/tests.py`: Change `API_BASE` to `"/loris"` (line 5)

## 3. Update email template

- [x] 3.1 `loris/templates/loris/mail.html`: Replace hardcoded logo URL with `{% static 'loris/imgs/logo.png' %}` (line 36)

## 4. Register the app in the project

- [x] 4.1 `ezbookingtours_store/settings.py`: Add `"loris",` to `INSTALLED_APPS`
- [x] 4.2 `ezbookingtours_store/settings.py`: Add "Lori's Birthday" section in UNFOLD navigation with links to `admin:loris_sale_changelist`, `admin:loris_hotel_changelist`, `admin:loris_transport_changelist`
- [x] 4.3 `ezbookingtours_store/urls.py`: Add `path("loris/", include("loris.urls"))`

## 5. Database migrations

- [x] 5.1 Run `python manage.py makemigrations loris`
- [x] 5.2 Run `python manage.py migrate loris`

## 6. Verify

- [x] 6.1 Run `python manage.py test loris` — all tests pass
- [x] 6.2 Run `python manage.py check` — no system check errors
- [x] 6.3 Start dev server and verify `GET /loris/` returns `{"status": "running"}`
- [x] 6.4 Verify admin at `/admin/` shows "Lori's Birthday" section with Hotel, Transport, Sale links
