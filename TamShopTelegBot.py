import telebot
from telebot import types

bot = telebot.TeleBot('6593665838:AAEc7nT7jDupea2TObZILqNbG87O3WX0Z5U')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
#    btn1 = types.KeyboardButton('Перейти на сайт')
#    markup.row(btn1)
#    btn2 = types.KeyboardButton('Удалить фото')
#    btn3 = types.KeyboardButton('Добавить описание и пояснения.')
#    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, Перетащите в чат фото товара, который вы бы хотели купить. Мы подберём вам его или максимально близкий и предложим цену с доставкой из Китая', reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.avito.ru/user/2dfcbe5a3bfc27a6cad279df3359ccbf/profile/all?src=fs&page_from=from_favorite_sellers&sellerId=2dfcbe5a3bfc27a6cad279df3359ccbf')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Добавить описание и пояснения.', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Ваше фото принято к рассмотрению. Скоро мы вернёмся с ответом. А пока, ознакомьтесь, пожалуйста с нашим каталогом', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)
