## Why

The client (Omar) requires creating a new Django application `seyis` based on the existing `loris` app as a reference baseline. This phase focuses strictly on creating and scaffolding the `seyis` app codebase, models, admin registration, views, templates, and tests.

## What Changes

- Create a new Django app directory `seyis/` cloned from the `loris` reference app.
- Define `Hotel`, `Transport`, and `Sale` models inside `seyis/models.py`.
- Register `seyis` models in Django Admin using `unfold` (`ModelAdminUnfoldBase`) in `seyis/admin.py`.
- Create `seyis/views.py`, `seyis/urls.py`, and `seyis/apps.py`.
- Add email template file `seyis/templates/seyis/mail.html`.
- Add initial test structure in `seyis/tests.py`.

## Capabilities

### New Capabilities
- `seyis-reservation-app`: Standalone `seyis` Django app structure with models, Unfold admin registration, templates, and tests cloned from `loris`.

### Modified Capabilities
<!-- None -->

## Impact

- **New App Directory**: `seyis/` created with `models.py`, `admin.py`, `views.py`, `urls.py`, `apps.py`, `templates/seyis/mail.html`, and `tests.py`.
- **Database**: New migration file created for `seyis` models.
