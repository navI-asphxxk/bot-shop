import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import data

bot = telebot.TeleBot('5995969827:AAEHc4p9-gY0gE_b511y7rXADUAO_qWEcyI')


def count_pages(arr):
    count = 0
    for i in arr:
        count += 1

    return count


def text_shoes_pages(message):
    count = count_pages(data.shoes_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"shoes\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.shoes_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/shoesPages/{page}.jpg', 'rb'),
                   caption=f'{data.shoes_name_pages[0]}', reply_markup=markup)
    # bot.send_message(message.from_user.id, f'{data.shoes_name_pages[0]}', reply_markup=markup)


def text_clothes_pages(message):
    count = count_pages(data.clothes_name_pages)
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->',
                                    callback_data="{\"method\":\"clothes\",\"NumberPage\":" + str(
                                        page + 1) + ",\"CountPage\":" + str(count) + "}"))
    markup.add(InlineKeyboardButton(text=f'{data.clothes_price_pages[page - 1]}руб - Купить', callback_data='buy'))

    bot.send_photo(message.chat.id, open(f'pages/clothesPages/{page}.jpg', 'rb'),
                   caption=f'{data.clothes_name_pages[0]}', reply_markup=markup)

