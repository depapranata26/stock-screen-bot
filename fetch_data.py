import yfinance as yf
import pandas as pd

def fetch(symbols):
    rows = []

    for s in symbols:
        df = yf.download(s, period="1mo", interval="1d", progress=False)
        if df.empty or len(df) < 20:
            continue

        rows.append({
            "kode": s.replace(".JK", ""),
            "harga": round(df["Close"].iloc[-1]),
            "volume_5d": int(df["Volume"].tail(5).mean()),
            "low_20d": round(df["Low"].tail(20).min())
        })

    return pd.DataFrame(rows)