from fastapi import FastAPI

from app.api.weather import router as weather_router

app = FastAPI(
    title="Smart Weather Assistant API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Weather Assistant API"
    }


app.include_router(weather_router)