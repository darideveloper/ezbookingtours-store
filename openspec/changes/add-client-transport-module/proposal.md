# Change: Add Digital Realty Transport Module

## Why

The `rohan_karisma` module provides a fully functional airport transportation booking system with Stripe payment integration and email confirmations. This proven pattern needs to be replicated for the **Digital Realty** client with different branding and endpoint while maintaining the same core functionality.

## What Changes

### Django App Files to MODIFY (app already created via `startapp`)

The `digitalrealty` app already exists with skeleton files. The following files need to be **modified**:

| File | Current State | Required Changes |
|------|---------------|------------------|
| `digitalrealty/apps.py` | ✅ Already configured | No changes needed |
| `digitalrealty/models.py` | Empty (placeholder) | Add Sale model (copy from rohan_karisma) |
| `digitalrealty/views.py` | Empty (placeholder) | Add SaleView, SaleDoneView (adapted from rohan_karisma) |
| `digitalrealty/urls.py` | Wrong import (uses rohan_karisma views) | Fix import to use digitalrealty views |
| `digitalrealty/admin.py` | Empty (placeholder) | Add Sale admin registration |
| `digitalrealty/tests.py` | Empty (placeholder) | Add test cases |

### New Files to CREATE

| File | Purpose |
|------|---------|
| `digitalrealty/templates/digitalrealty/email.html` | Email confirmation template with Digital Realty branding |
| `digitalrealty/static/digitalrealty/imgs/logo.png` | Digital Realty logo |

### Project-Level Configuration to MODIFY

| File | Change Type | Details |
|------|-------------|---------|
| `ezbookingtours_store/settings.py` | MODIFY | Add `'digitalrealty'` to `INSTALLED_APPS` |
| `ezbookingtours_store/urls.py` | MODIFY | Add `path('digitalrealty/', include('digitalrealty.urls'))` |
| `Dockerfile` | MODIFY | Add `DIGITALREALTY_PAGE` environment variable |

## Configuration Values

| Placeholder | Resolved Value |
|-------------|----------------|
| `{new_app}` | `digitalrealty` |
| `{NEW_APP}` | `DIGITALREALTY` |
| `{new-app}` | `digitalrealty` |
| `{New App}` | `Digital Realty` |
| `{NEW_APP}_PAGE` | `DIGITALREALTY_PAGE` |

## Impact

### Affected Specs
- None (new capability)

### Affected Code
- `ezbookingtours_store/settings.py:34-51` (INSTALLED_APPS)
- `ezbookingtours_store/urls.py:9-19` (urlpatterns)
- `Dockerfile:35-71` (environment variables)

### Database Impact
- New `digitalrealty_sale` table created via migrations

### Environment Variables Required
- `DIGITALREALTY_PAGE`: Frontend URL for redirects and email CTAs

### Shared Environment Variables (already configured, no changes needed)
- `STRIPE_FLASK_API`: Stripe payment API endpoint (shared across all modules)
- `HOST`: Backend server URL for success callbacks (shared)
- `EMAIL_HOST_USER_OMAR`: Email sender address (shared)

---

## ✅ Prerequisites (Resolved)

| Prerequisite | Value |
|--------------|-------|
| **Frontend URL** | `https://cancunconciergedmc.com/digitalrealty-airport-transfers` |
| **Logo URL** | `https://cancunconciergedmc.com/imgs/digital-realty-logo.png` |
| **Contact email** | `omar@cancunconciergedmc.com` (same as rohan_karisma) |
| **Email branding** | Cancun Concierge DMC (same as rohan_karisma) |

### Logo Hosting

✅ Logo is already hosted externally: `https://cancunconciergedmc.com/imgs/digital-realty-logo.png`
- No need to add static files to the repo
- Email template will reference this URL directly

---

## Detailed File Changes

### 1. `digitalrealty/models.py` — MODIFY (replace placeholder)

**Current content:**
```python
from django.db import models

# Create your models here.
```

**New content (copy from rohan_karisma/models.py):**
```python
from django.db import models


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    transport_type = models.CharField(max_length=150, verbose_name='Tipo de transporte', default='')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo', default='')
    passengers = models.IntegerField(verbose_name='Pasajeros', default=1)
    price = models.IntegerField(verbose_name='Precio', default=0)
    arriving = models.TextField(verbose_name='Info de Llegada', default='')
    departing = models.TextField(verbose_name='Info de Salida', default='')
    transport_vehicule = models.CharField(max_length=150, verbose_name='Vehiculo de transporte', default='')
    sale_done = models.BooleanField(verbose_name='Venta realizada', default=False)
    
    def __str__(self):
        return f"{self.name} {self.last_name} - {self.transport_type}"
        
    class Meta:
        verbose_name = 'Venta (Digital Realty)'
        verbose_name_plural = 'Ventas (Digital Realty)'
```

---

### 2. `digitalrealty/views.py` — MODIFY (replace placeholder)

**Current content:**
```python
from django.shortcuts import render

# Create your views here.
```

**Changes from rohan_karisma/views.py:**
- Line 6: `from rohan_karisma import models` → `from digitalrealty import models`
- Line 20: `ROHAN_KARISMA_PAGE = os.getenv("ROHAN_KARISMA_PAGE")` → `DIGITALREALTY_PAGE = os.getenv("DIGITALREALTY_PAGE")`
- Line 71: URL path `'/rohan-karisma/sale/{sale.id}'` → `'/digitalrealty/sale/{sale.id}'`
- Line 136: `"cta": ROHAN_KARISMA_PAGE` → `"cta": DIGITALREALTY_PAGE`
- Line 142: Template path `'rohan_karisma/email.html'` → `'digitalrealty/email.html'`
- Line 147: Email subject `"New Sale in Rohan Karisma"` → `"New Sale in Digital Realty"`
- Line 148: Email subject `"Rohan & Karisma Wedding - Transportation Confirmation"` → `"Digital Realty - Transportation Confirmation"`
- Line 151: Print statement updated to `"Sending digitalrealty email to {to_email}"`
- Line 169: `ROHAN_KARISMA_PAGE` → `DIGITALREALTY_PAGE`

---

### 3. `digitalrealty/urls.py` — MODIFY (fix incorrect import)

**Current content (INCORRECT):**
```python
from rohan_karisma import views  # WRONG - references rohan_karisma!
from django.urls import path

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='sales'),
    path('sale/<int:sale_id>/', views.SaleDoneView.as_view(), name='sale_detail'),
]
```

**New content:**
```python
from digitalrealty import views  # FIXED
from django.urls import path

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='digitalrealty_sales'),
    path('sale/<int:sale_id>/', views.SaleDoneView.as_view(), name='digitalrealty_sale_detail'),
]
```

---

### 4. `digitalrealty/admin.py` — MODIFY (replace placeholder)

**Current content:**
```python
from django.contrib import admin

# Register your models here.
```

**New content (adapted from rohan_karisma/admin.py):**
```python
from django.contrib import admin
from digitalrealty.models import Sale


@admin.register(Sale)
class AdminDigitalRealtySale(admin.ModelAdmin):
    
    list_display = [field.name for field in Sale._meta.get_fields()]
    search_fields = [field.name for field in Sale._meta.get_fields()]
    list_filter = [
        'transport_type',
        'passengers',
        'price',
        'transport_vehicule',
        'sale_done',
    ]
    ordering = [field.name for field in Sale._meta.get_fields()]
    list_per_page = 50
```

---

### 5. `digitalrealty/tests.py` — MODIFY (add test cases)

**Current content:**
```python
from django.test import TestCase

# Create your tests here.
```

**New content:** Add test cases for SaleView and SaleDoneView

---

### 6. `digitalrealty/templates/digitalrealty/email.html` — CREATE

**Create directory and file, copy from rohan_karisma/templates/rohan_karisma/email.html with these changes:**

| Line | Original | New Value |
|------|----------|-----------|
| 485 | `Cancun Concierge DMC Airport Transfers` | `Digital Realty Airport Transfers` |
| 488 | `https://raw.githubusercontent.com/.../rohan_karisma/.../logo.png` | `https://cancunconciergedmc.com/imgs/digital-realty-logo.png` |
| 488 | `alt="Logo Rohan Karisma Airport Transfers"` | `alt="Logo Digital Realty Airport Transfers"` |
| 502 | Keep same (Cancun Concierge DMC branding) | No change |
| 584-585 | `omar@cancunconciergedmc.com` | No change (same contact) |
| 587 | `The Cancun Concierge DMC Team` | No change (same branding) |
| 612 | `Cancun Concierge` | No change (same branding) |

**Summary**: Only the header text and logo URL change. All other Cancun Concierge branding remains the same.

**Template context variables (no changes needed):**
- `{{ today }}` - Invoice date
- `{{ name }}` - Client first name
- `{{ last_name }}` - Client last name
- `{{ price }}` - Total price with currency
- `{{ cta }}` - `https://cancunconciergedmc.com/digitalrealty-airport-transfers`
- `{{ id }}` - Sale reference number
- `{{ details }}` - Arriving/departing info dictionary

---

### 7. `digitalrealty/static/digitalrealty/imgs/` — CREATE

**Create directory and add:**
- `logo.png` (required for email template)

---

### 8. `ezbookingtours_store/settings.py` — MODIFY

**Add to INSTALLED_APPS (line ~34-51):**
```python
INSTALLED_APPS = [
    'digitalrealty',  # ADD THIS LINE
    'andrea_scott',
    # ... rest unchanged
]
```

---

### 9. `ezbookingtours_store/urls.py` — MODIFY

**Add to urlpatterns (line ~9-19):**
```python
urlpatterns = [
    # ... existing paths
    path('digitalrealty/', include('digitalrealty.urls')),  # ADD THIS LINE
]
```

---

### 10. `Dockerfile` — MODIFY

**Add around line 39:**
```dockerfile
ARG DIGITALREALTY_PAGE
```

**Add around line 71:**
```dockerfile
ENV DIGITALREALTY_PAGE=${DIGITALREALTY_PAGE}
```

---

### 11. `.env` (local development) — MODIFY

**Add:**
```env
DIGITALREALTY_PAGE=https://cancunconciergedmc.com/digitalrealty-airport-transfers
```
