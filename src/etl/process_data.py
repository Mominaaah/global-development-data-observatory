import json
import pandas as pd
from pathlib import Path


def process_file(raw_file: Path):
    """
    Process one World Bank JSON file into a clean DataFrame.
    """

    with open(raw_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Check whether the World Bank returned valid data
    if not isinstance(data, list) or len(data) < 2:
        print(f"⚠️ No usable data in {raw_file.name}")
        return None

    records = data[1]

    # Check if records are empty
    if not records:
        print(f"⚠️ Empty records in {raw_file.name}")
        return None

    df = pd.DataFrame(records)

    df["country"] = df["country"].apply(
        lambda x: x["value"]
    )

    df["date"] = df["date"].astype(int)

    df = df[
        [
            "country",
            "countryiso3code",
            "date",
            "value"
        ]
    ]

    df.rename(
        columns={
            "countryiso3code": "country_code",
            "date": "year"
        },
        inplace=True
    )

    return df