from aiogram import types


def get_houses_kb(houses):
    buttons = []
    for house in houses:
        button = [types.InlineKeyboardButton(text=house.get('title'), url=house.get('link'))]
        buttons.append(button)

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )

    return kb
