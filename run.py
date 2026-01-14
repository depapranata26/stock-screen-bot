from fetch_data import fetch
from screen import screen
from notify_bot import send
import config

SYMBOLS = [
    "BBRI.JK",
    "TLKM.JK",
    "PGAS.JK",
    "ANTM.JK",
    "PTBA.JK",
    "ADRO.JK",
]

def main():
    df = fetch(SYMBOLS)

    if df is None or df.empty:
        send(config.BOT_TOKEN, config.CHAT_ID, df)
        return

    filtered = screen(
        df,
        float(config.MAX_PRICE),
        float(config.MIN_VOLUME)
    )

    send(config.BOT_TOKEN, config.CHAT_ID, filtered)

if __name__ == "__main__":
    main()
