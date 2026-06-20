import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import load_css

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Board Pack",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

risk_df = pd.read_csv(
    "outputs/risk_scores.csv"
)

metrics_df = pd.read_csv(
    "outputs/model_metrics.csv"
)

risk_df = risk_df.sort_values(
    "Risk_Score",
    ascending=False
)

# =====================================================
# EXECUTIVE HEADER
# =====================================================

st.title("📋 Executive Board Pack")

st.markdown(
    """
    **FinSight AI – Executive Risk Intelligence Platform**

    AI-Powered Stock Volatility Forecasting and Investment Risk Monitoring
    """
)

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.subheader("Executive Summary")

avg_risk = risk_df["Risk_Score"].mean()

highest_stock = risk_df.iloc[0]

buy_count = len(
    risk_df[
        risk_df["Recommendation"] == "BUY"
    ]
)

monitor_count = len(
    risk_df[
        risk_df["Recommendation"] == "MONITOR"
    ]
)

hold_count = len(
    risk_df[
        risk_df["Recommendation"] == "HOLD"
    ]
)

reduce_count = len(
    risk_df[
        risk_df["Recommendation"] ==
        "REDUCE EXPOSURE"
    ]
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    if avg_risk < 30:
        st.success("🟢 Stable")

    elif avg_risk < 60:
        st.warning("🟡 Moderate")

    else:
        st.error("🔴 High Risk")

with c2:
    st.metric(
        "Market Risk Score",
        f"{avg_risk:.1f}/100"
    )

with c3:
    st.metric(
        "Highest Risk Stock",
        highest_stock["Code"]
    )

with c4:
    st.metric(
        "Stocks Covered",
        len(risk_df)
    )

# =====================================================
# BOARD COMMENTARY
# =====================================================

st.subheader("Board Commentary")

if avg_risk < 30:
    market_state = "LOW"
elif avg_risk < 60:
    market_state = "MODERATE"
else:
    market_state = "HIGH"

st.info(
    f"""
    The NSE market currently exhibits
    **{market_state} risk conditions**
    with an aggregate market risk score of
    **{avg_risk:.1f}/100**.

    The AI forecasting engine identified:

    • {buy_count} BUY opportunities

    • {monitor_count} MONITOR positions

    • {hold_count} HOLD positions

    • {reduce_count} REDUCE EXPOSURE positions

    Executive attention should be focused on
    high-risk securities while maintaining
    exposure to low-volatility opportunities.
    """
)

# =====================================================
# PORTFOLIO OVERVIEW
# =====================================================

st.subheader("Portfolio Intelligence")

allocation = (
    risk_df["Recommendation"]
    .value_counts()
    .reset_index()
)

allocation.columns = [
    "Recommendation",
    "Count"
]

fig_pie = px.pie(
    allocation,
    names="Recommendation",
    values="Count",
    hole=0.5,
    title="Portfolio Allocation"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# TOP RISKS
# =====================================================

st.subheader("Top Risk Securities")

top_risk = risk_df.head(10)

fig_risk = px.bar(
    top_risk,
    x="Code",
    y="Risk_Score",
    color="Risk_Score",
    title="Highest Risk Stocks",
    text_auto=".0f"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)

st.dataframe(
    top_risk,
    use_container_width=True
)

# =====================================================
# TOP OPPORTUNITIES
# =====================================================

st.subheader("Top Investment Opportunities")

opportunities = (
    risk_df.sort_values(
        "Risk_Score"
    )
    .head(10)
)

st.dataframe(
    opportunities,
    use_container_width=True
)

# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.subheader("AI Model Performance")

rmse = metrics_df.loc[
    metrics_df["Metric"] == "RMSE",
    "Value"
].values[0]

mae = metrics_df.loc[
    metrics_df["Metric"] == "MAE",
    "Value"
].values[0]

r2 = metrics_df.loc[
    metrics_df["Metric"] == "R2",
    "Value"
].values[0]

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "RMSE",
        f"{rmse:.4f}"
    )

with m2:
    st.metric(
        "MAE",
        f"{mae:.4f}"
    )

with m3:
    st.metric(
        "R²",
        f"{r2:.4f}"
    )

# =====================================================
# STRATEGIC RECOMMENDATIONS
# =====================================================

st.subheader("Strategic Recommendations")

st.success(
    """
    1. Prioritize low-risk securities identified
       by the AI recommendation engine.

    2. Monitor moderate-risk positions for
       changing volatility patterns.

    3. Review high-risk securities identified
       for potential portfolio rebalancing.

    4. Continue leveraging machine learning
       forecasts for proactive risk management.

    5. Maintain diversification across
       sectors and risk categories.
    """
)

# =====================================================
# RESEARCH CONCLUSION
# =====================================================

st.subheader("Research Conclusion")

st.info(
    f"""
    The Random Forest model achieved an
    R² score of {r2:.4f}, demonstrating strong
    predictive performance in forecasting
    stock price volatility.

    The integration of machine learning with
    executive risk monitoring provides an
    effective framework for supporting
    investment and portfolio management decisions.
    """
)

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Executive Board Pack • Powered by Random Forest Volatility Forecasting"
)