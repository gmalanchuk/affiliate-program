from aiogram import Router, types, F

buyer_router = Router(name="buyer")


@buyer_router.message(F.text.lower() == "трафер")
async def buyer(message: types.Message):
    await message.reply("buyer")
