from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.styles import load_css

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Portfolio Risk Simulator",
    page_icon="💼",
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
# LOAD DATA
# =====================================================

try:

    risk_df = pd.read_csv(
        OUTPUT_DIR / "risk_scores.csv"
    )

except Exception as e:

    st.error(
        f"Unable to load risk_scores.csv: {e}"
    )

    st.stop()

investable = risk_df[
    risk_df["Recommendation"] != "LOW LIQUIDITY"
].copy()

# =====================================================
# PAGE HEADER
# =====================================================

st.title("💼 Portfolio Risk Simulator")

st.markdown(
    """
Build a custom investment portfolio and
evaluate its expected volatility risk using
FinSight AI forecasts.

This simulator helps investors understand:

• Portfolio risk exposure

• Portfolio concentration

• Risk contribution by holding

• Portfolio construction quality
"""
)

# =====================================================
# MARKET SNAPSHOT
# =====================================================

avg_market_risk = round(
    investable["Risk_Score"].mean(),
    1
)

highest_risk_security = (
    investable
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .iloc[0]
)

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Securities Available",
        len(investable)
    )

with c2:

    st.metric(
        "Average Market Risk",
        f"{avg_market_risk}/100"
    )

with c3:

    st.metric(
        "Highest Risk Security",
        highest_risk_security["Name"]
    )

st.divider()

# =====================================================
# PORTFOLIO CONSTRUCTION
# =====================================================

st.header("Portfolio Construction")

stocks = sorted(
    investable["Code"].unique()
)

col1, col2 = st.columns(2)

with col1:

    holding1 = st.selectbox(
        "Portfolio Holding 1",
        stocks,
        index=0
    )

    weight1 = st.slider(
        "Allocation 1 (%)",
        0,
        100,
        25
    )

with col2:

    holding2 = st.selectbox(
        "Portfolio Holding 2",
        stocks,
        index=1
    )

    weight2 = st.slider(
        "Allocation 2 (%)",
        0,
        100,
        25
    )

col3, col4 = st.columns(2)

with col3:

    holding3 = st.selectbox(
        "Portfolio Holding 3",
        stocks,
        index=2
    )

    weight3 = st.slider(
        "Allocation 3 (%)",
        0,
        100,
        25
    )

with col4:

    holding4 = st.selectbox(
        "Portfolio Holding 4",
        stocks,
        index=3
    )

    weight4 = st.slider(
        "Allocation 4 (%)",
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
        f"""
Portfolio allocations must total 100%.

Current allocation: {total_weight}%
"""
    )

    st.stop()

# =====================================================
# PORTFOLIO DATA
# =====================================================

portfolio_codes = [
    holding1,
    holding2,
    holding3,
    holding4
]

portfolio_weights = [
    weight1,
    weight2,
    weight3,
    weight4
]

portfolio_df = investable[
    investable["Code"].isin(
        portfolio_codes
    )
].copy()

portfolio_df = (
    portfolio_df
    .set_index("Code")
    .loc[portfolio_codes]
    .reset_index()
)

portfolio_df["Weight (%)"] = (
    portfolio_weights
)

# =====================================================
# PORTFOLIO RISK SCORE
# =====================================================

portfolio_risk = round(
    (
        portfolio_df["Risk_Score"]
        *
        portfolio_df["Weight (%)"]
    ).sum() / 100,
    2
)

# =====================================================
# PORTFOLIO STRUCTURE
# =====================================================

unique_holdings = len(
    set(portfolio_codes)
)

max_weight = portfolio_df[
    "Weight (%)"
].max()

if unique_holdings == 1:

    diversification = (
        "Single Security Exposure"
    )

elif unique_holdings == 2:

    diversification = (
        "Highly Concentrated"
    )

elif unique_holdings == 3:

    diversification = (
        "Moderately Concentrated"
    )

else:

    if max_weight <= 30:

        diversification = (
            "Well Diversified"
        )

    elif max_weight <= 50:

        diversification = (
            "Moderately Concentrated"
        )

    else:

        diversification = (
            "Highly Concentrated"
        )

# =====================================================
# PORTFOLIO RISK CATEGORY
# =====================================================

if portfolio_risk <= 33:

    risk_category = "Low Risk"

elif portfolio_risk <= 65:

    risk_category = "Moderate Risk"

else:

    risk_category = "High Risk"
# =====================================================
# PORTFOLIO RISK ASSESSMENT
# =====================================================

st.header("Portfolio Risk Assessment")

if portfolio_risk <= 33:

    st.success(
        f"""
### 🟢 LOW RISK PORTFOLIO

Portfolio Risk Score: {portfolio_risk}/100
"""
    )

elif portfolio_risk <= 65:

    st.warning(
        f"""
### 🟡 MODERATE RISK PORTFOLIO

Portfolio Risk Score: {portfolio_risk}/100
"""
    )

else:

    st.error(
        f"""
### 🔴 HIGH RISK PORTFOLIO

Portfolio Risk Score: {portfolio_risk}/100
"""
    )

# =====================================================
# PORTFOLIO INTELLIGENCE
# =====================================================

st.header("Portfolio Intelligence")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Portfolio Risk",
        risk_category
    )

with k2:

    st.metric(
        "Portfolio Structure",
        diversification
    )

with k3:

    st.metric(
        "Risk Score",
        f"{portfolio_risk}/100"
    )

st.divider()

# =====================================================
# PORTFOLIO HOLDINGS SUMMARY
# =====================================================

st.header("Portfolio Holdings Summary")

display_df = portfolio_df[
    [
        "Code",
        "Name",
        "Weight (%)",
        "Risk_Score",
        "Recommendation"
    ]
]

display_df.columns = [
    "Security",
    "Company",
    "Weight (%)",
    "Risk Score",
    "Risk Classification"
]

st.dataframe(
    display_df,
    use_container_width=True
)

st.divider()

# =====================================================
# PORTFOLIO ALLOCATION
# =====================================================

st.header("Portfolio Allocation")

fig_alloc = px.pie(
    portfolio_df,
    names="Code",
    values="Weight (%)",
    hole=0.55,
    title="Portfolio Allocation Breakdown"
)

fig_alloc.update_layout(
    height=500
)

st.plotly_chart(
    fig_alloc,
    use_container_width=True
)

# =====================================================
# RISK CONTRIBUTION ANALYSIS
# =====================================================

st.header("Risk Contribution Analysis")

portfolio_df[
    "Risk Contribution"
] = (
    portfolio_df["Risk_Score"]
    *
    portfolio_df["Weight (%)"]
) / 100

fig_risk = px.bar(
    portfolio_df,
    x="Code",
    y="Risk Contribution",
    color="Risk Contribution",
    text_auto=".1f",
    title="Contribution of Each Security to Portfolio Risk"
)

fig_risk.update_layout(
    height=500,
    xaxis_title="Security",
    yaxis_title="Risk Contribution"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)

st.divider()

# =====================================================
# EXECUTIVE COMMENTARY
# =====================================================

st.header("Executive Commentary")

highest_holding = (
    portfolio_df
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .iloc[0]
)

largest_weight = portfolio_df[
    "Weight (%)"
].max()

largest_position = (
    portfolio_df.loc[
        portfolio_df["Weight (%)"].idxmax(),
        "Name"
    ]
)

st.info(
    f"""
The simulated portfolio is classified as
**{risk_category}** with an overall risk
score of **{portfolio_risk}/100**.

Portfolio construction is assessed as
**{diversification}**.

The highest-risk security in the portfolio is
**{highest_holding['Name']}**.

The largest portfolio allocation is
**{largest_weight}%** invested in
**{largest_position}**.

Investors should monitor both portfolio risk
and concentration levels to ensure alignment
with investment objectives and risk tolerance.
"""
)

st.divider()

# =====================================================
# STRATEGIC GUIDANCE
# =====================================================

st.header("Strategic Guidance")

if diversification == "Single Security Exposure":

    st.error(
        """
This portfolio is entirely dependent on a
single security.

Performance and risk are fully concentrated
in one investment, increasing vulnerability
to company-specific events.
"""
    )

elif diversification == "Highly Concentrated":

    st.warning(
        """
The portfolio exhibits significant
concentration risk.

Consider increasing the number of distinct
holdings to improve diversification and
reduce dependence on a small number of
securities.
"""
    )

elif diversification == "Moderately Concentrated":

    st.info(
        """
The portfolio has a moderate level of
concentration.

Additional diversification may improve
risk-adjusted performance depending on
investment objectives.
"""
    )

else:

    st.success(
        """
The portfolio appears reasonably diversified.

Capital is distributed across multiple
holdings, helping reduce concentration risk.
"""
    )

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Portfolio Risk Simulator • Executive Investment Intelligence"
)