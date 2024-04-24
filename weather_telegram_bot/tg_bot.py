import requests
import datetime
from config import tg_bot_token, open_weather_token
import telebot

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["weather"])
    def start_message(message):
        bot.send_message(message.chat.id, "Write a name of the city and I will give you a weather forecast")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
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
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}"
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

        except Exception as ex:
            bot.send_message(
                message.chat.id,
                f"Check the name of the city {message.text}"
            )
            print(ex)
            print("Check the name of the city")

        try:
            bot.send_message(
                message.chat.id,
                f"***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n"
                f"The weather in the {message.text}\nTemperature: {cur_weather} {wd}\n"
                f"Humidity: {humidity}\nPressure: {pressure}\n Wind: {wind}\n"
                f"Sunrise: {sunrise_timestamp}\n Length of the day: {length_of_the_day}"
            )
        except Exception as ex:
            print(ex)
            bot.send_message(
                message.chat.id,
                "Something went wrong"
            )

    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(tg_bot_token)