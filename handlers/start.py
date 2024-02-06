from aiogram import Router, types
from aiogram.filters import Command
from bot import commands

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n\n{commands}")
