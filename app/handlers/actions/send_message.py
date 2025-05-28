from aiogram import types, Bot

from app.schemes.actions.send_message import SendMessageAction, Keyboard


def generate_keyboard(keyboard: Keyboard, is_inline: bool) -> types.ReplyKeyboardMarkup | types.InlineKeyboardMarkup:
    buttons = []
    for row in keyboard:
        buttons_row = []
        for btn in row:
            if is_inline:
                buttons_row.append(types.InlineKeyboardButton(
                    text=btn.text,
                    callback_data=btn.callback_data,
                    url=btn.url
                ))
            else:
                buttons_row.append(types.KeyboardButton(text=btn.text))
        buttons.append(buttons_row)

    if is_inline:
        return types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text=btn.text, callback_data=btn.callback_data) for btn in row]
                for row in keyboard
            ]
        )
    else:
        return types.ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
            one_time_keyboard=True
        )


async def handle(
    message: types.Message | None,
    query: types.CallbackQuery | None,
    bot: Bot,
    data: SendMessageAction
) -> bool:
    chat_id = message.chat.id if message else query.message.chat.id
    if data.chat:
        chat_id = data.chat

    if len(data.keyboard):
        reply_markup = generate_keyboard(data.keyboard, data.is_inline)
    else:
        reply_markup = None

    await bot.send_message(
        chat_id=chat_id,
        text=data.text,
        reply_markup=reply_markup
    )
