## ADDED Requirements

### Requirement: Lori's Birthday app exists as a Django app
The system SHALL provide a Django app named `loris` with the package name `loris`.

#### Scenario: App is installed
- **WHEN** checking `INSTALLED_APPS` in settings
- **THEN** `"loris"` SHALL be present

#### Scenario: AppConfig is configured
- **WHEN** inspecting `loris/apps.py`
- **THEN** the AppConfig class SHALL be named `LorisConfig` with `name = 'loris'`

### Requirement: API endpoints serve at /loris/ prefix
The system SHALL expose the following endpoints under the `/loris/` URL prefix:
- `GET /loris/` → health check
- `GET /loris/hotels/` → list of hotels, sorted by name descending
- `GET /loris/transports/` → list of transports, sorted by name ascending
- `POST /loris/sale/` → create a new sale (name, last-name, price, details, email)

#### Scenario: Health check endpoint
- **WHEN** sending `GET /loris/`
- **THEN** response SHALL be `{"status": "running"}` with status 200

#### Scenario: Hotels endpoint works
- **WHEN** sending `GET /loris/hotels/`
- **THEN** response SHALL be 200 with a JSON array of hotels sorted by name descending

#### Scenario: Transports endpoint works
- **WHEN** sending `GET /loris/transports/`
- **THEN** response SHALL be 200 with a JSON array of transports sorted by name ascending

#### Scenario: Sale creation succeeds
- **WHEN** sending `POST /loris/sale/` with valid JSON body (name, last-name, price, details, email)
- **THEN** response SHALL be `{"status": "success", "message": "Sale saved"}` with status 200
- **AND** a Sale record SHALL be created in the database

#### Scenario: Sale creation fails with missing data
- **WHEN** sending `POST /loris/sale/` with incomplete JSON body
- **THEN** response SHALL be `{"status": "error", "message": "missing data"}` with status 400

### Requirement: Email sends on sale creation with Lori's Birthday subjects
The system SHALL send two emails when a sale is created:
- Client email with subject `"Voucher Lori's Birthday Celebration Airport Transfer"`
- Admin email with subject `"(#{sale.id}) Lori's Birthday Celebration Airport Transfer"`

#### Scenario: Email subjects are correct
- **WHEN** a sale is created via `POST /loris/sale/`
- **THEN** the email SHALL use subject `"Voucher Lori's Birthday Celebration Airport Transfer"` for the client
- **AND** subject `"(#{sale.id}) Lori's Birthday Celebration Airport Transfer"` for the admin

### Requirement: Data models match source app
The `loris` app SHALL define the same three models as `will_ryan_airport_transfers`:
- `Hotel` with fields: `name` (unique), `extra_price`
- `Transport` with fields: `key` (unique), `name` (unique), `price`, `por_defecto`
- `Sale` with fields: `id` (AutoField, primary key), `name`, `last_name`, `email`, `sale_datetime`, `price` (Decimal), `full_data` (Text)

#### Scenario: Hotel model exists
- **WHEN** checking `loris.models.Hotel`
- **THEN** it SHALL have fields `name` and `extra_price` with the same types and constraints as the source

#### Scenario: Transport model exists
- **WHEN** checking `loris.models.Transport`
- **THEN** it SHALL have fields `key`, `name`, `price`, `por_defecto` with the same types and constraints as the source

#### Scenario: Sale model exists
- **WHEN** checking `loris.models.Sale`
- **THEN** it SHALL have fields `id` (AutoField, primary_key), `name`, `last_name`, `email`, `sale_datetime`, `price`, `full_data` with the same types as the source

### Requirement: Admin registration with Lori's Birthday sidebar section
The app SHALL register Hotel, Transport, and Sale in the Django admin under the app label `loris`. The Unfold sidebar SHALL display a "Lori's Birthday" collapsible section with links to each model's changelist.

#### Scenario: Admin models are registered
- **WHEN** accessing the Django admin
- **THEN** Hotel, Transport, Sale SHALL appear under the `loris` app section

#### Scenario: Sidebar section exists
- **WHEN** viewing the Unfold admin sidebar
- **THEN** there SHALL be a collapsible section titled "Lori's Birthday"
- **AND** it SHALL contain links to `admin:loris_sale_changelist`, `admin:loris_hotel_changelist`, `admin:loris_transport_changelist`

### Requirement: Tests pass for the loris app
The test suite SHALL cover hotels listing, transports listing, and sale creation/missing-data scenarios under the `/loris/` base URL.

#### Scenario: All loris tests pass
- **WHEN** running `python manage.py test loris`
- **THEN** all tests SHALL pass
