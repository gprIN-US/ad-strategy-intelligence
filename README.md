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

# Ad Strategy Intelligence from Real Meta Ads
### dbt • SQL • DuckDB • Python

This project analyzes how brands structure, test, and sustain advertising campaigns on Meta platforms using real ad data.

Instead of building a dashboard, this project focuses on analytics engineering and data modeling to convert raw ads into structured strategy intelligence.

The goal is to understand:

- How many ad creatives brands test
- How long brands keep ads active
- Whether brands experiment with multiple landing domains or focus on one
- The difference in advertising behavior between established companies and startups

---

## Why this project is different

Most ad analytics projects focus on visualization.

This project focuses on building the data models that make meaningful ad strategy analysis possible.

Using dbt and DuckDB, raw ads were transformed into analytical tables that can answer strategic questions about brand behavior.

---

## Tech Stack

- dbt for data modeling
- DuckDB as the analytical warehouse
- SQL for transformations
- Python for querying and exporting results

---

## Data Modeling Approach

Raw ad data was cleaned and structured into three layers:

### 1. Staging Layer
`stg_ads` – cleaned version of raw ads

### 2. Dimension Table
`dim_brand` – brand attributes such as segment and industry

### 3. Analytical Marts

#### `mart_brand_weekly_strategy`
Weekly view of how each brand runs ads:
- distinct_ads
- ad_active_days
- distinct_landing_domains
- week_start

#### `mart_brand_profile`
Aggregated strategic view per brand:
- total_ads
- total_active_days
- avg_domains_per_week
- segment

This table becomes the source of strategic insight.

---

## Key Metrics Engineered

### total_ads
Number of different ad creatives a brand tests.

### total_active_days
How long brands keep ads live, indicating stability vs rapid testing.

### avg_domains_per_week
Whether brands experiment with multiple landing pages or focus traffic on a single domain.

---

## Insights Observed

When grouping brands by segment:

- Enterprise brands run more ads and keep them active longer.
- Enterprise brands tend to use consistent landing domains.
- Startup brands run short bursts of ads with minimal domain experimentation.

This indicates that established brands optimize and scale proven creatives, while startups focus on rapid experimentation.

---

## How to Run

1. Install dbt and DuckDB
2. Run:
# Ad Strategy Intelligence from Real Meta Ads
### dbt • SQL • DuckDB • Python

This project analyzes how brands structure, test, and sustain advertising campaigns on Meta platforms using real ad data.

Instead of building a dashboard, this project focuses on analytics engineering and data modeling to convert raw ads into structured strategy intelligence.

The goal is to understand:

- How many ad creatives brands test
- How long brands keep ads active
- Whether brands experiment with multiple landing domains or focus on one
- The difference in advertising behavior between established companies and startups

---

## Why this project is different

Most ad analytics projects focus on visualization.

This project focuses on building the data models that make meaningful ad strategy analysis possible.

Using dbt and DuckDB, raw ads were transformed into analytical tables that can answer strategic questions about brand behavior.

---

## Tech Stack

- dbt for data modeling
- DuckDB as the analytical warehouse
- SQL for transformations
- Python for querying and exporting results

---

## Data Modeling Approach

Raw ad data was cleaned and structured into three layers:

### 1. Staging Layer
`stg_ads` – cleaned version of raw ads

### 2. Dimension Table
`dim_brand` – brand attributes such as segment and industry

### 3. Analytical Marts

#### `mart_brand_weekly_strategy`
Weekly view of how each brand runs ads:
- distinct_ads
- ad_active_days
- distinct_landing_domains
- week_start

#### `mart_brand_profile`
Aggregated strategic view per brand:
- total_ads
- total_active_days
- avg_domains_per_week
- segment

This table becomes the source of strategic insight.

---

## Key Metrics Engineered

### total_ads
Number of different ad creatives a brand tests.

### total_active_days
How long brands keep ads live, indicating stability vs rapid testing.

### avg_domains_per_week
Whether brands experiment with multiple landing pages or focus traffic on a single domain.

---

## Insights Observed

When grouping brands by segment:

- Enterprise brands run more ads and keep them active longer.
- Enterprise brands tend to use consistent landing domains.
- Startup brands run short bursts of ads with minimal domain experimentation.

This indicates that established brands optimize and scale proven creatives, while startups focus on rapid experimentation.

---

## How to Run

1. Install dbt and DuckDB
2. Run:
dbt seed
dbt run
3. Query the analytical tables using Python or DuckDB CLI.

---

## Project Structure

marketing_playbooks/
├── models/
├── seeds/
├── dbt_project.yml
├── dev.duckdb

---

## What this project demonstrates

- Analytics engineering using dbt
- Designing fact and dimension tables from unstructured ad data
- Deriving business strategy insights from modeled data
- Using SQL and DuckDB for fast analytical workflows
