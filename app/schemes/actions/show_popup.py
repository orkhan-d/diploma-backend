from pydantic import BaseModel


class ShowPopupAction(BaseModel):
    text: str
    show_alert: bool
