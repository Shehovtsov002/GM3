from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

commands = (f"Действующие команды:\n"
            f"/myinfo - ваши данные(id, first_name, username)\n"
            f"/random_pic - присылает случайную картинку")
