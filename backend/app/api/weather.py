from fastapi import APIRouter, HTTPException

from app.services.weather_service import get_weather

router = APIRouter()


@router.get("/weather")
async def weather(city: str):

    result = await get_weather(city)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="City not found."
        )

    return result