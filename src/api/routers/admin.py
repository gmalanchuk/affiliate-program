from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.constants import admin_text, create_offer_text, view_offers_text, select_suggested_action_text, main_menu_text
from src.services.offer import OfferService
from src.services.user import UserService

admin_router = Router(name="admin")


@admin_router.message(F.text.lower() == admin_text.lower())
async def admin_command(
        message: types.Message,
        user_service: UserService = UserService()
):
    user = await user_service.get_user(telegram_user_id=message.from_user.id)
    if not user:
        await user_service.create_user(telegram_user_id=message.from_user.id)

    kb = [
        [
            types.KeyboardButton(text=create_offer_text),
            types.KeyboardButton(text=view_offers_text)
        ],
        [
            types.KeyboardButton(text=main_menu_text)
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=select_suggested_action_text
    )

    await message.answer(
        text='Вибери нижче, ти хочеш передивится вже створені тобою офери чи створити новий',  # todo переписать
        reply_markup=keyboard,
    )


# ------------------------------------------


class OfferStates(StatesGroup):
    waiting_for_name = State()


@admin_router.message(F.text.lower() == create_offer_text.lower())
async def create_offer_command(message: types.Message, state: FSMContext):
    await message.reply("Придумайте назву для свого оферу")  # todo переписать
    await state.set_state(OfferStates.waiting_for_name)


@admin_router.message(OfferStates.waiting_for_name)
async def process_offer_name(message: types.Message, state: FSMContext):
    offer_name = message.text



    await message.reply(f"Офер '{offer_name}' успішно створено!")
    await state.clear()  # очищаем состояние
