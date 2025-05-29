from aiogram import Dispatcher
from app.handlers.message import router as message_router
from app.handlers.callback import router as callback_router


def get_dp() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(message_router)
    dp.include_router(callback_router)
    return dp
