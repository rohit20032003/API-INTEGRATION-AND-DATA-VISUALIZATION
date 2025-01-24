from fetch_weather import fetch_weather_data
from process_data import process_weather_data
from visualize_data import create_visualizations

def main():
    city = "India"  # Specify the city
    print(f"Fetching weather data for {city}...")

    # Fetch weather data
    data = fetch_weather_data(city)
    if data:
        # Process weather data
        weather_details = process_weather_data(data)
        if weather_details:
            temp, feels_like, humidity, weather_desc = weather_details

            # Print weather details
            print(f"Weather in {city}: {weather_desc.capitalize()}")
            print(f"Temperature: {temp}°C, Feels Like: {feels_like}°C, Humidity: {humidity}%")

            # Create visualizations
            create_visualizations(temp, feels_like, humidity, city)
        else:
            print("Error processing weather data.")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    main()
