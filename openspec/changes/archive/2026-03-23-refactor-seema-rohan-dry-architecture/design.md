# Design: Seema Rohan DRY and Architectural Refactor

Refine the internal structure and logic to ensure maintainability and data integrity.

## Decisions

### 1. Centralized Parsing Logic
A new static method `from_payload` will be added to the `Sale` model in `seema_rohan/models.py`. This method will handle the complex parsing of the `stripe_data` and `description` string. This approach ensures that any part of the system (views, management commands, tasks) can create a `Sale` from a raw payload using the same logic.

### 2. Standardized Date/Time Parsing
A new utility `parse_dt` will be added to `ezbookingtours_store/tools.py`. This utility will attempt to parse a string using a list of common formats (e.g., `"%Y-%m-%d"`, `"%H:%M"`, etc.) and return `None` if it fails. This utility can then be used by all transfer apps (`andrea_scott`, `rohan_karisma`, etc.) to improve the robustness of date/time handling.

### 3. Pricing Consistency
The `Transport.price` field will be changed from `FloatField` to `DecimalField` (max_digits=10, decimal_places=2) to match `Sale.price`. This change requires a migration.

### 4. Refined Admin View
The `SaleAdmin` will be further optimized by organizing all fields into logical fieldsets, using `readonly_fields` for audit information, and adding relevant `list_filter` and `search_fields` to make management more efficient.

## Data Migration
When changing `Transport.price` from `FloatField` to `DecimalField`, Django's standard migration system will handle the conversion. No data loss is expected since the precision of `DecimalField` is higher than `FloatField` for two decimal places.

## Open Questions
- Should the `parse_dt` utility be part of a larger `TransferUtils` class in `tools.py`?
  - *Decision*: Keep it as a standalone utility for now to maintain the current project structure in `tools.py`.
