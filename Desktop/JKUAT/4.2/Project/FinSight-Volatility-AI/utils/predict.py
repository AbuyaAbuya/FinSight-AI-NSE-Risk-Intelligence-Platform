import pandas as pd
import numpy as np
import joblib

from pathlib import Path

from utils.model_training import build_features

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

model = joblib.load(MODEL_PATH)

df = build_features()

features = [
    "Lag_1",
    "Lag_2",
    "Lag_3",
    "Volatility_5",
    "Volatility_10",
    "Volatility_30"
]

prediction_df = df.dropna(
    subset=features
).copy()

prediction_df["Predicted_Volatility"] = model.predict(
    prediction_df[features]
)

latest = (
    prediction_df
    .sort_values("Date")
    .groupby("Code")
    .tail(1)
    .copy()
)

max_vol = latest["Predicted_Volatility"].max()

latest["Risk_Score"] = (
    latest["Predicted_Volatility"]
    / max_vol
) * 100

def recommendation(score):

    if score >= 70:
        return "REDUCE EXPOSURE"

    elif score >= 40:
        return "HOLD"

    elif score >= 20:
        return "MONITOR"

    else:
        return "BUY"

latest["Recommendation"] = (
    latest["Risk_Score"]
    .apply(recommendation)
)

risk_scores = latest[
    [
        "Code",
        "Name",
        "Predicted_Volatility",
        "Risk_Score",
        "Recommendation"
    ]
]

risk_scores = risk_scores.sort_values(
    "Risk_Score",
    ascending=False
)

risk_scores.to_csv(
    OUTPUT_DIR / "risk_scores.csv",
    index=False
)

print("Risk scores generated.")