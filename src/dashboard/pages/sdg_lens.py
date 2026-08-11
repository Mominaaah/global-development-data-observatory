import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(
    page_title="SDG Development Lens",
    page_icon="🇺🇳",
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

st.title("🇺🇳 SDG Development Lens")

st.markdown(
    """
    Explore development performance across economic, social,
    infrastructure, and employment dimensions.

    **Note:** The Development Index is a portfolio analytical
    measure created for this project. It is not an official
    United Nations SDG index.
    """
)

st.divider()


# ============================================================
# COUNTRY SELECTOR
# ============================================================

countries = sorted(df["country"].dropna().unique())

selected_country = st.selectbox(
    "🌍 Select a country",
    countries
)


country = df[
    df["country"] == selected_country
].iloc[0]


# ============================================================
# TOP METRICS
# ============================================================

col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Overall Development",
        f"{country['development_index']:.1f}/100"
    )


with col2:
    st.metric(
        "Economic",
        f"{country['economic_score']:.1f}/100"
    )


with col3:
    st.metric(
        "Social",
        f"{country['social_score']:.1f}/100"
    )


with col4:
    st.metric(
        "Infrastructure",
        f"{country['infrastructure_score']:.1f}/100"
    )

with col5:
    st.metric(
        "Employment",
        f"{country['employment_score']:.1f}/100"
    )

st.divider()


# ============================================================
# DEVELOPMENT DIMENSIONS
# ============================================================

st.subheader("📊 Development Dimensions")


dimensions = pd.DataFrame(
    {
        "Dimension": [
            "Economic Development",
            "Social Development",
            "Infrastructure",
            "Employment"
        ],
        "Score": [
            country["economic_score"],
            country["social_score"],
            country["infrastructure_score"],
            country["employment_score"]
        ]
    }
)

# ============================================================
# DEVELOPMENT STRENGTHS & GAPS
# ============================================================

st.subheader("🔎 Development Strengths & Gaps")

dimension_scores = {
    "Economic Development": country["economic_score"],
    "Social Development": country["social_score"],
    "Infrastructure": country["infrastructure_score"],
    "Employment": country["employment_score"]
}

strongest_area = max(
    dimension_scores,
    key=dimension_scores.get
)

weakest_area = min(
    dimension_scores,
    key=dimension_scores.get
)

strongest_score = dimension_scores[strongest_area]
weakest_score = dimension_scores[weakest_area]


col1, col2 = st.columns(2)


with col1:

    st.success(
        f"🟢 Strongest Area\n\n"
        f"**{strongest_area}** — "
        f"{strongest_score:.1f}/100"
    )


with col2:

    st.error(
        f"🔴 Largest Development Gap\n\n"
        f"**{weakest_area}** — "
        f"{weakest_score:.1f}/100"
    )

# ============================================================
# SDG PRIORITY
# ============================================================

sdg_mapping = {

    "Economic Development": (
        "SDG 8",
        "Decent Work & Economic Growth"
    ),

    "Social Development": (
        "SDG 3 / SDG 4",
        "Good Health & Quality Education"
    ),

    "Infrastructure": (
        "SDG 7",
        "Affordable & Clean Energy"
    ),

    "Employment": (
        "SDG 8",
        "Decent Work & Economic Growth"
    )
}

sdg_code, sdg_name = sdg_mapping[weakest_area]


st.subheader("🎯 Priority SDG Area")

st.info(
    f"**{weakest_area}** is currently the weakest "
    f"development dimension for **{selected_country}**.\n\n"
    f"**Related SDG:** {sdg_code} — {sdg_name}"
)

st.bar_chart(
    dimensions.set_index("Dimension")
)


# ============================================================
# COUNTRY RANKING
# ============================================================

st.subheader("🏆 Global Development Ranking")


ranking = df[
    [
        "country",
        "development_group",
        "development_index",
        "development_rank"
    ]
].sort_values("development_rank")


st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# SDG CONNECTIONS
# ============================================================

st.divider()

st.subheader("🎯 SDG Lens")

st.markdown(
    """
    **SDG 3 — Good Health & Well-being**  
    Represented through life expectancy.

    **SDG 4 — Quality Education**  
    Represented through school enrollment.

    **SDG 7 — Affordable & Clean Energy**  
    Represented through electricity access.

    **SDG 8 — Decent Work & Economic Growth**  
    Represented through GDP per capita and unemployment.
    """
)