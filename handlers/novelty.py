from aiogram import Router, types, F
from aiogram.filters import Command

novelty_router = Router()


@novelty_router.message(Command("novelty"))
async def get_genres(message: types.Message):
    await message.answer(text="Что-то из новенького")


@novelty_router.callback_query(F.data == "novelty")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Что-то из новенького")
