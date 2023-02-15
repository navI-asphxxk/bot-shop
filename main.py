import telebot
from telebot import types

bot = telebot.TeleBot('5995969827:AAEHc4p9-gY0gE_b511y7rXADUAO_qWEcyI')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    back = types.KeyboardButton(text='🔙Назад')
    menu = types.KeyboardButton(text='🏠Главное меню🏠')
    clear = types.KeyboardButton(text='🧹Очистить чат')
    keyboard_menu.add(menu, back, clear)

    bot.send_message(message.chat.id, 'Ваше приветствие',
                     parse_mode='html', reply_markup=keyboard_menu)


bot.polling(none_stop=True)