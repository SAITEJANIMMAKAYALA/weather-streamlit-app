from weather.api_handler import get_weather

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)

    if 'error' in weather_data:
        print("Error:", weather_data['error'])
    else:
        print("\nWeather in", weather_data['name'])
        print("Temperature:", weather_data['main']['temp'], "°C")
        print("Feels like:", weather_data['main']['feels_like'], "°C")
        print("Condition:", weather_data['weather'][0]['description'].capitalize())
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Wind Speed:", weather_data['wind']['speed'], "m/s")
