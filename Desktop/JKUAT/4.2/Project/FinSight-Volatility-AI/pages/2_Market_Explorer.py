import streamlit as st
import pandas as pd
import plotly.express as px

from utils.styles import load_css
from utils.data_loader import load_data

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

from utils.data_loader import load_data

# =========================================================
# PAGE TITLE
# =========================================================

st.title("📈 Market Explorer")

st.markdown(
    "Interactive analysis of NSE listed companies."
)

# =========================================================
# LOAD DATA
# =========================================================

df = load_data()

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Day Price"] = pd.to_numeric(
    df["Day Price"],
    errors="coerce"
)

# Clean Volume
df["Volume"] = (
    df["Volume"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("-", "0", regex=False)
)

df["Volume"] = pd.to_numeric(
    df["Volume"],
    errors="coerce"
).fillna(0)

df = df.dropna(
    subset=["Day Price"]
)

# =========================================================
# STOCK SELECTION
# =========================================================

stocks = sorted(
    df["Code"].dropna().unique()
)

selected_stock = st.selectbox(
    "Select NSE Stock",
    stocks
)

stock_df = (
    df[df["Code"] == selected_stock]
    .copy()
    .sort_values("Date")
)

# =========================================================
# RETURNS
# =========================================================

stock_df["Daily Return"] = (
    stock_df["Day Price"]
    .pct_change()
    * 100
)

# =========================================================
# EXECUTIVE KPIs
# =========================================================

latest_price = stock_df["Day Price"].iloc[-1]

avg_price = stock_df["Day Price"].mean()

max_price = stock_df["Day Price"].max()

avg_return = stock_df["Daily Return"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest Price",
        f"{latest_price:.2f}"
    )

with col2:
    st.metric(
        "Average Price",
        f"{avg_price:.2f}"
    )

with col3:
    st.metric(
        "Highest Price",
        f"{max_price:.2f}"
    )

with col4:
    st.metric(
        "Average Return %",
        f"{avg_return:.2f}"
    )

# =========================================================
# PRICE TREND
# =========================================================

st.subheader("📊 Share Price Trend")

fig_price = px.line(
    stock_df,
    x="Date",
    y="Day Price",
    title=f"{selected_stock} Share Price"
)

st.plotly_chart(
    fig_price,
    use_container_width=True
)

# =========================================================
# RETURNS TREND
# =========================================================

st.subheader("📈 Daily Returns")

fig_return = px.line(
    stock_df,
    x="Date",
    y="Daily Return",
    title=f"{selected_stock} Daily Returns (%)"
)

st.plotly_chart(
    fig_return,
    use_container_width=True
)

# =========================================================
# RETURN DISTRIBUTION
# =========================================================

st.subheader("📉 Return Distribution")

fig_hist = px.histogram(
    stock_df,
    x="Daily Return",
    nbins=50,
    title=f"{selected_stock} Return Distribution"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# =========================================================
# VOLUME
# =========================================================

if stock_df["Volume"].sum() > 0:

    st.subheader("📦 Trading Volume")

    fig_volume = px.bar(
        stock_df,
        x="Date",
        y="Volume",
        title=f"{selected_stock} Trading Volume"
    )

    st.plotly_chart(
        fig_volume,
        use_container_width=True
    )

# =========================================================
# DATA TABLE
# =========================================================

st.subheader("📋 Market Data")

display_cols = [
    "Date",
    "Code",
    "Name",
    "Day Price",
    "Volume",
    "Daily Return"
]

st.dataframe(
    stock_df[display_cols].tail(20),
    use_container_width=True
)