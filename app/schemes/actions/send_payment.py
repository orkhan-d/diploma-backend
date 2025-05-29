from pydantic import BaseModel
from app.schemes.common.keyboards import Keyboard


class SendPaymentAction(BaseModel):
    text: str
    price: int
