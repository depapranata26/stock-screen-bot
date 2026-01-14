import yfinance as yf
import pandas as pd

def fetch(symbols):
    rows = []

    for symbol in symbols:
        df = yf.download(symbol, period="1mo", interval="1d", progress=False)

        if df.empty or len(df) < 20:
            continue

        close = df["Close"].iloc[-1]
        low_20 = df["Low"].rolling(20).min().iloc[-1]
        vol_5 = df["Volume"].rolling(5).mean().iloc[-1]

        # SEMUA SUDAH SCALAR
        if pd.isna(close) or pd.isna(low_20) or pd.isna(vol_5):
            continue

        rows.append({
            "kode": symbol.replace(".JK", ""),
            "harga": float(close),
            "low_20d": float(low_20),
            "volume_5d": float(vol_5),
        })

    return pd.DataFrame(rows)
