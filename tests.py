import requests
import telebot
import pyowm

from config_bot import TOKEN, OPEN_WEATHER_API_KEY

current_weather_url = 'http://api.openweathermap.org/data/2.5/weather'
month_forecast_url = 'https://pro.openweathermap.org/data/2.5/climate/month'

BOT = telebot.TeleBot(TOKEN)
# OWM = OPEN_WEATHER_API_KEY

# локализация
owm = pyowm.OWM(OPEN_WEATHER_API_KEY, language='RU')

states = {}

"""params = {
    'q': input('City name '),
    'appid': OWM
}"""

obs = owm.weather_at_place(input('Какой город интересует? '))
w = obs.get_weather()
a = w.get_temperature('celsius')
b = w.get_temperature('celsius').get('temp')
c = w.get_detailed_status()
d = w.get_wind()
e = w.get_wind()['speed']

compassSector = ["северный",
                 "северный, северо-восточный",
                 "северо-восточный",
                 "восточный, северо-восточный",
                 "восточный",
                 "восточный, юго-восточный",
                 "юго-восточный",
                 "южный",
                 "южный, юго-западный",
                 "юго-западный",
                 "западный, юго-западный",
                 "западный",
                 "западный, северо-западный",
                 "северо-западный",
                 "северный, северо-западный",
                 "северный"
                 ]

wind_direction = compassSector[int(-5 / 22.5) - 1]

print(compassSector[5])

# res = (requests.get(current_weather_url, params=params)).json()
print(w)
print(a)
print(b)
print(c.capitalize())
print(d)
print(e)
print(wind_direction)
"""for key, value in res.items():
    if key == 'found':
        if res[key]:
            print('Interesting')
        else:
            print('Boring')"""
