## Why

Clone the existing `will_ryan_airport_transfers` Django app as `loris` — a new branded app for "Lori's Birthday Celebration Airport Transfer" — reusing the same data models (Hotel, Transport, Sale), admin, views, tests, email template, and static assets. This follows the established pattern in the project (e.g., `rhea_peeyush_airport_transfers` was cloned from `tony_thoa_airport_transfers`).

## What Changes

- Create a new Django app `loris/` as a direct clone of `will_ryan_airport_transfers/`
- Rename and register the app in the project's `INSTALLED_APPS`, admin navigation, and URL configuration
- Wire the API at the `/loris/` URL prefix
- Update email subjects to reference "Lori's Birthday Celebration Airport Transfer"
- Update the email template's logo URL to use `{% static %}`
- Generate fresh database migrations for the new app
- Create new database tables (`loris_hotel`, `loris_transport`, `loris_sale`)

## Capabilities

### New Capabilities
- `loris-app`: The complete `loris` Django app — models (Hotel, Transport, Sale), admin registration, API views, URL routing, tests, email template, and static assets — wired into the project at the `/loris/` API prefix and the Django admin sidebar.

### Modified Capabilities
*None*

## Impact

- **New app**: `loris/` with its own models, views, URLs, admin, tests, templates, and static files
- **Settings**: `INSTALLED_APPS` gains `"loris"`; Unfold admin nav gains a "Lori's Birthday" section
- **URLs**: `ezbookingtours_store/urls.py` gains `path("loris/", include("loris.urls"))`
- **Database**: New tables `loris_hotel`, `loris_transport`, `loris_sale` (fresh, empty)
- **Tests**: Full test suite from source app carries over (updated for `/loris/` base URL)
