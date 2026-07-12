WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Slight Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm"
}


def get_weather_condition(code: int) -> str:
    return WEATHER_CODES.get(code, "Unknown")


def generate_advice(condition: str, temperature: float) -> str:

    condition = condition.lower()

    if "rain" in condition:
        return "Carry an umbrella before going out."

    if "thunderstorm" in condition:
        return "Avoid outdoor activities if possible."

    if temperature >= 35:
        return "It's extremely hot today. Stay hydrated and avoid prolonged exposure to the sun."

    if temperature >= 28:
        return "It's warm today. Wear light clothing and drink plenty of water."

    if temperature <= 18:
        return "It's quite cool today. Consider wearing a jacket."

    return "The weather looks pleasant. Have a great day!"