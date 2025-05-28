from aiogram import Router, types

router = Router()


@router.message()
async def handle_message(message: types.Message):
    """
    Handle incoming messages.
    """
    # Here you can process the message, e.g., log it, respond, etc.
    await message.answer("Received your message!")