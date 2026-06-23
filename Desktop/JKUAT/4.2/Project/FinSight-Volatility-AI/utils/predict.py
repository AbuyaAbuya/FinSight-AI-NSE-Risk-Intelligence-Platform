import pandas as pd
import numpy as np
import joblib

from pathlib import Path

from utils.model_training import build_features

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(MODEL_PATH)

# =====================================================
# BUILD FEATURES
# =====================================================

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

# =====================================================
# PREDICT VOLATILITY
# =====================================================

prediction_df["Predicted_Volatility"] = model.predict(
    prediction_df[features]
)

# =====================================================
# LATEST OBSERVATION PER SECURITY
# =====================================================

latest = (
    prediction_df
    .sort_values("Date")
    .groupby("Code")
    .tail(1)
    .copy()
)

# =====================================================
# EXCLUDE NSE INDICES
# =====================================================

index_codes = [
    "^NBDI",
    "^N10I",
    "^NASI",
    "^ZKEQTU"
]

latest = latest[
    ~latest["Code"].isin(index_codes)
].copy()

# =====================================================
# RISK SCORE
# =====================================================

max_vol = latest["Predicted_Volatility"].max()

latest["Risk_Score"] = (
    latest["Predicted_Volatility"]
    / max_vol
) * 100

# =====================================================
# LOW LIQUIDITY SECURITIES
# =====================================================

low_liquidity = latest[
    latest["Risk_Score"] < 1
].copy()

low_liquidity["Recommendation"] = (
    "LOW LIQUIDITY"
)

low_liquidity["Volatility_Rank"] = np.nan

# =====================================================
# INVESTABLE SECURITIES
# =====================================================

eligible = latest[
    latest["Risk_Score"] >= 1
].copy()

eligible = eligible.sort_values(
    "Risk_Score",
    ascending=True
).reset_index(drop=True)

# =====================================================
# VOLATILITY RANK
# =====================================================

eligible["Volatility_Rank"] = (
    eligible.index + 1
)

# =====================================================
# DATA-DRIVEN RISK CLASSIFICATION
# =====================================================

LOW_THRESHOLD = 33
HIGH_THRESHOLD = 65

eligible["Recommendation"] = (
    "MODERATE VOLATILITY RISK"
)

eligible.loc[
    eligible["Risk_Score"] <= LOW_THRESHOLD,
    "Recommendation"
] = "LOW VOLATILITY RISK"

eligible.loc[
    eligible["Risk_Score"] > HIGH_THRESHOLD,
    "Recommendation"
] = "HIGH VOLATILITY RISK"

# =====================================================
# COMBINE RESULTS
# =====================================================

risk_scores = pd.concat(
    [
        eligible,
        low_liquidity
    ],
    ignore_index=True
)

risk_scores = risk_scores[
    [
        "Volatility_Rank",
        "Code",
        "Name",
        "Predicted_Volatility",
        "Risk_Score",
        "Recommendation"
    ]
]

# =====================================================
# SORT RESULTS
# =====================================================

risk_scores = risk_scores.sort_values(
    [
        "Recommendation",
        "Volatility_Rank"
    ],
    na_position="last"
)

# =====================================================
# SAVE OUTPUT
# =====================================================

risk_scores.to_csv(
    OUTPUT_DIR / "risk_scores.csv",
    index=False
)

# =====================================================
# SUMMARY OUTPUT
# =====================================================

print("\nRisk Category Distribution\n")

print(
    risk_scores["Recommendation"]
    .value_counts()
)

print("\nLowest Volatility Risk Securities\n")

print(
    risk_scores[
        risk_scores["Recommendation"]
        == "LOW VOLATILITY RISK"
    ][
        [
            "Volatility_Rank",
            "Code",
            "Risk_Score"
        ]
    ]
)

print("\nHighest Volatility Risk Securities\n")

print(
    risk_scores[
        risk_scores["Recommendation"]
        == "HIGH VOLATILITY RISK"
    ][
        [
            "Volatility_Rank",
            "Code",
            "Risk_Score"
        ]
    ]
)

print("\nLow Liquidity Securities\n")

print(
    risk_scores[
        risk_scores["Recommendation"]
        == "LOW LIQUIDITY"
    ][
        [
            "Code",
            "Risk_Score"
        ]
    ]
)

print("\nRisk Classification Methodology")

print(
    """
LOW VOLATILITY RISK:
Risk Score <= 33

MODERATE VOLATILITY RISK:
Risk Score > 33 and <= 65

HIGH VOLATILITY RISK:
Risk Score > 65

LOW LIQUIDITY:
Insufficient trading activity for reliable
volatility assessment.
"""
)

print("\nRisk scores generated.")