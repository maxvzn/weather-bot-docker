import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, Location
from dotenv import load_dotenv
import bot.keyboards as kb
from bot.services import fetch_weather

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/ping")
async def ping_handler(message: Message):
    await message.answer("pong")


@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "Привет! Пришли мне свою геолокацию, и я покажу погоду рядом с тобой.",
        reply_markup=kb.get_request_location_keyboard(),
    )


@dp.message(F.location)
async def location_handler(message: Message):
    loc: Location = message.location
    data = await fetch_weather(loc.latitude, loc.longitude)
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    await message.answer(f"{desc}, {temp}°C")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
