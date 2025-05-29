from aiogram import types

from app.handlers.conditions import word_check, success_payment
from app.handlers.conditions import text_equality
from app.handlers.conditions import check_state
from app.handlers.conditions import chat_member_check
from app.handlers.conditions import callback_equality


async def handle_conditions(
    conditions: list[dict[str, any]],
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
) -> bool:
    success = True

    for condition in conditions:
        data = condition.get('data', {})
        res = False

        match condition['name']:
            case 'word_check':
                data = word_check.WordsCheckCondition(**data)
                res = await word_check.handle(
                    message=message,
                    query=query,
                    data=data
                )
            case 'text_equailty':
                data = text_equality.TextEqualityCondition(**data)
                res = await text_equality.handle(
                    message=message,
                    query=query,
                    data=data
                )
            case 'check_state':
                data = check_state.CheckState(**data)
                res = await check_state.handle(
                    message=message,
                    query=query,
                    data=data
                )
            case 'chat_member_check':
                data = chat_member_check.ChatMemberCheck(**data)
                res = await chat_member_check.handle(
                    message=message,
                    query=query,
                    data=data
                )
            case 'success_payment':
                data = success_payment.SuccessPayment()
                res = await success_payment.handle(
                    message=message,
                    query=query,
                    data=data
                )
            case 'callback_equailty':
                data = callback_equality.CallbackEqualityCondition(**data)
                res = await callback_equality.handle(
                    message=message,
                    query=query,
                    data=data
                )
        success = res != condition['negative']

    return success
