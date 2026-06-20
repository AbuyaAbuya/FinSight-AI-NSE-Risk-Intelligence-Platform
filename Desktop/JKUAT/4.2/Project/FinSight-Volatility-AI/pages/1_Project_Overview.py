import streamlit as st
from utils.styles import load_css

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

st.title("📈 FinSight AI")

st.header(
    "Executive Market Risk Intelligence Platform"
)

st.markdown(
    """
    Machine Learning-based stock volatility forecasting,
    portfolio risk management and executive decision support
    for companies listed on the Nairobi Securities Exchange (NSE).
    """
)

st.divider()

# =====================================================
# RESEARCH PROJECT
# =====================================================

st.subheader("Research Project")

st.write(
    """
    Machine Learning-Based Stock Volatility Forecasting
    and Executive Risk Intelligence Platform for Companies
    Listed on the Nairobi Securities Exchange (NSE).
    """
)

# =====================================================
# AUTHOR
# =====================================================

st.subheader("Author")

st.write("Joseph Abuya Abich")

# =====================================================
# PROJECT STATISTICS
# =====================================================

st.subheader("Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Stocks Analyzed",
        "68"
    )

with c2:
    st.metric(
        "Records Processed",
        "32,000+"
    )

with c3:
    st.metric(
        "Model Accuracy (R²)",
        "98.64%"
    )

with c4:
    st.metric(
        "Risk Engine",
        "Random Forest"
    )

st.divider()

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

st.subheader("Executive Overview")

st.write(
    """
    FinSight AI is a Machine Learning-powered
    financial intelligence platform designed
    to forecast stock volatility and support
    investment decision-making.
    """
)

st.write(
    """
    The platform combines Random Forest forecasting,
    risk scoring, executive dashboards, portfolio
    intelligence, board reporting, and AI-driven
    investment recommendations.
    """
)

# =====================================================
# PLATFORM CAPABILITIES
# =====================================================

st.subheader("Platform Capabilities")

st.success("Market Explorer")

st.success("Volatility Forecasting")

st.success("Executive Dashboard")

st.success("AI Advisory Center")

st.success("Board Pack")

st.success("Portfolio Simulator")

st.divider()

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.subheader("Technology Stack")

st.info(
    """
    Python

    Streamlit

    Plotly

    Pandas

    Scikit-Learn

    Random Forest Machine Learning

    Financial Risk Analytics
    """
)

# =====================================================
# CONCLUSION
# =====================================================

st.success(
    """
    FinSight AI demonstrates how Machine Learning
    can be used to transform stock market data
    into actionable executive intelligence for
    investors, analysts, CFOs and boards.
    """
)