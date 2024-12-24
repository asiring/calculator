import telebot
from telebot import types

TOKEN = ' '
bot = telebot.TeleBot(token=TOKEN)

def generate_kb(number):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text= f'Добавить 1', callback_data=f'number_{number+1}'))
    markup.add(types.InlineKeyboardButton(text=f'Отнять 1', callback_data=f'number_{number - 1}'))
    markup.add(types.InlineKeyboardButton(text=f'Обнулить счет', callback_data='number_0'))
    return markup

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,
                     'Текущая сумма: 0',
                     reply_markup=generate_kb(0))

@bot.callback_query_handler(func = lambda call: call.data.startswith('number_'))
def number_handler(call):
    current_number = int(call.data.split('_')[1])
    bot.edit_message_text(f'Текущее число: {current_number}',
                          chat_id= call.message.chat.id,
                          message_id=call.message.message_id,
                          reply_markup=generate_kb(current_number))
bot.infinity_polling()

