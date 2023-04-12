from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/test1')
button2 = KeyboardButton('/test2')
button3 = KeyboardButton('/test3')
button4 = KeyboardButton('/contact', request_contact=True)
button5 = KeyboardButton('/location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# one_time_keyboard = True Прятать клавиатуру после нажатия.

kb_client.add(button3).add(button1).add(button2).row(button4, button5)  # каждое добавление с новой строки
# insert - добавляет если есть место
# row(a, b, c) - добавление всего в одну строку
