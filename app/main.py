from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_db

app = FastAPI()


@app.get("/ping")
async def ping_pong():
    return {"ping": "pong!"}


@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(1))
    value = result.scalar_one()
    return {"db": value}
