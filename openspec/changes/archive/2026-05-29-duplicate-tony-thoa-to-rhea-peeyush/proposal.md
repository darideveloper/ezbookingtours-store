## Why

The project requires a new airport transfer module for "Rhea & Peeyush", following the pattern of existing modules like "Tony & Thoa". Duplicating an existing, functional module ensures consistency and speeds up the delivery of this new specific instance.

## What Changes

- Create a new Django app `rhea_peeyush_airport_transfers` by duplicating `tony_thoa_airport_transfers`.
- Rename and update internal references (imports, classes, variables) to reflect the new module name.
- Update template paths and content (emails, logos, branding).
- Integrate the new module into the global project settings and URL routing.
- Configure the admin sidebar (UNFOLD) for the new module.
- Initialize the database schema for the new module through migrations.

## Capabilities

### New Capabilities
- `rhea-peeyush-airport-transfers`: A dedicated airport transfer booking and management module for Rhea & Peeyush, including front-end views, back-end logic, and admin integration.

### Modified Capabilities
- `client-transport-module`: The general pattern for client transport modules is being applied to a new instance.
- `configuration`: Global settings and URL routing are updated to include the new module.

## Impact

- **New App**: `rhea_peeyush_airport_transfers/` directory.
- **Global Settings**: `ezbookingtours_store/settings.py` (INSTALLED_APPS and UNFOLD config).
- **Global Routing**: `ezbookingtours_store/urls.py`.
- **Database**: New tables for the `rhea_peeyush_airport_transfers` app.
