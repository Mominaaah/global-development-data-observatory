import pandas as pd
from pathlib import Path


# Load dataset
data_path = Path("data/processed/development_data.csv")

df = pd.read_csv(data_path)


# ==================================================
# 1. GDP ANALYSIS
# ==================================================

gdp_df = df[df["indicator"] == "gdp"].copy()

latest_gdp = (
    gdp_df
    .sort_values("year")
    .groupby("country")
    .tail(1)
    .sort_values("value", ascending=False)
)

print("\n" + "=" * 60)
print("LATEST GDP BY COUNTRY")
print("=" * 60)

print(
    latest_gdp[
        [
            "country",
            "development_group",
            "year",
            "value"
        ]
    ].to_string(index=False)
)


# ==================================================
# 2. POPULATION ANALYSIS
# ==================================================

population_df = df[df["indicator"] == "population"].copy()

latest_population = (
    population_df
    .sort_values("year")
    .groupby("country")
    .tail(1)
    .sort_values("value", ascending=False)
)

print("\n" + "=" * 60)
print("LATEST POPULATION BY COUNTRY")
print("=" * 60)

print(
    latest_population[
        [
            "country",
            "development_group",
            "year",
            "value"
        ]
    ].to_string(index=False)
)


# ==================================================
# 3. UNEMPLOYMENT ANALYSIS
# ==================================================

unemployment_df = df[df["indicator"] == "unemployment"].copy()

latest_unemployment = (
    unemployment_df
    .sort_values("year")
    .groupby("country")
    .tail(1)
    .sort_values("value", ascending=False)
)

print("\n" + "=" * 60)
print("LATEST UNEMPLOYMENT BY COUNTRY")
print("=" * 60)

print(
    latest_unemployment[
        [
            "country",
            "development_group",
            "year",
            "value"
        ]
    ].to_string(index=False)
)
# ==================================================
# 4. GDP PER CAPITA ANALYSIS
# ==================================================

gdp_per_capita_df = df[
    df["indicator"] == "gdp_per_capita"
].copy()

latest_gdp_per_capita = (
    gdp_per_capita_df
    .sort_values("year")
    .groupby("country")
    .tail(1)
    .sort_values("value", ascending=False)
)

print("\n" + "=" * 60)
print("LATEST GDP PER CAPITA BY COUNTRY")
print("=" * 60)

print(
    latest_gdp_per_capita[
        [
            "country",
            "development_group",
            "year",
            "value"
        ]
    ].to_string(index=False)
)


# ==================================================
# 5. DEVELOPMENT GROUP ANALYSIS
# ==================================================

group_gdp = (
    gdp_df
    .groupby(["development_group", "year"])["value"]
    .mean()
    .reset_index()
)

print("\n" + "=" * 60)
print("AVERAGE GDP BY DEVELOPMENT GROUP")
print("=" * 60)

print(
    group_gdp
    .sort_values(["year", "value"], ascending=[False, False])
    .head(15)
    .to_string(index=False)
)


# ==================================================
# 6. MISSING DATA ANALYSIS
# ==================================================

missing_data = (
    df
    .groupby(["indicator", "development_group"])["value"]
    .apply(lambda x: x.isna().sum())
    .reset_index(name="missing_values")
)

print("\n" + "=" * 60)
print("MISSING VALUES BY INDICATOR AND GROUP")
print("=" * 60)

print(missing_data.to_string(index=False))