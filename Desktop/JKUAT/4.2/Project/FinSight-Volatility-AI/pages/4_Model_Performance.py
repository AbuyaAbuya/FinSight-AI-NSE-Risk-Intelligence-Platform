from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import load_css

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
# PAGE TITLE
# =====================================================

st.title("📊 Model Performance")

st.header("Random Forest Volatility Forecasting Model")

st.write(
    """
    This section presents the performance of the
    Random Forest model used for stock volatility
    forecasting on NSE listed companies.
    """
)

# =====================================================
# LOAD METRICS
# =====================================================

try:

    metrics = pd.read_csv(
        OUTPUT_DIR / "model_metrics.csv"
    )

    rmse = float(
        metrics.loc[
            metrics["Metric"] == "RMSE",
            "Value"
        ].iloc[0]
    )

    mae = float(
        metrics.loc[
            metrics["Metric"] == "MAE",
            "Value"
        ].iloc[0]
    )

    r2 = float(
        metrics.loc[
            metrics["Metric"].isin(["R2", "R²"]),
            "Value"
        ].iloc[0]
    )

except Exception:

    rmse = 0
    mae = 0
    r2 = 0

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "RMSE",
        round(rmse, 4)
    )

with col2:
    st.metric(
        "MAE",
        round(mae, 4)
    )

with col3:
    st.metric(
        "R² Score",
        round(r2, 4)
    )

# =====================================================
# VISUALIZATION
# =====================================================

metric_df = pd.DataFrame({
    "Metric": ["RMSE", "MAE", "R²"],
    "Value": [rmse, mae, r2]
})

fig = px.bar(
    metric_df,
    x="Metric",
    y="Value",
    color="Metric",
    title="Random Forest Evaluation Metrics"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# METRICS TABLE
# =====================================================

try:
    st.subheader("Model Metrics")

    st.dataframe(
        metrics,
        use_container_width=True
    )

except Exception:
    pass

# =====================================================
# INTERPRETATION
# =====================================================

st.subheader("Research Interpretation")

st.success(
    f"""
    The Random Forest model achieved an
    R² score of {r2:.4f},
    demonstrating strong predictive ability.
    """
)

st.info(
    f"""
    Forecasting errors remained low with
    RMSE = {rmse:.4f}
    and MAE = {mae:.4f}.
    """
)

# =====================================================
# CONCLUSION
# =====================================================

st.subheader("Conclusion")

st.success(
    """
    Random Forest was selected as the final
    production model due to its strong
    predictive accuracy and ability to
    capture nonlinear stock market behaviour.
    """
)