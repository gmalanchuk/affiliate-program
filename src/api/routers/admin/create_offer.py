from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.constants import create_offer_text

create_offer_router = Router(name="create_offer")


class OfferStates(StatesGroup):
    waiting_for_name = State()


@create_offer_router.message(F.text.lower() == create_offer_text.lower())
async def create_offer_command(message: types.Message, state: FSMContext):
    await message.reply("Придумайте назву для свого оферу")  # todo переписать
    await state.set_state(OfferStates.waiting_for_name)


@create_offer_router.message(OfferStates.waiting_for_name)
async def process_offer_name(message: types.Message, state: FSMContext):
    offer_name = message.text

    await message.reply(f"Офер '{offer_name}' успішно створено!")
    await state.clear()  # очищаем состояние
