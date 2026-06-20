import pandas as pd
import numpy as np
import joblib

from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from utils.data_loader import load_data

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


def build_features():

    df = load_data()

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

    df = df.sort_values(
        ["Code", "Date"]
    )

    # Daily Returns

    df["Daily_Return"] = (
        df.groupby("Code")["Day Price"]
        .pct_change() * 100
    )

    # Lag Features

    df["Lag_1"] = (
        df.groupby("Code")["Daily_Return"]
        .shift(1)
    )

    df["Lag_2"] = (
        df.groupby("Code")["Daily_Return"]
        .shift(2)
    )

    df["Lag_3"] = (
        df.groupby("Code")["Daily_Return"]
        .shift(3)
    )

    # Rolling Volatility

    df["Volatility_5"] = (
        df.groupby("Code")["Daily_Return"]
        .rolling(5)
        .std()
        .reset_index(level=0, drop=True)
    )

    df["Volatility_10"] = (
        df.groupby("Code")["Daily_Return"]
        .rolling(10)
        .std()
        .reset_index(level=0, drop=True)
    )

    df["Volatility_30"] = (
        df.groupby("Code")["Daily_Return"]
        .rolling(30)
        .std()
        .reset_index(level=0, drop=True)
    )

    # Forecast target

    df["Target"] = (
        df.groupby("Code")["Volatility_30"]
        .shift(-1)
    )

    return df


def train_model():

    df = build_features()

    features = [
        "Lag_1",
        "Lag_2",
        "Lag_3",
        "Volatility_5",
        "Volatility_10",
        "Volatility_30"
    ]

    model_df = df[
        features + ["Target"]
    ].dropna()

    X = model_df[features]

    y = model_df["Target"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    metrics = pd.DataFrame({
        "Metric": [
            "RMSE",
            "MAE",
            "R2"
        ],
        "Value": [
            rmse,
            mae,
            r2
        ]
    })

    metrics.to_csv(
        OUTPUT_DIR / "model_metrics.csv",
        index=False
    )

    joblib.dump(
        model,
        MODEL_DIR / "random_forest.pkl"
    )

    return model


if __name__ == "__main__":

    train_model()

    print("Model trained successfully.")