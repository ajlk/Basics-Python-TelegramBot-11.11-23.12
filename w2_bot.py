import telebot
from datetime import datetime
from config_bot import TOKEN

bot = telebot.TeleBot(TOKEN)
states = {}


@bot.message_handler(func=lambda message: True)
def dispatcher(message):
    user_id = message.from_user.id
    current_user_state = states.get(user_id, "START")

    if current_user_state == "START":
        start_handler(message)
    else:  # current_user_state == "CITY":
        city_handler(message)


def start_handler(message):
    if message.text.lower() == "/start":
        bot.send_message(
            message.from_user.id,
            "Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?"
        )
        bot.send_message(
            message.from_user.id,
            """Если хочешь, можешь запросить погоду на конкретное число. Формат запроса: ГОРОД DD.MM.
Используя данный метод, ты можешь узнать погоду на сегодня, и даже заглянуть в будущее на целых три дня!
На данный момент я знаю погоду только для Москвы. Но я постоянно развиваюсь и становлюсь сообразительнее ;)"""
        )
        states[message.from_user.id] = "CITY"
    else:
        bot.send_message(message.chat.id, """Я тебя не понял.
Для того, чтобы я заработал, тебе нужно отправить команду
/start""")
        states[message.from_user.id] = "START"


def city_handler(message):
    # Проверка на случай, если пользователь решит начать всё с начала.
    if message.text.lower() == "/start":
        states[message.from_user.id] = "START"
        start_handler(message)
        exit()
    # ------------
    # ------------
    # Если пользователь указал дату, вся магия произойдёт здесь.
    try:
        day = int(message.text[-5:-3])
        month = int(message.text[-2:])
        is_date = 1
    except ValueError:
        is_date = 0

    if is_date == 1:
        delta = data_checker(day, month)
        if delta > 3:
            bot.send_message(message.from_user.id, """Так далеко в будущее я заглядывать пока не умею, попробуй 
изменить дату.
Ты всегда можешь начать сначала, отправив команду
 /start""")
        elif delta == 0:
            bot.send_message(message.from_user.id, "Сегодня отличная погода!")
            states[message.from_user.id] = "START"
        elif delta == 1:
            bot.send_message(message.from_user.id, "Завтра будет лучше, чем сегодня!")
            states[message.from_user.id] = "START"
        elif delta == 2:
            bot.send_message(message.from_user.id, "Послезавтра небесная канцелярия обещала дождь. Возможно с грозой.")
            states[message.from_user.id] = "START"
        else:
            bot.send_message(message.from_user.id,
                             f"{day}.{month} пасмурно, с прояснениями. +21")
            states[message.from_user.id] = "START"

    # ------------
    # ------------
    # Этот унылый кусок кода меня удручает. Примитивно и нежизнеспособно.
    else:
        if message.text.lower() == "москва":
            bot.send_message(message.from_user.id, "Сейчас отличная погода!")
            states[message.from_user.id] = "START"
        elif message.text.lower() == "москва завтра":
            bot.send_message(message.from_user.id, "Завтра ещё лучше чем сегодня!")
            states[message.from_user.id] = "START"
        else:
            bot.send_message(message.from_user.id, """Я тебя не понял, попробуй ввести название города ещё раз.
Ты всегда можешь начать сначала, отправив команду 
/start""")


def data_checker(day, month):
    now = datetime.now()
    then = datetime(now.year, month, day)
    delta = then.day - now.day
    if delta < 0:
        then = datetime(now.year + 1, month, day)
        delta = then.day - now.day
    return delta


bot.polling()
