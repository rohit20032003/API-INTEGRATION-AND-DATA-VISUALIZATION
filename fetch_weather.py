import requests

API_KEY = "d383b5083a5975f2a8442420199881fd"  # Replace with your valid API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    """Fetch weather data for a city from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
