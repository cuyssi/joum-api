from fastapi import APIRouter
from schemas.word_schema import WordSchema
from database.mongo import (
    save_word,
    get_pronunciation,
    get_pronunciation_by_translation,
)
from utils.text_utils import normalizar

router = APIRouter()


@router.get("/buscar")
def buscar(word: str):
    word = normalizar(word)
    pronunciation = get_pronunciation_by_translation(word)
    return {"word": word, "pronunciation": pronunciation}


@router.post("/guardar")
def guardar_palabra(data: WordSchema):
    word_normalizada = normalizar(data.word)
    save_word(data.word, data.translation, data.pronunciation)
    return {"message": "Palabra guardada correctamente"}
