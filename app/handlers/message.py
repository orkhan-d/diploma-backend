import json

from aiogram import Router, types
import os

from app.handlers.actions import handle_actions
from app.handlers.conditions import handle_conditions

router = Router()


@router.message()
async def handle_message(message: types.Message):
    try:
        bot_token = message.bot.token
        # get json file from bots folder like bots/bot_token.json
        scheme = json.load(open(os.path.join('bots', f'{bot_token}.json'), 'r'))
        blocks = scheme['blocks']

        for block in blocks:
            if block['block_types']['system_name'] == 'new_message':
                block_scheme = block.get('scheme', {})
                conditions = block_scheme.get('conditions', [])
                actions = block_scheme.get('actions', [])

                if handle_conditions(conditions, message=message):
                    await handle_actions(actions, message.bot, message=message)
                    return
    except Exception as e:
        print(e, flush=True)
    return {"ok": True, "message": "Message handled successfully"}