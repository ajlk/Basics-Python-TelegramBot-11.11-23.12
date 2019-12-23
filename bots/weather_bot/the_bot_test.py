"""- Бот умеет смотреть погоду на сегодня для любого города. Ограничение: города, находящиеся за пределами России или
Белоруссии, должны быть заданы на английском языке. По всей видимости проблема вызвана неполной локализацией под
русский язык;
- Запросы реализованы через библиотеку pyowm;
- Использован API от OWM."""

from datetime import datetime

import keyboards_weather_bot as kb  # клавиатура
import pyowm
import telebot
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

    if 'deg' in w.get_wind():  # для некоторых городов направление ветра не указано
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


# Этот def ещё не готов
def forecast(city, what_date):
    obs = owm.daily_forecast()
    w = obs.get_weather_at(f'{what_date[1].year}-{what_date[1].month}-{what_date[1].day} 12:00:00+00')


def date_checker(day, month):
    now = datetime.now()
    then = datetime(now.year, month, day)
    delta = then.day - now.day
    if delta < 0:
        then = datetime(now.year + 1, month, day)
        delta = then.day - now.day
    return [delta, then]


@BOT.message_handler(commands=['help'])
def process_help_command(message):
    BOT.send_message(
        message.from_user.id,
        'Я - бот, помогающий узнать погоду в интересующем тебя городе.\n\nНеобходимо выбрать один из предложенных '
        'вариантов взаимодействия со мной.\n\nПосле выполнения каждого запроса ты снова должны выбрать погоду либо '
        'на сегодня, либо на определённую дату.'
    )


@BOT.message_handler(commands=['start'])
def process_start_command(message):
    BOT.send_message(
        message.from_user.id,
        "Привет! Это бот-погода. Я помогу узнать погоду в любом городе.\n\n"
        "Города, находящиеся за пределами России, должны быть написаны на английском языке.\n\n"
        "Выбери один из доступных вариантов:",
        reply_markup=kb.reply_kb)


@BOT.message_handler(func=lambda message: True)
def dispatcher(message):
    user_id = message.from_user.id
    current_user_state = states.get(user_id, "START")
    # ===============================================
    # 0 - параметр не определён;
    # 1 - погода на сегодня;
    # 2 - погода на определённую дату.
    check_type = 0
    # ===============================================
    if message.text == 'Начать сначала':
        states[message.from_user.id] = 'START'
        process_start_command(message)
    elif message.text == 'Погода на сегодня':
        check_type = 1
        states[message.from_user.id] = 'CITY'
    elif message.text == 'Погода на определённую дату':
        check_type = 2
        states[message.from_user.id] = 'CITY'
    else:
        if check_type == 0:
            BOT.send_message(
                message.from_user.id,
                'Я тебя не понял.\n'
                'Выбери один из предложенных вариантов.'
            )
        elif check_type == 1:
            try:
                weather = current_weather(message.text.lower())
            except pyowm.exceptions.api_response_error.NotFoundError:
                BOT.send_message(message.from_user.id, """Я тебя не понял, попробуй ввести название города ещё раз.
            Ты всегда можешь начать сначала, отправив команду 
            /start""")
                return


"""    if current_user_state == "START":
        start_handler(message)
    else:  # current_user_state == "CITY":
        city_handler(message)"""


def start_handler(message):
    if message.text.lower() == "/start":
        BOT.send_message(
            message.from_user.id,
            "Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?"
        )
        BOT.send_message(
            message.from_user.id,
            """Если хочешь, можешь запросить погоду на конкретное число. Формат запроса: ГОРОД DD.MM.
Используя данный метод, ты можешь узнать погоду на сегодня, и даже заглянуть в будущее на целых четыре дня!"""
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
        return
    # ------------
    # Смотрим, есть ли дата
    try:
        day = int(message.text[-5:-3])
        month = int(message.text[-2:])
        is_date = 1
    except ValueError:
        is_date = 0

    if is_date == 0:
        try:
            weather = current_weather(message.text.lower())
        except pyowm.exceptions.api_response_error.NotFoundError:
            BOT.send_message(message.from_user.id, """Я тебя не понял, попробуй ввести название города ещё раз.
Ты всегда можешь начать сначала, отправив команду 
/start""")
            return

    # =================================
    # Эта часть ещё не готова.
    if is_date == 1:
        what_date = date_checker(day, month)
        if what_date[0] > 4:
            BOT.send_message(message.from_user.id, """Так далеко в будущее я заглядывать не умею, попробуй 
изменить дату.
Ты всегда можешь начать сначала, отправив команду
/start""")
        else:
            try:
                weather = forecast(message.text.lower(), what_date)
            except pyowm.exceptions.api_response_error.NotFoundError:
                BOT.send_message(message.from_user.id, """Я тебя не понял, попробуй ввести название города ещё раз.
            Ты всегда можешь начать сначала, отправив команду 
            /start""")
                return
    # =================================

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


BOT.polling()
