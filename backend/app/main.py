from fastapi import FastAPI

from app.api.weather import router as weather_router

app = FastAPI(
    title="Smart Weather Assistant API",
    description="""
A simple REST API that provides current weather information
for any supported city using the Open-Meteo API.

Features:
- Current weather
- Smart weather advice
- Clean JSON responses
""",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Weather Assistant API"
    }


app.include_router(weather_router)