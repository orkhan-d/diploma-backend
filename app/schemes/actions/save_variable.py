from pydantic import BaseModel
from app.schemes.common.keyboards import Keyboard


class SaveVariableAction(BaseModel):
    variable_name: str
    variable_value: str
