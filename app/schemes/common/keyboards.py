import enum
from pydantic import BaseModel


class KeyboardButtonType(str, enum.Enum):
    text = "text"
    callback = "callback"
    url = "url"


class KeyboardButton(BaseModel):
    text: str
    callback_data: str | None = None
    url: str | None = None
    type: KeyboardButtonType


KeyboardRow = list[KeyboardButton]
Keyboard = list[KeyboardRow]
