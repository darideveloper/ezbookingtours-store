# Capability: Seema Rohan Refactor

Structured storage and centralized logic for Seema Rohan airport transfers.

## MODIFIED Requirements

### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys. Parsing logic **MUST** be encapsulated within the `Sale` model using a structured mapping approach.

#### Scenario: Sale Creation from Payload Method
Given a raw JSON payload from the frontend.
When the `Sale.from_payload()` method is called.
Then a `Sale` instance is returned with all fields correctly parsed and ForeignKeys correctly looked up.
And the implementation **SHALL** avoid deep nested `if-elif` chains by using a dictionary-based mapping system.
