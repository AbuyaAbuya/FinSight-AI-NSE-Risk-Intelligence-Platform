import streamlit as st
from utils.styles import load_css

# =====================================================
# STYLING
# =====================================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("📘 Project Overview")

st.markdown("""
Technical documentation and business overview for the
**FinSight AI Volatility Risk Intelligence Platform**.
""")

st.divider()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.header("Executive Summary")

st.write("""
FinSight AI is an end-to-end financial analytics platform designed
to forecast stock market volatility and transform raw market data
into actionable investment intelligence.

The solution integrates Machine Learning, Risk Analytics,
Business Intelligence and Executive Reporting into a unified
decision-support environment for investors, analysts,
portfolio managers and executives.
""")

st.divider()

# =====================================================
# PROJECT OBJECTIVES
# =====================================================

st.header("Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("Forecast future stock volatility")
    st.success("Classify securities by risk level")
    st.success("Support portfolio construction")

with col2:
    st.success("Improve investment decision-making")
    st.success("Provide executive market intelligence")
    st.success("Enhance risk monitoring")

st.divider()

# =====================================================
# DATASET OVERVIEW
# =====================================================

st.header("Dataset Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Stocks", "68")

with c2:
    st.metric("Records", "32,000+")

with c3:
    st.metric("Exchange", "NSE")

with c4:
    st.metric("Coverage", "2023-2024")

st.write("""
The dataset contains historical market information for companies
listed on the Nairobi Securities Exchange (NSE), including stock
prices, trading volumes, returns and engineered volatility indicators.
""")

st.divider()

# =====================================================
# METHODOLOGY
# =====================================================

st.header("Methodology")

st.write("""
FinSight AI follows a structured analytics workflow that transforms
historical market data into predictive volatility intelligence and
actionable investment insights.
""")

st.subheader("1️⃣ Data Preparation")

st.info("""
📥 Market Data Collection

🧹 Data Cleaning & Validation

⚙️ Feature Engineering
""")

st.write("""
Historical stock market data is collected from the Nairobi Securities
Exchange (NSE). Data quality checks, validation procedures and feature
engineering techniques are applied to prepare the dataset for machine
learning.
""")

st.subheader("2️⃣ Machine Learning Engine")

st.info("""
🤖 Random Forest Model Training

📈 Volatility Forecasting
""")

st.write("""
A Random Forest Regression model is trained using engineered market
features to learn historical volatility patterns and generate future
volatility forecasts.
""")

st.subheader("3️⃣ Decision Intelligence")

st.info("""
🚦 Risk Classification

📊 Executive Intelligence

💼 Portfolio Analytics
""")

st.write("""
Forecasted volatility scores are translated into risk categories and
used to generate portfolio insights, executive dashboards and
decision-support intelligence.
""")

st.divider()

# =====================================================
# MACHINE LEARNING FORECASTING ENGINE
# =====================================================

st.header("Machine Learning Forecasting Engine")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Model", "Random Forest")

with c2:
    st.metric("R² Score", "96.53%")

with c3:
    st.metric("RMSE", "0.3607")

with c4:
    st.metric("Risk Classes", "3")

st.write("""
The Random Forest Regression model was selected due to its ability
to capture complex non-linear relationships within financial data
while maintaining strong predictive performance across varying
market conditions.
""")

st.success("""
Model Objective: Forecast Future Stock Volatility

Prediction Output: Volatility Score

Business Outcome: Risk Classification and Investment Intelligence
""")

st.divider()
# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.header("Model Performance")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "RMSE",
        "0.3607"
    )

with c2:
    st.metric(
        "MAE",
        "0.1098"
    )

with c3:
    st.metric(
        "R² Score",
        "0.9653"
    )

st.success("""
The forecasting engine achieved strong predictive performance,
explaining approximately 96.5% of observed volatility variation
within the evaluation dataset.
""")

st.divider()

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.header("Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### Programming

• Python

• Pandas

• NumPy
""")

with col2:
    st.info("""
### Machine Learning

• Scikit-Learn

• Random Forest

• Feature Engineering
""")

with col3:
    st.info("""
### Visualization

• Streamlit

• Plotly

• GitHub
""")

st.divider()

# =====================================================
# BUSINESS VALUE
# =====================================================

st.header("Business Value")

col1, col2 = st.columns(2)

with col1:
    st.success("""
✓ Improves investment decision-making

✓ Enhances portfolio risk monitoring

✓ Supports portfolio construction
""")

with col2:
    st.success("""
✓ Provides executive intelligence

✓ Enables proactive risk management

✓ Supports strategic planning
""")

st.divider()

# =====================================================
# PLATFORM MODULES
# =====================================================

st.header("Platform Modules")

col1, col2 = st.columns(2)

with col1:
    st.write("📈 Market Explorer")
    st.write("🔮 Volatility Forecasting")
    st.write("📰 Market Intelligence Briefing")

with col2:
    st.write("📊 Executive Dashboard")
    st.write("🤖 AI Advisory Center")
    st.write("💼 Portfolio Risk Simulator")

st.divider()

# =====================================================
# PROJECT OUTCOME
# =====================================================

st.header("Project Outcome")

st.success("""
FinSight AI demonstrates how Machine Learning,
Financial Analytics and Business Intelligence
can be integrated into a single platform capable
of transforming market data into actionable
investment intelligence.

The solution delivers forecasting, risk
classification, portfolio analytics,
executive reporting and AI-powered
decision support for modern investment
management.
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Volatility Risk Intelligence Platform • Built with Streamlit, Python and Machine Learning"
)