# Proposal: Consolidate Email Configuration

## Problem
The project currently manages two sets of SMTP configurations (`EMAIL_HOST_OMAR` and `EMAIL_HOST_INFO`) across various Django apps. This redundancy complicates maintenance, environment variable management, and inconsistency in how emails are sent across different modules.

## Solution
Refactor the entire project to use a single SMTP configuration. This involves:
1. Renaming the environment variable `EMAIL_HOST_OMAR` to `EMAIL_HOST`.
2. Removing `EMAIL_HOST_INFO` and its associated credentials (`EMAIL_HOST_USER_INFO`).
3. Updating all Django settings and applications to consume the unified `EMAIL_HOST` and `EMAIL_HOST_USER`.
4. Simplifying the `tools.send_sucess_mail` utility to use the unified configuration.

## Scope
- **Configuration:** `.env`, `Dockerfile`, `ezbookingtours_store/settings.py`.
- **Infrastructure:** `ezbookingtours_store/tools.py`.
- **Applications:** `wedding`, `tony_thoa_airport_transfers`, `will_ryan_airport_transfers`, `digitalrealty`, `rohan_karisma`.

## Refactoring Strategy for `send_sucess_mail`
The `ezbookingtours_store/tools.py:send_sucess_mail` function currently requires `from_email` and `host` as mandatory arguments. These will be converted to optional arguments defaulting to `None`.
- If `host` is `None`, it will use `settings.EMAIL_HOST`.
- If `from_email` is `None`, it will use `settings.EMAIL_HOST_USER`.
This allows for a smoother transition where we can refactor calling sites to omit these parameters.

## Benefits
- Reduced complexity in deployment and environment setup.
- Consistent email delivery mechanism across all modules.
- Easier maintenance of SMTP credentials.

## Detailed Refactoring Map

| File Path | Original Variable / Setting | Targeted Replacement |
| :--- | :--- | :--- |
| **Global Config** | | |
| `.env` | `EMAIL_HOST_OMAR`, `EMAIL_HOST_USER_OMAR` | `EMAIL_HOST`, `EMAIL_HOST_USER` |
| `.env` | `EMAIL_HOST_INFO`, `EMAIL_HOST_USER_INFO` | *Remove* (Use `EMAIL_HOST`/`USER`) |
| `Dockerfile` | `ARG/ENV EMAIL_HOST_OMAR` | `ARG/ENV EMAIL_HOST` |
| `Dockerfile` | `ARG/ENV EMAIL_HOST_USER_OMAR` | `ARG/ENV EMAIL_HOST_USER` |
| `ezbookingtours_store/settings.py` | `EMAIL_HOST_USER_OMAR`, `EMAIL_HOST_OMAR` | `EMAIL_HOST_USER`, `EMAIL_HOST` |
| `ezbookingtours_store/settings.py` | `EMAIL_HOST_USER_INFO`, `EMAIL_HOST_INFO` | *Remove* |
| **Logic & UI** | | |
| `ezbookingtours_store/tools.py` | `from_email` (param), `host` (param) | Default to `settings.EMAIL_HOST_USER`/`HOST` |
| `store/tools.py` | `settings.EMAIL_HOST_USER_OMAR` | `settings.EMAIL_HOST_USER` |
| `wedding/views.py` | `settings.EMAIL_HOST_USER_INFO` | `settings.EMAIL_HOST_USER` |
| `wedding/views.py` | `settings.EMAIL_HOST_INFO` | `settings.EMAIL_HOST` |
| `tony_thoa_airport_transfers/views.py` | `settings.EMAIL_HOST_USER_INFO` | `settings.EMAIL_HOST_USER` |
| `tony_thoa_airport_transfers/views.py` | `settings.EMAIL_HOST_INFO` | `settings.EMAIL_HOST` |
| `will_ryan_airport_transfers/views.py` | `settings.EMAIL_HOST_USER_OMAR` | `settings.EMAIL_HOST_USER` |
| `will_ryan_airport_transfers/views.py` | `settings.EMAIL_HOST_OMAR` | `settings.EMAIL_HOST` |
| `digitalrealty/views.py` | `os.getenv("EMAIL_HOST_USER_OMAR")` | `settings.EMAIL_HOST_USER` |
| `rohan_karisma/views.py` | `os.getenv("EMAIL_HOST_USER_OMAR")` | `settings.EMAIL_HOST_USER` |
