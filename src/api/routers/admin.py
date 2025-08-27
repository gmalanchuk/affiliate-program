from aiogram import Router, F, types

from src.database.models import User
from src.database.session import async_session

admin_router = Router(name="admin")


@admin_router.message(F.text.lower() == "адмін")
async def with_puree(
        message: types.Message,
):

    async with async_session() as session:
        new_user = User(telegram_user_id=message.from_user.id)
        session.add(new_user)
        await session.commit()


    await message.reply(f"admin {message.from_user.id}")

    # todo записать пользователя в базу если его там нет

    # создать оффер. посмотреть свои офферы (две кнопки)
