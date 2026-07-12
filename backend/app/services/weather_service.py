import httpx

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

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get current weather
        weather_response = await client.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
            }
        )

        weather_data = weather_response.json()

        current = weather_data["current"]

        return {
            "city": location["name"],
            "country": location["country"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
        }