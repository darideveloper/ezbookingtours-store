# Capability: Seema Rohan Refactor

Structured storage for Seema Rohan airport transfers.

## ADDED Requirements

### Requirement: Structured Sale Storage
The `Sale` model **MUST** capture all booking details in dedicated database columns and **MUST** relate to `Hotel` and `Transport` models via ForeignKeys.

#### Scenario: Sale Creation from POST Payload
Given a valid `POST /buy/` request to the `seema_rohan` app.
When the request is processed.
Then a `Sale` instance is created with:
- `transport_type` linked to the correct `Transport` instance.
- `hotel` linked to the correct `Hotel` instance (if applicable).
- `passengers`, `arriving_*`, and `departing_*` fields correctly parsed and stored.

#### Scenario: Handling "Other" Hotels
Given a request where the "Hotel" label is "other" and "Hotel name" is provided.
When the request is processed.
Then the `hotel_name` field in the `Sale` model is populated with the custom name.
And the `hotel` ForeignKey is set to `null` if no matching hotel is found.

#### Scenario: Duplicate Labels in Description (Round Trip)
Given a "Round Trip" request where "Airline" and "Flight" appear twice in the `description`.
When the request is processed.
Then the first occurrence of "Airline" is stored in `arriving_airline`.
And the second occurrence is stored in `departing_airline`.
