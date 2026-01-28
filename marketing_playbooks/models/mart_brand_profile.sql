select
    brand,
    segment,
    sum(distinct_ads)        as total_ads,
    sum(ad_active_days)      as total_active_days,
    avg(distinct_landing_domains) as avg_domains_per_week
from {{ ref('mart_brand_weekly_strategy') }}
group by 1,2
order by total_ads desc

