from pydantic import BaseModel


class Location(BaseModel):
    city: str
    country: str


class Weather(BaseModel):
    temperature: float
    humidity: int
    wind_speed: float
    condition: str


class WeatherResponse(BaseModel):
    location: Location
    weather: Weather
    advice: str