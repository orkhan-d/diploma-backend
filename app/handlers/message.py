import json

from aiogram import Router, types
import os

from app.handlers.actions import handle_actions
from app.handlers.conditions import handle_conditions

import traceback

router = Router()


@router.pre_checkout_query()
async def on_pre_checkout_query(
    pre_checkout_query: types.PreCheckoutQuery,
):
    await pre_checkout_query.answer(ok=True)


@router.message()
async def handle_message(message: types.Message):
    try:
        bot_token = message.bot.token
        # get json file from bots folder like bots/bot_token.json
        scheme = json.load(open(os.path.join('bots', f'{bot_token}.json'), 'r'))
        blocks: list[dict[str, any]] = scheme['blocks']

        for block in blocks:
            if not block['is_active']:
                continue
            if block['block_types']['system_name'] == 'new_message':
                block_scheme = block.get('scheme', {})
                conditions: list[dict[str, any]] = block_scheme.get('conditions', [])
                actions: list[dict[str, any]] = block_scheme.get('actions', [])

                if await handle_conditions(conditions, message=message):
                    await handle_actions(actions, message.bot, message=message)
                    return
    except Exception as e:
        print(e, flush=True)
        traceback.print_exc()
