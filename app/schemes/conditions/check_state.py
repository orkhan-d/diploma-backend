from pydantic import BaseModel


class CheckState(BaseModel):
    state_name: str
