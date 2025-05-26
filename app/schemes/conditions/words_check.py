from pydantic import BaseModel


class ShowPopupAction(BaseModel):
    words: list[str]
