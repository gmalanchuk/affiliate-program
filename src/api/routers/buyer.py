from aiogram import Router, types, F

buyer_router = Router(name="buyer")


@buyer_router.message(F.text.lower() == "трафер")
async def without_puree(message: types.Message):
    await message.reply("йо трафер")
