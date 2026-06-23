import numpy as np
import pandas as pd


def create_features(df):
    """
    Create volatility forecasting features.
    """

    df = df.copy()

    # Standardize column names
    df.columns = [c.strip() for c in df.columns]

    # Find stock code column
    stock_col = None

    for col in ["Code", "CODE", "Symbol", "SYMBOL"]:
        if col in df.columns:
            stock_col = col
            break

    # Find date column
    date_col = None

    for col in ["Date", "DATE", "date"]:
        if col in df.columns:
            date_col = col
            break

    # Find close price column
    close_col = None

    for col in ["Close", "CLOSE", "close"]:
        if col in df.columns:
            close_col = col
            break

    if close_col is None:
        return df

    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])

    if stock_col and date_col:
        df = df.sort_values([stock_col, date_col])

    # Daily return
    if stock_col:
        df["Return"] = (
            df.groupby(stock_col)[close_col]
            .pct_change()
        )
    else:
        df["Return"] = df[close_col].pct_change()

    # Lag returns
    df["Lag_1"] = df["Return"].shift(1)
    df["Lag_2"] = df["Return"].shift(2)
    df["Lag_3"] = df["Return"].shift(3)

    # Rolling volatility
    df["Volatility_5"] = (
        df["Return"]
        .rolling(5)
        .std()
    )

    df["Volatility_10"] = (
        df["Return"]
        .rolling(10)
        .std()
    )

    # Moving averages
    df["MA_5"] = (
        df[close_col]
        .rolling(5)
        .mean()
    )

    df["MA_10"] = (
        df[close_col]
        .rolling(10)
        .mean()
    )

    return df