import pandas as pd
from pathlib import Path


# ==================================================
# LOAD DATA
# ==================================================

def load_data():

    data_path = Path(
        "data/processed/development_data_with_growth.csv"
    )

    return pd.read_csv(data_path)


# ==================================================
# LATEST INDICATOR INSIGHTS
# ==================================================

def latest_indicator_insights(df):

    indicators = [
        "gdp",
        "population",
        "gdp_per_capita",
        "unemployment"
    ]

    print("\n")
    print("=" * 70)
    print("LATEST INDICATOR INSIGHTS")
    print("=" * 70)

    for indicator in indicators:

        data = df[
            df["indicator"] == indicator
        ].copy()

        latest = (
            data
            .sort_values("year")
            .groupby("country")
            .tail(1)
            .dropna(subset=["value"])
        )

        if latest.empty:
            continue

        highest = latest.loc[
            latest["value"].idxmax()
        ]

        lowest = latest.loc[
            latest["value"].idxmin()
        ]

        print(
            f"\n📊 {indicator.upper()}"
        )

        print(
            f"Highest: {highest['country']} "
            f"({highest['value']:,.2f})"
        )

        print(
            f"Lowest: {lowest['country']} "
            f"({lowest['value']:,.2f})"
        )


# ==================================================
# FASTEST GDP GROWTH
# ==================================================

def fastest_gdp_growth(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    latest_growth = (
        gdp
        .dropna(subset=["growth_rate"])
        .sort_values("year")
        .groupby("country")
        .tail(1)
        .sort_values(
            "growth_rate",
            ascending=False
        )
    )

    print("\n")
    print("=" * 70)
    print("GDP GROWTH INSIGHTS")
    print("=" * 70)

    fastest = latest_growth.iloc[0]

    slowest = latest_growth.iloc[-1]

    print(
        f"\n🚀 Fastest latest GDP growth: "
        f"{fastest['country']} "
        f"({fastest['growth_rate']:.2f}%)"
    )

    print(
        f"📉 Lowest latest GDP growth: "
        f"{slowest['country']} "
        f"({slowest['growth_rate']:.2f}%)"
    )


# ==================================================
# DEVELOPMENT GROUP INSIGHTS
# ==================================================

def development_group_insights(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    group_growth = (
        gdp
        .dropna(subset=["growth_rate"])
        .groupby(
            "development_group"
        )["growth_rate"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    print("\n")
    print("=" * 70)
    print("DEVELOPMENT GROUP INSIGHTS")
    print("=" * 70)

    highest_group = group_growth.index[0]

    lowest_group = group_growth.index[-1]

    print(
        f"\n🏆 Highest average GDP growth: "
        f"{highest_group} "
        f"({group_growth.iloc[0]:.2f}%)"
    )

    print(
        f"📉 Lowest average GDP growth: "
        f"{lowest_group} "
        f"({group_growth.iloc[-1]:.2f}%)"
    )


# ==================================================
# HISTORICAL PEAK GDP GROWTH
# ==================================================

def historical_growth_insight(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    highest_growth = gdp.loc[
        gdp["growth_rate"].idxmax()
    ]

    lowest_growth = gdp.loc[
        gdp["growth_rate"].idxmin()
    ]

    print("\n")
    print("=" * 70)
    print("HISTORICAL GROWTH EVENTS")
    print("=" * 70)

    print(
        f"\n📈 Highest recorded GDP growth: "
        f"{highest_growth['country']} "
        f"in {int(highest_growth['year'])} "
        f"({highest_growth['growth_rate']:.2f}%)"
    )

    print(
        f"📉 Largest GDP contraction: "
        f"{lowest_growth['country']} "
        f"in {int(lowest_growth['year'])} "
        f"({lowest_growth['growth_rate']:.2f}%)"
    )


# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    df = load_data()

    latest_indicator_insights(df)

    fastest_gdp_growth(df)

    development_group_insights(df)

    historical_growth_insight(df)

    print("\n")
    print("=" * 70)
    print("AUTOMATED INSIGHTS GENERATED SUCCESSFULLY")
    print("=" * 70)