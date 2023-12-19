from main.models import *
from main.database_set import database


async def add_user(data: dict):
    try:
        query = users.insert().values(
            full_name=data.get('full_name'),
            phone_number=data.get('phone_number'),
            language="uz",
            chat_id=data.get('chat_id'),
            created_at=data.get('created_at')
        )

        new_user = await database.execute(query=query)
        return new_user
    except Exception as exc:
        print(exc)
        return False


async def get_user(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        print(exc)
        return False


async def add_test(data: dict):
    try:
        query = test.insert().values(
            code=data.get("code"),
            created_at=data.get("created_at")
        ).returning(test.c.id)
        new_test = await database.execute(query=query)
        return new_test
    except Exception as exc:
        print(exc)
        return False
