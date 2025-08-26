from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, Router

start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_router(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
