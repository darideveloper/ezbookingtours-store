# Spec Delta: Fix Hotel Name Saving

## Related Capabilities
- [seema-rohan-refactor](../../../specs/seema-rohan-refactor/spec.md)

## MODIFIED Requirements
### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys. Parsing logic **MUST** be encapsulated within the `Sale` model using a structured mapping approach.

#### Scenario: Sale Creation from Payload Method
- **Given** a raw JSON payload from the frontend with `"Hotel: other"` and `"Hotel name: [Custom Name]"`
- **When** the `Sale.from_payload()` method is called
- **Then** the returned `Sale` instance MUST have `hotel_name` set to `[Custom Name]` and `hotel` ForeignKey set to `None` (if no `Hotel` record matches the name).
- **And** the `hotel_name` field **SHALL** correctly keep its value if the custom hotel name does not match any existing `Hotel` record.
