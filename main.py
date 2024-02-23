import asyncio
import logging
from aiogram import Bot
from bot import bot, dp, db, scheduler
from aiogram import types
from handlers import (
    start_router,
    picture_router,
    info_router,
    genres_router,
    novelty_router,
    popular_router,
    recommendations_router,
    registration_router,
    scheduled_message_router,
    unknown_router
)


async def on_startup(bot: Bot):
    db.create_tables()
    db.populate_tables()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="myinfo", description="Получить инфу"),
        types.BotCommand(command="random_pic", description="Получить пикчу"),
        types.BotCommand(command="random_pic", description="Напоминалка"),
        types.BotCommand(command="start", description="Главная")
    ])

    # include commands
    dp.include_routers(start_router,
                       info_router,
                       picture_router,
                       genres_router,
                       novelty_router,
                       popular_router,
                       recommendations_router,
                       registration_router,
                       scheduled_message_router,
                       unknown_router)

    dp.startup.register(on_startup)

    scheduler.start()
    # initialize bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
