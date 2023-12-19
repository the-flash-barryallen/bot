from keyboards.default.user import car_key
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types

from states.user import CarState
from utils.db_api.database import add_car, get_all_cars


@dp.message_handler(commands="CAR")
async def car_handler(message: types.Message):
    text = "here is the car list"
    await message.answer(text=text, reply_markup=car_key)


@dp.message_handler(text="ADD")
async def add_handler(message: types.Message, state: FSMContext):
    await CarState.model.set()
    text = "Please enter car model: "
    await message.answer(text=text)


@dp.message_handler(state=CarState.model)
async def get_car_model(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await CarState.price.set()
    text = "Enter price: "
    await message.answer(text=text)


@dp.message_handler(state=CarState.price)
async def get_price_model(message: types.Message, state: FSMContext):
    await state.update_data(price=int(message.text))
    await CarState.photo.set()
    text = "Forward photo: "
    await message.answer(text=text)


@dp.message_handler(state=CarState.photo, content_types=types.ContentType.PHOTO)
async def get_photo_model(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    new_car = await add_car(data)
    if new_car:
        text = "Finally added a car"
        await message.answer(text=text)
    else:
        text = "THERE IS PROBLEM IN BOT"
        await message.answer(text=text)
    await state.finish()


# @dp.message_handler(text="LIST")
# async def add_handler(message: types.Message, state: FSMContext):
#     all_cars = await get_all_cars()
#     text = "ALL CARS:\n\n"
#     for car in all_cars:
#         text += f"{car['photo']}\n{car['model']}--{car['price']}"
#     await message.answer(text=text)


@dp.message_handler(text="LIST")
async def show_all_cars_handler(message:types.Message):
    all_cars = await get_all_cars()
    text = "ALL CARS: \n\n"
    for cars in all_cars:
        text += f"{cars['model']} -- {cars['price']}\n"
        await message.answer_photo(photo=cars['photo'],caption=text)
