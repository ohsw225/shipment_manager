# Logistics Manager

Internal Django web app for managing quotes and shipments across Korea (KR) and Australia (AU) branches. Quotes are config-driven, generate PDFs, and become shipments with tracked status. Current codebase is a scaffold to be extended following the planned architecture.

## Current Status
- Django project structure created with apps: `core`, `shipments`, `quotes`.
- Settings split: `logistics_manager/settings/base.py`, `local.py`, `prod.py` using `django-environ` with SQLite default; media/static roots configured.
- URL wiring in `logistics_manager/urls.py` pointing to placeholder views in `shipments.views` and `quotes.views`; auth URLs included.
- Tooling configured via `pyproject.toml` (black, isort, ruff, mypy, pytest) and `.pre-commit-config.yaml`.
- Dependencies listed in `requirements.in` and `requirements-dev.in`; no virtualenv or installs yet.
- Core domain enums/constants added (`core/choices.py`, `constants.py`, `permissions.py`, `utils.py`).
- `Shipment` model scaffolded with branch/status/template, quote JSON/PDF fields, and owner references (no migrations run yet).
- AU quote template configs defined for 11 templates (IMP LCL/AIR/FCL, EXP LCL/FCL/AIR, AGENT IMP FCL/LCL DAP, AGENT EXP LCL EXW, AGENT EXP AIR EXW, AGENT EXP FCL); KR configs empty for now. Registry is in `quotes/registry.py`.

## Getting Started (fresh clone)
1. Create virtualenv (Python 3.12) and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.in
   ```
2. Copy `.env.example` (not yet present) to `.env` and set `SECRET_KEY`, `DATABASE_URL` (or use default SQLite), `DEBUG`, `ALLOWED_HOSTS`.
3. Run migrations after models are added:
   ```bash
   python logistics_manager/manage.py migrate
   ```
4. Run server:
   ```bash
   python logistics_manager/manage.py runserver
   ```

## Next Steps
- Add `.env.example` with baseline settings.
- Decide DB (Postgres recommended) and run initial migrations when ready.
- Implement dynamic quote forms and JSON helpers in `quotes/forms.py`; add PDF renderer `quotes/pdf.py`.
- Build quote create/edit/regenerate views using `TemplateRegistry`, and shipments list/dashboard views with permissions and filters.
- Add templates (`base.html`, dashboard, shipments lists, quote select/form) reflecting branches and template choices.
- Add tests (registry, forms, permissions, PDF output, views) and wire CI (GitHub Actions) to run lint/format/type-check/test.

## Repository Files of Note
- `pyproject.toml`: tooling config.
- `.pre-commit-config.yaml`: hook definitions.
- `requirements.in`, `requirements-dev.in`: dependency manifests.
- `core/`: enums/constants/permissions/utils.
- `shipments/`, `quotes/`: app scaffolds; shipments model implemented; quotes configs/registry for AU templates.
- `logistics_manager/settings/`: environment-specific settings.
