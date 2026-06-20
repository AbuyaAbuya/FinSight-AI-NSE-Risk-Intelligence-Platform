import streamlit as st
import pandas as pd
from pathlib import Path
from utils.styles import load_css

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("📑 Research Findings")

# =====================================================
# FILE PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

METRICS_FILE = (
    BASE_DIR
    / "outputs"
    / "model_metrics.csv"
)

# =====================================================
# INTRODUCTION
# =====================================================

st.header(
    "Machine Learning Volatility Forecasting Results"
)

st.write(
    """
    This study developed and evaluated a Random Forest
    Machine Learning model for forecasting stock price
    volatility of companies listed on the Nairobi
    Securities Exchange (NSE).
    """
)

st.write(
    """
    The Random Forest model was selected as the final
    production model due to its strong predictive
    performance and ability to capture nonlinear
    market behaviour.
    """
)

st.divider()

# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.header("Model Performance Results")

try:

    metrics = pd.read_csv(METRICS_FILE)

    st.dataframe(
        metrics.round(4),
        use_container_width=True
    )

except Exception as e:

    st.error(
        f"Unable to load model metrics file: {e}"
    )

st.divider()

# =====================================================
# KEY FINDINGS
# =====================================================

st.header("Key Findings")

st.success(
    """
    Random Forest achieved high predictive accuracy,
    with a strong R² score indicating that the model
    successfully explains most volatility variation.
    """
)

st.info(
    """
    NSE stocks exhibit varying volatility levels,
    enabling classification into Low, Medium and
    High Risk categories.
    """
)

st.warning(
    """
    A relatively small number of securities account
    for most observed market risk, suggesting that
    targeted portfolio monitoring is more effective
    than market-wide intervention.
    """
)

# =====================================================
# BUSINESS IMPLICATIONS
# =====================================================

st.header("Business Implications")

st.markdown(
    """
- Investors can identify high-risk stocks early.

- Portfolio managers can improve allocation decisions.

- CFOs can monitor market risk exposure.

- Boards can use risk dashboards for strategic oversight.

- Financial institutions can integrate AI forecasting into risk management frameworks.
"""
)

st.divider()

# =====================================================
# CONCLUSION
# =====================================================

st.header("Conclusion")

st.success(
    """
    The findings demonstrate that Random Forest
    Machine Learning models can provide reliable
    volatility forecasts and practical decision
    support for investors, executives and
    financial analysts.
    """
)