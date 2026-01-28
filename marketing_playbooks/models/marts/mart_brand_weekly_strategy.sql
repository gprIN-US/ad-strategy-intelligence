-- Marketing Playbooks: weekly brand strategy view (scaffold)
-- Once fact_ads is populated, this becomes your core table for dashboards.

with ads as (
    select * from {{ ref('stg_ads') }}
),
brands as (
    select * from {{ ref('dim_brand') }}
)
select
    b.brand_key,
    b.brand,
    b.segment,
    b.industry,
    date_trunc('week', a.active_date) as week_start,
    count(distinct a.ad_id) as distinct_ads,
    count(*) as ad_active_days,
    count(distinct a.landing_domain) as distinct_landing_domains
from brands b
left join ads a
    on lower(a.brand) = lower(b.brand)
group by 1,2,3,4,5
