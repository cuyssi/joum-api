from fastapi import APIRouter
from database.mongo import get_all_suggestions, update_suggestion_status
from schemas.suggestion_schema import SuggestionSchema
from database.mongo import save_word, delete_suggestion
from schemas.suggestion_schema import SuggestionAdminSchema

router = APIRouter()


@router.get("/sugerencias")
def ver_sugerencias():
    sugerencias = get_all_suggestions()
    return sugerencias


@router.put("/revisar")
def revisar(data: SuggestionAdminSchema):
    if data.status == "aprobado":
        save_word(data.translation, data.translation, data.suggested_pronunciation)
    update_suggestion_status(
        data.translation, data.suggested_pronunciation, data.status
    )
    delete_suggestion(data.translation, data.suggested_pronunciation)
    return {"message": "Sugerencia revisada con éxito"}
