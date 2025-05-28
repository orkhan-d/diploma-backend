import json

from aiogram import Router, types
import os

from app.handlers.actions import handle_actions
from app.handlers.conditions import handle_conditions

router = Router()


@router.message()
async def handle_message(message: types.Message):
    bot_token = message.bot.token
    # get json file from bots folder like bots/bot_token.json
    scheme = json.load(open(os.path.join('bots', f'{bot_token}.json'), 'r'))
    scheme = scheme['blocks']['scheme']

    conditions = scheme.get('conditions', [])
    actions = scheme.get('actions', [])

    if handle_conditions(conditions, message=message):
        await handle_actions(actions, message.bot, message=message)
