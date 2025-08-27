from aiogram import Router, types, F

from src.constants import buyer_text

buyer_router = Router(name="buyer")


@buyer_router.message(F.text.lower() == buyer_text.lower())
async def buyer(message: types.Message):
    await message.reply("buyer")
