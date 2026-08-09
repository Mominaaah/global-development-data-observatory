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

st.title("📈 Development Trends")

st.write(
    "Explore how key development indicators have changed "
    "across countries and development groups over time."
)

# -----------------------------
# FILTERS
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    indicator = st.selectbox(
        "Select Indicator",
        sorted(df["indicator"].unique())
    )

with col2:
    group = st.selectbox(
        "Select Development Group",
        ["All"] + sorted(df["development_group"].unique())
    )

filtered = df[df["indicator"] == indicator].copy()

if group != "All":
    filtered = filtered[
        filtered["development_group"] == group
    ]

# -----------------------------
# COUNTRY TREND
# -----------------------------

st.subheader("🌍 Country Trends")

countries = st.multiselect(
    "Select Countries",
    sorted(filtered["country"].unique()),
    default=sorted(filtered["country"].unique())[:5]
)

country_data = filtered[
    filtered["country"].isin(countries)
].dropna(subset=["value"])

fig = px.line(
    country_data,
    x="year",
    y="value",
    color="country",
    markers=True,
    title=f"{indicator.replace('_', ' ').title()} Over Time"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title=indicator.replace("_", " ").title(),
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# DEVELOPMENT GROUP TREND
# -----------------------------

st.subheader("🌐 Development Group Trend")

group_data = (
    df[df["indicator"] == indicator]
    .groupby(
        ["development_group", "year"],
        as_index=False
    )["value"]
    .mean()
)

fig = px.line(
    group_data,
    x="year",
    y="value",
    color="development_group",
    markers=True,
    title=f"Average {indicator.replace('_', ' ').title()} by Development Group"
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

# -----------------------------
# GROWTH SUMMARY
# -----------------------------

st.subheader("📊 Growth Summary")

summary = []

for country in filtered["country"].unique():

    country_df = (
        filtered[
            filtered["country"] == country
        ]
        .dropna(subset=["value"])
        .sort_values("year")
    )

    if len(country_df) >= 2:

        first_value = country_df["value"].iloc[0]
        last_value = country_df["value"].iloc[-1]

        growth = (
            (last_value - first_value)
            / first_value
        ) * 100

        summary.append({
            "Country": country,
            "Start Year": country_df["year"].iloc[0],
            "End Year": country_df["year"].iloc[-1],
            "Growth (%)": round(growth, 2)
        })

growth_df = pd.DataFrame(summary)

if not growth_df.empty:

    growth_df = growth_df.sort_values(
        "Growth (%)",
        ascending=False
    )

    st.dataframe(
        growth_df,
        use_container_width=True
    )