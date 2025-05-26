from pydantic import BaseModel


class SendAttachmentAction(BaseModel):
    files: list[str]
    caption: str
    allow_multiple: bool
    only_media: bool
    without_compression: bool
