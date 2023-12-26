from aiogram.dispatcher import FSMContext

from keyboards.default.user import new_answer
from loader import dp
from aiogram import types

from main.models import test
from states.user import TestStates, AnswerStates
from utils.db_api.user_commands import add_test, add_answer


@dp.message_handler(text="📖New_test")
async def add_test_handler(message: types.Message):
    text = "Test ni codini kriting"
    await message.answer(text=text)
    await TestStates.code.set()


@dp.message_handler(state=TestStates.code)
async def get_code_handler(message: types.Message, state: FSMContext):
    await state.update_data(code=message.text, created_at=message.date)
    data = await state.get_data()
    code = await add_test(data=data)
    await state.update_data(test_id=code)
    if code:
        text = "Javob kiriting"
        await AnswerStates.answers.set()
    else:
        text = "MuxriddieUzur Muxriddin aka botta hato bor"
    await message.answer(text=text)


@dp.message_handler(state=AnswerStates.answers)
async def add_answer_handler(message: types.Message, state: FSMContext):
    await state.update_data(answers=message.text)
    data = await state.get_data()
    ans = await add_answer(data=data)
    if ans:
        text = "🫡Javob koshildi✅ \n\n" \
               "yana koyish📖 yoki test ni tugatish🛑 \n\n" \
               "uchun knopkalardan foydalaning"
    else:
        text = "MuxriddieUzur Muxriddin aka botta hato bor"
    await message.answer(text=text, reply_markup=new_answer)
    await state.finish()


@dp.message_handler(text="📖Again")
async def again_test_handler(message: types.Message, state: FSMContext):
    text = "Javobni kiriting"
    await message.answer(text=text)
    await AnswerStates.answers.set()


@dp.message_handler(text="🛑The End📖")
async def the_end_handler(message: types.Message, state: FSMContext):
    text = "Test mufokiyatli koshildi"
    await message.answer(text=text)
    await state.finish()
