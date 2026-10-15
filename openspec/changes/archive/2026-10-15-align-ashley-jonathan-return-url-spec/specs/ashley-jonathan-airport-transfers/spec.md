## MODIFIED Requirements

### Requirement: Free Arrival Transfer Booking
The system SHALL record an arrival airport transfer booking as complete and confirmed immediately without requiring payment or redirecting to a payment gateway when the service price is zero.

#### Scenario: Guest submits arrival transfer request
- **WHEN** a client submits a valid booking request for an arrival service with price 0
- **THEN** the system SHALL create a Sale record with `sale_done` set to True
- **AND** the system SHALL return a response with a redirect URL to the confirmation landing page
- **AND** the system SHALL send confirmation emails to the client and admin

#### Scenario: Guest submits arrival request from a custom landing page
- **WHEN** a client submits a valid free arrival booking request including a valid `from-host` URL or a valid legacy `url` value
- **THEN** the system SHALL return a redirect URL equal to the sanitized frontend base with `?done=true` appended
- **AND** the system SHALL prefer `from-host` over `url` when both are present

#### Scenario: Guest submits arrival request without a return URL
- **WHEN** a client submits a valid free arrival booking request where neither `from-host` nor `url` yields a valid URL
- **THEN** the system SHALL return a redirect URL equal to the configured `ASHLEY_JONATHAN_PAGE` with `?done=true` appended

### Requirement: Frontend Return URL Handling
The system SHALL accept, sanitize, validate, and propagate an optional frontend-supplied return URL for paid and free bookings, reading the `from-host` field and, when that is absent, the legacy `url` field.

#### Scenario: Paid booking propagates frontend return URL to Stripe callback
- **WHEN** a client submits a paid departure or round-trip booking including a valid `from-host` URL or a valid legacy `url` value
- **THEN** the system SHALL create a pending Sale with `sale_done` set to False
- **AND** the system SHALL set the Stripe `url_success` to `{HOST}/ashley-jonathan/sale/<id>?from=<urlencoded sanitized base>`
- **AND** the system SHALL prefer `from-host` over `url` when both are present

#### Scenario: Invalid frontend return URL is rejected safely
- **WHEN** a booking request provides a `from-host` or `url` value that is missing, non-http(s), has no host, or includes credentials
- **THEN** the system SHALL ignore the value and use the configured `ASHLEY_JONATHAN_PAGE` behavior
- **AND** the system SHALL strip any query string or fragment before appending `?done=true`
