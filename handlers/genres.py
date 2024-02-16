from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.genres_kb import genres_keyboard, title_keyboard
from bot import db
import os

genres_router = Router()
genres = db.get_genres()


@genres_router.message(Command("genres"))
async def get_genres(message: types.Message):
    await message.answer(text="Выберите жанр из списка", reply_markup=genres_keyboard())


@genres_router.callback_query(F.data == "genres")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Выберите жанр из списка", reply_markup=genres_keyboard())


@genres_router.message(lambda message: message.text in genres)
async def get_titles(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    titles = db.get_titles(message.text)
    if not titles:
        await message.answer(text="Для этого жанра пока не добавлен ни один тайтл")
        return
    for title in titles:
        await message.answer_photo(caption=f"{title['type']}: {title['name']}\n"
                                        f"Жанр: {title['genre']}\n"
                                        f"Описание: {title['description']}",
                                   reply_markup=title_keyboard(title['url']),
                                   photo=types.FSInputFile(title['image']))

