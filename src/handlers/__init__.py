from aiogram import Router
from aiogram.filters import CommandStart

from .start import process_start_command


def register_user_commands(router: Router) -> None:
    router.message.register(
        process_start_command, CommandStart())
