# Sale Workflow Update Spec Delta

## MODIFIED Requirements

### Requirement: Automatic Sale Confirmation
The system MUST save and confirm a booking immediately when it is submitted via the `buy` endpoint, but it **MUST** be marked as `is_paid=False` initially.

#### Scenario: User submits a booking
- **Given** valid booking data (name, last name, phone, email, etc.)
- **When** the `buy` endpoint is called
- **Then** the sale MUST be saved as `is_paid=False`

### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys. Parsing logic **MUST** be encapsulated within the `Sale` model using a structured mapping approach.

#### Scenario: Sale Creation from Payload Method
Given a raw JSON payload from the frontend.
When the `Sale.from_payload()` method is called.
Then a `Sale` instance is returned with all fields correctly parsed and ForeignKeys correctly looked up.
**AND** the instance **SHALL NOT** store the `price` field in the database.
**AND** the `hotel_name` field **SHALL** be an empty string if a matching `Hotel` record is found.
**AND** the `hotel_name` field **SHALL** only be populated if no `Hotel` record matches the name from the payload.

## ADDED Requirements

### Requirement: Dynamic Price Calculation
The `Sale` model **MUST** provide a way to calculate the total price of the sale dynamically.

#### Scenario: Calculate Total Price
Given a `Sale` instance with a `transport_type` and optionally a `hotel`.
When accessing the `total_price` property.
Then it **SHALL** return the sum of the `transport_type.price` and `hotel.extra_price` (if available).
And it **SHALL** return 0 if no transport type is selected.
