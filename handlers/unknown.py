from aiogram import Router, types


unknown_router = Router()


@unknown_router.message()
async def unknown_command(message: types.Message):
    await message.answer(f"Я таких слов не знаю, сверьтесь со списком.")
