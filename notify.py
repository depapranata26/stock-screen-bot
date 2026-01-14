from telegram import Bot

def send(token, chat_id, df):
    bot = Bot(token=token)
    text = "📊 Screening Saham EOD\n\n"
    if df is None or df.empty:
        text += "Tidak ada saham lolos filter hari ini."
    else:
    for _, r in df.iterrows():
            text += f"- {r['kode']} | Harga: {int(r['harga'])}\n"
    bot.send_message(chat_id=chat_id, text=text)