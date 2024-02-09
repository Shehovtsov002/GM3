from aiogram import Router, types
from aiogram.filters import Command
import os
import random


picture_router = Router()


@picture_router.message(Command("random_pic"))
async def random_pic_command(message: types.Message):
    await message.answer_photo(photo=get_random_pic())


def get_random_pic() -> types.FSInputFile:
    """return path to file"""
    folder_path = "src/images"
    files = os.listdir(folder_path)
    return types.FSInputFile(os.path.join(folder_path, random.choice(files)))
