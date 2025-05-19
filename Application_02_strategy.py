import pandas as pd
import numpy as np
import requests


def fetch_klines(instId="BTC-USDT-SWAP", bar="1H", limit=100):
    url = f"https://www.okx.com/api/v5/market/candles?instId={
    instId}&bar={bar}&limit={limit}"
    response = requests.get(url)
    raw = response.json()['data']
    df = pd.DataFrame(raw, columns=["ts", "o", "h", "l", "c", "vol", "volCcy", "volCcyQuote", "confirm"])
    df = df.iloc[::-1].copy()
    df["Close"] = df["c"].astype(float)
    df["High"] = df["h"].astype(float)
    df["Low"] = df["l"].astype(float)
    return df.reset_index(drop=True)


def generate_signal(df, period=20, t=2.33):
    df["SMA"] = df["Close"].rolling(period).mean()
    df["STD"] = df["Close"].rolling(period).std()
    df["Upper"] = df["SMA"] + t * df["STD"]
    df["Lower"] = df["SMA"] - t * df["STD"]

    last_row = df.iloc[-1]
    if last_row["High"] >= last_row["Upper"] and last_row["High"] > last_row["SMA"]:
        return 1  # long
    elif last_row["Low"] <= last_row["Lower"] and last_row["Low"] < last_row["SMA"]:
        return -1  # short
    else:
        return 0  # no action
