from aiogram import types

from app.schemes.conditions.words_check import WordsCheckCondition


async def handle(
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
    data: WordsCheckCondition
) -> bool:
    return any(word in message.text for word in data.words) if message.text else False
