import streamlit as st
import pandas as pd
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Global Development Data Observatory",
    page_icon="🌍",
    layout="wide"
)


# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():

    data_path = Path(
        "data/processed/development_data_with_growth.csv"
    )

    return pd.read_csv(data_path)


df = load_data()


# ==================================================
# TITLE
# ==================================================

st.title(
    "🌍 Global Development Data Observatory"
)

st.markdown(
    """
    An interactive data analytics platform exploring
    economic, demographic, and social development
    across countries and development groups.
    """
)


# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header(
    "🔎 Filters"
)


selected_group = st.sidebar.multiselect(

    "Select Development Group",

    options=df[
        "development_group"
    ].unique(),

    default=df[
        "development_group"
    ].unique()
)


selected_indicator = st.sidebar.selectbox(

    "Select Indicator",

    options=df[
        "indicator"
    ].unique()
)


# ==================================================
# FILTER DATA
# ==================================================

filtered_df = df[
    df[
        "development_group"
    ].isin(
        selected_group
    )
]

filtered_df = filtered_df[
    filtered_df[
        "indicator"
    ] == selected_indicator
]


# ==================================================
# KEY METRICS
# ==================================================

col1, col2, col3, col4 = st.columns(4)


latest_year = filtered_df[
    "year"
].max()


latest_data = filtered_df[
    filtered_df[
        "year"
    ] == latest_year
]


with col1:

    st.metric(
        "Countries",
        latest_data[
            "country"
        ].nunique()
    )


with col2:

    st.metric(
        "Latest Year",
        latest_year
    )


with col3:

    st.metric(
        "Highest Value",
        f"{latest_data['value'].max():,.2f}"
    )


with col4:

    st.metric(
        "Average Value",
        f"{latest_data['value'].mean():,.2f}"
    )


# ==================================================
# MAIN DATA CHART
# ==================================================

st.subheader(
    f"📈 {selected_indicator.title()} Over Time"
)


chart_data = (

    filtered_df

    .pivot_table(

        index="year",

        columns="country",

        values="value"

    )

)


st.line_chart(
    chart_data
)


# ==================================================
# DATA TABLE
# ==================================================

st.subheader(
    "📊 Development Data"
)


st.dataframe(
    filtered_df,

    use_container_width=True
)