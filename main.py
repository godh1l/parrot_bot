import telebot
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! С этого момента я буду повторять всё, что ты мне напишешь')

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, 'Буду ждать тебя снова, прощай')

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
