from aiogram.filters import CommandStart
from aiogram import Router, types

from src.constants import buyer_text, admin_text, select_suggested_action_text

start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_router(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text=admin_text),
         types.KeyboardButton(text=buyer_text)]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=select_suggested_action_text
    )

    await message.answer(
        text=(
            'Привіт! Я бот для керування трафіком.\n'  # todo написать приветственное сообщение
        ),
        reply_markup=keyboard
    )
