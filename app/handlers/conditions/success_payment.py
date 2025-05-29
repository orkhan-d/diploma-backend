from aiogram import types

from app.schemes.conditions.success_payment import SuccessPayment


async def handle(
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
    data: SuccessPayment,
) -> bool:
    return message.successful_payment is not None
