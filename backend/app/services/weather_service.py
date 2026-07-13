import httpx
from app.utils.weather_utils import (
    get_weather_condition,
    generate_advice,
)
from datetime import datetime
from zoneinfo import ZoneInfo


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


async def get_weather(city: str):
    async with httpx.AsyncClient(timeout=10) as client:

        # Step 1: Get city coordinates
        geo_response = await client.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1
            }
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            return None

        location = geo_data["results"][0]

        timezone = location["timezone"]

        local_time = datetime.now(
            ZoneInfo(timezone)
        ).isoformat(timespec="minutes")

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get current weather
        weather_response = await client.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code,is_day"
            }
        )

        weather_data = weather_response.json()

        current = weather_data["current"]

        condition = get_weather_condition(current["weather_code"])

        advice = generate_advice(
            condition,
            current["temperature_2m"]
        )

        return {
            "location": {
                "city": location["name"],
                "country": location["country"],
                "timezone": timezone,
            },
            "weather": {
                "temperature": {
                    "value": current["temperature_2m"],
                    "unit": "°C",
                },
                "humidity": {
                    "value": current["relative_humidity_2m"],
                    "unit": "%",
                },
                "wind_speed": {
                    "value": current["wind_speed_10m"],
                    "unit": "km/h",
                },
                "condition": condition,
                "weather_code": current["weather_code"],
                "is_day": bool(current["is_day"]),
            },
            "advice": advice,
            "metadata": {
                "local_time": local_time,
                "last_updated": local_time,
            },
        }