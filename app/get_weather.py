import os
from http import HTTPStatus

import aiohttp

from app.core.config import get_settings
from app.db.crud.weather import CRUDWeather

settings = get_settings()

WEATHERMAP_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = settings.WEATHER_API_KEY

async def fetch_weather(city: str, session):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }

    async with aiohttp.ClientSession() as client:
        async with client.get(WEATHERMAP_URL, params=params) as resp:
            if resp.status == HTTPStatus.OK:
                result = await resp.json()
                description = (
                    f"В городе {city} сейчас {result['main']['temp']}°C, "
                    f"{result['weather'][0]['description']}. "
                    f"Ощущается как {result['main']['feels_like']}°C."
                )

                await CRUDWeather(session).create(city, description)
                return description

            return f"Ошибка при запросе погоды: {resp.status}"


# {
#   "coord": {
#     "lon": 37.6156,
#     "lat": 55.7522
#   },
#   "weather": [
#     {
#       "id": 804,
#       "main": "Clouds",
#       "description": "пасмурно",
#       "icon": "04d"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 8.13,
#     "feels_like": 6.23,
#     "temp_min": 7.24,
#     "temp_max": 8.15,
#     "pressure": 1005,
#     "humidity": 57,
#     "sea_level": 1005,
#     "grnd_level": 987
#   },
#   "visibility": 10000,
#   "wind": {
#     "speed": 3.06,
#     "deg": 218,
#     "gust": 6.31
#   },
#   "clouds": {
#     "all": 100
#   },
#   "dt": 1761739826,
#   "sys": {
#     "type": 2,
#     "id": 2095214,
#     "country": "RU",
#     "sunrise": 1761712147,
#     "sunset": 1761746232
#   },
#   "timezone": 10800,
#   "id": 524901,
#   "name": "Москва",
#   "cod": 200
# }