import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def load_data():
    return pd.read_csv(
        Path("data/processed/development_data.csv")
    )


df = load_data()

st.title("🧠 Automated Development Insights")

st.markdown(
    """
    This page automatically identifies important patterns,
    differences, and development gaps within the dataset.
    """
)

st.divider()

latest_year = df["year"].max()

latest = df[df["year"] == latest_year].copy()


# --------------------------------------------------
# GDP PER CAPITA GAP
# --------------------------------------------------

st.subheader("💰 Economic Development Gap")

gdp_pc = latest[
    latest["indicator"] == "gdp_per_capita"
].dropna(subset=["value"])


group_gdp_pc = (
    gdp_pc
    .groupby("development_group")["value"]
    .mean()
)


if (
    "Developed" in group_gdp_pc.index
    and "Least Developed" in group_gdp_pc.index
):

    developed_avg = group_gdp_pc["Developed"]
    ldc_avg = group_gdp_pc["Least Developed"]

    gap = (
        (developed_avg - ldc_avg)
        / developed_avg
    ) * 100

    st.info(
        f"📌 In {latest_year}, the average GDP per capita "
        f"of Developed countries was approximately "
        f"**{gap:.1f}% higher** than the Least Developed group."
    )


# --------------------------------------------------
# HIGHEST GDP
# --------------------------------------------------

st.subheader("🏆 Largest Economies")

gdp = latest[
    latest["indicator"] == "gdp"
].dropna(subset=["value"])


if not gdp.empty:

    highest_gdp = (
        gdp
        .sort_values("value", ascending=False)
        .iloc[0]
    )

    st.success(
        f"🏆 **{highest_gdp['country']}** had the largest "
        f"GDP among the countries analyzed in {latest_year}, "
        f"at approximately **${highest_gdp['value']:,.0f}**."
    )


# --------------------------------------------------
# POPULATION
# --------------------------------------------------

st.subheader("👥 Population Insight")

population = latest[
    latest["indicator"] == "population"
].dropna(subset=["value"])


if not population.empty:

    largest_population = (
        population
        .sort_values("value", ascending=False)
        .iloc[0]
    )

    st.info(
        f"👥 **{largest_population['country']}** had the "
        f"largest population in the dataset in {latest_year}, "
        f"with approximately **{largest_population['value']:,.0f} people**."
    )


# --------------------------------------------------
# UNEMPLOYMENT
# --------------------------------------------------

st.subheader("💼 Employment Insight")

unemployment = latest[
    latest["indicator"] == "unemployment"
].dropna(subset=["value"])


if not unemployment.empty:

    highest_unemployment = (
        unemployment
        .sort_values("value", ascending=False)
        .iloc[0]
    )

    lowest_unemployment = (
        unemployment
        .sort_values("value")
        .iloc[0]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.warning(
            f"🔴 Highest unemployment: "
            f"**{highest_unemployment['country']}** "
            f"({highest_unemployment['value']:.2f}%)"
        )

    with col2:

        st.success(
            f"🟢 Lowest unemployment: "
            f"**{lowest_unemployment['country']}** "
            f"({lowest_unemployment['value']:.2f}%)"
        )


# --------------------------------------------------
# DEVELOPMENT GROUP INSIGHT
# --------------------------------------------------

st.subheader("🌐 Development Group Insight")

group_gdp = (
    latest[
        latest["indicator"] == "gdp"
    ]
    .dropna(subset=["value"])
    .groupby("development_group")["value"]
    .mean()
    .sort_values(ascending=False)
)


if not group_gdp.empty:

    highest_group = group_gdp.index[0]

    st.info(
        f"📊 Among the three development groups, "
        f"**{highest_group}** had the highest average GDP "
        f"in {latest_year}."
    )


st.divider()

st.caption(
    "Insights are automatically generated from the latest available "
    "World Bank data in the project dataset."
)