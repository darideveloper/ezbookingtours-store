## ADDED Requirements

### Requirement: Confirmation email omits price
The loris booking confirmation email SHALL NOT display a price or any price-related information.

#### Scenario: Email sent without price
- **WHEN** a successful sale POST is received
- **THEN** the confirmation email SHALL be sent
- **THEN** the email body SHALL NOT contain the word "Price" or any price value

### Requirement: Price is optional in POST body
The `price` field in the sale POST body SHALL NOT be required. If omitted, the sale SHALL still be saved and the confirmation email sent.

#### Scenario: POST without price succeeds
- **WHEN** a POST request to `/loris/sale/` includes valid `name`, `last-name`, `details`, and `email`
- **AND** the request omits the `price` field
- **THEN** the response SHALL be `200` with `status: "success"`
- **THEN** the sale SHALL be saved with `price = 0`

#### Scenario: POST with price still works
- **WHEN** a POST request to `/loris/sale/` includes a `price` field
- **THEN** the response SHALL be `200` with `status: "success"`
- **THEN** the sale SHALL be saved with the provided price value
