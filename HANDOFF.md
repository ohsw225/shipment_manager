# Handoff Notes

## Summary
This repo is a fresh Django scaffold for the Logistics Manager app (quotes → shipments, KR/AU branches). Core architecture is planned; initial domain pieces are stubbed, with AU template configs defined. Tooling (lint/format/type/test), settings split, base migrations, and env sample are in place to build on.

## What Exists
- `logistics_manager/` project with `settings/base.py`, `local.py`, `prod.py`; default to SQLite via env or switch to Postgres via `DATABASE_URL`.
- Apps: `core`, `shipments`, `quotes` with placeholder views/urls; `manage.py` points to `settings.local`.
- Tooling: `pyproject.toml` (black, isort, ruff, mypy, pytest), `.pre-commit-config.yaml`, `.editorconfig`, `.gitignore`.
- Dependency manifests: `requirements.in`, `requirements-dev.in` (Django, environ, fpdf2, storages[boto3], psycopg2-binary, dev tools).
- Environment sample: `.env.example` with `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `ALLOWED_HOSTS` defaults (use `.env` in practice). `.env` should be created locally and kept out of VCS.
- Core layer: enums/constants/permissions/utils in `core/` (`choices.py`, `constants.py`, `permissions.py`, `utils.py`).
- `Shipment` model defined with branch/status/template, customer/route fields, `quote_json`, `quote_pdf`, owner, timestamps; initial migration added in `shipments/migrations/0001_initial.py`.
- Quote configs: AU-only templates for 11 codes (IMP LCL/AIR/FCL, EXP LCL/FCL/AIR, AGENT IMP FCL, AGENT IMP LCL DAP Charge, AGENT EXP LCL EXW Charge, AGENT EXP AIR EXW Charge, AGENT EXP FCL) are generated from the root `data.json` definitions (headers, shipment fields, charge columns/sections) in `quotes/template_configs_au.py`. Registry at `quotes/registry.py`; KR config file empty.

## Immediate Next Steps
1) Decide DB (Postgres recommended), set `DATABASE_URL`, create `.env` from `.env.example`, and run migrations (`python logistics_manager/manage.py migrate`).
2) Implement dynamic quote form helpers (`quotes/forms.py`) and quote JSON normalize/denormalize utilities.
3) Implement PDF renderer (`quotes/pdf.py`) using `fpdf2` and layout constants in `core/constants.py`.
4) Build quote create/edit/regenerate views using `TemplateRegistry`, and shipments list/dashboard views with branch filters and permissions (`OwnerOrStaff`).
5) Add templates (`base.html`, nav, dashboard, shipments lists, quote selection/form) wired to the new views.
6) Add tests (registry, forms round-trip, services, permissions, PDF bytes sanity, views) and configure CI (GitHub Actions) to run lint/format/type-check/test.

## How to Resume
- Create venv (py3.12), install deps: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.in`.
- Copy `.env.example` to `.env`; if using SQLite, defaults work, otherwise set `DATABASE_URL` for Postgres and update allowed hosts/secure flags.
- Run `python logistics_manager/manage.py migrate`, then `runserver` for local dev.
- Enable `pre-commit install` to enforce formatting/linting locally.
