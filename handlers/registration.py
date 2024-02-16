from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import registration_kb as keyboards
from keyboards.main_kb import main_keyboard
from bot import user


class Registration(StatesGroup):
    id = State()
    name = State()
    age = State()
    comics_type = State()
    favorite_genres = State()


registration_router = Router()


@registration_router.callback_query(F.data == "registration")
async def registration(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Registration.age)
    await state.update_data(id=callback.from_user.id)
    await state.update_data(name=callback.from_user.first_name)
    await callback.message.answer(text=f"{callback.from_user.first_name}, "
                              f"для регистрации вам нужно указать свой возраст\n"
                              f"Введите /stop для отмены")


@registration_router.message(Command("stop"))
async def stop_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Регистрация остановлена")


@registration_router.message(Registration.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer(text="Возраст должен быть числом")
        return
    elif int(age) < 6 or int(age) > 100:
        await message.answer(text="Возраст должен быть от 6 до 100")
        return
    await state.update_data(age=message.text)

    await message.answer(text="Для настройки рекомендаций пройдите опрос:\n"
                              "1. Что вы предпочитаете?", reply_markup=keyboards.types_keyboard())
    await state.set_state(Registration.comics_type)


@registration_router.callback_query(Registration.comics_type)
async def process_comics_type(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(comics_type=callback.data)
    await callback.message.answer(text=f"2: Любимый жанр в {callback.data}?\n"
                                       f"Выберите один или несколько и нажмите далее",
                                  reply_markup=keyboards.genres_keyboard())
    await state.set_state(Registration.favorite_genres)


@registration_router.callback_query(Registration.favorite_genres)
async def process_favorite(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback.data == "done":
        if not data.get("favorite_genres"):
            await callback.message.answer(text="Необходимо выбрать хотябы что-то одно из списка")
            return
        await callback.message.answer(text="На этом регистрация завершена!\n"
                                           "Теперь вы можете воспользоваться всеми функциями бота",
                                      reply_markup=main_keyboard())
        # TODO: Add user to db
        await state.clear()
    favorites = data.get("favorite_genres", set())
    favorites.add(callback.data)
    await state.update_data(favorite_genres=favorites)
    await callback.message.answer(text=f"{favorites}")
