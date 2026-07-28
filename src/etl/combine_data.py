from pathlib import Path
import pandas as pd

from src.utils.config import COUNTRIES


# Folders
processed_folder = Path("data/processed")

# Store all country-to-group mappings
country_groups = {}

for group, countries in COUNTRIES.items():
    for country_code in countries:
        country_groups[country_code] = group


all_data = []

# Read every processed CSV except the final master file
for csv_file in processed_folder.glob("*.csv"):

    if csv_file.name == "development_data.csv":
        continue

    print(f"📄 Reading {csv_file.name}")

    df = pd.read_csv(csv_file)

    # Extract indicator from filename
    # Example: pak_population.csv → population
    indicator = csv_file.stem.split("_", 1)[1]

    # Add indicator column
    df["indicator"] = indicator

    # Add development group
    df["development_group"] = df["country_code"].map(country_groups)

    all_data.append(df)


# Combine all datasets
master_df = pd.concat(all_data, ignore_index=True)

# Reorder columns
master_df = master_df[
    [
        "country",
        "country_code",
        "development_group",
        "indicator",
        "year",
        "value"
    ]
]

# Save final dataset
output_path = processed_folder / "development_data.csv"

master_df.to_csv(output_path, index=False)

print("\n" + "=" * 50)
print("MASTER DATASET CREATED")
print("=" * 50)
print(f"Rows: {len(master_df)}")
print(f"Columns: {len(master_df.columns)}")
print(f"Saved to: {output_path}")
print("=" * 50)

print("\nPreview:")
print(master_df.head())