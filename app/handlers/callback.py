import json

from aiogram import Router, types
import os

from app.handlers.actions import handle_actions
from app.handlers.conditions import handle_conditions

router = Router()


@router.callback_query()
async def handle_callback_query(query: types.CallbackQuery):
    try:
        bot_token = query.bot.token
        # get json file from bots folder like bots/bot_token.json
        scheme = json.load(open(os.path.join('bots', f'{bot_token}.json'), 'r'))
        blocks: list[dict[str, any]] = scheme['blocks']

        for block in blocks:
            if not block['is_active']:
                continue
            if block['block_types']['system_name'] == 'new_callback':
                block_scheme = block.get('scheme', {})
                conditions: list[dict[str, any]] = block_scheme.get('conditions', [])
                actions: list[dict[str, any]] = block_scheme.get('actions', [])

                if await handle_conditions(conditions, query=query):
                    await handle_actions(actions, query.bot, query=query)
                    return
    except Exception as e:
        print(e, flush=True)