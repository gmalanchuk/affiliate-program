from aiogram.filters import CommandStart
from aiogram import Router, types


start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_router(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Адмін"),
         types.KeyboardButton(text="Трафер")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть запропоновану дію"
    )

    await message.answer(
        text=(
            'Привіт! Я бот для керування трафіком.\n'  # todo написать приветственное сообщение
        ),
        reply_markup=keyboard
    )
