import streamlit as st
import pandas as pd
from pathlib import Path


st.title("🌍 Development & SDG Overview")

st.markdown("""
### Measuring Development Beyond GDP

This dashboard uses World Bank indicators to compare development
across **Developed, Developing, and Least Developed Countries (LDCs)**.

The indicators are selected to provide a broader view of development,
including **economic performance, population, employment, and living standards**.
""")


# Load master dataset
data_path = Path("data/processed/development_data.csv")
df = pd.read_csv(data_path)


# Latest year
latest_year = df["year"].max()

st.subheader(f"📊 Global Development Snapshot — {latest_year}")


# Latest data
latest = df[df["year"] == latest_year]


# KPI calculations
countries = latest["country"].nunique()

developed = (
    latest[latest["development_group"] == "Developed"]["country"]
    .nunique()
)

developing = (
    latest[latest["development_group"] == "Developing"]["country"]
    .nunique()
)

ldcs = (
    latest[latest["development_group"] == "Least Developed"]["country"]
    .nunique()
)


col1, col2, col3, col4 = st.columns(4)

col1.metric("🌎 Countries", countries)
col2.metric("🏭 Developed", developed)
col3.metric("📈 Developing", developing)
col4.metric("🌱 LDCs", ldcs)


st.divider()


# Development group comparison
st.subheader("🌐 Development Group Comparison")

comparison = (
    latest
    .groupby("development_group")["value"]
    .count()
    .reset_index(name="observations")
)

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)


st.divider()


st.subheader("🎯 SDG-Relevant Indicators")

st.markdown("""
The dashboard currently tracks indicators connected to major
development priorities:

- 💰 **GDP & GDP per capita** → economic development
- 👥 **Population** → demographic change
- 💼 **Unemployment** → decent work and economic opportunity
- 🌍 **CO₂ emissions** → environmental sustainability

These indicators can be used to explore development gaps between
different country groups.
""")