from pydantic import BaseModel


class DeleteMessageAction(BaseModel):
    chat_id: str | None
    message_id: str | None
