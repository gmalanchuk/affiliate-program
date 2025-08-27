from aiogram import Router, F, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.constants import admin_text, create_offer_text, view_offers_text, select_suggested_action_text
from src.services.user import UserService


admin_router = Router(name="admin")

@admin_router.message(F.text.lower() == admin_text.lower())
async def admin(
        message: types.Message,
):
    user_service = UserService() # todo вынести в DI паттерн

    user = await user_service.get_user(telegram_user_id=message.from_user.id)
    if not user:
        await user_service.create_user(telegram_user_id=message.from_user.id)

    kb = [
        [types.KeyboardButton(text=create_offer_text),
         types.KeyboardButton(text=view_offers_text)]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=select_suggested_action_text
    )

    await message.answer(
        text=(
            'Вибери нижче, ти хочеш передивится вже створені тобою офери чи створити новий'  # todo переписать
        ),
        reply_markup=keyboard
    )


@admin_router.message(F.text.lower() == create_offer_text.lower())
async def create_offer(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    builder.row(types.KeyboardButton(
        text="Головне меню",
        request_poll=types.KeyboardButtonPollType(type="quiz"))
    )
    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

