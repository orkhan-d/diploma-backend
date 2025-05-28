from aiogram import types

from app.handlers.conditions import word_check


def handle_conditions(
    conditions: list[dict[str, any]],
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
) -> bool:
    success = True

    for condition in conditions:
        data = condition.get('data', {})
        if condition['name'] == 'word_check':
            data = word_check.WordsCheckCondition(**data)
            if not word_check.handle(message, data):
                success = False
                break

    return success
