from pathlib import Path
import streamlit as st
import pandas as pd
from utils.styles import load_css

st.set_page_config(
    page_title="AI Advisory",
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

# =====================================================
# PAGE HEADER
# =====================================================

st.title("🤖 AI Advisory Center")

# =====================================================
# STOCK SELECTION
# =====================================================

stock = st.selectbox(
    "Select Stock",
    sorted(df["Code"].unique())
)

row = df[
    df["Code"] == stock
].iloc[0]

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Risk Score",
        round(row["Risk_Score"], 1)
    )

with c2:
    st.metric(
        "Predicted Volatility",
        round(
            row["Predicted_Volatility"],
            2
        )
    )

with c3:
    st.metric(
        "AI Action",
        row["Recommendation"]
    )

# =====================================================
# EXECUTIVE RECOMMENDATION
# =====================================================

st.subheader(
    "Executive Recommendation"
)

if row["Recommendation"] == "BUY":

    st.success(
        f"""
        LOW RISK

        {stock} exhibits relatively
        stable behaviour.

        Recommendation:
        Increase exposure.
        """
    )

elif row["Recommendation"] == "MONITOR":

    st.info(
        f"""
        MODERATE RISK

        Continue monitoring
        market movements.

        Recommendation:
        Watch closely.
        """
    )

elif row["Recommendation"] == "HOLD":

    st.warning(
        f"""
        ELEVATED RISK

        Current volatility levels
        require caution.

        Recommendation:
        Hold position.
        """
    )

else:

    st.error(
        f"""
        HIGH RISK

        Volatility is significantly
        above market average.

        Recommendation:
        Reduce exposure.
        """
    )

# =====================================================
# ALL RECOMMENDATIONS
# =====================================================

st.subheader("All Recommendations")

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "FinSight AI • AI Advisory Center • Powered by Machine Learning"
)