from src.api.world_bank import WorldBankAPI
from src.utils.config import COUNTRIES, INDICATORS


# Initialize API client
wb = WorldBankAPI()


# Counters
countries_processed = 0
files_downloaded = 0
files_skipped = 0


# ============================================================
# DOWNLOAD DATA
# ============================================================

for category, countries in COUNTRIES.items():

    print(f"\n===== {category} Countries =====")

    for country_code, country_name in countries.items():

        print(f"\n🌍 {country_name} ({country_code})")

        countries_processed += 1

        for indicator_name, indicator_code in INDICATORS.items():

            print(f"   Downloading {indicator_name}")

            data = wb.get_indicator_data(
                country_code=country_code,
                indicator=indicator_code
            )

            # If API request failed
            if data is None:

                print(
                    f"⚠️ Skipping "
                    f"{country_code} - {indicator_name}"
                )

                files_skipped += 1

                continue

            # Create filename
            filename = (
                f"{country_code.lower()}_"
                f"{indicator_name}.json"
            )

            # Save raw data
            wb.save_raw_data(
                data,
                filename
            )

            files_downloaded += 1


# ============================================================
# DOWNLOAD SUMMARY
# ============================================================

print("\n" + "=" * 50)
print("DOWNLOAD SUMMARY")
print("=" * 50)

print(
    f"Countries Processed : "
    f"{countries_processed}"
)

print(
    f"Indicators Processed: "
    f"{len(INDICATORS)}"
)

print(
    f"Files Downloaded    : "
    f"{files_downloaded}"
)

print(
    f"Files Skipped       : "
    f"{files_skipped}"
)

print("=" * 50)