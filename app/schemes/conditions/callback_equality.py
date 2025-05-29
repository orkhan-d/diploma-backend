from pydantic import BaseModel


class CallbackEqualityCondition(BaseModel):
    callback: str
