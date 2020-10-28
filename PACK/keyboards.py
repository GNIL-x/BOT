import telebot

key1 = telebot.types.ReplyKeyboardMarkup(True, True)
key1.row('/start')
key1.row('/help')
key2 = telebot.types.InlineKeyboardMarkup()
key2.add(telebot.types.InlineKeyboardButton('команда1', url='Google.com'))
key2.add(telebot.types.InlineKeyboardButton('callback', callback_data='testcallback'))
