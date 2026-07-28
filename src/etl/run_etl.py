from pathlib import Path

from src.etl.process_data import process_file

# Folder containing raw JSON files
raw_folder = Path("data/raw")

# Folder to save processed CSV files
processed_folder = Path("data/processed")

# Create processed folder if it doesn't exist
processed_folder.mkdir(exist_ok=True)

# Counter
processed_count = 0

# Process every JSON file
for raw_file in raw_folder.glob("*.json"):

    print(f"\n📂 Processing {raw_file.name}")

    df = process_file(raw_file)

    csv_name = raw_file.stem + ".csv"

    output_path = processed_folder / csv_name

    df.to_csv(output_path, index=False)

    print(f"✅ Saved {csv_name}")

    processed_count += 1

print("\n" + "=" * 50)
print("ETL COMPLETED")
print("=" * 50)
print(f"Files Processed : {processed_count}")
print("=" * 50)