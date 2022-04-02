import telebot
from telebot import types

bot = telebot.TeleBot('5105614333:AAFfStT7dnY91GSNQR2h_oy034p4UxuapTU')

@bot.message_handler(commands=['start'])
def start_and_help(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="button 1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button 2")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/'))
    bot.send_message(
        message.chat.id,
        'Если есть предложения по изменению бота, свяжитесь с разработчиком.',
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    print(call)
    if call.data == "button 1":
        bot.send_message(call.message.chat.id, "Нажали на первую кнопку")
    if call.data == "button 2":
        bot.send_message(call.message.chat.id, "Нажали на вторую кнопку")


@bot.message_handler(content_types=['text'])
def echo(message):
    user = message.chat.id
    img = open('.')
    bot.send_message(user, message.text)



bot.polling()