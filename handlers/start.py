from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
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
    await message.answer(f"Привет, {message.from_user.first_name}!\n\n"
                         f"MangaBot - это телеграм-бот, разработанный для любителей манги.\n "
                         f"Он предоставляет широкий спектр функций, включая поиск манги по жанрам, "
                         f"получение информации о самых популярных и новых выпусках", reply_markup=keyboard)
