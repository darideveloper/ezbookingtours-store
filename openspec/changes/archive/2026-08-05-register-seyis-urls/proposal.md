## Why

The `seyis` app is installed in `INSTALLED_APPS` and its models are registered in the admin, but its `urls.py` is not included in the project's root URLconf (`ezbookingtours_store/urls.py`). As a result, the Seyis API endpoints (`/seyis/`, `/seyis/hotels/`, `/seyis/transports/`, `/seyis/sale/`) are unreachable at runtime, and the `seyis` test suite (which requests `API_BASE = "/seyis"`) fails with 404s.

## What Changes

- Register the `seyis` URLconf globally in `ezbookingtours_store/urls.py` under the `seyis/` path prefix, matching the convention used by the other client apps (`loris`, `wedding`, `digitalrealty`, etc.).
- No changes to the `seyis` app itself; its existing routes become reachable.

## Capabilities

### New Capabilities
- `seyis-url-registration`: Global registration of the `seyis` URLconf in the project root URLconf so its API endpoints are reachable under `/seyis/`.

### Modified Capabilities
<!-- Existing capabilities whose REQUIREMENTS are changing (not just implementation).
     Only list here if spec-level behavior changes. Each needs a delta spec file.
     Use existing spec names from openspec/specs/. Leave empty if no requirement changes. -->

## Impact

- `ezbookingtours_store/urls.py`: new `path("seyis/", include("seyis.urls"))` entry.
- `seyis` app: unchanged (routes already defined).
- The previously-failing `seyis` tests (`seyis/tests.py`) will pass once routing is live.
