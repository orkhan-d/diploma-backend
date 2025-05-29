from aiogram import types, Bot

from app.schemes.actions.save_variable import SaveVariableAction
from app.supabase import supabase


async def handle(
    message: types.Message | None,
    query: types.CallbackQuery | None,
    bot: Bot,
    data: SaveVariableAction
) -> bool:
    user_id = message.from_user.id if message else query.from_user.id
    value = ''

    match data.variable_value:
        case 'message_text':
            value = message.text
        case 'sender_name':
            value = message.from_user.full_name if message else query.from_user.full_name

    supabase.from_('variables').insert({
        'name': f'{user_id}-{data.variable_name}',
        'value': value,
        'bot_id': bot.token
    }).execute()
