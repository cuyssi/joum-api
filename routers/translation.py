from fastapi import APIRouter
from schemas.word_schema import WordRequest
from services.translator import translate_word

router = APIRouter()


@router.post("/traducir")
def traducir(data: WordRequest):
    palabra = data.word.lower().strip()
    traduccion = translate_word(palabra)
    return {"original": palabra, "translation": traduccion}
