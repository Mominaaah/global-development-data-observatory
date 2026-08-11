import requests
import time
import json
from pathlib import Path


class WorldBankAPI:
    """Client for interacting with the World Bank API."""

    def __init__(self):
        self.base_url = "https://api.worldbank.org/v2"

    def get_indicator_data(self, country_code: str, indicator: str):
        """
        Fetch indicator data from the World Bank API.
        Retries automatically if the request fails.
        """

        url = (
            f"{self.base_url}/country/{country_code}/indicator/"
            f"{indicator}?format=json&per_page=100"
        )

        print(f"Requesting data from:\n{url}")

        for attempt in range(3):

            try:
                response = requests.get(
                    url,
                    timeout=60
                )

                print(f"Status Code: {response.status_code}")

                if response.status_code != 200:
                    print(
                        f"⚠️ Request failed: "
                        f"{country_code} - {indicator}"
                    )
                    print(
                        f"Response: {response.text[:200]}"
                    )
                    return None

                try:
                    return response.json()

                except ValueError:
                    print(
                        f"⚠️ Invalid JSON response: "
                        f"{country_code} - {indicator}"
                    )
                    return None

            except requests.exceptions.Timeout:

                print(
                    f"⏳ Timeout on attempt "
                    f"{attempt + 1}/3"
                )

                if attempt < 2:
                    time.sleep(3)

                else:
                    print(
                        f"❌ Giving up on "
                        f"{country_code} - {indicator}"
                    )
                    return None

            except requests.exceptions.RequestException as e:

                print(
                    f"❌ Request error: {e}"
                )
                return None

    def save_raw_data(self, data, filename):
        """
        Save API response as a JSON file.
        """

        raw_folder = Path("data/raw")
        raw_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = raw_folder / filename

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print(
            f"✅ Data saved to {file_path}"
        )


if __name__ == "__main__":

    wb = WorldBankAPI()

    data = wb.get_indicator_data(
        country_code="AUS",
        indicator="NY.GDP.PCAP.CD"
    )

    if data is not None:

        wb.save_raw_data(
            data,
            "australia_gdp_per_capita.json"
        )

        print(type(data))