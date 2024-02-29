from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.houses_kb import get_houses_kb
from parser.house_kg_parse import get_houses, insert_houses

houses_router = Router()


@houses_router.message(F.text.lower().startswith("дома"))
async def get_house(message: types.Message):
    count = int(message.text[4:])
    houses = get_houses(count)
    kb = get_houses_kb(houses)
    await message.answer(text="Дома:", reply_markup=kb)


@houses_router.message(Command("houses"))
async def insert_houses_to_db(message: types.Message):
    houses = insert_houses()
    await message.answer(text=f"В бд добавлены {len(houses)} записи")
