# Marketing Playbooks 2026 (SQL + dbt)

This repo is a **Marketing Data Analyst** portfolio project that compares **Enterprise vs Startup** marketing strategies using a repeatable analytics warehouse built with **SQL + dbt** (DuckDB local).

## What’s included (ready now)
- dbt project wired for DuckDB
- Seed data for `brands` (includes Apple)
- Models:
  - `stg_brands` (clean + dedupe)
  - `dim_brand` (surrogate key)
  - `stg_ads` placeholder (empty for now)
  - `mart_brand_weekly_strategy` scaffold (builds once ads data exists)
- Basic tests in `schema.yml`

## Setup (local)
1. Create a venv and install:
   - `pip install dbt-duckdb`
2. Copy `profiles.yml.template` into `~/.dbt/profiles.yml` (or merge it).
3. From inside `marketing_playbooks/` run:
   - `dbt debug`
   - `dbt seed`
   - `dbt run`
   - `dbt test`

This will create a local DuckDB file `dev.duckdb` inside the project.

## Next (you’ll do dashboarding later)
We will add a simple loader that pulls public ad-library data into a raw table, then implement:
- `fact_ads` (ad active-days)
- creative strategy tagging
- channel mix + concentration metrics
- enterprise vs startup comparisons

