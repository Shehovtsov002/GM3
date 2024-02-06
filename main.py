import asyncio
import logging
from bot import bot, dp
from aiogram import types
from handlers import (
    start_router,
    picture_router,
    info_router,
    unknown_router
)


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="myinfo", description="Получить инфу"),
        types.BotCommand(command="random_pic", description="Получить пикчу")
    ])

    # include commands
    dp.include_routers(start_router,
                       info_router,
                       picture_router,
                       unknown_router)

    # initialize bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
