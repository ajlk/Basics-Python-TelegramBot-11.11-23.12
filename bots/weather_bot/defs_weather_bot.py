"""All possible functions"""

from datetime import datetime
import requests
import pyowm
from config_bot import TOKEN, OPEN_WEATHER_API_KEY

# локализация
owm = pyowm.OWM(OPEN_WEATHER_API_KEY, language='RU')


# смотрим расположение города
def location_details(city):
    city_location = owm.city_id_registry(city)

    if city_location.get_name():
        city_name = city_location.get_name()
    else:
        city_name = None

    if city_location.get_country():
        country_code = city_location.get_country()
    else:
        country_code = None
    return [city_name, country_code]


# смотрим погоду на сегодня
def current_weather(city):
    obs = owm.weather_at_place(city)
    return weather_details(obs)


# смотрим погоду на указанную дату
def forecast(city, date):
    obs = owm.three_hours_forecast(city)
    return weather_details(obs.get_forecast())


# определение средней температуры, направления и силы ветра, краткого дополнительного описания
def weather_details(w):
    city_weather = w.get_weather()

    if city_weather.get_temperature('celsius').get('temp'):
        temperature = city_weather.get_temperature('celsius').get('temp')
    else:
        temperature = None

    if city_weather.get_wind()['speed']:
        wind_speed = city_weather.get_wind()['speed']
    else:
        wind_speed = None

    if 'deg' in city_weather.get_wind():  # для некоторых городов направление ветра не указано
        compassSector = ["Северный ветер",
                         "Северный, северо-восточный ветер",
                         "Северо-восточный ветер",
                         "Восточный, северо-восточный ветер",
                         "Восточный ветер",
                         "Восточный, юго-восточный ветер",
                         "Юго-восточный ветер",
                         "Южный ветер",
                         "Южный, юго-западный ветер",
                         "Юго-западный ветер",
                         "Западный, юго-западный ветер",
                         "Западный ветер",
                         "Западный, северо-западный ветер",
                         "Северо-западный ветер",
                         "Северный, северо-западный ветер",
                         "Северный ветер"
                         ]
        wind_direction = compassSector[int(city_weather.get_wind()['deg'] / 22.5) - 1]
    else:
        wind_direction = None
    detailed_status = city_weather.get_detailed_status()
    # ===================================WEATHER-END===================================

    return [temperature, wind_direction, wind_speed, detailed_status.capitalize()]


# проверка даты
def date_checker(day, month):
    now = datetime.now()
    then = datetime(now.year, month, day)
    delta = then.day - now.day
    if delta < 0:
        then = datetime(now.year + 1, month, day)
        delta = then - now
        delta = delta.days
    return [delta, then]


# собираем ответ пользователю
def answer_constructor(the_city, weather):
    degree_sign = u'\N{DEGREE SIGN}'  # знак градуса

    city_details_string = f'Погода на сегодня для города {the_city.capitalize()}:\n'

    temperature = weather[0]
    if temperature is not None:
        temperature_string = f'Температура воздуха {temperature} {degree_sign}C;\n'
    else:
        temperature_string = ''
    wind_direction = weather[1]
    if wind_direction is not None:
        wind_direction_string = f'{wind_direction};\n'
    else:
        wind_direction_string = ''
    wind_speed = weather[2]
    if wind_speed is not None:
        wind_speed_string = f'Скорость ветра {wind_speed} м/с;\n'
    else:
        wind_speed_string = ''
    detailed_info = weather[3]
    if detailed_info is not None:
        detailed_info_string = f'{detailed_info}\n'
    else:
        detailed_info_string = ''

    the_message = f'{city_details_string}' \
                  f'{temperature_string}' \
                  f'{wind_direction_string}' \
                  f'{wind_speed_string}' \
                  f'{detailed_info_string}'
    return the_message
