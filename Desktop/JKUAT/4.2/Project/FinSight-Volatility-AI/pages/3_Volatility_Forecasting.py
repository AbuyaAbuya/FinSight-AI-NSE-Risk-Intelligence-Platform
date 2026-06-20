import streamlit as st
import pandas as pd
import plotly.express as px
from utils.styles import load_css

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

from utils.data_loader import load_data

st.title("🔮 Volatility Forecasting Center")

st.markdown(
    "Machine Learning based stock volatility forecasting and risk assessment."
)

# =====================================================
# LOAD DATA
# =====================================================

df = load_data()

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Day Price"] = pd.to_numeric(
    df["Day Price"],
    errors="coerce"
)

df = df.dropna(subset=["Day Price"])

# =====================================================
# STOCK SELECTION
# =====================================================

stocks = sorted(df["Code"].dropna().unique())

selected_stock = st.selectbox(
    "Select NSE Stock",
    stocks
)

stock_df = (
    df[df["Code"] == selected_stock]
    .copy()
    .sort_values("Date")
)

# =====================================================
# RETURNS
# =====================================================

stock_df["Daily_Return"] = (
    stock_df["Day Price"]
    .pct_change()
    * 100
)

# =====================================================
# VOLATILITY FEATURES
# =====================================================

stock_df["Volatility_5"] = (
    stock_df["Daily_Return"]
    .rolling(5)
    .std()
)

stock_df["Volatility_10"] = (
    stock_df["Daily_Return"]
    .rolling(10)
    .std()
)

stock_df["Volatility_30"] = (
    stock_df["Daily_Return"]
    .rolling(30)
    .std()
)

latest_vol = round(
    stock_df["Volatility_30"].iloc[-1],
    2
)

# =====================================================
# RISK CLASSIFICATION
# =====================================================

if latest_vol >= 5:
    recommendation = "REDUCE EXPOSURE"
    risk = "HIGH"

elif latest_vol >= 3:
    recommendation = "HOLD"
    risk = "MODERATE"

elif latest_vol >= 2:
    recommendation = "MONITOR"
    risk = "LOW"

else:
    recommendation = "BUY"
    risk = "VERY LOW"

# =====================================================
# EXECUTIVE KPIs
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Forecast Volatility",
        latest_vol
    )

with c2:
    st.metric(
        "Risk Level",
        risk
    )

with c3:
    st.metric(
        "Recommendation",
        recommendation
    )

# =====================================================
# AI FORECAST SUMMARY
# =====================================================

st.subheader("🤖 Forecast Summary")

if recommendation == "BUY":
    st.success(
        f"{selected_stock} exhibits relatively stable behaviour. "
        "Current volatility remains low."
    )

elif recommendation == "MONITOR":
    st.info(
        f"{selected_stock} shows moderate fluctuations. "
        "Continue monitoring price movements."
    )

elif recommendation == "HOLD":
    st.warning(
        f"{selected_stock} volatility has increased. "
        "Maintain current position and monitor closely."
    )

else:
    st.error(
        f"{selected_stock} exhibits elevated risk. "
        "Consider reducing exposure."
    )

# =====================================================
# VOLATILITY TREND
# =====================================================

st.subheader("📊 Volatility Trend")

fig = px.line(
    stock_df,
    x="Date",
    y=[
        "Volatility_5",
        "Volatility_10",
        "Volatility_30"
    ],
    title=f"{selected_stock} Rolling Volatility"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# DAILY RETURNS
# =====================================================

st.subheader("📈 Daily Returns")

fig_return = px.line(
    stock_df,
    x="Date",
    y="Daily_Return",
    title=f"{selected_stock} Daily Returns"
)

st.plotly_chart(
    fig_return,
    use_container_width=True
)

# =====================================================
# RECENT FORECAST DATA
# =====================================================

st.subheader("📋 Forecast Data")

display_cols = [
    "Date",
    "Day Price",
    "Daily_Return",
    "Volatility_5",
    "Volatility_10",
    "Volatility_30"
]

st.dataframe(
    stock_df[display_cols].tail(20),
    use_container_width=True
)