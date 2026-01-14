from fetch_data import fetch
from screen import screen
from notify import send
import config
import sys

SYMBOLS = [
    "BBRI.JK",
    "TLKM.JK",
    "PGAS.JK",
    "ANTM.JK",
    "PTBA.JK",
    "ADRO.JK",
]

def main():
    # 1. ambil data
    df = fetch(SYMBOLS)

    # 2. validasi fetch
    if df is None or df.empty:
        # tetap kirim pesan agar bot "terasa hidup"
        send(
            config.BOT_TOKEN,
            config.CHAT_ID,
            df
        )
        return

    # 3. screening (AMAN)
    filtered = screen(
        df,
        float(config.MAX_PRICE),
        float(config.MIN_VOLUME)
    )

    # 4. kirim hasil
    send(
        config.BOT_TOKEN,
        config.CHAT_ID,
        filtered
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # FAIL-SAFE: kirim error ke Telegram
        try:
            from telegram import Bot
            Bot(token=config.BOT_TOKEN).send_message(
                chat_id=config.CHAT_ID,
                text=f"❌ Bot error:\n{e}"
            )
        except:
            pass
        sys.exit(1)