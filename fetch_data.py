import yfinance as yf
import pandas as pd

def fetch(symbols):
    rows = []

    for symbol in symbols:
        df = yf.download(
            symbol,
            period="1mo",
            interval="1d",
            progress=False,
            group_by="column"
        )

        if df.empty or len(df) < 20:
            continue

        # ⬇️ PAKSA JADI SCALAR
        close = float(df["Close"].values[-1])
        low_20 = float(df["Low"].rolling(20).min().values[-1])
        vol_5 = float(df["Volume"].rolling(5).mean().values[-1])

        # sekarang AMAN
        if pd.isna(close) or pd.isna(low_20) or pd.isna(vol_5):
            continue

        rows.append({
            "kode": symbol.replace(".JK", ""),
            "harga": close,
            "low_20d": low_20,
            "volume_5d": vol_5,
        })

    return pd.DataFrame(rows)
