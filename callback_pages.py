import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

import data
import json

bot = telebot.TeleBot('5995969827:AAEHc4p9-gY0gE_b511y7rXADUAO_qWEcyI')
def callback_shoes_pages(call):
    req = call.data.split('_')
    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # Обработка кнопок - вперед и назад
    elif 'pagination' in req[0]:
        # Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
        # Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        # markup для первой страницы
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))

        # markup для второй страницы
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))

        # markup для остальных страниц
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))


        markup.add(InlineKeyboardButton(text=f'{data.shoes_price_pages[page - 1]}руб - Купить', callback_data='buy'))
        bot.edit_message_text(f' {data.shoes_name_pages[page-1]} ', reply_markup=markup, chat_id=call.message.chat.id,
                              message_id=call.message.message_id)