# Design: Install and Setup django-unfold

This design outlines the integration of `django-unfold` into the Django project to modernise the admin interface.

## Branding
The client's primary color is `#4f6a9e`. I'll map this into a 10-step OKLCH scale for `django-unfold`'s primary colors.
The logo and favicon are already in `static/` at the root.

## Architecture
- `utils/callbacks.py`: Functions to provide environment context to the Unfold header (Prod, Staging, Dev).
- `ezbookingtours_store/admin.py`: A new location for a base `ModelAdminUnfoldBase` that common models will inherit from. This will provide consistent features like row actions, compressed fields, and filters.
- `settings.py`: Centralized configuration for `UNFOLD` dictionary, including site title, logo, and color theme.

## Color Scale for #4f6a9e
We'll use the following primary scale based on the OKLCH conversion:
```python
"primary": {
    "50": "oklch(0.97 0.01 255)",
    "100": "oklch(0.92 0.03 255)",
    "200": "oklch(0.85 0.05 255)",
    "300": "oklch(0.75 0.07 255)",
    "400": "oklch(0.65 0.08 255)",
    "500": "oklch(0.48 0.08 255)",
    "600": "oklch(0.40 0.07 255)",
    "700": "oklch(0.32 0.06 255)",
    "800": "oklch(0.25 0.05 255)",
    "900": "oklch(0.18 0.04 255)",
    "950": "oklch(0.12 0.03 255)",
}
```

## Static Files
`STATICFILES_DIRS` will be updated to include the root `static/` directory to ensure `logo.webp` and `favicon.png` are correctly served.
