import pandas as pd
from pathlib import Path


# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = Path("data/processed/development_data.csv")

df = pd.read_csv(DATA_PATH)


# ============================================================
# GET LATEST NON-NULL VALUE FOR EACH COUNTRY + INDICATOR
# ============================================================

latest = (
    df.dropna(subset=["value"])
    .sort_values("year")
    .groupby(
        [
            "country",
            "country_code",
            "development_group",
            "indicator"
        ],
        as_index=False
    )
    .tail(1)
)


# ============================================================
# PIVOT INDICATORS
# ============================================================

pivot = latest.pivot_table(
    index=[
        "country",
        "country_code",
        "development_group"
    ],
    columns="indicator",
    values="value",
    aggfunc="first"
).reset_index()


# ============================================================
# MAKE SURE REQUIRED INDICATORS EXIST
# ============================================================

required_indicators = [
    "gdp_per_capita",
    "life_expectancy",
    "school_enrollment",
    "electricity_access",
    "unemployment"
]

for indicator in required_indicators:

    if indicator not in pivot.columns:
        pivot[indicator] = pd.NA


# ============================================================
# NORMALIZATION FUNCTION
# ============================================================

def normalize(series):

    minimum = series.min()
    maximum = series.max()

    if pd.isna(minimum) or pd.isna(maximum):
        return pd.Series(
            50,
            index=series.index,
            dtype="float64"
        )

    if maximum == minimum:
        return pd.Series(
            50,
            index=series.index,
            dtype="float64"
        )

    return (
        (series - minimum)
        / (maximum - minimum)
        * 100
    )


# ============================================================
# INDIVIDUAL SCORES
# ============================================================

pivot["economic_score"] = normalize(
    pivot["gdp_per_capita"]
)

pivot["health_score"] = normalize(
    pivot["life_expectancy"]
)

pivot["education_score"] = normalize(
    pivot["school_enrollment"]
)

pivot["infrastructure_score"] = normalize(
    pivot["electricity_access"]
)


# ============================================================
# EMPLOYMENT SCORE
# LOWER UNEMPLOYMENT = BETTER
# ============================================================

pivot["employment_score"] = (
    100 - normalize(pivot["unemployment"])
)


# ============================================================
# SOCIAL DEVELOPMENT SCORE
# ============================================================

pivot["social_score"] = (
    pivot["health_score"]
    + pivot["education_score"]
) / 2


# ============================================================
# OVERALL DEVELOPMENT INDEX
# ============================================================

pivot["development_index"] = (
    pivot["economic_score"]
    + pivot["social_score"]
    + pivot["infrastructure_score"]
    + pivot["employment_score"]
) / 4


# ============================================================
# ROUND SCORES
# ============================================================

score_columns = [
    "economic_score",
    "health_score",
    "education_score",
    "social_score",
    "infrastructure_score",
    "employment_score",
    "development_index"
]

pivot[score_columns] = pivot[score_columns].round(2)


# ============================================================
# RANK COUNTRIES
# ============================================================

result = pivot.sort_values(
    "development_index",
    ascending=False
).reset_index(drop=True)

result["development_rank"] = (
    result["development_index"]
    .rank(
        ascending=False,
        method="min"
    )
    .astype("Int64")
)


# ============================================================
# SAVE
# ============================================================

output_path = Path(
    "data/processed/development_index.csv"
)

result.to_csv(
    output_path,
    index=False
)


# ============================================================
# DISPLAY
# ============================================================

print("\n" + "=" * 70)
print("GLOBAL DEVELOPMENT INDEX")
print("=" * 70)

print(
    result[
        [
            "development_rank",
            "country",
            "development_group",
            "economic_score",
            "social_score",
            "infrastructure_score",
            "employment_score",
            "development_index"
        ]
    ].to_string(index=False)
)

print("=" * 70)
print(f"Saved to: {output_path}")
print("=" * 70)