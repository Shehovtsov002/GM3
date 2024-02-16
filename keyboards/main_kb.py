from aiogram import types


def start_keyboard():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Регистрация", callback_data="registration")
            ]
        ]
    )


def main_keyboard():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Жанры", callback_data="genres"),
                types.InlineKeyboardButton(text="Популярное", callback_data="popular")
            ],
            [
                types.InlineKeyboardButton(text="Новинки", callback_data="novelty"),
                types.InlineKeyboardButton(text="Рекомендации", callback_data="recommendations")
            ],
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://mangalib.me")
            ]
        ]
    )
