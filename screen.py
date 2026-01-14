def screen(df, max_price, min_volume):
    return df[
        (df["harga"] <= max_price) &
        (df["volume_5d"] >= min_volume) &
        (df["harga"] >= df["low_20d"])
    ]