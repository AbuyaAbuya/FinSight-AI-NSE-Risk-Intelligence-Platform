from pathlib import Path
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_data
def load_data():
    """
    Load and combine NSE datasets.
    """

    file_2023 = DATA_DIR / "NSE_data_all_stocks_2023.csv"
    file_2024 = DATA_DIR / "NSE_data_all_stocks_2024.csv"

    df_2023 = pd.read_csv(file_2023)
    df_2024 = pd.read_csv(file_2024)

    df = pd.concat(
        [df_2023, df_2024],
        ignore_index=True
    )

    return df


@st.cache_data
def get_stock_list(df):
    """
    Return available stock symbols.
    """

    possible_cols = [
        "Code",
        "CODE",
        "Symbol",
        "SYMBOL",
        "Ticker"
    ]

    for col in possible_cols:
        if col in df.columns:
            return sorted(df[col].dropna().unique())

    return []