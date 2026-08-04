## Context

The `ezbookingtours-store` repository hosts multiple client transportation service applications. The client (Omar) requested a new application `seyis` that mirrors the functionality of the `loris` base app. This initial phase focuses purely on creating the `seyis` Django app structure and components using `loris` as the reference base.

## Goals / Non-Goals

**Goals:**
- Create clean `seyis` Django app files: `apps.py`, `models.py`, `admin.py`, `views.py`, `urls.py`, `tests.py`.
- Define `Hotel`, `Transport`, and `Sale` models matching `loris` schema.
- Register `seyis` models in Django Admin with Unfold styling (`ModelAdminUnfoldBase`).
- Create email voucher template at `seyis/templates/seyis/mail.html`.
- Generate database migrations for `seyis`.

**Non-Goals:**
- Setting up root URL route integration in `ezbookingtours_store/urls.py` (reserved for next task).
- Registering app in `settings.py` (reserved for next task).
- API verification or production deployment.

## Decisions

1. **Base Reference Architecture (`loris`)**:
   - *Decision*: Clone model structure (`Hotel`, `Transport`, `Sale`), admin layout, and views from `loris`.
   - *Rationale*: `loris` serves as the verified baseline for non-Stripe reservation apps in this codebase.

2. **Template Isolation**:
   - *Decision*: Place email template at `seyis/templates/seyis/mail.html`.
   - *Rationale*: Keeps Seyis branding assets encapsulated inside the app directory.

## Risks / Trade-offs

- **[Risk] Unmigrated Database Models** → *Mitigation*: Run `python manage.py makemigrations seyis` to generate explicit migration files for `seyis`.
