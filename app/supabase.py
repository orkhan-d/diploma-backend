import aiocron
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

if not os.path.exists("bots"):
    os.makedirs("bots")


@aiocron.crontab('*/1 * * * *')
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
            "system_name": bot['bot_types']['system_name']
        }
        file_path = f"bots/{token}.json"
        with open(file_path, 'w') as f:
            import json
            json.dump(bot_data, f, indent=4)
