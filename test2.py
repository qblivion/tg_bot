"""тестовый запуск бота"""
import telebot
from _token import token
import mc_speach
import settings

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help', 'info'])
def command_helper(message):
    if message.text == '/start':
        bot.send_message(chat_id=message.from_user.id, text="Hi " + message.from_user.first_name + ", i'm testBot. "
                                                                                                   "Send /help to get "
                                                                                                   "help")
    if message.text == '/help':
        bot.reply_to(message, text="It is still hard for me to perceive your messages, "
                                   "please be patient. Try to send me a text or photo. "
                                   "\nActual commands: "
                                   "  /text_to_voice   /info. \nAll questions to my creator: "
                                   "@qblivion. ")
    if message.text == '/info':
        bot.reply_to(message, text="Current language is " + settings.language)


@bot.message_handler(commands=['text_to_voice', 'en', 'ru'])
def tts_mode(message):
    if message.text == '/text_to_voice':
        bot.send_message(chat_id=message.from_user.id, text="Great! You choose text to speech mode. Send me message "
                                                            "and i will convert it to voice. Supported languages /ru"
                                                            "  /en")
    if message.text == '/en':
        bot.send_message(chat_id=message.from_user.id, text="You have chosen English. Send a message for voiceover")
        settings.language = 'en'
    if message.text == '/ru':
        bot.send_message(chat_id=message.from_user.id, text="Вы выбрали русский язык. Отправьте сообщение для озвучки")
        settings.language = 'ru'


@bot.message_handler(func=lambda m: True)
def final_tts(message):
    if settings.language == 'ru':
        mc_speach.Say_my_name(myText=message.text, language='ru')
    if settings.language == 'en':
        mc_speach.Say_my_name(myText=message.text, language='en')
    audio = open('output.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()


bot.polling()
