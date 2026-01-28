select
    -- a stable surrogate key for joins
    md5(lower(brand)) as brand_key,
    brand,
    segment,
    industry
from {{ ref('stg_brands') }}
