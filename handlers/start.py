from aiogram import Router, types
from aiogram.filters import Command
from keyboards.main_kb import main_keyboard, start_keyboard
from bot import db

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = start_keyboard()
    greetings = (f"Привет, {message.from_user.first_name}!\n\n"
                 f"MangaBot - это телеграм-бот, разработанный для любителей манги.\n"
                 f"Он предоставляет широкий спектр функций, включая поиск манги по жанрам, "
                 f"получение информации о самых популярных и новых выпусках!\n\n"
                 f"Чтобы воспользоваться всеми функциями бота необходимо пройти "
                 f"простенькую регистрацию")
    # Add registration check
    if db.get_user(message.from_user.id):
        keyboard = main_keyboard()
        greetings = f"И так, {message.from_user.first_name}, чем займемся?"
    await message.answer(text=greetings, reply_markup=keyboard)
