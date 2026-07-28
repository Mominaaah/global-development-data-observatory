import pandas as pd
from pathlib import Path


# ==================================================
# LOAD DATA
# ==================================================

def load_data():
    """
    Load the master development dataset.
    """

    data_path = Path("data/processed/development_data.csv")

    return pd.read_csv(data_path)


# ==================================================
# CALCULATE GROWTH RATES
# ==================================================

def calculate_growth_rates(df):
    """
    Calculate year-over-year percentage growth
    for GDP, population, and GDP per capita.
    """

    growth_df = df.copy()

    # Sort data correctly before calculating growth
    growth_df = growth_df.sort_values(
        [
            "country",
            "indicator",
            "year"
        ]
    )

    # Calculate previous year's value
    growth_df["previous_value"] = (
        growth_df
        .groupby(
            [
                "country",
                "indicator"
            ]
        )["value"]
        .shift(1)
    )

    # Calculate growth rate
    growth_df["growth_rate"] = (
        (
            growth_df["value"]
            - growth_df["previous_value"]
        )
        / growth_df["previous_value"]
    ) * 100

    return growth_df


# ==================================================
# LATEST GROWTH RATES
# ==================================================

def show_latest_growth_rates(growth_df):

    selected_indicators = [
        "gdp",
        "population",
        "gdp_per_capita"
    ]

    latest_growth = growth_df[
        growth_df["indicator"].isin(
            selected_indicators
        )
    ].copy()

    latest_growth = (
        latest_growth
        .dropna(subset=["growth_rate"])
        .sort_values("year")
        .groupby(
            [
                "country",
                "indicator"
            ]
        )
        .tail(1)
    )

    print("\n")
    print("=" * 60)
    print("LATEST YEAR-OVER-YEAR GROWTH RATES")
    print("=" * 60)

    print(
        latest_growth[
            [
                "country",
                "development_group",
                "indicator",
                "year",
                "growth_rate"
            ]
        ]
        .sort_values(
            [
                "indicator",
                "growth_rate"
            ],
            ascending=[True, False]
        )
        .to_string(index=False)
    )


# ==================================================
# AVERAGE GROWTH BY DEVELOPMENT GROUP
# ==================================================

def average_growth_by_group(growth_df):

    selected_indicators = [
        "gdp",
        "population",
        "gdp_per_capita"
    ]

    group_growth = growth_df[
        growth_df["indicator"].isin(
            selected_indicators
        )
    ].copy()

    result = (
        group_growth
        .dropna(subset=["growth_rate"])
        .groupby(
            [
                "development_group",
                "indicator"
            ],
            as_index=False
        )["growth_rate"]
        .mean()
    )

    print("\n")
    print("=" * 60)
    print("AVERAGE GROWTH RATE BY DEVELOPMENT GROUP")
    print("=" * 60)

    print(
        result
        .sort_values(
            [
                "indicator",
                "growth_rate"
            ],
            ascending=[True, False]
        )
        .to_string(index=False)
    )


# ==================================================
# SAVE GROWTH DATASET
# ==================================================

def save_growth_data(growth_df):

    output_path = Path(
        "data/processed/development_data_with_growth.csv"
    )

    growth_df.to_csv(
        output_path,
        index=False
    )

    print("\n")
    print("=" * 60)
    print("GROWTH DATASET SAVED")
    print("=" * 60)

    print(
        f"Saved to: {output_path}"
    )


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    df = load_data()

    growth_df = calculate_growth_rates(df)

    show_latest_growth_rates(
        growth_df
    )

    average_growth_by_group(
        growth_df
    )

    save_growth_data(
        growth_df
    )