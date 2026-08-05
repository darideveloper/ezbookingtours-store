## Context

The `seyis` app (cloned from `loris`) is registered in `INSTALLED_APPS` (settings.py:51) and its models are admin-registered, but its URLconf is never included in the project root URLconf (`ezbookingtours_store/urls.py`). The app's routes are defined at `seyis/urls.py` (`""`, `hotels/`, `transports/`, `sale/`). Its test suite targets `API_BASE = "/seyis"` (seyis/tests.py:6), so the expected mount point is `/seyis/`.

## Goals / Non-Goals

**Goals:**
- Make the `seyis` endpoints reachable at `/seyis/` in the running project.
- Make the existing `seyis` test suite pass.

**Non-Goals:**
- No changes to `seyis` routes, views, models, or templates.
- No changes to the URLs of other client apps.

## Decisions

- **Mount at `/seyis/`** — `path("seyis/", include("seyis.urls"))`, added to `ezbookingtours_store/urls.py`. Matches the `API_BASE` used by `seyis/tests.py` and follows the convention of sibling apps (e.g., `riviera/`, `wedding/`, `loris/`, `digitalrealty/`).
- **Reuse the app's existing URLconf** — no new `urls.py` or route wrappers are needed; the app already exposes the correct paths.
- **No URL namespacing** — sibling apps in this project are included without `namespace=`, so `seyis` follows the same pattern for consistency.

## Risks / Trade-offs

- [Route collision] → Unlikely: `/seyis/` is unused in the root URLconf today; the prefix is unique among registered apps.
- [Existing tests change behavior] → The `seyis` tests were written against `/seyis/` but 404'd; mounting at `/seyis/` only makes them pass, it does not alter their assertions.
