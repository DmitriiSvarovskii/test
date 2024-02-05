import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import register_user_commands


sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src.")))


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    bot: Bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    register_user_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
