from pydantic import BaseModel


class ChatMemberCheck(BaseModel):
    chat_id: str
