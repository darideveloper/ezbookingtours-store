# seyis-url-registration Specification

## Purpose
TBD - created by archiving change register-seyis-urls. Update Purpose after archive.

## Requirements
### Requirement: Global registration of seyis URLs
The project root URLconf SHALL include the `seyis` app URLconf mounted at the `seyis/` path prefix.

#### Scenario: Root URLconf includes seyis routes
- **WHEN** the project root URLconf `ezbookingtours_store/urls.py` is inspected
- **THEN** it SHALL contain a `path("seyis/", include("seyis.urls"))` entry

#### Scenario: Seyis index endpoint is reachable
- **WHEN** a client requests `/seyis/`
- **THEN** the request SHALL resolve to the `seyis.index` view and return HTTP 200

#### Scenario: Seyis hotels endpoint is reachable
- **WHEN** a client requests `/seyis/hotels/`
- **THEN** the request SHALL resolve to the `seyis.hotels` view and return HTTP 200

#### Scenario: Seyis transports endpoint is reachable
- **WHEN** a client requests `/seyis/transports/`
- **THEN** the request SHALL resolve to the `seyis.transports` view and return HTTP 200

#### Scenario: Seyis sale endpoint accepts posts
- **WHEN** a client POSTs a valid payload to `/seyis/sale/`
- **THEN** the request SHALL resolve to the `seyis` sales view and save the sale
