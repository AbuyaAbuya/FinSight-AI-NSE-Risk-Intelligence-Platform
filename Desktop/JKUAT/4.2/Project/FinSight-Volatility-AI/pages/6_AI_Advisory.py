from pathlib import Path
import streamlit as st
import pandas as pd

from utils.styles import load_css
from utils.data_loader import load_data

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Advisory Center",
    page_icon="🤖",
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

    raw_df = load_data()

except Exception as e:

    st.error(
        f"Unable to load data: {e}"
    )

    st.stop()

# =====================================================
# DATASET COVERAGE
# =====================================================

raw_df["Date"] = pd.to_datetime(
    raw_df["Date"],
    errors="coerce"
)

min_date = raw_df["Date"].min()
max_date = raw_df["Date"].max()

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🤖 AI Advisory Center")

st.markdown(
    """
AI-generated investment intelligence and
volatility risk assessment for securities
listed on the Nairobi Securities Exchange.
"""
)

st.info(
    f"""
Dataset Coverage:
{min_date.strftime('%d-%b-%Y')}
to
{max_date.strftime('%d-%b-%Y')}
"""
)

# =====================================================
# SECURITY SELECTION
# =====================================================

selected_stock = st.selectbox(
    "Select Security",
    sorted(risk_df["Code"].unique())
)

row = risk_df[
    risk_df["Code"] == selected_stock
].iloc[0]

# =====================================================
# MARKET RANK
# =====================================================

rank_df = (
    risk_df
    .sort_values(
        "Risk_Score",
        ascending=True
    )
    .reset_index(drop=True)
)

market_rank = (
    rank_df.index[
        rank_df["Code"] == selected_stock
    ][0]
    + 1
)

# =====================================================
# KPI SECTION
# =====================================================

st.subheader(row["Name"])

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Risk Score",
        f"{row['Risk_Score']:.2f}"
    )

with c2:

    st.metric(
        "Expected Volatility",
        f"{row['Predicted_Volatility']:.2f}"
    )

with c3:

    st.metric(
        "Risk Classification",
        row["Recommendation"]
    )

with c4:

    st.metric(
        "Market Rank",
        f"{market_rank}/{len(risk_df)}"
    )
# =====================================================
# AI ADVISORY ASSESSMENT
# =====================================================

st.header("AI Advisory Assessment")

classification = row["Recommendation"]

if classification == "LOW VOLATILITY RISK":

    st.success(
        f"""
### Low Risk Assessment

{row['Name']} exhibits relatively stable
volatility characteristics and ranks among
the lower-risk securities within the NSE
universe.

The security may be suitable for investors
seeking lower market risk exposure.
"""
    )

elif classification == "MODERATE VOLATILITY RISK":

    st.warning(
        f"""
### Moderate Risk Assessment

{row['Name']} exhibits moderate volatility
characteristics.

The security remains investable but may
require periodic monitoring as market
conditions evolve.
"""
    )

elif classification == "HIGH VOLATILITY RISK":

    st.error(
        f"""
### High Risk Assessment

{row['Name']} ranks among the higher-risk
securities in the NSE universe.

Elevated volatility suggests the need for
enhanced monitoring and careful portfolio
allocation decisions.
"""
    )

else:

    st.info(
        f"""
### Limited Trading Activity

Trading activity for {row['Name']} appears
insufficient for reliable volatility
forecasting.

Risk assessment should be interpreted with
caution.
"""
    )

st.divider()

# =====================================================
# MARKET COMPARISON
# =====================================================

st.header("Market Comparison")

market_avg = risk_df[
    risk_df["Recommendation"] != "LOW LIQUIDITY"
]["Risk_Score"].mean()

difference = (
    row["Risk_Score"]
    - market_avg
)

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Security Risk Score",
        f"{row['Risk_Score']:.2f}"
    )

with c2:

    st.metric(
        "Market Average",
        f"{market_avg:.2f}"
    )

if difference > 0:

    st.warning(
        f"""
This security's risk score is
{difference:.2f} points ABOVE
the market average.
"""
    )

else:

    st.success(
        f"""
This security's risk score is
{abs(difference):.2f} points BELOW
the market average.
"""
    )

st.divider()

# =====================================================
# PEER POSITIONING
# =====================================================

st.header("Peer Positioning")

peer_view = (
    risk_df[
        [
            "Volatility_Rank",
            "Code",
            "Name",
            "Risk_Score",
            "Recommendation"
        ]
    ]
    .sort_values("Volatility_Rank")
)

st.dataframe(
    peer_view.head(15),
    use_container_width=True
)

st.divider()

# =====================================================
# HIGHEST RISK SECURITIES
# =====================================================

st.header("Securities Requiring Attention")

attention = (
    risk_df[
        risk_df["Recommendation"]
        == "HIGH VOLATILITY RISK"
    ]
    .sort_values(
        "Risk_Score",
        ascending=False
    )
)

st.dataframe(
    attention[
        [
            "Volatility_Rank",
            "Code",
            "Name",
            "Risk_Score"
        ]
    ],
    use_container_width=True
)

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • AI Advisory Center • Volatility Risk Intelligence Platform"
)