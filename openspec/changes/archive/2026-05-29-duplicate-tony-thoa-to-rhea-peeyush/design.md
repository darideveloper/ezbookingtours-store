## Context

The project follows a multi-tenant-like structure where different transport modules are created for different clients or landing pages. These modules share a similar structure: models for sales, views for booking and payment confirmation, and integration with Stripe. Currently, `tony_thoa_airport_transfers` is the reference module for duplication.

## Goals / Non-Goals

**Goals:**
- Rapidly deploy a new transport module `rhea_peeyush_airport_transfers` by duplicating existing logic.
- Maintain consistency with the existing architecture.
- Ensure proper separation of concerns and data isolation for the new module.
- Integrate the new module into the admin interface and global routing.

**Non-Goals:**
- Refactoring the core transport logic into a reusable base class (this is out of scope for this specific duplication task).
- Modifying the Stripe Flask API.

## Decisions

### Decision 1: Duplication over Abstraction
- **Choice**: Duplicate the `tony_thoa_airport_transfers` folder.
- **Rationale**: The project currently relies on independent modules for each client. While abstraction would reduce code duplication, it adds complexity and potential regressions for existing modules. Duplication is faster and safer for this specific requirement.
- **Alternatives**: Create a generic transport app. (Rejected: Requires significant refactoring of all existing modules).

### Decision 2: Naming Convention
- **Choice**: Use snake_case for the app name (`rhea_peeyush_airport_transfers`) and kebab-case for the URL prefix (`/rhea-peeyush/`).
- **Rationale**: Consistent with Django conventions and existing patterns in the project (e.g., `will_ryan_airport_transfers` -> `/will-ryan/`).

### Decision 3: Initial Migration Reset
- **Choice**: Delete copied migrations and run `makemigrations` for the new app.
- **Rationale**: Ensures a clean initial state for the new app's database tables, avoiding conflicts with the source app's migration history.

## Risks / Trade-offs

- **[Risk]** Manual renaming errors → **Mitigation**: Comprehensive search and replace for all strings in the new directory; verification of imports and template paths.
- **[Risk]** Database schema conflicts → **Mitigation**: Use a distinct table name (Django handles this by default using the app name as prefix) and fresh migrations.
