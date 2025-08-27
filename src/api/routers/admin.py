from aiogram import Router, F, types

from src.services.user import UserService

admin_router = Router(name="admin")


@admin_router.message(F.text.lower() == "адмін")
async def admin(
        message: types.Message,
):

    user_service = UserService()
    await user_service.create_user(telegram_user_id=message.from_user.id)


    await message.reply(f"admin {message.from_user.id}")


    # создать оффер. посмотреть свои офферы (две кнопки)
