# Django Unfold Integration Guide

This document describes how `django-unfold` is integrated into this project to provide a modern, responsive, and customizable Django Admin interface.

## 1. Dependencies

Add the following package to your `requirements.txt`:

```text
django-unfold==0.77.1
```

## 2. Configuration in `settings.py`

### 2.1 Installed Apps

Ensure `unfold` and its optional components are placed **before** `django.contrib.admin`:

```python
INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    # ... other apps
    "django.contrib.admin",
    "django.contrib.auth",
    # ...
]
```

### 2.2 Static Files & Templates

Ensure root static and templates directories are configured to allow overriding admin assets:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        # ...
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

### 2.3 UNFOLD Settings Dictionary

Key logic:
- **SITE_ICON**: When used, the **SITE_HEADER** and **SITE_SUBHEADER** remain visible in the sidebar.
- **SITE_FAVICONS**: When used, it replaces the **SITE_ICON**, but the **SITE_HEADER** and **SITE_SUBHEADER** remain visible.
- **SITE_LOGO**: When used, it replaces the **SITE_FAVICONS**, **SITE_HEADER**, and **SITE_SUBHEADER** in the sidebar.
- **COLORS**: Defined using OKLCH for modern browser support and consistent shading.
- **SIDEBAR**: `show_all_applications: False` is used to allow manual, collapsible grouping via `navigation`.

```python
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Omar Dashboard",
    "SITE_HEADER": "Omar Admin", # Fallback when logo is missing
    "SITE_SUBHEADER": "Omar Dashboard", # Visible below logo
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("favicon.png"),
    "SITE_LOGO": lambda request: static("logo.webp"),
    "SITE_SYMBOL": "directions_car",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            "href": lambda request: static("favicon.png"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "ENVIRONMENT": "utils.callbacks.environment_callback",
    "THEME": "light",
    "COLORS": {
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
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Autenticación"),
                "separator": True,
                "collapsible": False, # Keep open by default
                "items": [
                    {
                        "title": _("Usuarios"),
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
            {
                "title": _("Tienda"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Ventas"),
                        "icon": "payments",
                        "link": reverse_lazy("admin:store_sale_changelist"),
                    },
                ],
            },
            {
                "title": _("Sección de Traslados"),
                "separator": True,
                "items": [], # Used as a section divider
            },
            {
                "title": _("App Name"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Models"),
                        "icon": "directions_car",
                        "link": reverse_lazy("admin:app_model_changelist"),
                    },
                ],
            },
        ],
    },
}
```

## 3. Custom Callbacks (`utils/callbacks.py`)

Provides environment-specific badges in the admin header.

```python
import os

def environment_callback(request):
    env = os.getenv("ENV", "dev")
    env_mapping = {
        "prod": ["Production", "danger"],
        "staging": ["Staging", "warning"],
        "dev": ["Development", "info"],
        "local": ["Local", "success"],
    }
    return env_mapping.get(env, ["Unknown", "info"])
```

## 4. Admin Implementation

### 4.1 Customizing Auth Models (`project/admin.py`)

```python
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass
```

### 4.2 Base Admin Class (`ModelAdminUnfoldBase`)

Provides common UI enhancements like row actions and compressed fields.

```python
from unfold.admin import ModelAdmin
from unfold.decorators import action
from django.shortcuts import redirect
from django.urls import reverse

class ModelAdminUnfoldBase(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_sheet = False
    change_form_show_cancel_button = True
    
    actions_row = ["edit"]

    @action(description="Edit", permissions=["change"])
    def edit(self, request, object_id):
        return redirect(reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=[object_id]))
```
