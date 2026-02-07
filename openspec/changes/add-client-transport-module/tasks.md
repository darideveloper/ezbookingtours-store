# Tasks: Add Digital Realty Transport Module

## Prerequisites
- [x] 0.1 Django app created (`python manage.py startapp digitalrealty`) ✅
- [x] 0.2 Frontend URL: `https://cancunconciergedmc.com/digitalrealty-airport-transfers` ✅
- [x] 0.3 Logo URL: `https://cancunconciergedmc.com/imgs/digital-realty-logo.png` ✅
- [x] 0.4 Email branding: Same as Cancun Concierge (only header + logo change) ✅

---

## 1. Fix URL Configuration (Critical - currently broken)

- [ ] 1.1 **MODIFY** `digitalrealty/urls.py`
  - Change `from rohan_karisma import views` → `from digitalrealty import views`
  - Update URL names to avoid conflicts: `name='digitalrealty_sales'`, `name='digitalrealty_sale_detail'`

---

## 2. Add Data Model

- [ ] 2.1 **MODIFY** `digitalrealty/models.py`
  - Replace placeholder with Sale model (copy structure from `rohan_karisma/models.py`)
  - Update Meta class: `verbose_name = 'Venta (Digital Realty)'`
  - Update Meta class: `verbose_name_plural = 'Ventas (Digital Realty)'`

- [ ] 2.2 Create migration
  ```bash
  python manage.py makemigrations digitalrealty
  ```

- [ ] 2.3 Apply migration
  ```bash
  python manage.py migrate
  ```

---

## 3. Add Views

- [ ] 3.1 **MODIFY** `digitalrealty/views.py`
  - Replace placeholder with full view implementation
  - Copy from `rohan_karisma/views.py` with these changes:
    - Import: `from digitalrealty import models`
    - Env var: `DIGITALREALTY_PAGE = os.getenv("DIGITALREALTY_PAGE")`
    - Success URL: `f'{HOST}/digitalrealty/sale/{sale.id}'`
    - Template: `'digitalrealty/email.html'`
    - Email subject (owner): `"New Sale in Digital Realty"`
    - Email subject (client): `"Digital Realty - Transportation Confirmation"`
    - All `ROHAN_KARISMA_PAGE` → `DIGITALREALTY_PAGE`
    - Print statement: `"Sending digitalrealty email to {to_email}"`

---

## 4. Add Admin Configuration

- [ ] 4.1 **MODIFY** `digitalrealty/admin.py`
  - Replace placeholder with admin registration
  - Import: `from digitalrealty.models import Sale`
  - Register Sale model with list_display, search_fields, list_filter, ordering, list_per_page

---

## 5. Create Email Template

- [ ] 5.1 Create directories
  ```bash
  mkdir -p digitalrealty/templates/digitalrealty
  ```

- [ ] 5.2 **CREATE** `digitalrealty/templates/digitalrealty/email.html`
  - Copy from `rohan_karisma/templates/rohan_karisma/email.html`
  - Update line 485: Header text → "Digital Realty Airport Transfers"
  - Update line 488: Logo URL → `https://cancunconciergedmc.com/imgs/digital-realty-logo.png`
  - Update line 488: alt text → "Logo Digital Realty Airport Transfers"
  - Keep all other Cancun Concierge branding unchanged

---

## 6. Static Assets

> **Note**: Logo is hosted externally at `https://cancunconciergedmc.com/imgs/digital-realty-logo.png`
> No static files need to be added to the repository.

- [x] 6.1 Logo hosting ✅ (already hosted externally)

---

## 7. Project Configuration

- [ ] 7.1 **MODIFY** `ezbookingtours_store/settings.py`
  - Add `'digitalrealty'` to `INSTALLED_APPS` list (around line 34)

- [ ] 7.2 **MODIFY** `ezbookingtours_store/urls.py`
  - Add `path('digitalrealty/', include('digitalrealty.urls'))` to urlpatterns

---

## 8. Environment Configuration

- [ ] 8.1 **MODIFY** `Dockerfile`
  - Add `ARG DIGITALREALTY_PAGE` (around line 39)
  - Add `ENV DIGITALREALTY_PAGE=${DIGITALREALTY_PAGE}` (around line 71)

- [ ] 8.2 Add to local `.env` file
  ```env
  DIGITALREALTY_PAGE=https://cancunconciergedmc.com/digitalrealty-airport-transfers
  ```

- [ ] 8.3 Add `DIGITALREALTY_PAGE` to production environment (CapRover/Heroku)

---

## 9. Testing

- [ ] 9.1 **MODIFY** `digitalrealty/tests.py`
  - Add test case for `SaleView.post()` (creates sale, returns Stripe response)
  - Add test case for `SaleDoneView.get()` (marks sale as done)
  - Add test case for sale not found (returns 404)
  - Add test case for email preview mode

- [ ] 9.2 Run tests
  ```bash
  python manage.py test digitalrealty
  ```

---

## 10. Validation

- [ ] 10.1 Run Django checks
  ```bash
  python manage.py check
  ```

- [ ] 10.2 Verify migrations are up to date
  ```bash
  python manage.py showmigrations digitalrealty
  ```

- [ ] 10.3 Verify static files collection
  ```bash
  python manage.py collectstatic --dry-run
  ```

- [ ] 10.4 Start development server and test manually
  ```bash
  python manage.py runserver
  ```

---

## Summary of File Operations

### MODIFY Existing Files (7 files)
| File | Current State | Change |
|------|---------------|--------|
| `digitalrealty/urls.py` | Wrong import | Fix import to use digitalrealty views |
| `digitalrealty/models.py` | Empty placeholder | Add Sale model |
| `digitalrealty/views.py` | Empty placeholder | Add SaleView, SaleDoneView |
| `digitalrealty/admin.py` | Empty placeholder | Add Sale admin registration |
| `digitalrealty/tests.py` | Empty placeholder | Add test cases |
| `ezbookingtours_store/settings.py` | Missing app | Add to INSTALLED_APPS |
| `ezbookingtours_store/urls.py` | Missing route | Add URL pattern |

### MODIFY Configuration Files (2 files)
| File | Change |
|------|--------|
| `Dockerfile` | Add DIGITALREALTY_PAGE env var |
| `.env` | Add DIGITALREALTY_PAGE value |

### CREATE New Files (2 files)
| File | Purpose |
|------|---------|
| `digitalrealty/templates/digitalrealty/email.html` | Email template |
| `digitalrealty/migrations/0001_initial.py` | Auto-generated migration |

> **Note**: Logo is hosted externally, no static files needed in repo.
