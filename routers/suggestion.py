from fastapi import APIRouter
from schemas.suggestion_schema import SuggestionSchema
from database.mongo import save_suggestion, get_all_suggestions

router = APIRouter()


@router.post("/sugerir")
def sugerir_palabra(data: SuggestionSchema):
    save_suggestion(data.translation, data.suggested_pronunciation)
    return {"message": "Sugerencia enviada ✅"}


@router.get("/")
def obtener_sugerencias():
    return get_all_suggestions()
