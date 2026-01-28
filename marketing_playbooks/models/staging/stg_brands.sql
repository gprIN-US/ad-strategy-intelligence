with src as (
    select
        trim(brand) as brand,
        trim(segment) as segment,
        trim(industry) as industry
    from {{ ref('brands') }}
),
dedup as (
    select
        brand,
        segment,
        industry,
        row_number() over (partition by lower(brand) order by brand) as rn
    from src
)
select
    brand,
    segment,
    industry
from dedup
where rn = 1
