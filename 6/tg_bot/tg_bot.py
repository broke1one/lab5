import sqlite3
import telebot
from telebot import types


api = "6693379477:AAEDzGhFjv3Ixedwd_HgpUpKtPJtkHw0qRA"
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def start(message):

    print("Received start command")
    markup = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton('Выбрать город')
    markup.row(button_1)
    bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}! Данный бот поможет вам определиться, в каком заведении можно скоротать ваш досуг исходя из ваших предпочтений", reply_markup=markup)
    bot.register_next_step_handler(message, choice_city)


def choice_city(message):

    print(f"Received message: {message.text}")
    if message.text == 'Выбрать город':
        markup = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton("Минск", callback_data="Minsk")
        button_2 = types.InlineKeyboardButton("Брест", callback_data="Brest")
        button_3 = types.InlineKeyboardButton("Гродно", callback_data="Grodno")
        button_4 = types.InlineKeyboardButton("Гомель", callback_data="Gomel")
        button_5 = types.InlineKeyboardButton("Могилев", callback_data="Mogilev")
        button_6 = types.InlineKeyboardButton("Витебск", callback_data="Vitebsk")
       
        markup.row(button_1, button_2)
        markup.row(button_3, button_4)
        markup.row(button_5, button_6)

        bot.send_message(message.chat.id, "Выберите город, в котором находится: ", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data in ['Minsk', 'Brest', 'Grodno', 'Gomel', 'Mogilev', 'Vitebsk'])
def information_from_db(callback):

    print(f"Received callback query: {callback.data}")
    location = callback.data

    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        sql_query_2 = "SELECT * FROM institution WHERE location = ?"
        cursor.execute(sql_query_2, (location,))
        results = cursor.fetchall()

        markup = types.InlineKeyboardMarkup()
        for row in results:
            button = types.InlineKeyboardButton(row[1], callback_data=str(row[0]))
            markup.add(button)

        button = types.InlineKeyboardButton("🔙", callback_data="back")
        markup.add(button)
        bot.send_message(callback.message.chat.id, "Результаты по выбранному городу:", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data.isdigit())
def show_info(callback):

    institution_id = callback.data
    print(institution_id)

    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        sql_query = "SELECT * FROM institution WHERE id = ?"
        cursor.execute(sql_query, (int(institution_id),))
        result = cursor.fetchone()

        markup = types.InlineKeyboardMarkup()  
        button = types.InlineKeyboardButton("🔙", callback_data="back")
        markup.add(button)

        if result:
            info_message = f"Название заведения: {result[1]}\n\nАдрес:{result[4]}\n   \nОписание: {result[5]}"
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=info_message, reply_markup=markup)
        else:
            bot.send_message(callback.message.chat.id, "Заведение не найдено", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == "back")
def back_to_menu(callback):

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    choice_city(callback.message)


bot.infinity_polling()