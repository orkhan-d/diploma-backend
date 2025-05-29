from aiogram import types, Bot
from app.handlers.actions import send_message
from app.handlers.actions import save_variable
from app.handlers.actions import send_payment
from app.handlers.actions import set_state
from app.handlers.actions import send_qr_code


async def handle_actions(
    actions: list[dict[str, any]],
    bot: Bot,
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
) -> bool:
    success = True

    for action in actions:
        data = action.get('data', {})
        match action['name']:
            case 'save_variable':
                data = save_variable.SaveVariableAction(**data)
                await save_variable.handle(message, query, bot, data)
            case 'send_message':
                data = send_message.SendMessageAction(**data)
                await send_message.handle(message, query, bot, data)
            case 'send_payment':
                data = send_payment.SendPaymentAction(**data)
                await send_payment.handle(message, query, bot, data)
            case 'set_state':
                data = set_state.SetState(**data)
                await set_state.handle(message, query, bot, data)
            case 'send_qr_code':
                data = send_qr_code.SendQrCode(**data)
                await send_qr_code.handle(message, query, bot, data)

    return success
