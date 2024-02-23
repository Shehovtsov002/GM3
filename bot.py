from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from db.base import DB
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
db = DB()
scheduler = AsyncIOScheduler()
reminders = {}