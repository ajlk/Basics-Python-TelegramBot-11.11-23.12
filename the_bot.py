"""Бот умеет смотреть погоду на сегодня для любого города. Ограничение: города, находящиеся не в России, должны быть
заданы на английском языке. По всей видимости проблема вызвана неполной локализацией под русский язык.
Запросы реализованы через библиотеку pyowm."""

import telebot
import pyowm
from datetime import datetime
from config_bot import TOKEN, OPEN_WEATHER_API_KEY

BOT = telebot.TeleBot(TOKEN)

states = {}
degree_sign = u'\N{DEGREE SIGN}'

# локализация
owm = pyowm.OWM(OPEN_WEATHER_API_KEY, language='RU')


# определение средней температуры, направления и силы ветра, краткого дополнительного описания
def weather_details(w):
    temperature = w.get_temperature('celsius').get('temp')
    wind_speed = w.get_wind()['speed']

    if 'deg' in w.get_wind():  # для некоторых городов скорость ветра не указана
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
        wind_direction = compassSector[int(w.get_wind()['deg'] / 22.5) - 1]
    else:
        wind_direction = None
    detailed_status = w.get_detailed_status()

    return [temperature, wind_direction, wind_speed, detailed_status.capitalize()]


# смотрим погоду на сегодня
def current_weather(city):
    obs = owm.weather_at_place(city)
    return weather_details(obs.get_weather())


@BOT.message_handler(func=lambda message: True)
def dispatcher(message):
    user_id = message.from_user.id
    current_user_state = states.get(user_id, "START")

    if current_user_state == "START":
        start_handler(message)
    else:  # current_user_state == "CITY":
        city_handler(message)


def start_handler(message):
    if message.text.lower() == "/start":
        BOT.send_message(
            message.from_user.id,
            "Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?"
        )
        BOT.send_message(
            message.from_user.id,
            """Если хочешь, можешь запросить погоду на конкретное число. Формат запроса: ГОРОД DD.MM.
Используя данный метод, ты можешь узнать погоду на сегодня, и даже заглянуть в будущее на целых три дня!"""
        )
        BOT.send_message(
            message.from_user.id,
            """Города, находящиеся за пределами России, должны быть написаны на английском языке."""
        )
        states[message.from_user.id] = "CITY"
    else:
        BOT.send_message(message.chat.id, """Я тебя не понял.
Для того, чтобы я заработал, тебе нужно отправить команду
/start""")
        states[message.from_user.id] = "START"


def city_handler(message):
    # Проверка на случай, если пользователь решит начать всё с начала.
    if message.text.lower() == "/start":
        states[message.from_user.id] = "START"

    # ------------
    # ------------
    # Если пользователь указал дату, вся магия произойдёт здесь.
    else:
        try:
            day = int(message.text[-5:-3])
            month = int(message.text[-2:])
            is_date = 1
        except ValueError:
            is_date = 0

        if is_date == 0:
            weather = current_weather(message.text.lower())
        if is_date == 1:
            delta = data_checker(day, month)

        # ===========================
        # Основной обработчик
        if weather[1] is None:
            message_1 = f'''Температура на сегодня в городе {message.text.lower().capitalize()} {weather[0]} {degree_sign}C; 
Скорость ветра {weather[2]} м/с;
{weather[3]}.'''
        else:
            message_1 = f'''Температура на сегодня в городе {message.text.lower().capitalize()} {weather[0]} {degree_sign}C; 
{weather[1]}, {weather[2]} м/с;
{weather[3]}.'''

        BOT.send_message(message.from_user.id, message_1)
        states[message.from_user.id] = "START"
    # ===========================


def data_checker(day, month):
    now = datetime.now()
    then = datetime(now.year, month, day)
    delta = then.day - now.day
    if delta < 0:
        then = datetime(now.year + 1, month, day)
        delta = then.day - now.day
    return delta


BOT.polling()
