import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from utils.styles import load_css

# =====================================================
# PAGE CONFIG
# =====================================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("📡 Market Intelligence Briefing")

st.markdown(
    """
    Executive overview of current market risk conditions,
    volatility patterns and key securities requiring attention
    across the Nairobi Securities Exchange (NSE).
    """
)

# =====================================================
# FILE PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RISK_FILE = (
    BASE_DIR
    / "outputs"
    / "risk_scores.csv"
)

# =====================================================
# LOAD DATA
# =====================================================

try:

    risk_df = pd.read_csv(
        RISK_FILE
    )

except Exception as e:

    st.error(
        f"Unable to load risk data: {e}"
    )

    st.stop()

# =====================================================
# MARKET SNAPSHOT
# =====================================================

st.header("Market Snapshot")

low_risk = (
    risk_df[
        risk_df["Recommendation"]
        == "LOW VOLATILITY RISK"
    ]
    .shape[0]
)

moderate_risk = (
    risk_df[
        risk_df["Recommendation"]
        == "MODERATE VOLATILITY RISK"
    ]
    .shape[0]
)

high_risk = (
    risk_df[
        risk_df["Recommendation"]
        == "HIGH VOLATILITY RISK"
    ]
    .shape[0]
)

low_liquidity = (
    risk_df[
        risk_df["Recommendation"]
        == "LOW LIQUIDITY"
    ]
    .shape[0]
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Low Volatility Risk",
        low_risk
    )

with c2:
    st.metric(
        "Moderate Volatility Risk",
        moderate_risk
    )

with c3:
    st.metric(
        "High Volatility Risk",
        high_risk
    )

with c4:
    st.metric(
        "Low Liquidity",
        low_liquidity
    )

st.divider()

# =====================================================
# MARKET RISK DISTRIBUTION
# =====================================================

st.header("Market Risk Distribution")

distribution = (
    risk_df["Recommendation"]
    .value_counts()
    .reset_index()
)

distribution.columns = [
    "Risk Category",
    "Count"
]

fig = px.pie(
    distribution,
    names="Risk Category",
    values="Count",
    title="Distribution of Securities by Risk Classification"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================================
# LOWEST VOLATILITY SECURITIES
# =====================================================

st.header("Lowest Volatility Risk Securities")

low_risk_table = (
    risk_df[
        risk_df["Recommendation"]
        == "LOW VOLATILITY RISK"
    ]
    .sort_values(
        "Risk_Score",
        ascending=True
    )
)

display_cols = [
    "Volatility_Rank",
    "Code",
    "Name",
    "Risk_Score"
]

available_cols = [
    col
    for col in display_cols
    if col in low_risk_table.columns
]

st.dataframe(
    low_risk_table[
        available_cols
    ],
    use_container_width=True
)

st.divider()
# =====================================================
# HIGHEST VOLATILITY SECURITIES
# =====================================================

st.header("Highest Volatility Risk Securities")

high_risk_table = (
    risk_df[
        risk_df["Recommendation"]
        == "HIGH VOLATILITY RISK"
    ]
    .sort_values(
        "Risk_Score",
        ascending=False
    )
)

available_cols = [
    col
    for col in display_cols
    if col in high_risk_table.columns
]

st.dataframe(
    high_risk_table[
        available_cols
    ],
    use_container_width=True
)

st.divider()

# =====================================================
# EXECUTIVE COMMENTARY
# =====================================================

st.header("Executive Commentary")

st.info(
    f"""
The NSE universe currently contains
{low_risk} Low Volatility Risk securities,
{moderate_risk} Moderate Volatility Risk securities,
and {high_risk} High Volatility Risk securities.

Current volatility exposure appears concentrated
within a relatively small segment of the market,
suggesting selective rather than broad-based
market instability.

Portfolio managers should focus monitoring
efforts on securities classified as High
Volatility Risk while maintaining awareness
of liquidity limitations affecting
{low_liquidity} securities.

The market continues to present a blend of
defensive and growth-oriented opportunities,
with risk levels varying significantly across
individual securities.
"""
)

st.divider()

# =====================================================
# INVESTMENT CONSIDERATIONS
# =====================================================

st.header("Investment Considerations")

st.success(
    """
• Prioritize securities classified as
  Low Volatility Risk for defensive
  portfolio positioning.

• Maintain diversified exposure across
  sectors to mitigate concentration risk.

• Monitor High Volatility Risk securities
  closely for significant market movements.
"""
)

st.warning(
    """
• Elevated volatility may create both
  investment opportunities and downside
  risk.

• Liquidity constraints should be
  considered before portfolio allocation
  decisions are made.
"""
)

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Market Intelligence Briefing • Executive Market Risk Intelligence Platform"
)