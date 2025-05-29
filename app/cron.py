import aiocron
import os
from app.supabase import supabase

if not os.path.exists("bots"):
    os.makedirs("bots")


@aiocron.crontab('*/3 * * * *')
async def scheduled_task():
    response = (
        supabase.table("bots")
        .select("token, is_running, bot_blocks(scheme, is_active, block_types(system_name))")
        .execute()
    )

    for bot in response.data:
        # create json file for each bot including its data and named as {token}.json
        token = bot['token']
        bot_data = {
            "token": token,
            "is_running": bot['is_running'],
            "blocks": bot['bot_blocks'],
        }
        file_path = f"bots/{token}.json"
        with open(file_path, 'w') as f:
            import json
            json.dump(bot_data, f, indent=4)
