import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import json

from telegram_bot_pagination import InlineKeyboardPaginator

import callback_pages
import text_pages

bot = telebot.TeleBot('5995969827:AAEHc4p9-gY0gE_b511y7rXADUAO_qWEcyI')


def main_menu():
    # Кол-во позиций в меню клавиатуры - много
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    info = types.KeyboardButton(text='📢Информация')
    helping = types.KeyboardButton(text='❓Помощь в выборе')
    katalog = types.KeyboardButton(text='🛍️Каталог')
    feedback = types.KeyboardButton(text='📩Отзывы')

    keyboard_menu.add(info)
    keyboard_menu.add(helping, katalog)
    keyboard_menu.add(feedback)

    return keyboard_menu


def katalog_menu():
    # Кол-во позиций в меню клавиатуры - много
    katalog_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    shoes = types.KeyboardButton(text='Обувь')
    clothes = types.KeyboardButton(text='Одежда')
    accessories = types.KeyboardButton(text='Аксессуары')
    back = types.KeyboardButton(text='Назад')

    katalog_menu.add(shoes, clothes, accessories)
    katalog_menu.add(back)

    return katalog_menu


@bot.message_handler(commands=['start'])
def start(message):

    photo = open('photoPrivet.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=main_menu())

    bot.send_message(message.chat.id, '<b>мы занимаемся доставкой оригинальной продукции '
                                      'всех самых популярных брендов: Nike, Adidas, Jordan, Gucci, '
                                      'Balenciaga и др. - с магазина Poizon. При нынешних ограничениях '
                                      'достать оригинальный товар проблематично, поэтому мы предоставляем '
                                      'свои услуги по низким ценам.</b>',
                     parse_mode='html', reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    # исправляет значок загрузки
    if call.message:
        bot.answer_callback_query(callback_query_id=call.id)

        # Удаление последнего сообщения бота
        if call.data == "cancel":
            keyboard_menu = main_menu()

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text='cancel', parse_mode='html', reply_markup=keyboard_menu)
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text='cancel')

        # Удаление 2х последних сообщений бота
        if call.data == "cancell":
            keyboard_menu = main_menu()

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_message(call.message.chat.id, text='cancel', parse_mode='html', reply_markup=keyboard_menu)

        callback_pages.callback_shoes_pages(call)
        callback_pages.callback_clothes_pages(call)
        callback_pages.callback_accesory_pages(call)

        if call.data == "buy":
            bot.send_message(call.message.chat.id,
                             text='<b>тиньк</b> 12345678\n'
                                  'после оплаты - @asphxxk',
                             parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == '📢Информация':
        # фотка инфы
        info = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancell")
        info.add(cancel)

        photo = open('photoInfo.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)

        # кнопка отмены, чтобы не спамить, удаляет 2 сообщения

        bot.send_message(message.chat.id, text='<b>1.	Что такое POIZON и зачем заказывать из Китая?</b>\n'
                                               'POIZON(DeWu)- китайский магазин ОРИГИНАЛЬНЫХ брендов. '
                                               'При нынешних введенных ограничениях, это звучит очень интересно,'
                                               ' а учитывая стоимость, которая НИЖЕ чем в РФ НА 30-40%...',
                         parse_mode='html', reply_markup=info)

    if message.text == '❓Помощь в выборе':
        helping = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancel")
        helping.add(cancel)
        bot.send_message(message.chat.id, text='<i>Помощь в выборе товара -</i>\n'
                                               ' @asphxxk', parse_mode='html', reply_markup=helping)

    if message.text =='📩Отзывы':
        feedback = types.InlineKeyboardMarkup()
        feed = types.InlineKeyboardButton("Отзывы", url="https://otzovik.com/lastreviews")
        cancel = types.InlineKeyboardButton("❌Отмена", callback_data="cancel")
        feedback.add(feed)
        feedback.add(cancel)
        bot.send_message(message.chat.id, text='здесь вы можете ознакомиться с отзывами',
                         parse_mode='html', reply_markup=feedback)

    if message.text == '🛍️Каталог':
        # категории в каталоге в меню клавиатуры, прикреплены к фото
        photo = open('photoKatalog.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=katalog_menu())

        bot.send_message(message.chat.id, text='Каталог товаров',
                         parse_mode='html')

    if message.text == 'Назад':
        # категории в каталоге в меню клавиатуры, прикреплены к фото

        bot.send_message(message.chat.id, text='back',
                         parse_mode='html', reply_markup=main_menu())

    if message.text == 'Обувь':
        text_pages.text_shoes_pages(message)

    if message.text == 'Одежда':
        text_pages.text_clothes_pages(message)

    if message.text == 'Аксессуары':
        text_pages.text_accesory_pages(message)


# def callback_shoes_pages(call):


# def start_shoes_pages(m):


bot.polling(none_stop=True)
