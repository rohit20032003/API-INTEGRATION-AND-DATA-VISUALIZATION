from fetch_weather import fetch_weather_data
from process_data import process_weather_data
from visualize_data import create_visualizations

def main():
    city = "India"  # Specify the city or country
    api_key = "8953e3ced96a15b85a35e94531721eec"  # Replace with your actual API key
    print(f"Fetching weather data for {city}...")
    
    try:
        weather_data = fetch_weather_data(city, api_key)
        temp, feels_like, humidity, weather_desc = process_weather_data(weather_data)
        create_visualizations(temp, feels_like, humidity, city)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
