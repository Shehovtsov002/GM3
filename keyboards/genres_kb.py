from aiogram import types


# TODO: Get genres from db
genres = ["Приключения", "Фэнтези", "Драма", "Комедия", "Исекай", "Меха", "Ужасы"]


def genres_keyboard():
    kb_buttons = []
    sub_list = []
    for genre in genres:
        kb_button = types.KeyboardButton(
            text=genre,
            callback_data=genre.lower()
        )
        sub_list.append(kb_button)
        if len(sub_list) == 2:
            kb_buttons.append(sub_list)
            sub_list = []
    if sub_list:
        kb_buttons.append(sub_list)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_buttons)
    return keyboard
