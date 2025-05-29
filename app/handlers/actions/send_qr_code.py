import json
import re
import uuid

from aiogram import types, Bot
from app.supabase import supabase
from app.schemes.actions.send_qr_code import SendQrCode
import qrcode


async def handle(
    message: types.Message | None,
    query: types.CallbackQuery | None,
    bot: Bot,
    data: SendQrCode
) -> bool:
    vars = {}
    user_id = message.from_user.id if message else query.from_user.id

    for variable in data.variables:
        value = variable.value
        if re.match(r'\$\{.*\}', variable.value):
            value = await (supabase.table('variables').select('value')
                           .eq('name', f'{user_id}-{variable.value[2:-1]}').single())

        vars[variable.name] = value['value']

    img = qrcode.make(json.dumps(vars))

    qr_path = f"{uuid.uuid4()}.png"
    img.save(qr_path)
    await bot.send_photo(
        chat_id=user_id,
        photo=types.FSInputFile(path=qr_path)
    )
