import yfinance as yf
import pandas as pd

def fetch(symbols):
    rows = []

    for s in symbols:
        df = yf.download(
            s,
            period="1mo",
            interval="1d",
            progress=False
        )

        if df.empty or len(df) < 20:
            continue

        close = df["Close"].iloc[-1]
        low_20 = df["Low"].tail(20).min()
        vol_5 = df["Volume"].tail(5).mean()

        if pd.isna(close) or pd.isna(low_20) or pd.isna(vol_5):
            continue

        rows.append({
            "kode": s.replace(".JK", ""),
            "harga": float(close),
            "volume_5d": float(vol_5),
            "low_20d": float(low_20),
        })

    return pd.DataFrame(rows)