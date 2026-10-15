# Design

## Context

The system hosts airport transfer reservation workflows for multiple wedding events. The `rohan_karisma` application serves as the established baseline convention for this family of applications: a single `Sale` model storing customer details and serialized arrival/departure metadata, paired with `SaleView` and `SaleDoneView` endpoints, Unfold admin configuration, and transactional confirmation emails.

See `proposal.md` for background and business requirements.

## Goals / Non-Goals

**Goals:**
- Implement `ashley_jonathan` application matching `rohan_karisma` structure and conventions.
- Provide zero-dollar ($0) confirmation for arrival services: save sale immediately with `sale_done=True`, dispatch confirmation emails, and redirect to the confirmation landing page without contacting Stripe.
- Provide Stripe checkout flow for departure and round-trip services: save sale with `sale_done=False`, request Stripe checkout URL, and complete the sale upon payment callback.
- Match round-trip pricing to departure pricing.
- Register `Sale` in Django Admin using Unfold styling.
- Provide comprehensive test coverage for both free and paid flows.

**Non-Goals:**
- Relational schema normalization (separate `Hotel` and `Transport` tables) - the application strictly follows `rohan_karisma` conventions with a single `Sale` model as requested.
- Modifying other existing apps (`rohan_karisma`, `seema_rohan`, etc.).

## Decisions

### Decision 1: Adhering to `rohan_karisma` Single Table Model Architecture
- **Choice**: Implement `ashley_jonathan.models.Sale` with the exact fields and metadata structure of `rohan_karisma.models.Sale` (`transport_type`, `name`, `last_name`, `email`, `passengers`, `price`, `arriving`, `departing`, `transport_vehicule`, `sale_done`).
- **Rationale**: User explicitly instructed to follow `rohan_karisma` conventions. This ensures complete consistency in data parsing, email template rendering, and admin behavior.
- **Alternatives Considered**: Multi-table schema with `Hotel` and `Transport` foreign keys (like `seema_rohan`). Rejected to respect user requirement.

### Decision 2: Unified Booking Endpoint Handling Free and Paid Flows
- **Choice**: Use `ashley_jonathan/sale/` (`SaleView.post`) as the single entrypoint for all booking submissions:
  - If `price == 0` or service is arrival:
    - Set `sale_done = True` upon record creation.
    - Immediately send confirmation emails to guest and admin.
    - Return `{"stripe_url": f"{ASHLEY_JONATHAN_PAGE}?done=true"}`.
  - If `price > 0` (departure or round trip):
    - Set `sale_done = False`.
    - Request Stripe checkout URL via `STRIPE_FLASK_API`.
    - Return Stripe checkout URL in JSON response.
- **Rationale**: The frontend JS uses `window.location.href = data.stripe_url`. Returning the confirmation redirect URL in `data.stripe_url` for free bookings allows seamless redirection without requiring any custom branching or fragile client-side logic.
- **Alternatives Considered**: Creating a dedicated `/buy-free/` endpoint. Rejected because keeping one endpoint simplifies frontend form handling.

### Decision 3: Shared Confirmation Email Helper
- **Choice**: Extract email generation and delivery into a dedicated helper function (e.g., `send_confirmation_email(sale, preview=False)`).
- **Rationale**: Both the free arrival flow (`SaleView.post`) and the paid callback flow (`SaleDoneView.get`) need to render `email.html`, populate booking details, and send emails to both the client and `EMAIL_USER`. Sharing this logic eliminates duplication.

### Decision 4: Unfold Admin Registration
- **Choice**: Register `Sale` in `ashley_jonathan/admin.py` extending `ezbookingtours_store.admin.ModelAdminUnfoldBase`, with `list_display`, `search_fields`, `list_filter`, and `ordering` mirroring `rohan_karisma`.
- **Rationale**: Maintains a consistent UI in the Omar Dashboard with searchable and filterable sales.

## Risks / Trade-offs

- **[Risk] Email delivery timeout during free checkout** → Mitigation: Catch SMTP exceptions gracefully and log errors so that client redirection is never blocked if an email server is temporarily unreachable.
- **[Risk] Frontend price tampering** → Mitigation: Validate that only arrival transfers qualify for zero-dollar pricing; departure and round-trip transfers with price <= 0 should be rejected or flagged.
- **[Risk] Missing environment variable `ASHLEY_JONATHAN_PAGE`** → Mitigation: Fall back to a default landing page URL if the environment variable is not defined.

## Migration Plan

1. Generate migration: `python manage.py makemigrations ashley_jonathan`
2. Apply migration: `python manage.py migrate`
3. Rollback: Run `python manage.py migrate ashley_jonathan zero` and remove `ashley_jonathan` from `INSTALLED_APPS`.
