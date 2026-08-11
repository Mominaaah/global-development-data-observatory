import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Development Gap",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# LOAD DEVELOPMENT INDEX
# ============================================================

DATA_PATH = Path(
    "data/processed/development_index.csv"
)

df = pd.read_csv(DATA_PATH)


# ============================================================
# HEADER
# ============================================================

st.title("⚖️ Development Gap Analysis")

st.markdown(
    """
    Compare development performance across countries and
    identify the dimensions where the largest disparities exist.
    """
)

st.divider()


# ============================================================
# DEVELOPMENT GROUP SUMMARY
# ============================================================

st.subheader("🌍 Development Group Comparison")


group_summary = (
    df
    .groupby("development_group")["development_index"]
    .mean()
    .reset_index()
    .sort_values(
        "development_index",
        ascending=False
    )
)


col1, col2, col3 = st.columns(3)


for i, row in group_summary.iterrows():

    group = row["development_group"]
    score = row["development_index"]

    if i == group_summary.index[0]:
        with col1:
            st.metric(
                group,
                f"{score:.1f}/100"
            )

    elif i == group_summary.index[1]:
        with col2:
            st.metric(
                group,
                f"{score:.1f}/100"
            )

    elif i == group_summary.index[2]:
        with col3:
            st.metric(
                group,
                f"{score:.1f}/100"
            )


# ============================================================
# GROUP CHART
# ============================================================

st.bar_chart(
    group_summary.set_index(
        "development_group"
    )["development_index"]
)


# ============================================================
# COUNTRY RANKING
# ============================================================

st.divider()

st.subheader("🏆 Country Development Ranking")


ranking = df[
    [
        "country",
        "development_group",
        "development_index",
        "development_rank"
    ]
].sort_values(
    "development_rank"
)


st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DEVELOPMENT DIMENSION GAPS
# ============================================================

st.divider()

st.subheader("📊 Development Dimension Gaps")


dimensions = [
    "economic_score",
    "social_score",
    "infrastructure_score",
    "employment_score"
]


dimension_names = {
    "economic_score": "Economic",
    "social_score": "Social",
    "infrastructure_score": "Infrastructure",
    "employment_score": "Employment"
}


gap_data = []

for dimension in dimensions:

    highest = df[dimension].max()
    lowest = df[dimension].min()

    gap = highest - lowest

    gap_data.append(
        {
            "Dimension": dimension_names[dimension],
            "Highest Score": round(highest, 2),
            "Lowest Score": round(lowest, 2),
            "Development Gap": round(gap, 2)
        }
    )


gap_df = pd.DataFrame(gap_data)


st.dataframe(
    gap_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# LARGEST GAP
# ============================================================

largest_gap = gap_df.loc[
    gap_df["Development Gap"].idxmax()
]


st.warning(
    f"🔴 **Largest development disparity:** "
    f"{largest_gap['Dimension']} "
    f"({largest_gap['Development Gap']:.1f} points)"
)


# ============================================================
# TOP 5 DEVELOPMENT GAPS
# ============================================================

st.divider()

st.subheader("🔻 Countries with Lowest Development Scores")


bottom_5 = (
    df[
        [
            "country",
            "development_group",
            "development_index"
        ]
    ]
    .sort_values(
        "development_index"
    )
    .head(5)
)


st.dataframe(
    bottom_5,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# PEER GAP ANALYSIS
# ============================================================

st.divider()

st.subheader("🤝 Peer Group Gap Analysis")

st.markdown(
    """
    Compare a country against the average development performance
    of countries in the same development group.
    """
)


# ------------------------------------------------------------
# COUNTRY SELECTOR
# ------------------------------------------------------------

selected_country = st.selectbox(
    "Select a country for peer comparison",
    sorted(df["country"].unique())
)


country_data = df[
    df["country"] == selected_country
].iloc[0]


selected_group = country_data["development_group"]


# ------------------------------------------------------------
# PEER GROUP
# ------------------------------------------------------------

peer_data = df[
    df["development_group"] == selected_group
]


peer_average = peer_data[
    "development_index"
].mean()


country_score = country_data[
    "development_index"
]


peer_gap = country_score - peer_average


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Country Score",
        f"{country_score:.1f}/100"
    )


with col2:

    st.metric(
        "Peer Group Average",
        f"{peer_average:.1f}/100"
    )


with col3:

    st.metric(
        "Gap vs Peers",
        f"{peer_gap:+.1f}"
    )


# ------------------------------------------------------------
# INTERPRETATION
# ------------------------------------------------------------

if peer_gap < 0:

    st.warning(
        f"📉 **{selected_country}** is "
        f"{abs(peer_gap):.1f} points below the "
        f"average of its **{selected_group}** peers."
    )

elif peer_gap > 0:

    st.success(
        f"📈 **{selected_country}** is "
        f"{peer_gap:.1f} points above the "
        f"average of its **{selected_group}** peers."
    )

else:

    st.info(
        f"⚖️ **{selected_country}** is exactly "
        f"at the average of its peer group."
    )


# ------------------------------------------------------------
# DIMENSION-LEVEL PEER GAP
# ------------------------------------------------------------

st.subheader(
    f"📊 {selected_country} vs {selected_group} Peers"
)


peer_dimensions = []

dimension_columns = {
    "Economic": "economic_score",
    "Social": "social_score",
    "Infrastructure": "infrastructure_score",
    "Employment": "employment_score"
}


for dimension, column in dimension_columns.items():

    country_value = country_data[column]

    peer_value = peer_data[column].mean()

    gap = country_value - peer_value

    peer_dimensions.append(
        {
            "Dimension": dimension,
            selected_country: round(country_value, 2),
            "Peer Average": round(peer_value, 2),
            "Gap": round(gap, 2)
        }
    )


peer_gap_df = pd.DataFrame(
    peer_dimensions
)


st.dataframe(
    peer_gap_df,
    use_container_width=True,
    hide_index=True
)


# ------------------------------------------------------------
# PEER GAP CHART
# ------------------------------------------------------------

chart_data = peer_gap_df.set_index(
    "Dimension"
)[
    [
        selected_country,
        "Peer Average"
    ]
]


st.bar_chart(chart_data)