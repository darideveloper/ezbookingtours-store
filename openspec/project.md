# Project Context

## Purpose
Ezbookingtours Store is a Django-based management dashboard and widget system designed to provide a highly custom and dynamic checkout experience for tour and airport transfer bookings. It serves as a backend to generate widgets that are embedded into WordPress-based online stores (like [ezbookingtours.com](https://ezbookingtours.com/)), allowing for complex booking logic (hotel pickups, dynamic pricing, specific tour times) that standard WordPress plugins may not support.

## Tech Stack
- **Backend:** Python 3.x, Django 4.2.7
- **Database:** PostgreSQL (Production), SQLite (Local/Testing). Managed via environment variables.
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap.
- **Payments:** Stripe Integration (via an external proxy service at `services.darideveloper.com`).
- **Server/DevOps:** Gunicorn, WhiteNoise (for static files), Heroku, Docker.
- **Integrations:** WordPress (via iframes), SMTP (Gmail, managed via `.env`).

## Project Conventions

### Code Style
- **Naming:** Follow standard Django conventions (PascalCase for Models/Classes, snake_case for views/methods/variables).
- **Localization:** Code logic and variables are in English, while administrative labels (`verbose_name`), help texts, and user-facing messages are in Spanish (`es-mx`).
- **Modern JS:** Per user rules, `clsx` is preferred over `class:list` if using Astro or modern JS libraries.
- **Timezone:** `America/Mexico_City`.

### Architecture Patterns
- **Modular Monolith:** Each major client, event, or specific service is isolated into its own Django app (e.g., `store`, `rohan_karisma`, `wedding`, `andrea_scott`).
- **App-Specific Sales:** Client apps often define their own `Sale` model to accommodate unique requirements (e.g., airport transfer details vs. tour pickups).
- **MVT (Model-View-Template):** Standard Django pattern for rendering widgets and landing pages.
- **Widget-Based Integration:** The system is designed to be consumed as an `iframe` or embedded script within external WordPress sites.

### Testing Strategy
- Local testing environment uses SQLite for speed and simplicity.
- Standard Django testing suite (`python manage.py test`).
- Continuous verification of SMTP credentials via dedicated test views.

### Git Workflow
- Standard Git flow with a main branch for continuous deployment to Heroku.
- Conventional Commits are required.

## Domain Context
- **Industry:** Tourism and hospitality in Mexico (primarily Cancun and Riviera Maya).
- **Operations:** Managing airport transfers (arrival/departure flights, airlines), private tours, hotel pickup schedules, and group booking coordination.
- **UX Focus:** High-conversion, mobile-friendly landing pages and frictionless checkout widgets.

## Important Constraints
- **CORS/X-Frame:** Must explicitly allow embedding in external WordPress domains (`X_FRAME_OPTIONS = 'ALLOWALL'`, `CORS_ALLOW_ALL_ORIGINS = True`).
- **Security:** Ensure Stripe secret keys and SMTP credentials remain in `.env` and are never hardcoded.

## External Dependencies
- **Stripe:** For all payment processing (proxied).
- **WordPress:** The parent platform hosting the embedded widgets.
- **Gmail/SMTP:** For automated booking confirmations and client notifications.
