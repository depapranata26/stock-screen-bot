from telegram import Bot

def send(token, chat_id, df):
    bot = Bot(token=token)

    if df.empty:
        text = (
            "📊 Screening Saham EOD\n\n"
            "Tidak ada saham lolos filter hari ini.\n\n"
            "Catatan:\n"
            "- Ini BUKAN sinyal beli\n"
            "- Tetap analisis manual"
        )
    else:
        lines = ["📊 Screening Saham EOD\n"]

        for _, r in df.iterrows():
            lines.append(
                f"- {r['kode']} | Harga: {int(r['harga'])} | "
                f"Vol(5d): {int(r['volume_5d']):,}"
            )

        lines.append("\nCatatan:")
        lines.append("- Ini BUKAN sinyal beli")
        lines.append("- Wajib analisis manual")

        text = "\n".join(lines)

    bot.send_message(chat_id=chat_id, text=text)