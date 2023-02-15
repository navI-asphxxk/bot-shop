import telebot
from telebot import types

bot = telebot.TeleBot('5995969827:AAEHc4p9-gY0gE_b511y7rXADUAO_qWEcyI')


def main_menu():
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    info = types.KeyboardButton(text='📢Информация')
    helping = types.KeyboardButton(text='❓Помощь в выборе')
    katalog = types.KeyboardButton(text='🛍️Каталог')
    feedback = types.KeyboardButton(text='📩Отзывы')

    keyboard_menu.add(info)
    keyboard_menu.add(helping, katalog)
    keyboard_menu.add(feedback)

    return keyboard_menu


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_menu = main_menu()

    bot.send_message(message.chat.id, '<b>мы занимаемся доставкой оригинальной продукции '
                                      'всех самых популярных брендов: Nike, Adidas, Jordan, Gucci, '
                                      'Balenciaga и др. - с магазина Poizon. При нынешних ограничениях '
                                      'достать оригинальный товар проблематично, поэтому мы предоставляем '
                                      'свои услуги по низким ценам.</b>',
                     parse_mode='html', reply_markup=keyboard_menu)

    photo = open('photoPrivet.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=keyboard_menu)

bot.polling(none_stop=True)