import requests

def fetch_weather_data(city_name, api_key):
    """
    Fetch weather data for a specified city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    print("Generated URL:", url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to fetch weather data.")
        print("Response:", response.text)  
        return None

def display_weather_data(weather_data, unit):
    """
    Display weather information to the user.
    """
    if weather_data:
        print("\nCurrent Weather Conditions:")
        print(f"Location: {weather_data['name']}")
        temperature = weather_data['main']['temp']
        if unit == 'C':
            temperature = round(temperature - 273.15, 2)
            unit_str = '°C'
        else:
            temperature = round((temperature - 273.15) * 9/5 + 32, 2)
            unit_str = '°F'
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_desc = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature} {unit_str}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather: {weather_desc}")
    else:
        print("No weather data available.")

def main():
    api_key = "YOUR_API_KEY" 
    unit = input("Choose temperature unit (C/F): ").upper()
    while unit not in ['C', 'F']:
        print("Invalid unit. Please choose C or F.")
        unit = input("Choose temperature unit (C/F): ").upper()
    city_name = input("Enter city name: ")
    weather_data = fetch_weather_data(city_name, api_key)
    display_weather_data(weather_data, unit)

if __name__ == "__main__":
    main()
