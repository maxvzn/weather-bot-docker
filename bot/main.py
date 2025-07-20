import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/ping")
async def ping_handler(message: Message):
    await message.answer("pong")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())