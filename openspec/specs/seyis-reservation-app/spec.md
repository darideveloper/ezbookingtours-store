# seyis-reservation-app Specification

## Purpose
TBD - created by archiving change create-seyis-app. Update Purpose after archive.
## Requirements
### Requirement: Seyis app module creation
The system SHALL contain a standalone `seyis` Django application directory with `apps.py`, `models.py`, `admin.py`, `views.py`, `urls.py`, `tests.py`, and `templates/seyis/mail.html`.

#### Scenario: Verify seyis app directory structure
- **WHEN** the `seyis` directory is inspected
- **THEN** it SHALL contain all standard Django app files (`apps.py`, `models.py`, `admin.py`, `views.py`, `urls.py`, `tests.py`) cloned from `loris`.

### Requirement: Seyis data models definition
The `seyis/models.py` file SHALL define `Hotel`, `Transport`, and `Sale` models equivalent to the `loris` models.

#### Scenario: Hotel model definition
- **WHEN** the `Hotel` model is inspected in `seyis/models.py`
- **THEN** it SHALL define `name` (CharField) and `extra_price` (FloatField).

#### Scenario: Transport model definition
- **WHEN** the `Transport` model is inspected in `seyis/models.py`
- **THEN** it SHALL define `key` (CharField), `name` (CharField), `price` (FloatField), and `por_defecto` (BooleanField).

#### Scenario: Sale model definition
- **WHEN** the `Sale` model is inspected in `seyis/models.py`
- **THEN** it SHALL define `id`, `name`, `last_name`, `email`, `sale_datetime`, `price`, and `full_data`.

### Requirement: Seyis Unfold Admin registration
The `seyis/admin.py` file SHALL register `Hotel`, `Transport`, and `Sale` models using `ezbookingtours_store.admin.ModelAdminUnfoldBase`.

#### Scenario: Admin registration
- **WHEN** `seyis/admin.py` is loaded
- **THEN** `Hotel`, `Transport`, and `Sale` SHALL be registered with custom list displays and ordering matching `loris`.

### Requirement: Seyis email template setup
The system SHALL include the email template file `seyis/templates/seyis/mail.html` with Seyis event voucher placeholder structures.

#### Scenario: Email template existence
- **WHEN** `seyis/templates/seyis/mail.html` is rendered
- **THEN** it SHALL provide variables for `id`, `first_name`, `last_name`, and `details`.

