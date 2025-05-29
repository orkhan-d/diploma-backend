from aiogram import types

from app.supabase import supabase
from app.schemes.conditions.check_state import CheckState


async def handle(
        *,
        message: types.Message | None = None,
        query: types.CallbackQuery | None = None,
        data: CheckState,
) -> bool:
    res = (supabase.from_("states")
                 .select('*')
                 .eq('tg_user_id', message.from_user.id)
                 .eq('bot_id', message.bot.id)
                 .eq('value', data.state_name)
                 .execute())
    return res.count > 0
