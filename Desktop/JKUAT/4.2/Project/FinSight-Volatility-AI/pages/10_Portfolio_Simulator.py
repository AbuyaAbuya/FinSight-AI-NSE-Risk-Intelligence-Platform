from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import load_css

st.set_page_config(
    page_title="Portfolio Risk Simulator",
    layout="wide"
)

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

# =====================================================
# FILE PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

# =====================================================
# PAGE HEADER
# =====================================================

st.title("💼 Portfolio Risk Simulator")

st.markdown(
    """
    Construct an investment portfolio and evaluate
    its overall risk profile using FinSight AI's
    Machine Learning volatility forecasts.

    The simulator combines predicted volatility,
    risk scores and portfolio allocation weights
    to estimate portfolio-level investment risk.
    """
)

# =====================================================
# LOAD RISK SCORES
# =====================================================

try:

    df = pd.read_csv(
        OUTPUT_DIR / "risk_scores.csv"
    )

except Exception as e:

    st.error(f"Unable to load risk_scores.csv: {e}")
    st.stop()

df = df.sort_values(
    "Risk_Score",
    ascending=False
)

stocks = sorted(df["Code"].unique())

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Stocks Available",
        len(df)
    )

with c2:
    st.metric(
        "Average Market Risk",
        round(df["Risk_Score"].mean(), 1)
    )

with c3:
    st.metric(
        "Highest Risk Stock",
        df.iloc[0]["Code"]
    )

st.divider()

# =====================================================
# PORTFOLIO BUILDER
# =====================================================

st.subheader("Portfolio Construction")

col1, col2 = st.columns(2)

with col1:
    stock1 = st.selectbox(
        "Stock 1",
        stocks,
        index=0
    )

    weight1 = st.slider(
        "Weight 1 (%)",
        0,
        100,
        25
    )

with col2:
    stock2 = st.selectbox(
        "Stock 2",
        stocks,
        index=1
    )

    weight2 = st.slider(
        "Weight 2 (%)",
        0,
        100,
        25
    )

col3, col4 = st.columns(2)

with col3:
    stock3 = st.selectbox(
        "Stock 3",
        stocks,
        index=2
    )

    weight3 = st.slider(
        "Weight 3 (%)",
        0,
        100,
        25
    )

with col4:
    stock4 = st.selectbox(
        "Stock 4",
        stocks,
        index=3
    )

    weight4 = st.slider(
        "Weight 4 (%)",
        0,
        100,
        25
    )

# =====================================================
# VALIDATION
# =====================================================

total_weight = (
    weight1 +
    weight2 +
    weight3 +
    weight4
)

if total_weight != 100:

    st.error(
        f"Portfolio weights must total 100%. Current total = {total_weight}%"
    )

    st.stop()

# =====================================================
# GET RISK SCORES
# =====================================================

risk1 = df.loc[
    df["Code"] == stock1,
    "Risk_Score"
].iloc[0]

risk2 = df.loc[
    df["Code"] == stock2,
    "Risk_Score"
].iloc[0]

risk3 = df.loc[
    df["Code"] == stock3,
    "Risk_Score"
].iloc[0]

risk4 = df.loc[
    df["Code"] == stock4,
    "Risk_Score"
].iloc[0]

portfolio_risk = (
    risk1 * weight1 +
    risk2 * weight2 +
    risk3 * weight3 +
    risk4 * weight4
) / 100

portfolio_risk = round(
    portfolio_risk,
    2
)

# =====================================================
# RISK CLASSIFICATION
# =====================================================

if portfolio_risk >= 70:
    risk_level = "HIGH"

elif portfolio_risk >= 40:
    risk_level = "MODERATE"

else:
    risk_level = "LOW"

# =====================================================
# EXECUTIVE KPI SECTION
# =====================================================

st.subheader("Portfolio Risk Assessment")

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "Portfolio Risk Score",
        portfolio_risk
    )

with k2:
    st.metric(
        "Risk Level",
        risk_level
    )

with k3:
    st.metric(
        "Total Weight",
        f"{total_weight}%"
    )

# =====================================================
# EXECUTIVE INVESTMENT RECOMMENDATION
# =====================================================

st.subheader("🤖 Executive Investment Recommendation")

if portfolio_risk < 30:

    st.success(
        """
        LOW RISK PORTFOLIO

        The proposed allocation is considered
        conservative and suitable for risk-averse
        investors seeking capital preservation.
        """
    )

elif portfolio_risk < 60:

    st.warning(
        """
        MODERATE RISK PORTFOLIO

        The allocation provides a balanced mix
        of growth and risk exposure and is suitable
        for medium-term investors.
        """
    )

else:

    st.error(
        """
        HIGH RISK PORTFOLIO

        The allocation contains significant
        exposure to volatile securities.

        Consider reducing allocations to
        high-risk stocks.
        """
    )

# =====================================================
# PORTFOLIO TABLE
# =====================================================

portfolio_df = pd.DataFrame({

    "Stock": [
        stock1,
        stock2,
        stock3,
        stock4
    ],

    "Weight (%)": [
        weight1,
        weight2,
        weight3,
        weight4
    ],

    "Risk Score": [
        risk1,
        risk2,
        risk3,
        risk4
    ]
})

st.subheader("Portfolio Composition")

st.dataframe(
    portfolio_df,
    use_container_width=True
)

# =====================================================
# PORTFOLIO ALLOCATION
# =====================================================

fig = px.pie(
    portfolio_df,
    names="Stock",
    values="Weight (%)",
    title="Portfolio Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# RISK CONTRIBUTION
# =====================================================

portfolio_df["Risk Contribution"] = (
    portfolio_df["Weight (%)"]
    *
    portfolio_df["Risk Score"]
) / 100

fig2 = px.bar(
    portfolio_df,
    x="Stock",
    y="Risk Contribution",
    color="Risk Contribution",
    title="Risk Contribution by Stock"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================================
# EXECUTIVE COMMENTARY
# =====================================================

st.subheader("📋 Executive Commentary")

highest = portfolio_df.sort_values(
    "Risk Score",
    ascending=False
).iloc[0]

st.info(
    f"""
    Portfolio Risk Score: {portfolio_risk}

    Risk Classification: {risk_level}

    Highest Risk Holding: {highest['Stock']}

    FinSight AI recommends continuous monitoring
    of concentrated positions and periodic
    portfolio rebalancing to maintain an
    acceptable risk profile.
    """
)

# =====================================================
# FINAL EXECUTIVE RECOMMENDATION
# =====================================================

st.divider()

st.subheader("📌 Executive Recommendation")

st.info(
    f"""
    Based on the current allocation,
    the largest portfolio risk contributor is
    {highest['Stock']}.

    Portfolio Risk Score: {portfolio_risk}

    Recommended Action:
    Maintain diversification and continuously
    monitor high-risk positions.

    FinSight AI assessment indicates a
    {risk_level.lower()} portfolio risk profile.
    """
)