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
            data = await resp.json()
            return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "desc": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"]
            }