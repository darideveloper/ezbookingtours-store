## MODIFIED Requirements

### Requirement: Rhea Peeyush Branding
The system SHALL use "Rhea & Peeyush" branding and updated confirmation email content.

#### Scenario: Confirmation email branding
- **WHEN** a confirmation email is sent for a Rhea Peeyush sale
- **THEN** the email subject SHALL be "Rhea & Peeyush Airport Transfer"
- **AND** the email template SHALL use the logo from `https://cancunconciergedmc.com/imgs/logo-v1.png`
- **AND** the email template SHALL contain the updated body text with the following message:
  "Dear Guest,
  Thank you very much for providing us your payment and the Cancun travel information. You will receive a detailed e-mail confirmation including arrival process at the airport and hotel departure time (for departure back to the airport) soon.
  Warm Regards. The Cancun Concierge DMC team."

#### Scenario: Index view message
- **WHEN** a GET request is made to `/rhea-peeyush/`
- **THEN** the system SHALL return a JSON response with `"message": "Rhea Peeyush App Running"`.
