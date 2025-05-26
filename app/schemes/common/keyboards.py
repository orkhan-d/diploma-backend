import enum
from pydantic import BaseModel


class KeyboardButtonType(enum.Enum, str):
    text = "text"
    callback = "callback"
    url = "url"


class KeyboardButton(BaseModel):
    value: str
    type: KeyboardButtonType


KeyboardRow = list[KeyboardButton]
Keyboard = list[KeyboardRow]
