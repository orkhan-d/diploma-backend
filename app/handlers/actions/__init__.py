from aiogram import types, Bot
from app.handlers.actions import send_message


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
        if action['name'] == 'send_message':
            data = send_message.SendMessageAction(**data)
            await send_message.handle(message, query, bot, data)

    return success
