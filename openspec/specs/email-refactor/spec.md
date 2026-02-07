# email-refactor Specification

## Purpose
TBD - created by archiving change consolidate-email-configuration. Update Purpose after archive.
## Requirements
### Requirement: Use Unified Email Configuration
The system SHALL ensure all outgoing emails use a single SMTP host and user defined in the global settings.

#### Scenario: Sending Success Email from Wedding App
- **Given** a user has completed a purchase in the Wedding app.
- **When** the system sends a confirmation email.
- **Then** it must use the configuration associated with `EMAIL_HOST` instead of `EMAIL_HOST_INFO`.

#### Scenario: Sending Success Email from Tony Thoa App
- **Given** a user has completed a purchase in the Tony Thoa app.
- **When** the system sends a confirmation email.
- **Then** it must use the configuration associated with `EMAIL_HOST` instead of `EMAIL_HOST_INFO`.

### Requirement: Renamed Environment Variables
The system SHALL rename environment variables for email to follow a standard naming convention without brand suffixes.

#### Scenario: Environment Variable Access
- **Given** the application is running in a production or development environment.
- **When** the setting `EMAIL_HOST` is accessed.
- **Then** it should return the value of the environment variable formerly known as `EMAIL_HOST_OMAR`.

### Requirement: Unified SMTP Host Selection
The system SHALL NOT support multiple SMTP hosts for different apps.

#### Scenario: Attempting to use a secondary host
- **Given** a new app is being added to the system.
- **When** attempting to configure a secondary SMTP host.
- **Then** the system must reject this in favor of the global `EMAIL_HOST` configuration.

