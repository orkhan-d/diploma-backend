from aiogram import types, Bot
from app.supabase import supabase
from app.schemes.actions.set_state import SetState


async def handle(
    message: types.Message | None,
    query: types.CallbackQuery | None,
    bot: Bot,
    data: SetState
) -> bool:
    res = supabase.table('states').select(
        '*'
    ).eq(
        'tg_user_id', message.from_user.id
    ).eq(
        'bot_id', bot.id
    ).execute()
    if len(res.data):
        supabase.table('states').update(
            {'value': data.variable_name}
        ).eq(
            'tg_user_id', message.from_user.id
        ).eq(
            'bot_id', bot.id
        ).execute()
    else:
        supabase.table('states').insert({
            'tg_user_id': message.from_user.id,
            'bot_id': bot.id,
            'value': data.variable_name
        }).execute()
