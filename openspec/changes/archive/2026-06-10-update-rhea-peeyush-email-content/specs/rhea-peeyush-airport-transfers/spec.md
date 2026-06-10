## MODIFIED Requirements

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
