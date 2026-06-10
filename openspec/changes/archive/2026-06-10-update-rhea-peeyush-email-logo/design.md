## Context

The confirmation email template for the `rhea_peeyush_airport_transfers` application is rendering with a black background behind the logo on some email clients (like Gmail and Outlook). This is caused by using the WebP image format, which gets transcoded to JPEG (which lacks transparency support) by email proxy services. The solution is to use a transparent PNG hosted at `https://cancunconciergedmc.com/imgs/logo-v1.png`.

## Goals / Non-Goals

**Goals:**
- Update the image source URL in the HTML template for the confirmation email to reference the transparent PNG logo.
- Resolve the black background rendering issue in Gmail, Outlook, and other webmail proxies.

**Non-Goals:**
- Modifying styling or content other than the image source URL in the email template.
- Adjusting other email templates or logo paths in different applications.

## Decisions

- **Decision 1: Change WebP to PNG**: Use the PNG version of the logo hosted at `https://cancunconciergedmc.com/imgs/logo-v1.png` in the email template.
  - *Rationale*: PNG is universally supported across all major email clients and email proxy servers, preserving alpha transparency.
  - *Alternatives considered*: Keep WebP (rejected, doesn't solve the issue) or bake in a white background (rejected, looks bad in dark mode).

## Risks / Trade-offs

- **Risk**: The new PNG image is hosted on an external server and must remain accessible.
  - *Mitigation*: The host `cancunconciergedmc.com` is owned/controlled by the same entity and hosts other media assets.
