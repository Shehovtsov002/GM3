from aiogram import types


# TODO: Get genres from db
genres = ["Приключения", "Фэнтези", "Драма", "Комедия", "Исекай", "Меха", "Ужасы"]


def types_keyboard():
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Манга", callback_data="Манга"),
            types.InlineKeyboardButton(text="Манхва", callback_data="Манхва"),
            types.InlineKeyboardButton(text="Маньхуа", callback_data="Маньхуа")
        ]
    ])
    return keyboard


def genres_keyboard():
    kb_buttons = []
    sub_list = []
    for genre in genres:
        kb_button = types.InlineKeyboardButton(
            text=genre,
            callback_data=genre
        )
        sub_list.append(kb_button)
        if len(sub_list) == 3:
            kb_buttons.append(sub_list)
            sub_list = []
    if sub_list:
        kb_buttons.append(sub_list)
    sub_list = [
        types.InlineKeyboardButton(
            text="Далее",
            callback_data="done"
        )
    ]
    kb_buttons.append(sub_list)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb_buttons)
    return keyboard
