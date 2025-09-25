import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return {"error": "City not found or API error."}

if __name__ == "__main__":
    print("🌦️ Simple Weather App 🌦️")
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter a city name: ")
    weather = get_weather(city, api_key)

    if "error" in weather:
        print(weather["error"])
    else:
        print(f"Weather in {weather['city']}: {weather['temperature']}°C, {weather['description']}")
