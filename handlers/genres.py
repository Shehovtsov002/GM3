from aiogram import Router, types, F
from aiogram.filters import Command

genres_router = Router()
genres = ["Приключения", "Фэнтези", "Драма", "Комедия", "Исекай", "Меха", "Ужасы"]


def get_genres_keyboard():
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


@genres_router.message(Command("genres"))
async def get_genres(message: types.Message):
    await message.answer(text="Выберите жанр из списка", reply_markup=get_genres_keyboard())


@genres_router.callback_query(F.data == "genres")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Выберите жанр из списка", reply_markup=get_genres_keyboard())


@genres_router.message(lambda message: message.text.lower() in [genre.lower() for genre in genres])
async def get_adventures(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(text=f"Какой-нибудь список с {message.text}", reply_markup=kb)
