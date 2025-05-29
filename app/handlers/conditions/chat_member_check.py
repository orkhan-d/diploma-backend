from aiogram import types, enums

from app.schemes.conditions.chat_member_check import ChatMemberCheck


async def handle(
    *,
    message: types.Message | None = None,
    query: types.CallbackQuery | None = None,
    data: ChatMemberCheck,
) -> bool:
    user_id = message.from_user.id if message else query.from_user.id
    # check if user in chat

    if message:
        chat_member = await message.bot.get_chat_member(chat_id=data.chat_id, user_id=user_id)
    else:
        chat_member = await query.bot.get_chat_member(chat_id=data.chat_id, user_id=user_id)

    statuses = [
        enums.ChatMemberStatus.CREATOR,
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.MEMBER,
    ]

    return chat_member.status in statuses