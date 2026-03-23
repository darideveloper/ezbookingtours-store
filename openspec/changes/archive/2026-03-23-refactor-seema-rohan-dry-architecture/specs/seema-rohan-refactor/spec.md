# Capability: Seema Rohan Refactor

Structured storage and centralized logic for Seema Rohan airport transfers.

## MODIFIED Requirements

### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys. Parsing logic **MUST** be encapsulated within the `Sale` model.

#### Scenario: Sale Creation from Payload Method
Given a raw JSON payload from the frontend.
When the `Sale.from_payload()` method is called.
Then a `Sale` instance is returned with all fields correctly parsed and ForeignKeys correctly looked up.

## ADDED Requirements

### Requirement: Shared Date/Time Utility
A centralized date/time parsing utility **MUST** be available for all transfer-related applications.

#### Scenario: Parse Various Date/Time Formats
Given a string "2026-03-23" or "14:30".
When the `parse_dt` utility is called with the corresponding format list.
Then it **SHALL** return a valid `date` or `time` object.
And it **SHALL** return `None` if the input does not match any format.
