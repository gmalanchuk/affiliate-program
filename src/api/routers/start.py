from aiogram.filters import CommandStart
from aiogram import Router, types, F

from src.constants import buyer_text, admin_text, select_suggested_action_text, main_menu_text

start_router = Router(name="start")


@start_router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    kb = [
        [
            types.KeyboardButton(text=admin_text),
            types.KeyboardButton(text=buyer_text)
        ]
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


@start_router.message(F.text.lower() == main_menu_text.lower())
async def main_menu_command(message: types.Message) -> None:
    return await start_command(message)
