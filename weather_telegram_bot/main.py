import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather):

    code_to_emoji = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather}"
        )
        data = r.json()

        weather_descr = data["weather"][0]["main"]
        if weather_descr in code_to_emoji:
            wd = code_to_emoji[weather_descr]

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp
        
        print(f"***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n"
              f"The weather in the {city}\nTemperature: {cur_weather} {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}\n Wind: {wind}\n"
              f"Sunrise: {sunrise_timestamp}\n Length of the day: {length_of_the_day}")

    except Exception as ex:
        print(ex)
        print("Check the name of the city")

def main():
    city = input("Write your city: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()