select
  brand,
  channel,
  ad_library_id as ad_id,
  cast(start_date as date) as active_date,
  headline as creative_text,
  landing_domain
from {{ ref('ads_meta') }}
