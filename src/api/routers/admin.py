from aiogram import Router, F, types

admin_router = Router(name="admin")


@admin_router.message(F.text.lower() == "адмін")
async def with_puree(message: types.Message):
    await message.reply(f"admin {message.from_user.id}")
