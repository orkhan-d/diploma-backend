from aiogram import types

from app.schemes.conditions.text_equality import TextEqualityCondition
from app.schemes.conditions.words_check import WordsCheckCondition


async def handle(
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
    data: TextEqualityCondition,
) -> bool:
    if data.case_sensitive:
        return message.text == data.text
    else:
        return message.text.lower() == data.text.lower()