from aiogram import types

from app.schemes.conditions.words_check import WordsCheckCondition


def handle(
    message: types.Message,
    data: WordsCheckCondition
) -> bool:
    return any(word in message.text for word in data.words) if message.text else False
