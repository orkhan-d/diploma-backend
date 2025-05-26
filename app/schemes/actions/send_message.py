from pydantic import BaseModel
from app.schemes.common.keyboards import Keyboard


class SendMessageAction(BaseModel):
    text: str
    chat: str | None
    keyboard: Keyboard
    is_inline: bool
