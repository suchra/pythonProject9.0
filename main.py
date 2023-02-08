import telebot

bot = telebot.TeleBot('5994187663:AAHXkQARYqJTCd-6MheCOLCUxzAGuzcHl5g')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я телеграмм бот!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, как твои дела?')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id, 'Я рад это слышать!')

bot.polling()