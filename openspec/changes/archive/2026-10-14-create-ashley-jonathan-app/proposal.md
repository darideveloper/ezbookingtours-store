# Proposal

## Why

Cancun Concierge requires a dedicated transportation booking service for the Ashley & Jonathan Wedding Transfers at Maroma, A Belmond Hotel. Replicating the established `rohan_karisma` application conventions provides a consistent baseline, while introducing a new pricing and confirmation workflow: arrival services must be 100% free across all vehicles and dates (recorded directly in the dashboard and confirmed immediately), whereas departure and round-trip services require full Stripe payment before generating confirmations.

## What Changes

- **Create `ashley_jonathan` Application**: Scaffold the new Django app directory `ashley_jonathan/` replicating `rohan_karisma` structure, models, admin, views, templates, and tests.
- **Free Arrival Service Workflow**: Support 100% free ($0) arrival bookings. When a guest selects an arrival service:
  - Save the sale record immediately with `sale_done=True`.
  - Bypass Stripe checkout completely.
  - Dispatch confirmation emails immediately to the guest and admin.
  - Return the confirmation landing redirect URL.
- **Paid Departure & Round Trip Workflow**: Support Stripe payments for departure and round-trip bookings (where round trip matches the departure price):
  - Save initial sale record with `sale_done=False`.
  - Create checkout session via the Stripe Flask API and return the Stripe URL.
  - Upon successful Stripe callback, mark `sale_done=True`, send confirmation emails, and redirect to the confirmation page.
- **Unfold Admin Registration**: Register `Sale` in `ashley_jonathan/admin.py` using `ModelAdminUnfoldBase` and add the application under the Unfold sidebar navigation in `ezbookingtours_store/settings.py`.
- **Branded Confirmation Email Template**: Add `ashley_jonathan/templates/ashley_jonathan/email.html` with Ashley & Jonathan wedding transfer branding and details.
- **Root URL and Environment Integration**:
  - Register `/ashley-jonathan/` in `ezbookingtours_store/urls.py`.
  - Add `ASHLEY_JONATHAN_PAGE` setting to `.env` and `.env.example`.
- **Test Suite**: Add comprehensive test cases in `ashley_jonathan/tests.py` covering free arrival booking, paid departure/round-trip Stripe creation, and post-payment sale completion.

## Capabilities

### New Capabilities
- `ashley-jonathan-airport-transfers`: Dedicated booking and confirmation service for Ashley & Jonathan wedding airport transfers following `rohan_karisma` conventions, supporting free arrival bookings and Stripe-paid departure and round-trip services.

### Modified Capabilities
<!-- None -->

## Impact

- **Backend Codebase**: New app `ashley_jonathan/` added to `ezbookingtours_store/settings.py` (`INSTALLED_APPS` and `UNFOLD["SIDEBAR"]`), `ezbookingtours_store/urls.py`, and `.env.example`.
- **Database**: New migration file generating `ashley_jonathan_sale` table.
- **Frontend Integration**: Frontend in `../cancun-concierge/ashley-jonathan-airport-transfers` connects to `/ashley-jonathan/sale/` with arrival priced at $0 and round trip equal to departure price.
- **External Dependencies**: Stripe Flask API for paid transactions; Django SMTP email backend for confirmation receipts.
