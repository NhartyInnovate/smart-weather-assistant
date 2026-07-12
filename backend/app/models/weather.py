from pydantic import BaseModel

class Measurement(BaseModel):
    value: float
    unit: str

class Location(BaseModel):
    city: str
    country: str


class Weather(BaseModel):
    temperature: Measurement
    humidity: Measurement
    wind_speed: Measurement
    condition: str


class WeatherResponse(BaseModel):
    location: Location
    weather: Weather
    advice: str