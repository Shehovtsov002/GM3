import asyncio
import os
import random
import logging
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

commands = (f"Действующие команды:\n"
            f"/myinfo - ваши данные(id, first_name, username)\n"
            f"/random_pic - присылает случайную картинку")


def get_random_pic() -> types.FSInputFile:
    """return path to file"""
    folder_path = "src/images"
    files = os.listdir(folder_path)
    return types.FSInputFile(os.path.join(folder_path, random.choice(files)))


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n\n{commands}")


@dp.message(Command("myinfo"))
async def info_command(message: types.Message):
    await message.answer_photo(photo=get_random_pic(),
                               caption=f"Ваш id: {message.from_user.id}\n"
                                       f"Звать вас: {message.from_user.first_name}\n"
                                       f"Никнейм: {message.from_user.username}")


@dp.message(Command("random_pic"))
async def random_pic_command(message: types.Message):
    await message.answer_photo(photo=get_random_pic())


@dp.message()
async def unknown_command(message: types.Message):
    await message.answer(f"Я таких слов не знаю, сверьтесь со следующим списком.\n{commands}")


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="myinfo", description="Получить инфу"),
        types.BotCommand(command="random_pic", description="Получить пикчу")
    ])
    # initialize bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
