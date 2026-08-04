# loris-confirmation-email Specification

## Purpose
TBD - created by archiving change fix-loris-seyis-email-logo. Update Purpose after archive.

## Requirements
### Requirement: Loris confirmation email displays brand logo
The loris booking confirmation email SHALL display the site-wide brand logo from `https://cancunconciergedmc.com/imgs/logo.png` in the email body.

#### Scenario: Email renders with working logo URL
- **WHEN** the loris confirmation email template is rendered
- **THEN** the email body SHALL contain an `<img>` element whose `src` is `https://cancunconciergedmc.com/imgs/logo.png`

#### Scenario: Logo URL resolves
- **WHEN** the logo URL `https://cancunconciergedmc.com/imgs/logo.png` is requested (manual/out-of-band network check, not a CI unit test)
- **THEN** the response SHALL be HTTP 200 with an image content type

### Requirement: Loris email template avoids broken logo references
The loris confirmation email SHALL NOT reference the non-existent path `https://cancunconciergedmc.com/loris/imgs/logo.png`.

#### Scenario: No broken logo URL in template
- **WHEN** the loris confirmation email template is inspected
- **THEN** the template SHALL NOT contain the string `https://cancunconciergedmc.com/loris/imgs/logo.png`
