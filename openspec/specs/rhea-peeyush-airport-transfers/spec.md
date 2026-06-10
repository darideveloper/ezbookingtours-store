# rhea-peeyush-airport-transfers Specification

## Purpose
Specification for the Rhea & Peeyush Airport Transfers app.
## Requirements
### Requirement: Rhea Peeyush Module Existence
The system SHALL have a dedicated module named `rhea_peeyush_airport_transfers` to handle specific transportation bookings.

#### Scenario: Module setup
- **WHEN** the system is running
- **THEN** the `rhea_peeyush_airport_transfers` app SHALL be included in `INSTALLED_APPS`
- **AND** the app configuration SHALL use the name `rhea_peeyush_airport_transfers`.

### Requirement: Rhea Peeyush Sale Creation
The system SHALL accept transportation booking data via POST request to `/rhea-peeyush/buy/` and create a sale record.

#### Scenario: Successful sale creation
- **WHEN** a valid POST request is sent to `/rhea-peeyush/buy/` with booking data
- **THEN** the system SHALL create a new Sale record in the `rhea_peeyush_airport_transfers_sale` table
- **AND** the system SHALL return a Stripe payment link with `user` set to `rhea-peeyush`.

### Requirement: Rhea Peeyush Branding
The system SHALL use "Rhea & Peeyush" branding and updated confirmation email content.

#### Scenario: Confirmation email branding
- **WHEN** a confirmation email is sent for a Rhea Peeyush sale
- **THEN** the email subject SHALL be "Rhea & Peeyush Airport Transfer"
- **AND** the email template SHALL use the logo from `https://cancunconciergedmc.com/logo.webp`
- **AND** the email template SHALL contain the updated body text with the sign-off on the same line using non-breaking spaces:
  "Dear Guest,
  Thank you for sharing your flight details for your upcoming trip to Cancun.
  As the wedding date approaches, you will receive a detailed confirmation email approximately two weeks prior to your arrival. This email will include all transportation arrangements, airport arrival instructions, and your scheduled hotel departure time for your return transfer to the airport.
  Warm regards &nbsp; &nbsp; The Cancun Concierge DMC team"

#### Scenario: Index view message
- **WHEN** a GET request is made to `/rhea-peeyush/`
- **THEN** the system SHALL return a JSON response with `"message": "Rhea Peeyush App Running"`.

### Requirement: Rhea Peeyush Admin Integration
The system SHALL display the Rhea Peeyush sales in the admin sidebar.

#### Scenario: Admin sidebar presence
- **WHEN** an admin user logs in
- **THEN** the sidebar SHALL include a section for "Rhea Peeyush"
- **AND** it SHALL link to the Rhea Peeyush sale list.

