# Design: Email Configuration Consolidation

## Architecture Overview
The current architecture uses a "multi-SMTP" approach where different apps can specify different hosts. The new design shifts to a "unified SMTP" approach.

### Current State
- `settings.py` loads both `EMAIL_HOST_OMAR` and `EMAIL_HOST_INFO`.
- `tools.send_sucess_mail` accepts `host` and `from_email` as parameters and creates a manual connection.
- Some apps use `settings.EMAIL_HOST_USER_OMAR` directly via `os.getenv` in their views.

### Proposed State
- `settings.py` will load `EMAIL_HOST` and `EMAIL_HOST_USER`.
- `tools.send_sucess_mail` will still support custom parameters but will defaults to the unified settings, or we can simplify it to use `from django.core.mail import send_mail` if appropriate, although the current implementation uses `EmailMultiAlternatives` for HTML support.
- All apps will refer to `settings.EMAIL_HOST_USER` and `settings.EMAIL_HOST`.

## Component Changes

### 1. Global Settings
- `EMAIL_HOST_OMAR` -> `EMAIL_HOST`
- `EMAIL_HOST_USER_OMAR` -> `EMAIL_HOST_USER`
- Delete `EMAIL_HOST_INFO`
- Delete `EMAIL_HOST_USER_INFO`

### 2. Tools Utility
The `send_sucess_mail` logic will be updated to remove the requirement for passing `host` if it's always the same, but to maintain backward compatibility during the refactor, we will first update the calls and then simplify the function.

### 3. App-Specific Views
Apps like `wedding` and `tony_thoa` which were using the `INFO` host will be transitioned to the `OMAR` (now `DEFAULT`) host.

## Environment Variables
The following changes are required in `.env` and `Dockerfile`:
- Rename `EMAIL_HOST_OMAR` to `EMAIL_HOST`.
- Rename `EMAIL_HOST_USER_OMAR` to `EMAIL_HOST_USER`.
- Remove `EMAIL_HOST_INFO`.
- Remove `EMAIL_HOST_USER_INFO`.
