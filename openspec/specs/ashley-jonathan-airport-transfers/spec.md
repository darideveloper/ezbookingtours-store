# ashley-jonathan-airport-transfers Specification

## Purpose

Provides transportation reservation, automated free arrival confirmation, and Stripe payment processing for Ashley & Jonathan Wedding Transfers.

## Requirements

### Requirement: Free Arrival Transfer Booking
The system SHALL record an arrival airport transfer booking as complete and confirmed immediately without requiring payment or redirecting to a payment gateway when the service price is zero.

#### Scenario: Guest submits arrival transfer request
- **WHEN** a client submits a valid booking request for an arrival service with price 0
- **THEN** the system SHALL create a Sale record with `sale_done` set to True
- **AND** the system SHALL return a response with a redirect URL to the confirmation landing page
- **AND** the system SHALL send confirmation emails to the client and admin

#### Scenario: Guest submits arrival request from a custom landing page
- **WHEN** a client submits a valid free arrival booking request including a valid `from-host` URL
- **THEN** the system SHALL return a redirect URL equal to the sanitized `from-host` base with `?done=true` appended

#### Scenario: Guest submits arrival request without a return URL
- **WHEN** a client submits a valid free arrival booking request without `from-host` or with an invalid value
- **THEN** the system SHALL return a redirect URL equal to the configured `ASHLEY_JONATHAN_PAGE` with `?done=true` appended

### Requirement: Paid Departure Transfer Checkout
The system SHALL initiate a Stripe checkout session and record a pending sale when a client books a paid departure service.

#### Scenario: Guest initiates departure booking checkout
- **WHEN** a client submits a booking request for a departure service with a non-zero price
- **THEN** the system SHALL create a Sale record with `sale_done` set to False
- **AND** the system SHALL request a checkout session from the Stripe API
- **AND** the system SHALL return the Stripe checkout URL to redirect the user

### Requirement: Paid Round Trip Transfer Checkout
The system SHALL initiate a Stripe checkout session at the departure service rate when a client books a round-trip service.

#### Scenario: Guest initiates round trip booking checkout
- **WHEN** a client submits a booking request for a round-trip service
- **THEN** the system SHALL charge the same price as the departure service
- **AND** the system SHALL create a pending Sale record with `sale_done` set to False and return the Stripe checkout URL

### Requirement: Sale Payment Completion Callback
The system SHALL mark a pending sale as completed, dispatch confirmation emails, and redirect to the confirmation page upon receiving a successful payment callback.

#### Scenario: Successful payment confirmation callback
- **WHEN** a GET request is received at `/sale/<sale_id>/` for an existing pending sale
- **THEN** the system SHALL update `sale_done` to True
- **AND** the system SHALL send confirmation emails to the client and admin
- **AND** the system SHALL redirect to the configured landing page with `?done=true`

#### Scenario: Payment callback carries a frontend return URL
- **WHEN** a GET request is received at `/sale/<sale_id>/?from=<frontend_base>` with a valid `from` URL
- **THEN** the system SHALL redirect to the sanitized `from` base with `?done=true` appended

#### Scenario: Payment callback without a valid return URL
- **WHEN** a GET request is received at `/sale/<sale_id>/` without `from` or with an invalid value
- **THEN** the system SHALL redirect to the configured `ASHLEY_JONATHAN_PAGE` with `?done=true`

#### Scenario: Payment confirmation callback for non-existent sale
- **WHEN** a GET request is received at `/sale/<sale_id>/` with an invalid ID
- **THEN** the system SHALL return a 404 response with an error message

### Requirement: Administrative Sale Management
The system SHALL register the Sale model in Django Admin with Unfold styling, list display, search capabilities, and filtering.

#### Scenario: Admin views sales in dashboard
- **WHEN** an authenticated staff user navigates to the sales admin changelist
- **THEN** the system SHALL display the sales with filters for transport type, vehicle, passengers, price, and completion status
- **AND** the system SHALL allow searching by customer name, email, and transport fields

### Requirement: Frontend Return URL Handling
The system SHALL accept, sanitize, validate, and propagate an optional frontend-supplied return URL for paid and free bookings.

#### Scenario: Paid booking propagates frontend return URL to Stripe callback
- **WHEN** a client submits a paid departure or round-trip booking including a valid `from-host` URL
- **THEN** the system SHALL create a pending Sale with `sale_done` set to False
- **AND** the system SHALL set the Stripe `url_success` to `{HOST}/ashley-jonathan/sale/<id>?from=<urlencoded sanitized base>`

#### Scenario: Invalid frontend return URL is rejected safely
- **WHEN** a booking request includes a `from-host` value that is missing, non-http(s), has no host, or includes credentials
- **THEN** the system SHALL ignore the value and use the configured `ASHLEY_JONATHAN_PAGE` behavior
- **AND** the system SHALL strip any query string or fragment before appending `?done=true`
