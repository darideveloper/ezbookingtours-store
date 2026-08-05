## 1. Register seyis URLs

- [x] 1.1 Add `path("seyis/", include("seyis.urls"))` to `ezbookingtours_store/urls.py` using the `include` import already present
- [x] 1.2 Verify the seyis routes resolve by running the seyis test suite (`python manage.py test seyis`)

## 2. Supporting fix: django.utils.timezone.utc compatibility shim

- [x] 2.1 Add `django.utils.timezone.utc = datetime.timezone.utc` alias in `ezbookingtours_store/__init__.py` so the legacy `store` migrations (0009-0015) load under Django 5.2 (migration files untouched)
- [x] 2.2 Verify the seyis test suite still passes after the shim
