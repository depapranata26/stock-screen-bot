from telegram import Bot
import asyncio

async def send_async(token, chat_id, df):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text="TEST OK")

def send(token, chat_id, df):
