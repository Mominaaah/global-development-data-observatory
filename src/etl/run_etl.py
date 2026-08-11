from pathlib import Path

from src.etl.process_data import process_file


# Folder containing raw JSON files
raw_folder = Path("data/raw")

# Folder to save processed CSV files
processed_folder = Path("data/processed")

# Create processed folder if it doesn't exist
processed_folder.mkdir(
    parents=True,
    exist_ok=True
)

# Counter
processed_count = 0
skipped_count = 0


# Process every JSON file
for raw_file in raw_folder.glob("*.json"):

    print(f"\n📂 Processing {raw_file.name}")

    df = process_file(raw_file)

    # Skip files with no usable data
    if df is None:
        print(f"⏭️ Skipping {raw_file.name}")
        skipped_count += 1
        continue

    # Create CSV filename
    csv_name = raw_file.stem + ".csv"

    # Create output path
    output_path = processed_folder / csv_name

    # Save processed data
    df.to_csv(
        output_path,
        index=False
    )

    print(f"✅ Saved {csv_name}")

    processed_count += 1


print("\n" + "=" * 50)
print("ETL COMPLETED")
print("=" * 50)
print(f"Files Processed : {processed_count}")
print(f"Files Skipped   : {skipped_count}")
print("=" * 50)