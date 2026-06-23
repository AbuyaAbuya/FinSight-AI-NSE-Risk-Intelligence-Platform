from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.styles import load_css

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Board Pack",
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

    metrics_df = pd.read_csv(
        OUTPUT_DIR / "model_metrics.csv"
    )

except Exception as e:

    st.error(
        f"Unable to load required files: {e}"
    )

    st.stop()

# =====================================================
# PREP DATA
# =====================================================

investable = risk_df[
    risk_df["Recommendation"] != "LOW LIQUIDITY"
].copy()

avg_risk = round(
    investable["Risk_Score"].mean(),
    1
)

highest_risk = (
    investable
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .iloc[0]
)

low_risk_count = len(
    investable[
        investable["Recommendation"]
        == "LOW VOLATILITY RISK"
    ]
)

moderate_risk_count = len(
    investable[
        investable["Recommendation"]
        == "MODERATE VOLATILITY RISK"
    ]
)

high_risk_count = len(
    investable[
        investable["Recommendation"]
        == "HIGH VOLATILITY RISK"
    ]
)

# =====================================================
# BOARD HEADER
# =====================================================

st.title("📋 Board Pack")

st.markdown(
    """
    Executive briefing prepared from the
    FinSight AI Volatility Risk Intelligence Platform.

    This report provides a high-level assessment of
    market volatility conditions, key risk exposures
    and strategic investment considerations across
    the Nairobi Securities Exchange.
    """
)

# =====================================================
# BOARD RISK POSITION
# =====================================================

if avg_risk < 35:

    banner_color = "#D1FAE5"
    market_status = "LOW RISK MARKET ENVIRONMENT"

elif avg_risk < 65:

    banner_color = "#FEF3C7"
    market_status = "MODERATE RISK MARKET ENVIRONMENT"

else:

    banner_color = "#FEE2E2"
    market_status = "ELEVATED RISK MARKET ENVIRONMENT"

st.markdown(
    f"""
    <div style="
        background:{banner_color};
        padding:25px;
        border-radius:12px;
        text-align:center;
        margin-bottom:30px;
    ">
        <h3 style="margin:0;">
            BOARD RISK ASSESSMENT
        </h3>

        <h1 style="margin-top:10px;">
            {market_status}
        </h1>

        <h4>
            Average Market Risk Score:
            {avg_risk}/100
        </h4>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# BOARD KPIs
# =====================================================

st.header("Board Snapshot")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Average Market Risk",
        f"{avg_risk}/100"
    )

with c2:

    st.metric(
        "Highest Risk Security",
        highest_risk["Name"]
    )

with c3:

    st.metric(
        "Securities Covered",
        len(risk_df)
    )

st.divider()

# =====================================================
# RISK DISTRIBUTION
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

fig_pie = px.pie(
    distribution,
    names="Risk Category",
    values="Count",
    hole=0.55
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# =====================================================
# BOARD ATTENTION LIST
# =====================================================

st.header("Securities Requiring Board Attention")

attention = (
    investable
    .sort_values(
        "Risk_Score",
        ascending=False
    )
    .head(10)
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
# LOW RISK OPPORTUNITIES
# =====================================================

st.header("Potential Defensive Holdings")

opportunities = (
    investable
    .sort_values(
        "Risk_Score",
        ascending=True
    )
    .head(10)
)

st.dataframe(
    opportunities[
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
# MODEL PERFORMANCE
# =====================================================

st.header("Forecasting Engine Performance")

rmse = float(
    metrics_df.loc[
        metrics_df["Metric"] == "RMSE",
        "Value"
    ].iloc[0]
)

mae = float(
    metrics_df.loc[
        metrics_df["Metric"] == "MAE",
        "Value"
    ].iloc[0]
)

r2 = float(
    metrics_df.loc[
        metrics_df["Metric"].isin(
            ["R2", "R²"]
        ),
        "Value"
    ].iloc[0]
)

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
        "R² Score",
        f"{r2:.4f}"
    )

# =====================================================
# BOARD COMMENTARY
# =====================================================

st.header("Board Commentary")

st.info(
    f"""
The market currently contains:

• {low_risk_count} Low Volatility Risk securities

• {moderate_risk_count} Moderate Volatility Risk securities

• {high_risk_count} High Volatility Risk securities

The overall market risk profile remains classified as
a {market_status.lower()}.

The highest forecast volatility is currently observed
within {highest_risk['Name']}, indicating elevated
uncertainty relative to the broader market universe.

Management should maintain diversification, monitor
high-volatility securities closely and prioritize
capital allocation toward lower-risk opportunities
where appropriate.
"""
)

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • Board Pack • Executive Volatility Intelligence"
)