from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))
db = client[os.getenv("DB_NAME")]

palabras_collection = db["palabras"]
sugerencias_collection = db["sugerencias"]


def get_pronunciation(original: str):
    result = palabras_collection.find_one({"translation": original})
    return result["pronunciation"] if result else None


def save_word(word: str, translation: str, pronunciation: str):
    palabras_collection.update_one(
        {"word": word},
        {"$set": {"translation": translation, "pronunciation": pronunciation}},
        upsert=True,
    )


def save_suggestion(word, pronunciation):
    # Verificamos si la palabra ya existe en la colección de palabras
    existente = palabras_collection.find_one({"word": word})

    tipo = "modificación" if existente else "nueva"

    sugerencia = {
        "translation": word,
        "suggested_pronunciation": pronunciation,
        "status": "pendiente",
        "tipo": tipo,
        "fecha": datetime.now(),
    }

    sugerencias_collection.insert_one(sugerencia)


def get_all_suggestions():
    suggestions = []
    for doc in sugerencias_collection.find({"status": "pendiente"}):
        doc["_id"] = str(doc["_id"])
        suggestions.append(doc)
    return suggestions


def update_suggestion_status(
    translation: str, suggested_pronunciation: str, new_status: str
):
    result = sugerencias_collection.update_one(
        {
            "translation": translation,
            "suggested_pronunciation": suggested_pronunciation,
        },
        {"$set": {"status": new_status}},
    )
    if new_status == "aprobado":
        palabras_collection.update_one(
            {"translation": translation},
            {"$set": {"pronunciation": suggested_pronunciation}},
            upsert=True,
        )
    return result.modified_count


def get_pronunciation_by_translation(translation: str):
    result = palabras_collection.find_one({"translation": translation})
    return result["pronunciation"] if result else None


def delete_suggestion(translation: str, pronunciation: str):
    sugerencias_collection.delete_one(
        {"translation": translation, "suggested_pronunciation": pronunciation}
    )
