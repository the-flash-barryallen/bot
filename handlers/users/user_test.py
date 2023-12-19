from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types

from states.user import TestStates
from utils.db_api.user_commands import add_test



@dp.message_handler(text="📖New_test")
async def add_test_handler(message: types.Message):
    text = "Test ni codini kriting"
    await message.answer(text=text)
    await TestStates.code.set()


@dp.message_handler(state=TestStates.code)
async def get_code_handler(message: types.Message, state: FSMContext):
    await state.update_data(code=int(message.text), created_at=message.date)
    data = await state.get_data()
    code = await add_test(data=data)
    if code:
        text = "Code kiritildi iltimos javob kiritish uchun button da foydalaning"
    else:
        text = "MuxriddieUzur Muxriddin aka botta hato bor"
    await message.answer(text=text)
    await state.finish()
