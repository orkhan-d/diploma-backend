from fastapi import FastAPI
from aiogram import types, Bot

from app.bots import get_dp

app = FastAPI()
dp = get_dp()


@app.get("/ping")
async def ping_pong():
    return {"ping": "pong!"}


@app.post('/api/update/{token}')
async def bot_webhook(token: str, update: dict):
    bot = Bot(token)
    update = types.Update.model_validate(
        update,
        context={
            "bot": Bot(token)
        }
    )
    await dp.feed_update(bot, update)