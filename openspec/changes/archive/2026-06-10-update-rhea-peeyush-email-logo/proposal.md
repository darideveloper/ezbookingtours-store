## Why

The current logo image in the confirmation email for Rhea & Peeyush Airport Transfers uses the WebP format (`https://cancunconciergedmc.com/logo.webp`). Certain email clients (such as Gmail and Outlook) convert transparent WebP images to JPEGs during delivery, resulting in a black background instead of a transparent background. Using a transparent PNG instead resolves this rendering issue.

## What Changes

- Update the image source in the confirmation email template for Rhea & Peeyush Airport Transfers to point to `https://cancunconciergedmc.com/imgs/logo-v1.png`.

## Capabilities

### New Capabilities

*(None)*

### Modified Capabilities

- `rhea-peeyush-airport-transfers`: The logo source in the confirmation email template is updated to use a PNG image instead of a WebP image to ensure transparency rendering.

## Impact

- Affected files: `rhea_peeyush_airport_transfers/templates/rhea_peeyush_airport_transfers/mail.html`
- No database changes or API updates are required.
