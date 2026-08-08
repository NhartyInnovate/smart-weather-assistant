from fastapi import APIRouter, HTTPException
from app.models.weather import WeatherResponse

from app.services.weather_service import get_weather

router = APIRouter()


@router.get(
    "/weather",
    response_model=WeatherResponse,
    summary="Get current weather by city",
    description="Returns the current weather conditions and a simple recommendation."
)
async def weather(city: str):

    result = await get_weather(city)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"No weather information found for '{city}'."
        )

    return result