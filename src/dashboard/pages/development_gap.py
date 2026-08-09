import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


@st.cache_data
def load_data():
    path = Path("data/processed/development_data.csv")
    return pd.read_csv(path)


df = load_data()

st.title("🌐 Development Group Comparison")

st.write(
    "Compare economic, demographic, and employment indicators "
    "across Developed, Developing, and Least Developed countries."
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
    selected_year = st.selectbox(
        "Select Year",
        sorted(df["year"].unique(), reverse=True)
    )


filtered = df[
    (df["indicator"] == indicator) &
    (df["year"] == selected_year)
].copy()

# -----------------------------
# AVERAGE BY DEVELOPMENT GROUP
# -----------------------------

group_data = (
    filtered
    .groupby("development_group", as_index=False)["value"]
    .mean()
)

st.subheader(
    f"📊 {indicator.replace('_', ' ').title()} — {selected_year}"
)

fig = px.bar(
    group_data,
    x="development_group",
    y="value",
    title=f"Average {indicator.replace('_', ' ').title()} by Development Group",
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

# -----------------------------
# COUNTRY COMPARISON
# -----------------------------

st.subheader("🌍 Country-Level Comparison")

fig = px.bar(
    filtered.sort_values("value"),
    x="value",
    y="country",
    color="development_group",
    orientation="h",
    title=f"{indicator.replace('_', ' ').title()} by Country — {selected_year}",
)

fig.update_layout(
    xaxis_title=indicator.replace("_", " ").title(),
    yaxis_title="Country"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# HISTORICAL GROUP TREND
# -----------------------------

st.subheader("📈 Development Group Trends")

trend = (
    df[df["indicator"] == indicator]
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
# DATA TABLE
# -----------------------------

with st.expander("📋 View Comparison Data"):

    st.dataframe(
        filtered.sort_values(
            "value",
            ascending=False
        ),
        use_container_width=True
    )