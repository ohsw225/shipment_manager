# Handoff Notes

## Summary
This repo is a fresh Django scaffold for the Logistics Manager app (quotes → shipments, KR/AU branches). Core architecture is planned; initial domain pieces are stubbed, with AU template configs defined. Tooling (lint/format/type/test) and settings split are in place to build on.

## What Exists
- `logistics_manager/` project with `settings/base.py`, `local.py`, `prod.py`; default to SQLite via env or switch to Postgres via `DATABASE_URL`.
- Apps: `core`, `shipments`, `quotes` with placeholder views/urls; `manage.py` points to `settings.local`.
- Tooling: `pyproject.toml` (black, isort, ruff, mypy, pytest), `.pre-commit-config.yaml`, `.editorconfig`, `.gitignore`.
- Dependency manifests: `requirements.in`, `requirements-dev.in` (Django, environ, fpdf2, storages[boto3], psycopg2-binary, dev tools).
- Core layer: enums/constants/permissions/utils in `core/` (`choices.py`, `constants.py`, `permissions.py`, `utils.py`).
- `Shipment` model defined with branch/status/template, customer/route fields, `quote_json`, `quote_pdf`, owner, timestamps (migrations not run yet).
- Quote configs: AU-only templates for 11 codes (IMP LCL/AIR/FCL, EXP LCL/FCL/AIR, AGENT IMP FCL/LCL DAP, AGENT EXP LCL EXW, AGENT EXP AIR EXW, AGENT EXP FCL) in `quotes/template_configs_au.py`; registry at `quotes/registry.py`; KR config file empty.

## Immediate Next Steps
1) Add `.env.example` with `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `ALLOWED_HOSTS`, `USE_S3` placeholders.
2) Decide DB (Postgres recommended), set `DATABASE_URL`, and run initial migrations once models are finalized.
3) Implement dynamic quote form helpers (`quotes/forms.py`) and quote JSON normalize/denormalize utilities.
4) Implement PDF renderer (`quotes/pdf.py`) using `fpdf2` and layout constants in `core/constants.py`.
5) Build quote create/edit/regenerate views using `TemplateRegistry`, and shipments list/dashboard views with branch filters and permissions (`OwnerOrStaff`).
6) Add templates (`base.html`, nav, dashboard, shipments lists, quote selection/form) wired to the new views.
7) Add tests (registry, forms round-trip, services, permissions, PDF bytes sanity, views) and configure CI (GitHub Actions) to run lint/format/type-check/test.

## How to Resume
- Create venv (py3.12), install deps: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.in`.
- Export env or create `.env`; if using SQLite, no DB setup needed; otherwise set `DATABASE_URL` for Postgres.
- Run `python logistics_manager/manage.py migrate` after adding models, then `runserver` for local dev.
- Enable `pre-commit install` to enforce formatting/linting locally.
