from aiogram.dispatcher.filters.state import StatesGroup,State


class RegisterStates(StatesGroup):
    full_name = State()
    phone_number = State()
    chat_id = State()
    created_at = State()


class TestStates(StatesGroup):
    code = State()


class AnswerStates(StatesGroup):
    answers = State()
    test_id = State()