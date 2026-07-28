import pandas as pd
import matplotlib.pyplot as plt
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
# OUTPUT FOLDER
# ==================================================

OUTPUT_PATH = Path(
    "data/visualizations"
)

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ==================================================
# CHART 1: GDP GROWTH RATE
# ==================================================

def gdp_growth_chart(df):

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
        gdp["country"].isin(
            selected_countries
        )
    ]

    plt.figure(
        figsize=(12, 7)
    )

    for country in selected_countries:

        country_data = gdp[
            gdp["country"] == country
        ]

        plt.plot(
            country_data["year"],
            country_data["growth_rate"],
            label=country
        )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.title(
        "GDP Year-over-Year Growth Rate"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Growth Rate (%)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH
        / "gdp_growth_rate.png",

        dpi=300,

        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==================================================
# CHART 2: POPULATION GROWTH RATE
# ==================================================

def population_growth_chart(df):

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
        population["country"].isin(
            selected_countries
        )
    ]

    plt.figure(
        figsize=(12, 7)
    )

    for country in selected_countries:

        country_data = population[
            population["country"] == country
        ]

        plt.plot(
            country_data["year"],
            country_data["growth_rate"],
            label=country
        )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.title(
        "Population Year-over-Year Growth Rate"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Growth Rate (%)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH
        / "population_growth_rate.png",

        dpi=300,

        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==================================================
# CHART 3: DEVELOPMENT GROUP GROWTH
# ==================================================

def development_group_growth_chart(df):

    gdp = df[
        df["indicator"] == "gdp"
    ].copy()

    group_growth = (
        gdp
        .groupby(
            [
                "development_group",
                "year"
            ],
            as_index=False
        )["growth_rate"]
        .mean()
    )

    development_groups = [
        "Developed",
        "Developing",
        "Least Developed"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    for group in development_groups:

        group_data = group_growth[
            group_growth[
                "development_group"
            ] == group
        ]

        plt.plot(
            group_data["year"],
            group_data["growth_rate"],
            label=group
        )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.title(
        "Average GDP Growth Rate by Development Group"
    )

    plt.xlabel(
        "Year"
    )

    plt.ylabel(
        "Average Growth Rate (%)"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH
        / "development_group_growth_rate.png",

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

    print(
        "Creating GDP growth chart..."
    )

    gdp_growth_chart(df)

    print(
        "Creating population growth chart..."
    )

    population_growth_chart(df)

    print(
        "Creating development group growth chart..."
    )

    development_group_growth_chart(df)

    print(
        "\nAll growth visualizations created successfully!"
    )