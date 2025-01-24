import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city, api_key):
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

