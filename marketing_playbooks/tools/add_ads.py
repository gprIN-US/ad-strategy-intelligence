import csv
import os
from datetime import datetime

CSV_PATH = os.path.join("seeds", "ads_meta.csv")
FIELDS = ["brand","channel","ad_library_id","start_date","creative_type","headline","cta","landing_domain"]

def ensure_csv():
    os.makedirs("seeds", exist_ok=True)
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()

def clean(s: str) -> str:
    return (s or "").strip()

def require(s: str, name: str) -> str:
    s = clean(s)
    if not s:
        raise ValueError(f"{name} is required")
    return s

def validate_date(s: str) -> str:
    s = clean(s)
    # Expect YYYY-MM-DD
    datetime.strptime(s, "%Y-%m-%d")
    return s

def main():
    ensure_csv()
    print("Add Meta/TikTok/Google ads -> seeds/ads_meta.csv")
    print("Type 'q' for brand to quit.\n")

    while True:
        brand = input("brand (q to quit): ").strip()
        if brand.lower() == "q":
            break

        channel = input("channel (Meta/Google/TikTok): ").strip() or "Meta"
        ad_library_id = input("ad_library_id (keep as text): ").strip()
        start_date = input("start_date (YYYY-MM-DD): ").strip()
        creative_type = input("creative_type (Image/Video/Carousel): ").strip()
        headline = input("headline (paste): ").strip()
        cta = input("cta (e.g., Install Now, Learn More): ").strip()
        landing_domain = input("landing_domain (e.g., itunes.apple.com): ").strip()

        # validations
        row = {
            "brand": require(brand, "brand"),
            "channel": require(channel, "channel"),
            "ad_library_id": require(ad_library_id, "ad_library_id"),
            "start_date": validate_date(start_date),
            "creative_type": require(creative_type, "creative_type"),
            "headline": require(headline, "headline"),
            "cta": require(cta, "cta"),
            "landing_domain": require(landing_domain, "landing_domain"),
        }

        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writerow(row)

        print("✅ added 1 row\n")

    print("\nDone. Current file:")
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()
