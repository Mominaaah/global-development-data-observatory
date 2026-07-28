import pandas as pd
import matplotlib.pyplot as plt
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
# CREATE OUTPUT FOLDER
# ==================================================

OUTPUT_PATH = Path("data/visualizations")

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ==================================================
# CHART 1: GDP PER CAPITA
# ==================================================

def latest_gdp_per_capita_chart(df):

    gdp_pc = df[
        df["indicator"] == "gdp_per_capita"
    ].copy()

    latest = (
        gdp_pc
        .sort_values("year")
        .groupby("country")
        .tail(1)
        .dropna(subset=["value"])
        .sort_values("value")
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        latest["country"],
        latest["value"]
    )

    plt.title(
        "GDP Per Capita by Country"
    )

    plt.xlabel(
        "GDP Per Capita (USD)"
    )

    plt.ylabel(
        "Country"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH / "gdp_per_capita_by_country.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==================================================
# CHART 2: GDP TREND OVER TIME
# ==================================================

def gdp_trend_chart(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    selected_countries = [
        "United States",
        "China",
        "India",
        "Pakistan",
        "Germany"
    ]

    gdp = gdp[
        gdp["country"].isin(selected_countries)
    ]

    plt.figure(figsize=(12, 7))

    for country in selected_countries:

        country_data = gdp[
            gdp["country"] == country
        ]

        plt.plot(
            country_data["year"],
            country_data["value"],
            label=country
        )

    plt.title(
        "GDP Growth Trend Over Time"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "GDP (USD)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH / "gdp_trend_over_time.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==================================================
# CHART 3: POPULATION TREND
# ==================================================

def population_trend_chart(df):

    population = df[
        df["indicator"] == "population"
    ].copy()

    selected_countries = [
        "India",
        "China",
        "United States",
        "Pakistan",
        "Nigeria"
    ]

    population = population[
        population["country"].isin(selected_countries)
    ]

    plt.figure(figsize=(12, 7))

    for country in selected_countries:

        country_data = population[
            population["country"] == country
        ]

        plt.plot(
            country_data["year"],
            country_data["value"],
            label=country
        )

    plt.title(
        "Population Growth Over Time"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Population"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH / "population_trend_over_time.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==================================================
# CHART 4: UNEMPLOYMENT COMPARISON
# ==================================================

def unemployment_comparison_chart(df):

    unemployment = df[
        df["indicator"] == "unemployment"
    ].copy()

    latest = (
        unemployment
        .sort_values("year")
        .groupby("country")
        .tail(1)
        .dropna(subset=["value"])
        .sort_values("value")
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        latest["country"],
        latest["value"]
    )

    plt.title(
        "Latest Unemployment Rate by Country"
    )

    plt.xlabel(
        "Unemployment Rate (%)"
    )

    plt.ylabel(
        "Country"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH / "unemployment_by_country.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()

# ==================================================
# CHART 5: DEVELOPMENT GROUP GDP COMPARISON
# ==================================================

def development_group_comparison_chart(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    # Calculate average GDP for each development group by year
    group_gdp = (
        gdp
        .groupby(
            [
                "development_group",
                "year"
            ],
            as_index=False
        )["value"]
        .mean()
    )

    plt.figure(figsize=(12, 7))

    development_groups = [
        "Developed",
        "Developing",
        "Least Developed"
    ]

    for group in development_groups:

        group_data = group_gdp[
            group_gdp["development_group"] == group
        ]

        plt.plot(
            group_data["year"],
            group_data["value"],
            label=group
        )

    plt.title(
        "Average GDP by Development Group Over Time"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Average GDP (USD)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH / "gdp_by_development_group.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()

# ==================================================
# MAIN PROGRAM
# ==================================================

if __name__ == "__main__":

    df = load_data()

    print("Creating Chart 1...")
    latest_gdp_per_capita_chart(df)

    print("Creating Chart 2...")
    gdp_trend_chart(df)

    print("Creating Chart 3...")
    population_trend_chart(df)

    print("Creating Chart 4...")
    unemployment_comparison_chart(df)

    print("Creating Chart 5...")
    development_group_comparison_chart(df)

    print("\nAll visualizations created successfully!")