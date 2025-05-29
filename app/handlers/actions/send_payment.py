from aiogram import types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.schemes.actions.send_payment import SendPaymentAction


async def handle(
    message: types.Message | None,
    query: types.CallbackQuery | None,
    bot: Bot,
    data: SendPaymentAction
) -> bool:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"Оплатить",
        pay=True
    )

    prices = [types.LabeledPrice(label="XTR", amount=data.price)]

    await message.answer_invoice(
        title=data.text,
        description="Оплата за услугу",
        prices=prices,
        provider_token="",
        payload=f"{data.price}_stars",
        currency="XTR",
        reply_markup=builder.as_markup()
    )
