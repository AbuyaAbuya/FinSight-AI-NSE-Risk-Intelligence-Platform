import streamlit as st
import pandas as pd
from utils.styles import load_css

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="AI Advisory",
    layout="wide"
)

st.title("🤖 AI Advisory Center")

df = pd.read_csv(
    "outputs/risk_scores.csv"
)

stock = st.selectbox(
    "Select Stock",
    sorted(df["Code"].unique())
)

row = df[
    df["Code"] == stock
].iloc[0]

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

st.subheader("All Recommendations")

st.dataframe(
    df,
    use_container_width=True
)