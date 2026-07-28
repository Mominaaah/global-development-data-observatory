import requests
import json
from pathlib import Path



class WorldBankAPI:
    """Client for interacting with the World Bank API."""

    def __init__(self):
        self.base_url = "https://api.worldbank.org/v2"

    def get_indicator_data(self, country_code: str, indicator: str):
        """
        Fetch indicator data for a specific country from the World Bank API.
        """

        url = (
            f"{self.base_url}/country/{country_code}/indicator/"
            f"{indicator}?format=json&per_page=100"
        )

        print(f"Requesting data from:\n{url}")

        response = requests.get(url)

        print(f"Status Code: {response.status_code}")

        return response.json()
    
    def save_raw_data(self, data, filename):
       """
       Save API response as a JSON file.
       """

       raw_folder = Path("data/raw")
       raw_folder.mkdir(parents=True, exist_ok=True)
   
       file_path = raw_folder / filename
   
       with open(file_path, "w", encoding="utf-8") as file:
           json.dump(data, file, indent=4)
   
       print(f"✅ Data saved to {file_path}")


if __name__ == "__main__":
    wb = WorldBankAPI()

    data = wb.get_indicator_data(
    country_code="AUS",
    indicator="NY.GDP.PCAP.CD"
)

    wb.save_raw_data(
        data,
        "australia_gdp_per_capita.json"
    )

    print(type(data))