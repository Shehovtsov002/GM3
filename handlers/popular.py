from aiogram import Router, types, F
from aiogram.filters import Command

popular_router = Router()


@popular_router.message(Command("popular"))
async def get_genres(message: types.Message):
    await message.answer(text="Что-то из часто просматриваемого")


@popular_router.callback_query(F.data == "popular")
async def get_genres(callback: types.CallbackQuery):
    await callback.message.answer(text="Что-то из часто просматриваемого")
