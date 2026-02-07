# client-transport-module Specification

## Purpose
TBD - created by archiving change add-client-transport-module. Update Purpose after archive.
## Requirements
### Requirement: Digital Realty Sale Creation
The system SHALL accept transportation booking data via POST request to `/digitalrealty/sale/` and create a sale record linked to Stripe payment.

#### Scenario: Successful sale creation
- **WHEN** a valid POST request is sent to `/digitalrealty/sale/` with booking data (name, email, passengers, transport details)
- **THEN** the system SHALL create a new Sale record in the `digitalrealty_sale` database table
- **AND** the system SHALL forward the booking data to the Stripe Flask API with success URL `/digitalrealty/sale/{id}`
- **AND** the system SHALL return the Stripe API response containing the payment link

#### Scenario: Sale with arriving and departing details
- **WHEN** booking data contains `arriving_*` and `departing_*` prefixed fields
- **THEN** the system SHALL parse and store these as formatted text in `arriving` and `departing` model fields

---

### Requirement: Digital Realty Payment Confirmation
The system SHALL mark sales as completed upon successful payment callback and send confirmation emails with Digital Realty branding.

#### Scenario: Successful payment confirmation
- **WHEN** Stripe redirects to `/digitalrealty/sale/{sale_id}/`
- **THEN** the system SHALL update the Sale record with `sale_done = True`
- **AND** the system SHALL send HTML email confirmation to the client email with subject "Digital Realty - Transportation Confirmation"
- **AND** the system SHALL send notification email to the business owner with subject "New Sale in Digital Realty"
- **AND** the system SHALL redirect to the frontend URL specified in `DIGITALREALTY_PAGE` environment variable

#### Scenario: Sale not found
- **WHEN** the `{sale_id}` does not exist in the `digitalrealty_sale` table
- **THEN** the system SHALL return a 404 JSON response with message "Venta no encontrada"

#### Scenario: Email preview mode
- **WHEN** the request includes `?preview=true` query parameter
- **THEN** the system SHALL render the `digitalrealty/email.html` template without sending emails
- **AND** the system SHALL return the HTML content directly for review

---

### Requirement: Digital Realty Email Notification
The system SHALL send HTML email confirmations using the `digitalrealty/email.html` template with Digital Realty branding.

#### Scenario: Email contains booking details
- **WHEN** a confirmation email is generated
- **THEN** the email SHALL include: client name, booking reference ID, date, total price
- **AND** the email SHALL include parsed arriving and departing details
- **AND** the email SHALL include passenger count, transport type, and vehicle type

#### Scenario: Email uses Digital Realty branding
- **WHEN** a confirmation email is generated
- **THEN** the email SHALL display the Digital Realty logo from `static/digitalrealty/imgs/logo.png`
- **AND** the email SHALL display "Digital Realty Airport Transfers" in the header
- **AND** the email SHALL include CTA button linking to `DIGITALREALTY_PAGE`

---

### Requirement: Digital Realty Admin Interface
The system SHALL provide Django admin access to manage Sale records under the `digitalrealty` app.

#### Scenario: Admin list view
- **WHEN** an admin user accesses the Digital Realty Sale list in Django admin
- **THEN** the system SHALL display all Sale model fields in the list view
- **AND** the system SHALL allow filtering by transport_type, passengers, price, transport_vehicule, sale_done
- **AND** the system SHALL display verbose name "Ventas (Digital Realty)"

#### Scenario: Admin pagination
- **WHEN** there are more than 50 Sale records
- **THEN** the system SHALL paginate results with 50 items per page

---

### Requirement: Digital Realty URL Routing
The system SHALL expose API endpoints under the `/digitalrealty/` URL prefix.

#### Scenario: Sale creation endpoint
- **WHEN** a POST request is made to `/digitalrealty/sale/`
- **THEN** the system SHALL route to the digitalrealty SaleView

#### Scenario: Payment confirmation endpoint
- **WHEN** a GET request is made to `/digitalrealty/sale/{id}/`
- **THEN** the system SHALL route to the digitalrealty SaleDoneView

---

### Requirement: Digital Realty Environment Configuration
The system SHALL use the `DIGITALREALTY_PAGE` environment variable for client-specific configuration.

#### Scenario: Frontend URL configuration
- **WHEN** the system needs to redirect after payment or include CTA in emails
- **THEN** the system SHALL read the frontend URL from `DIGITALREALTY_PAGE` environment variable

#### Scenario: Docker deployment configuration
- **WHEN** deploying via Docker
- **THEN** the Dockerfile SHALL accept `DIGITALREALTY_PAGE` as a build argument
- **AND** the Dockerfile SHALL set it as an environment variable

---

### Requirement: Digital Realty Data Isolation
The system SHALL store Digital Realty booking data in a dedicated table separate from other client modules.

#### Scenario: Separate database table
- **WHEN** a Digital Realty Sale record is created
- **THEN** the record SHALL be stored in the `digitalrealty_sale` table
- **AND** the record SHALL be independent from `rohan_karisma_sale` and other client tables

#### Scenario: Sale record structure
- **WHEN** a Sale record is created
- **THEN** the record SHALL contain: id (auto), transport_type, name, last_name, email, passengers, price, arriving, departing, transport_vehicule, sale_done

