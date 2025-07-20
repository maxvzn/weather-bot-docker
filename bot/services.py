import aiohttp
import os

async def fetch_weather(lat: float, lon: float) -> dict:
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={os.getenv('WEATHER_API_KEY')}"
        "&units=metric&lang=ru"
    )
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()