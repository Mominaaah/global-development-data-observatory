import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Automated Insights",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = Path(
    "data/processed/development_index.csv"
)

df = pd.read_csv(DATA_PATH)


# ============================================================
# HEADER
# ============================================================

st.title("🧠 Automated Development Insights")

st.markdown(
    """
    Automatically generated analytical insights based on
    development performance, peer-group comparisons, and
    development dimensions.
    """
)

st.divider()


# ============================================================
# COUNTRY SELECTION
# ============================================================

selected_country = st.selectbox(
    "🌍 Select a country",
    sorted(df["country"].unique())
)


country = df[
    df["country"] == selected_country
].iloc[0]


development_group = country["development_group"]


# ============================================================
# DEVELOPMENT DIMENSIONS
# ============================================================

dimensions = {
    "Economic Development": country["economic_score"],
    "Social Development": country["social_score"],
    "Infrastructure": country["infrastructure_score"],
    "Employment": country["employment_score"]
}


strongest_area = max(
    dimensions,
    key=dimensions.get
)

weakest_area = min(
    dimensions,
    key=dimensions.get
)

strongest_score = dimensions[strongest_area]
weakest_score = dimensions[weakest_area]


# ============================================================
# PEER ANALYSIS
# ============================================================

peers = df[
    df["development_group"] == development_group
]


peer_average = peers[
    "development_index"
].mean()


country_score = country[
    "development_index"
]


peer_gap = country_score - peer_average


# ============================================================
# RANK
# ============================================================

rank = int(
    country["development_rank"]
)

total_countries = len(df)


# ============================================================
# INSIGHT 1 — DEVELOPMENT PERFORMANCE
# ============================================================

st.subheader("📊 Development Performance")

if peer_gap > 0:

    st.success(
        f"📈 **{selected_country}** has a development "
        f"index of **{country_score:.1f}/100**, which is "
        f"**{peer_gap:.1f} points above** the average "
        f"of its {development_group} peers."
    )

elif peer_gap < 0:

    st.warning(
        f"📉 **{selected_country}** has a development "
        f"index of **{country_score:.1f}/100**, which is "
        f"**{abs(peer_gap):.1f} points below** the average "
        f"of its {development_group} peers."
    )

else:

    st.info(
        f"⚖️ **{selected_country}** is approximately "
        f"at the average development level of its peers."
    )


# ============================================================
# INSIGHT CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Development Rank",
        f"#{rank} / {total_countries}"
    )


with col2:

    st.metric(
        "Strongest Dimension",
        strongest_area,
        f"{strongest_score:.1f}/100"
    )


with col3:

    st.metric(
        "Weakest Dimension",
        weakest_area,
        f"{weakest_score:.1f}/100"
    )


# ============================================================
# STRENGTH
# ============================================================

st.divider()

st.subheader("🟢 Key Strength")

st.success(
    f"**{strongest_area}** is the strongest development "
    f"dimension for **{selected_country}**, with a score "
    f"of **{strongest_score:.1f}/100**."
)


# ============================================================
# WEAKNESS
# ============================================================

st.subheader("🔴 Key Development Gap")

st.error(
    f"**{weakest_area}** is the weakest development "
    f"dimension for **{selected_country}**, with a score "
    f"of **{weakest_score:.1f}/100**."
)


# ============================================================
# SDG PRIORITY
# ============================================================

sdg_mapping = {

    "Economic Development":
        ("SDG 8", "Decent Work & Economic Growth"),

    "Social Development":
        ("SDG 3 / SDG 4",
         "Good Health & Quality Education"),

    "Infrastructure":
        ("SDG 7",
         "Affordable & Clean Energy"),

    "Employment":
        ("SDG 8",
         "Decent Work & Economic Growth")
}


sdg_code, sdg_name = sdg_mapping[
    weakest_area
]


st.subheader("🎯 Recommended SDG Priority")

st.info(
    f"Based on the weakest development dimension, "
    f"**{selected_country}** should prioritize "
    f"**{sdg_code} — {sdg_name}**."
)


# ============================================================
# OVERALL AUTOMATED SUMMARY
# ============================================================

st.divider()

st.subheader("🧠 Automated Summary")

summary = (
    f"**{selected_country}** belongs to the "
    f"**{development_group}** group and currently has "
    f"an overall development score of "
    f"**{country_score:.1f}/100**. "
)

if peer_gap < 0:

    summary += (
        f"Its development performance is "
        f"**{abs(peer_gap):.1f} points below** "
        f"its peer-group average. "
    )

elif peer_gap > 0:

    summary += (
        f"Its development performance is "
        f"**{peer_gap:.1f} points above** "
        f"its peer-group average. "
    )

else:

    summary += (
        "Its development performance is close to "
        "its peer-group average. "
    )


summary += (
    f"The country's strongest area is "
    f"**{strongest_area} ({strongest_score:.1f}/100)**, "
    f"while **{weakest_area} ({weakest_score:.1f}/100)** "
    f"represents its largest development challenge. "
    f"The analysis therefore highlights "
    f"**{sdg_code} — {sdg_name}** as a priority area."
)


st.markdown(summary)


# ============================================================
# DIMENSION TABLE
# ============================================================

st.divider()

st.subheader("📋 Detailed Dimension Analysis")


dimension_df = pd.DataFrame(
    {
        "Dimension": list(dimensions.keys()),
        "Score": [
            round(value, 2)
            for value in dimensions.values()
        ]
    }
)


st.dataframe(
    dimension_df,
    use_container_width=True,
    hide_index=True
)