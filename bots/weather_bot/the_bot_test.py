"""- Бот умеет смотреть погоду на сегодня для любого города. Ограничение: города, находящиеся за пределами России или
Белоруссии, должны быть заданы на английском языке. По всей видимости проблема вызвана неполной локализацией под
русский язык;
- Запросы реализованы через библиотеку pyowm;
- Использован API от OWM."""

from config_bot import TOKEN, OPEN_WEATHER_API_KEY

import keyboards_weather_bot as kb  # клавиатура
import defs_weather_bot as defs  # проверка погоды
import telebot
import pyowm

BOT = telebot.TeleBot(TOKEN)

states = {}
degree_sign = u'\N{DEGREE SIGN}'


@BOT.message_handler(commands=['help'])
def process_help_command(message):
    BOT.send_message(
        message.from_user.id,
        'Я - бот, помогающий узнать погоду в интересующем тебя городе.\n\n'
        'Необходимо выбрать один из предложенных '
        'вариантов взаимодействия со мной.\n\n'
        'После выполнения каждого запроса ты снова должны выбрать погоду либо на сегодня, либо на определённую дату.'
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

    if message.text == 'Начать сначала':
        states[message.from_user.id] = 0
        process_start_command(message)
        return

    current_user_state = states.get(user_id, 0)
    # ===============================================
    # 0 - параметр не определён;
    # 1 - погода на сегодня;
    # 2 - погода на определённую дату.
    # ===============================================

    # =============ОПРЕДЕЛЯЕМ ПАРАМЕТР ЗАПРОСА============= #
    if current_user_state == 0:
        if message.text == 'Погода на сегодня':
            states[message.from_user.id] = 1
            BOT.send_message(
                message.from_user.id,
                'Для какого города ты хотел бы узнать погоду на сегодня?'
            )
        elif message.text == 'Погода на определённую дату':
            states[message.from_user.id] = 2
            BOT.send_message(
                message.from_user.id,
                'Какой город и какая дата тебя интересуют?\n\n'
                'Формат запроса: ГОРОД DD.MM\n\n'
                'Запрашиваемая дата не может быть позднее 16-ти дней от текущей.'
            )
        else:
            BOT.send_message(
                message.from_user.id,
                'Я тебя не понял.\n'
                'Выбери один из предложенных вариантов:'
            )
            return
    # =============КОНЕЦ ОПРЕДЕЛЕНИЯ ПАРАМЕТРА ЗАПРОСА============= #

    if current_user_state != 0:
        city_handler(message, current_user_state)


def city_handler(message, user_state):
    if user_state == 1:
        try:
            weather = defs.current_weather(message.text.lower())
        except pyowm.exceptions.api_response_error.NotFoundError:
            BOT.send_message(
                message.from_user.id,
                'Я тебя не понял. Попробуй ввести название города ещё раз.'
            )
            return
        the_city = message.text.lower()
    else:  # user_state==2
        # =======================================
        # Проверяем корректность введённой даты
        try:
            day = int(message.text[-5:-3])
            month = int(message.text[-2:])
        except ValueError:
            BOT.send_message(
                message.from_user.id,
                'Формат даты неверен.\n'
                'Попробуй ещё раз.'
            )
            return

        the_date = defs.date_checker(day, month)
        if the_date[0] > 5:
            BOT.send_message(
                message.from_user.id,
                'Запрашиваемая дата выходит за допустимые пределы.\n\n'
                'Пожалуйста введи другую дату, лежащую в пределах 5-ти дней от текущей.'
            )
            return
        # =======================================

        try:
            weather = defs.forecast(message.text[:-5].lower(), the_date)
        except pyowm.exceptions.api_response_error.NotFoundError:
            BOT.send_message(
                message.from_user.id,
                'Я тебя не понял. Попробуй ввести название города ещё раз.'
            )
            return
    # ===========================
    # Основной обработчик
    the_message = defs.answer_constructor(the_city, weather)

    BOT.send_message(message.from_user.id, the_message)
    states[message.from_user.id] = 0  # обнуление состояния


# ===========================


BOT.polling()
