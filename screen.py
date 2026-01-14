def screen(df, max_price, min_volume):
    if df.empty:
        return df

    df = df.copy()

    df["harga"] = df["harga"].astype(float)
    df["volume_5d"] = df["volume_5d"].astype(float)
    df["low_20d"] = df["low_20d"].astype(float)

    return df[
        (df["harga"] <= max_price) &
        (df["volume_5d"] >= min_volume) &
        (df["harga"] >= df["low_20d"])
    ]