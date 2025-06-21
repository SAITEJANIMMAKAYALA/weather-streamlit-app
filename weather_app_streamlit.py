import streamlit as st
from weather.api_handler import get_weather

st.title("🌤️ Weather App")

city = st.text_input("Enter city name:")

if city:
    weather_data = get_weather(city)

    if 'error' in weather_data:
        st.error(weather_data['error'])
    else:
        st.subheader(f"Weather in {weather_data['name']}")
        st.write(f"🌡 Temperature: {weather_data['main']['temp']} °C")
        st.write(f"🤒 Feels like: {weather_data['main']['feels_like']} °C")
        st.write(f"🌥 Condition: {weather_data['weather'][0]['description'].capitalize()}")
        st.write(f"💧 Humidity: {weather_data['main']['humidity']}%")
        st.write(f"🌬 Wind Speed: {weather_data['wind']['speed']} m/s")
