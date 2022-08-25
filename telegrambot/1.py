#5476128221:AAG4XVS_s6X_iKIf2LO94k2nVvs5oH9vPg8


import telebot
from telebot import types

token='5476128221:AAG4XVS_s6X_iKIf2LO94k2nVvs5oH9vPg8'
bot = telebot.TeleBot(token)


def create_keyboard():#создание кнопок
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')#1-номер кнопки
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    slip_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    smile_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')

    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(slip_btn)
    keyboard.add(smile_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('kak_pravilno_vybrat_vodu-1.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('1627001169_30-p-blini-s-fruktami-34.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('1647929019_17-kartinkin-net-p-progulka-kartinki-21.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка прогулка",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('dlc134hy7xc1n41erkqe33znp5x42jag.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка спать",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('original.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка шутка",
                reply_markup=keyboard)
            img.close()



if __name__=="__main__":
    bot.polling(none_stop=True)

