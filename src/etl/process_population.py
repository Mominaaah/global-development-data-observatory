import json
import pandas as pd
from pathlib import Path

# Load raw JSON file
with open(raw_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract records
records = data[1]

# Convert to DataFrame
df = pd.DataFrame(records)

# Keep only required columns
df = df[
    [
        "country",
        "countryiso3code",
        "date",
        "value"
    ]
]

# Extract country name from nested dictionary
df["country"] = df["country"].apply(lambda x: x["value"])

# Convert year to integer
df["date"] = df["date"].astype(int)

# Rename columns
df.rename(
    columns={
        "countryiso3code": "country_code",
        "date": "year",
        "value": "population"
    },
    inplace=True
)

# Save processed data
processed_path = Path("data/processed/population.csv")
df.to_csv(processed_path, index=False)

print(df.head())
print()
print(df.dtypes)
print()
print(f" Processed data saved to {processed_path}")