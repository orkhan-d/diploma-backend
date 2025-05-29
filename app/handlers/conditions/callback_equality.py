from aiogram import types

from app.schemes.conditions.callback_equality import CallbackEqualityCondition


async def handle(
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
    data: CallbackEqualityCondition,
) -> bool:
    return query.data == data.callback