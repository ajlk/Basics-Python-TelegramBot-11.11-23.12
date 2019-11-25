import telebot

token = ""

bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == "/start":
        bot.send_message(
            message.chat.id,
            "Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?"
        )
    elif message.text == "Москва":
        bot.send_message(
            message.chat.id,
            "Сейчас отличная погода!"
        )
    elif message.text == "Москва завтра":
        bot.send_message(
            message.chat.id,
            "Завтра еще лучше!"
        )
    elif message.text == "Мордор":                      # Пасхалка
        bot.send_message(
            message.chat.id,
            "В Мордоре всегда збс. Ждём в гости с печеньками и винишком!"
        )
    else:
        bot.send_message(
            message.chat.id,
            "Я тебя не понял"
        )


bot.polling()
