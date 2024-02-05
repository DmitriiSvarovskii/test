from aiogram.types import Message


async def process_start_command(message: Message):
    await message.answer(
        text='Бот запущен'
    )
