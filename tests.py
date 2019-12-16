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
obs = owm.daily_forecast('London', )
w = obs.get_weather_at(f'{what_date[1].year}-{what_date[1].month}-{what_date[1].day} 12:00:00+00')
print(w)