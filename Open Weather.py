import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15

        print(f"Weather in {city}: {weather_desc}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print("City not found or API error.")
        print("Details:", response.json())

if __name__ == "__main__":
    api_key = "5324fa9367df46ca01334c3dd0b1b25c"
    city_name = input("Enter municipality name: ")
    get_weather(api_key, city_name)
