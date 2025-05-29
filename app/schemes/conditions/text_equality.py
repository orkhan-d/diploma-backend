from pydantic import BaseModel


class TextEqualityCondition(BaseModel):
    text: str
    case_sensitive: bool
