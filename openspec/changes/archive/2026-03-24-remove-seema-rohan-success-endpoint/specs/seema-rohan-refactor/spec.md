# seema-rohan-refactor Specification Delta

## ADDED Requirements

### Requirement: Frontend Success Redirect
The `buy` endpoint MUST return a direct redirect URL to the frontend "thanks" page with a success flag.

#### Scenario: Redirect to frontend after save
- **Given** a successful booking save
- **When** processing the `buy` request
- **Then** the response MUST contain a direct redirect to the frontend URL with `?thanks=true` appended
- **And** the frontend URL SHOULD be cleaned to the root (e.g., removing trailing segments from `from-host`).

## MODIFIED Requirements

### Requirement: Automatic Sale Confirmation
The system MUST save and confirm a booking immediately when it is submitted via the `buy` endpoint, and it **SHOULD** stay marked as `is_paid=False` initially to allow manual cash payment tracking.

#### Scenario: User submits a booking
- **Given** valid booking data
- **When** the `buy` endpoint is called
- **Then** the sale MUST be saved as `is_paid=False` (default)

## REMOVED Requirements

### Requirement: Direct Success Redirect
The `buy` endpoint MUST return a redirect URL to the `success` view, bypassing any external payment providers.
