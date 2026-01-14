from telegram import Bot

def send(token, chat_id, df):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text="✅ Bot test OK")
