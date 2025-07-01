from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class SuggestionSchema(BaseModel):
    translation: str
    suggested_pronunciation: str


class SuggestionAdminSchema(SuggestionSchema):
    status: Literal["pendiente", "aprobado", "rechazado"]
    fecha: datetime
