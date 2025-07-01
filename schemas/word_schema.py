from pydantic import BaseModel
from typing import Literal
from datetime import datetime

# schemas/word_schema.py


class WordRequest(BaseModel):
    word: str


class WordSchema(BaseModel):
    word: str
    translation: str
    pronunciation: str
