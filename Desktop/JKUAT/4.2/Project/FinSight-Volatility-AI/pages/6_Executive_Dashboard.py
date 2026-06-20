from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import load_css

st.set_page_config(
    page_title="Executive Dashboard",
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

avg_risk = round(
    df["Risk_Score"].mean(),
    1
)

highest_stock = df.iloc[0]

# =====================================================
# PAGE HEADER
# =====================================================

st.title("🏢 Executive Intelligence Center")

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.subheader("Executive Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:

    if avg_risk < 30:
        st.success("🟢 Stable Market")

    elif avg_risk < 60:
        st.warning("🟡 Moderate Risk")

    else:
        st.error("🔴 High Risk Market")

with c2:
    st.metric(
        "Market Risk Score",
        f"{avg_risk}/100"
    )

with c3:
    st.metric(
        "Highest Risk Stock",
        highest_stock["Code"]
    )

with c4:
    st.metric(
        "Stocks Covered",
        len(df)
    )

# =====================================================
# EXECUTIVE RECOMMENDATIONS
# =====================================================

st.subheader("📌 Executive Recommendations")

top5 = df.head(5)

for _, row in top5.iterrows():

    recommendation = row["Recommendation"]

    message = (
        f"{row['Code']} → "
        f"{recommendation} "
        f"(Risk Score {row['Risk_Score']:.0f})"
    )

    if recommendation == "REDUCE EXPOSURE":
        st.error(message)

    elif recommendation == "HOLD":
        st.warning(message)

    elif recommendation == "MONITOR":
        st.info(message)

    else:
        st.success(message)

# =====================================================
# TOP RISK STOCKS
# =====================================================

st.subheader("Top 10 Risk Stocks")

fig_risk = px.bar(
    df.head(10),
    x="Code",
    y="Risk_Score",
    color="Risk_Score",
    title="Highest Risk NSE Stocks",
    text_auto=".0f"
)

fig_risk.update_layout(
    height=500
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)

# =====================================================
# PORTFOLIO INTELLIGENCE
# =====================================================

st.subheader("💼 Portfolio Intelligence")

allocation = (
    df["Recommendation"]
    .value_counts()
    .reset_index()
)

allocation.columns = [
    "Recommendation",
    "Count"
]

fig_portfolio = px.pie(
    allocation,
    names="Recommendation",
    values="Count",
    hole=0.5,
    title="Portfolio Allocation by AI Recommendation"
)

st.plotly_chart(
    fig_portfolio,
    use_container_width=True
)

# =====================================================
# TOP BUY OPPORTUNITIES
# =====================================================

st.subheader("🚀 Top Buy Opportunities")

buy_stocks = (
    df.sort_values(
        "Risk_Score",
        ascending=True
    )
    .head(10)
)

st.dataframe(
    buy_stocks[
        [
            "Code",
            "Name",
            "Predicted_Volatility",
            "Risk_Score",
            "Recommendation"
        ]
    ],
    use_container_width=True
)

# =====================================================
# RISK REGISTER
# =====================================================

st.subheader("Risk Register")

st.dataframe(
    df[
        [
            "Code",
            "Name",
            "Predicted_Volatility",
            "Risk_Score",
            "Recommendation"
        ]
    ],
    use_container_width=True,
    height=500
)

# =====================================================
# EXECUTIVE BOARD COMMENTARY
# =====================================================

st.subheader("🎯 Executive Board Commentary")

buy_count = len(
    df[df["Recommendation"] == "BUY"]
)

monitor_count = len(
    df[df["Recommendation"] == "MONITOR"]
)

hold_count = len(
    df[df["Recommendation"] == "HOLD"]
)

reduce_count = len(
    df[df["Recommendation"] == "REDUCE EXPOSURE"]
)

highest_risk = (
    df.sort_values(
        "Risk_Score",
        ascending=False
    )
    .head(3)
)

high_risk_names = ", ".join(
    highest_risk["Code"].tolist()
)

if avg_risk < 30:
    market_condition = "LOW"

elif avg_risk < 60:
    market_condition = "MODERATE"

else:
    market_condition = "HIGH"

commentary = f"""
### Executive Market Assessment

The NSE market currently exhibits **{market_condition} RISK CONDITIONS**
with an aggregate market risk score of **{avg_risk}/100**.

### Portfolio Breakdown

🟢 BUY Opportunities: **{buy_count}**

🟡 MONITOR Positions: **{monitor_count}**

🔵 HOLD Positions: **{hold_count}**

🔴 REDUCE EXPOSURE Positions: **{reduce_count}**

### Executive Attention Required

The highest-risk securities currently identified by the AI engine are:

**{high_risk_names}**

These positions should receive immediate management review due to elevated forecast volatility.

### Strategic Outlook

The market remains broadly stable with the majority of securities remaining within acceptable volatility thresholds. Portfolio managers should prioritize capital allocation toward BUY opportunities while actively monitoring high-risk positions.
"""

st.info(commentary)

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Executive Financial Intelligence Dashboard • Powered by Machine Learning"
)