## Context

The project hosts multiple branded airport-transfer Django apps, each as a self-contained package with models (Hotel, Transport, Sale), API views, admin registration, email templates, and tests. The established pattern for creating a new branded app is to clone an existing one, rename all references, and register it in the project. This was done previously for `rhea_peeyush_airport_transfers` (cloned from `tony_thoa_airport_transfers`).

The source app `will_ryan_airport_transfers` is a "generation 1" app with simple function-based views, no Stripe/VIP-code complexity, and full test coverage.

## Goals / Non-Goals

**Goals:**
- Create `loris/` app as a functional replica of `will_ryan_airport_transfers/`
- All existing API endpoints work at `/loris/` prefix: hotels, transports, sale
- Admin registration works under "Lori's Birthday" section in the Unfold sidebar
- Email sends with updated subjects referencing "Lori's Birthday Celebration Airport Transfer"
- Tests pass against the new `/loris/` API base URL
- Database tables `loris_hotel`, `loris_transport`, `loris_sale` are created

**Non-Goals:**
- No changes to model fields, business logic, or view behavior
- No Stripe integration, VIP codes, or other "generation 2" features
- No migration of existing data from `will_ryan_airport_transfers` tables

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| **App name** | `loris` (underscore, Python package name) | Follows project convention: snake_case package, kebab-case URL prefix |
| **URL prefix** | `/loris/` | Project pattern: `will-ryan/` → `will_ryan_airport_transfers`, so `loris/` → `loris` |
| **AppConfig name** | `LorisConfig` | PascalCase derived from package name, matching `WillRyanAirportTransfersConfig` pattern |
| **Migrations** | Fresh `makemigrations` from zero | Creates clean migration history; old migrations reference `will_ryan_airport_transfers` app label |
| **Template/static dirs** | `templates/loris/`, `static/loris/` | Must match app name so Django's template/static loaders resolve paths correctly |
| **Email logo** | Use external URL `https://cancunconciergedmc.com/loris/imgs/logo.png` | Avoids `ManifestStaticFilesStorage` dependency at test time; follows same pattern as source app |
| **Model class names** | Keep `Hotel`, `Transport`, `Sale` | Class names don't reference app name; no rename needed |
| **Admin changelist URLs** | `admin:loris_sale_changelist` etc. | Django convention: `admin:<app_label>_<model>_changelist`; app_label comes from `AppConfig.name` |

## Risks / Trade-offs

- **New tables, no data migration**: Production `will_ryan_airport_transfers` data stays untouched. The `loris` tables start empty. This is intentional — it's a separate brand/client.
- **Name collision with `store` app**: The `loris` app name is short and could theoretically conflict, but the project already has short names like `store` and `wedding` with no issues.
- **Template path is a string literal in `views.py`**: The OS-path-based template resolution (`os.path.join(current_folder, "templates", "loris", "mail.html")`) must match the actual directory name. Easy to get wrong if renamed inconsistently — covered by tests.
