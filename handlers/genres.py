from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.genres_kb import (
    genres_keyboard,
    genres
)

genres_router = Router()


@genres_router.message(Command("genres"))
async def get_genres(message: types.Message):
    await message.answer(text="Выберите жанр из списка", reply_markup=genres_keyboard())


@genres_router.callback_query(F.data == "genres")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Выберите жанр из списка", reply_markup=genres_keyboard())


@genres_router.message(lambda message: message.text.lower() in [genre.lower() for genre in genres])
async def get_adventures(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer(text=f"Какой-нибудь список с {message.text}", reply_markup=kb)
