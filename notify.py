from telegram import Bot

def send(token, chat_id, df):
    if df.empty:
        message = "📊 Screening EOD\n\nTidak ada saham lolos filter hari ini."
    else:
        lines = ["📊 Screening EOD\n"]
        for _, row in df.iterrows():
            lines.append(
                f"- {row['kode']} | Harga: {row['harga']} | Vol: {row['volume_5d']:,}"
            )
        message = "\n".join(lines)

    Bot(token=token).send_message(chat_id=chat_id, text=message)