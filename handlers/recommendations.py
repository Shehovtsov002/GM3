from aiogram import Router, types, F
from aiogram.filters import Command

recommendations_router = Router()


@recommendations_router.message(Command("recommendations"))
async def get_genres(message: types.Message):
    await message.answer(text="Что-то на основе предпочтений")


@recommendations_router.callback_query(F.data == "recommendations")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Что-то на основе предпочтений")
