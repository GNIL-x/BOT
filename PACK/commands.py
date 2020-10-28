import telebot
from .keyboards import *
from .static import *
import time

bot = telebot.TeleBot('1187300252:AAFs7M494ADx4nEysrgiN-cZeSPKFmjJr8Q')


@bot.message_handler(commands=['start'])
def starty(message):
    bot.send_message(message.chat.id, 'privet, strannik', reply_markup=key1)


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'Это помощник', reply_markup=key2)
    bot.send_message(message.chat.id, message)


@bot.message_handler(content_types=['text'])
def texts(message):
    for i in list_of_mats:
        if i in message.text.split():
            bot.send_message(message.chat.id, 'Cам соси жопу')
            time.sleep(1)
            bot.edit_message_text('Хотя не...', message.chat.id, message.message_id + 1)
            time.sleep(1)
            bot.edit_message_text('Иди нахуй, быдло', message.chat.id, message.message_id + 1)
    for i in list_of_mails:
        if message.text.endswith(i):
            bot.send_message(message.chat.id, 'Вы отправили email')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'testcallback':
        bot.send_message(call.message.chat.id, f'{call.message.chat.id} \n username {call.from_user.username}')
        bot.send_message(call.message.chat.id, call)
