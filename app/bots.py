from aiogram import Dispatcher
from app.handlers.message import router as message_router


def get_dp() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(message_router)
    return dp
