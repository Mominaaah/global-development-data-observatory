download_count = 0
from src.api.world_bank import WorldBankAPI
from src.utils.config import COUNTRIES, INDICATORS

wb = WorldBankAPI()

for category, countries in COUNTRIES.items():

    print(f"\n===== {category} Countries =====")

    for country_code, country_name in countries.items():

        print(f"\n🌍 {country_name} ({country_code})")

        for indicator_name, indicator_code in INDICATORS.items():

            print(f"   Downloading {indicator_name}")

            data = wb.get_indicator_data(
                
                


                country_code=country_code,
                indicator=indicator_code
            )

            filename = f"{country_code.lower()}_{indicator_name}.json"

            wb.save_raw_data(data, filename)

        print("\n" + "=" * 50)
        
print("DOWNLOAD SUMMARY")
print("=" * 50)
print(f"Countries Processed : {len(COUNTRIES)}")
print(f"Indicators Processed: {len(INDICATORS)}")
print(f"Files Downloaded    : {download_count}")
print("=" * 50)