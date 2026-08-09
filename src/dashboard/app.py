import streamlit as st


st.set_page_config(
    page_title="Global Development & SDG Observatory",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Main title
st.title("🌍 Global Development & SDG Observatory")

st.markdown(
    """
    **An interactive data analytics platform exploring economic, demographic,
    employment, and development disparities across countries and development groups.**
    """
)

st.divider()


# Navigation
pg = st.navigation(
    [
        st.Page(
            "pages/overview.py",
            title="Global Overview",
            icon="📊"
        ),

        st.Page(
            "pages/country_profile.py",
            title="Country Profile",
            icon="👤"
        ),

        st.Page(
            "pages/development_gap.py",
            title="Development Gap",
            icon="⚖️"
        ),

        st.Page(
            "pages/trends.py",
            title="Trends & Comparisons",
            icon="📈"
        ),

        st.Page(
            "pages/sdg_lens.py",
            title="SDG Development Lens",
            icon="🇺🇳"
        ),

        st.Page(
            "pages/insights.py",
            title="Automated Insights",
            icon="🧠"
),
    ]
)

pg.run()