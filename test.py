"""тестовый запуск бота"""
import telebot
from _token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am EchoBot.")


@bot.message_handler(func=lambda message: True)
def echo_welcome(message):
    bot.send_message(message.from_user.id,  text=message.text)


bot.polling()
