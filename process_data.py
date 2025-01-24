def process_weather_data(data):
    """Extract relevant weather details."""
    try:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        return temp, feels_like, humidity, weather_desc
    except KeyError as e:
        print(f"Error processing data: Missing key {e}")
        return None
