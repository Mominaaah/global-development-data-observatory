import pandas as pd
from pathlib import Path


# Load master dataset
data_path = Path("data/processed/development_data.csv")

df = pd.read_csv(data_path)

print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

# 1. Dataset shape
print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# 2. Column information
print("\nColumn Data Types:")
print(df.dtypes)

# 3. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 5. Countries
print("\nCountries:")
print(df["country"].unique())

# 6. Development groups
print("\nDevelopment Groups:")
print(df["development_group"].value_counts())

# 7. Indicators
print("\nIndicators:")
print(df["indicator"].value_counts())

# 8. Year range
print("\nYear Range:")
print(df["year"].min(), "to", df["year"].max())

print("\n" + "=" * 50)
print("VALIDATION COMPLETE")
print("=" * 50)