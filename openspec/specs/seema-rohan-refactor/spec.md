# seema-rohan-refactor Specification

## Purpose
TBD - created by archiving change remove-seema-rohan-payments. Update Purpose after archive.
## Requirements
### Requirement: Automatic Sale Confirmation
The system MUST save and confirm a booking immediately when it is submitted via the `buy` endpoint.
#### Scenario: User submits a booking
- **Given** valid booking data (name, last name, phone, email, price, etc.)
- **When** the `buy` endpoint is called
- **Then** the sale MUST be saved as `is_paid=True`

### Requirement: Immediate Confirmation Email
A confirmation email MUST be sent to the user upon successful booking submission.
#### Scenario: Send confirmation email
- **Given** a successful booking save
- **When** processing the `buy` request
- **Then** a confirmation email MUST be sent to the user's email address

### Requirement: Direct Success Redirect
The `buy` endpoint MUST return a redirect URL to the `success` view, bypassing any external payment providers.
#### Scenario: Redirect to success view
- **Given** a successful booking save
- **When** processing the `buy` request
- **Then** the response MUST contain a redirect to the success view

### Requirement: Index View
The index view MUST return a success message indicating the app is running.
#### Scenario: Get index
- **When** the index endpoint is called
- **Then** it MUST return a JSON with status "success" and message "Seema Rohan App Running"

### Requirement: Transports List
The transports endpoint MUST return all available transport options.
#### Scenario: Get transports
- **When** the transports endpoint is called
- **Then** it MUST return a JSON list of transport models

### Requirement: Hotels List
The hotels endpoint MUST return all available hotel options.
#### Scenario: Get hotels
- **When** the hotels endpoint is called
- **Then** it MUST return a JSON list of hotel models

### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys. Parsing logic **MUST** be encapsulated within the `Sale` model using a structured mapping approach.

#### Scenario: Sale Creation from Payload Method
Given a raw JSON payload from the frontend.
When the `Sale.from_payload()` method is called.
Then a `Sale` instance is returned with all fields correctly parsed and ForeignKeys correctly looked up.
And the implementation **SHALL** avoid deep nested `if-elif` chains by using a dictionary-based mapping system.

### Requirement: Shared Date/Time Utility
A centralized date/time parsing utility **MUST** be available for all transfer-related applications.

#### Scenario: Parse Various Date/Time Formats
Given a string "2026-03-23" or "14:30".
When the `parse_dt` utility is called with the corresponding format list.
Then it **SHALL** return a valid `date` or `time` object.
And it **SHALL** return `None` if the input does not match any format.

