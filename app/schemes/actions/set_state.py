from pydantic import BaseModel
from app.schemes.common.keyboards import Keyboard


class SetState(BaseModel):
    variable_name: str
