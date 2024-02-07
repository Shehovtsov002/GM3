from aiogram import Router, types
from aiogram.filters import Command
from .picture import get_random_pic


info_router = Router()


@info_router.message(Command("myinfo"))
async def info_command(message: types.Message):
    await message.answer_photo(photo=get_random_pic(),
                               caption=f"Ваш id: {message.from_user.id}\n"
                                       f"Звать вас: {message.from_user.first_name}\n"
                                       f"Никнейм: {message.from_user.username}")
