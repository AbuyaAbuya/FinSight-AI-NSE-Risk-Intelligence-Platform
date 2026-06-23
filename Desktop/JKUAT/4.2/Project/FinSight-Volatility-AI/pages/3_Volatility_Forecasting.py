import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from utils.styles import load_css
from utils.data_loader import load_data

# =====================================================
# PAGE CONFIG
# =====================================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

st.title("📊 Volatility Risk Intelligence")

st.markdown(
    """
    Volatility risk analytics and market intelligence
    powered by machine learning forecasting models.
    """
)

# =====================================================
# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

df = load_data()

risk_df = pd.read_csv(
    OUTPUT_DIR / "risk_scores.csv"
)

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Day Price"] = pd.to_numeric(
    df["Day Price"],
    errors="coerce"
)

df = df.dropna(
    subset=["Day Price"]
)

# =====================================================
# DATASET COVERAGE
# =====================================================

min_date = df["Date"].min()
max_date = df["Date"].max()

st.info(
    f"""
    Dataset Coverage:
    {min_date.strftime('%d-%b-%Y')}
    to
    {max_date.strftime('%d-%b-%Y')}
    """
)

# =====================================================
# DATE FILTER
# =====================================================

start_date, end_date = st.date_input(
    "Select Analysis Period",
    value=(
        min_date.date(),
        max_date.date()
    )
)

df = df[
    (df["Date"] >= pd.to_datetime(start_date))
    &
    (df["Date"] <= pd.to_datetime(end_date))
]

# =====================================================
# STOCK SELECTION
# =====================================================

stocks = sorted(
    risk_df["Code"].unique()
)

selected_stock = st.selectbox(
    "Select Security",
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
# VOLATILITY METRICS
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

# =====================================================
# DISPLAY LABELS
# =====================================================

plot_df = stock_df.copy()

plot_df = plot_df.rename(
    columns={
        "Volatility_5": "5-Day Volatility",
        "Volatility_10": "10-Day Volatility",
        "Volatility_30": "30-Day Volatility"
    }
)

# =====================================================
# RISK INTELLIGENCE DATA
# =====================================================

risk_row = risk_df[
    risk_df["Code"] == selected_stock
].iloc[0]

expected_volatility = round(
    risk_row["Predicted_Volatility"],
    2
)

risk_score = round(
    risk_row["Risk_Score"],
    2
)

risk_classification = (
    risk_row["Recommendation"]
)

volatility_rank = (
    risk_row["Volatility_Rank"]
)

investable_count = (
    risk_df["Volatility_Rank"]
    .notna()
    .sum()
)

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Expected 30-Day Volatility",
        expected_volatility
    )

with c2:

    st.metric(
        "Volatility Risk Score",
        risk_score
    )

with c3:

    if pd.notna(volatility_rank):

        st.metric(
            "Market Volatility Rank",
            f"{int(volatility_rank)} / {investable_count}"
        )

    else:

        st.metric(
            "Market Volatility Rank",
            "N/A"
        )

# =====================================================
# RISK CLASSIFICATION
# =====================================================

st.subheader("Risk Classification")

if risk_classification == "LOW VOLATILITY RISK":

    st.success(
        f"### {risk_classification}"
    )

elif risk_classification == "MODERATE VOLATILITY RISK":

    st.info(
        f"### {risk_classification}"
    )

elif risk_classification == "HIGH VOLATILITY RISK":

    st.warning(
        f"### {risk_classification}"
    )

else:

    st.error(
        f"### {risk_classification}"
    )

# =====================================================
# RISK INTELLIGENCE SUMMARY
# =====================================================

st.subheader("Risk Intelligence Summary")

if risk_classification == "LOW VOLATILITY RISK":

    st.write(
        f"""
        {selected_stock} ranks among the lowest-volatility
        securities within the investable universe,
        indicating relatively stable historical price
        behaviour compared to peer securities.
        """
    )

elif risk_classification == "MODERATE VOLATILITY RISK":

    st.write(
        f"""
        {selected_stock} exhibits moderate volatility
        characteristics and is positioned within the
        middle range of the market risk spectrum.
        """
    )

elif risk_classification == "HIGH VOLATILITY RISK":

    st.write(
        f"""
        {selected_stock} ranks among the highest-volatility
        securities within the investable universe,
        indicating elevated market risk relative to
        peer securities.
        """
    )

else:

    st.write(
        f"""
        {selected_stock} has been classified as a
        low-liquidity security. Limited trading
        activity may reduce the reliability of
        volatility-based risk interpretation.
        """
    )

# =====================================================
# VOLATILITY TRENDS
# =====================================================

st.subheader("📊 Historical Volatility Trends")

fig = px.line(
    plot_df,
    x="Date",
    y=[
        "5-Day Volatility",
        "10-Day Volatility",
        "30-Day Volatility"
    ],
    title=f"{selected_stock} Historical Volatility Profile"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# RETURN TRENDS
# =====================================================

st.subheader("📈 Historical Return Trends")

fig_return = px.line(
    stock_df,
    x="Date",
    y="Daily_Return",
    title=f"{selected_stock} Historical Daily Returns"
)

st.plotly_chart(
    fig_return,
    use_container_width=True
)

# =====================================================
# DATA TABLE
# =====================================================

st.subheader("📋 Volatility Analytics Data")

display_df = stock_df[
    [
        "Date",
        "Day Price",
        "Daily_Return",
        "Volatility_5",
        "Volatility_10",
        "Volatility_30"
    ]
].copy()

display_df.columns = [
    "Date",
    "Closing Price",
    "Daily Return (%)",
    "5-Day Volatility",
    "10-Day Volatility",
    "30-Day Volatility"
]

st.dataframe(
    display_df.tail(20),
    use_container_width=True
)