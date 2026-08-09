import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


@st.cache_data
def load_data():
    return pd.read_csv(
        Path("data/processed/development_data.csv")
    )


df = load_data()

st.title("🇺🇳 SDG Development Lens")

st.markdown("""
### Measuring Development Through an SDG-Aligned Lens

This section connects selected World Bank indicators with
major **UN Sustainable Development Goal (SDG)** themes.

> This is an independent analytical project and is **not an official UN dashboard**.
""")

st.divider()

# --------------------------------------------------
# SDG DEFINITIONS
# --------------------------------------------------

sdg_info = {
    "SDG 3 — Good Health & Well-being": {
        "indicator": "life_expectancy",
        "description": "Life expectancy is used as a broad indicator of population health."
    },

    "SDG 8 — Decent Work & Economic Growth": {
        "indicator": "gdp_per_capita",
        "description": "GDP per capita and unemployment help examine economic opportunity and employment."
    },

    "SDG 10 — Reduced Inequalities": {
        "indicator": "gdp_per_capita",
        "description": "GDP per capita differences help illustrate economic disparities between country groups."
    },

    "SDG 13 — Climate Action": {
        "indicator": "co2_emissions",
        "description": "CO₂ emissions per capita provide an environmental comparison across countries."
    }
}


# --------------------------------------------------
# SDG SELECTION
# --------------------------------------------------

selected_sdg = st.selectbox(
    "🎯 Select an SDG Theme",
    list(sdg_info.keys())
)

info = sdg_info[selected_sdg]

indicator = info["indicator"]

st.info(info["description"])


# --------------------------------------------------
# CHECK WHETHER INDICATOR EXISTS
# --------------------------------------------------

if indicator not in df["indicator"].unique():

    st.warning(
        f"The indicator `{indicator}` is not yet available in your dataset."
    )

    st.write(
        "Add this indicator to your World Bank API configuration, "
        "download the data, run the ETL pipeline, and return here."
    )

    st.stop()


# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

indicator_df = df[
    df["indicator"] == indicator
].dropna(subset=["value"])


latest_year = indicator_df["year"].max()

latest = indicator_df[
    indicator_df["year"] == latest_year
]


st.subheader(
    f"📊 Latest Comparison — {latest_year}"
)


# --------------------------------------------------
# GROUP COMPARISON
# --------------------------------------------------

group_data = (
    latest
    .groupby("development_group", as_index=False)["value"]
    .mean()
)


fig = px.bar(
    group_data,
    x="development_group",
    y="value",
    title=f"{indicator.replace('_', ' ').title()} by Development Group",
    text_auto=".2s"
)

fig.update_layout(
    xaxis_title="Development Group",
    yaxis_title=indicator.replace("_", " ").title()
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# --------------------------------------------------
# COUNTRY COMPARISON
# --------------------------------------------------

st.subheader("🌍 Country Comparison")


fig = px.bar(
    latest.sort_values("value"),
    x="value",
    y="country",
    color="development_group",
    orientation="h",
    title=f"{indicator.replace('_', ' ').title()} Across Countries"
)

fig.update_layout(
    xaxis_title=indicator.replace("_", " ").title(),
    yaxis_title="Country"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# --------------------------------------------------
# HISTORICAL TREND
# --------------------------------------------------

st.subheader("📈 Long-Term Development Trend")


trend = (
    indicator_df
    .groupby(
        ["development_group", "year"],
        as_index=False
    )["value"]
    .mean()
)


fig = px.line(
    trend,
    x="year",
    y="value",
    color="development_group",
    title=f"{indicator.replace('_', ' ').title()} — Development Groups Over Time",
    markers=True
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Average Value",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)