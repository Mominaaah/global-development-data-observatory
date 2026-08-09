import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


@st.cache_data
def load_data():
    path = Path("data/processed/development_data.csv")
    return pd.read_csv(path)


df = load_data()

st.title("🌍 Country Development Profile")
st.write(
    "Explore economic, demographic, and employment trends "
    "for an individual country."
)

# -----------------------------
# COUNTRY SELECTION
# -----------------------------

countries = sorted(df["country"].unique())

country = st.selectbox(
    "Select a country",
    countries
)

country_df = df[df["country"] == country].copy()

# -----------------------------
# COUNTRY INFORMATION
# -----------------------------

development_group = country_df["development_group"].iloc[0]

st.info(
    f"**{country}** | Development Group: **{development_group}**"
)

# -----------------------------
# KPI VALUES
# -----------------------------

latest_year = country_df["year"].max()

latest = country_df[
    country_df["year"] == latest_year
]

gdp = latest[
    latest["indicator"] == "gdp"
]["value"].dropna()

population = latest[
    latest["indicator"] == "population"
]["value"].dropna()

gdp_pc = latest[
    latest["indicator"] == "gdp_per_capita"
]["value"].dropna()

unemployment = latest[
    latest["indicator"] == "unemployment"
]["value"].dropna()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest Year",
        latest_year
    )

with col2:
    st.metric(
        "Population",
        f"{population.iloc[0]:,.0f}" if len(population) else "N/A"
    )

with col3:
    st.metric(
        "GDP",
        f"${gdp.iloc[0]:,.0f}" if len(gdp) else "N/A"
    )

with col4:
    st.metric(
        "GDP Per Capita",
        f"${gdp_pc.iloc[0]:,.0f}" if len(gdp_pc) else "N/A"
    )

# -----------------------------
# GDP TREND
# -----------------------------

st.subheader("📈 Economic Growth")

gdp_df = country_df[
    country_df["indicator"] == "gdp"
].dropna(subset=["value"])

fig = px.line(
    gdp_df,
    x="year",
    y="value",
    title=f"GDP Trend — {country}",
    markers=True
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="GDP (USD)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# POPULATION TREND
# -----------------------------

st.subheader("👥 Population Growth")

pop_df = country_df[
    country_df["indicator"] == "population"
].dropna(subset=["value"])

fig = px.line(
    pop_df,
    x="year",
    y="value",
    title=f"Population Trend — {country}",
    markers=True
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Population",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# UNEMPLOYMENT
# -----------------------------

st.subheader("💼 Employment")

unemployment_df = country_df[
    country_df["indicator"] == "unemployment"
].dropna(subset=["value"])

fig = px.line(
    unemployment_df,
    x="year",
    y="value",
    title=f"Unemployment Rate — {country}",
    markers=True
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Unemployment (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# RAW DATA
# -----------------------------

with st.expander("📊 View Country Data"):

    st.dataframe(
        country_df.sort_values(
            ["indicator", "year"],
            ascending=[True, False]
        ),
        use_container_width=True
    )