from pydantic import BaseModel


class WordsCheckCondition(BaseModel):
    words: list[str]
