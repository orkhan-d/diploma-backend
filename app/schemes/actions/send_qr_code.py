from pydantic import BaseModel


class QrCodeData(BaseModel):
    name: str
    value: str


class SendQrCode(BaseModel):
    variables: list[QrCodeData]
