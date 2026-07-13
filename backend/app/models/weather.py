from pydantic import BaseModel


class Measurement(BaseModel):
    value: float
    unit: str


class Location(BaseModel):
    city: str
    country: str
    timezone: str


class Weather(BaseModel):
    temperature: Measurement
    humidity: Measurement
    wind_speed: Measurement
    condition: str
    weather_code: int
    is_day: bool

class Metadata(BaseModel):
    local_time: str
    last_updated: str
class WeatherResponse(BaseModel):
    location: Location
    weather: Weather
    advice: str
    metadata: Metadata