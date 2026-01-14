from fetch_data import fetch
from screen import screen
from notify import send
import config

SYMBOLS = [
    "BBRI.JK",
    "TLKM.JK",
    "PGAS.JK",
    "ANTM.JK",
    "PTBA.JK"
]

df = fetch(SYMBOLS)
filtered = screen(df, config.MAX_PRICE, config.MIN_VOLUME)
send(config.BOT_TOKEN, config.CHAT_ID, filtered)