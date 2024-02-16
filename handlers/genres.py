from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.genres_kb import genres_keyboard
from bot import db

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
    await message.answer(text=f"{titles}")
    if not titles:
        await message.answer(text="Для этого жанра пока не добавлен ни один тайтл")
        return
    for title in titles:
        await message.answer(text=f"Image: {title['image']}\n"
                                  f"Name: {title['name']}\n"
                                  f"Description: {title['description']}", reply_markup=kb)
