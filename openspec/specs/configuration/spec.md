# configuration Specification

## Purpose
TBD - created by archiving change install-django-unfold. Update Purpose after archive.
## Requirements
### Requirement: Configure `INSTALLED_APPS`
The `INSTALLED_APPS` setting SHALL be updated to prioritize Unfold's components.
#### Scenario: Add `unfold` apps before `django.contrib.admin`
Given `django-unfold` is installed
When I update `INSTALLED_APPS` to include `unfold` and its contrib apps before `django.contrib.admin`
Then the admin interface should be powered by Unfold.

### Requirement: Configure `UNFOLD` settings
The `UNFOLD` configuration dictionary SHALL be defined to apply branding and UI features.
#### Scenario: Add branding and colors to `UNFOLD` dictionary
Given the client's branding requirements
When I add the `UNFOLD` dictionary to `settings.py` with custom colors, logo, and favicon
Then the admin interface should reflect the client's branding.

### Requirement: Configure `STATICFILES_DIRS`
The root `static/` directory SHALL be included in static file discovery.
#### Scenario: Include root `static/` directory
Given the logo and favicon are at the root `static/` folder
When I add `os.path.join(BASE_DIR, "static")` to `STATICFILES_DIRS`
Then the admin assets should be correctly served.

