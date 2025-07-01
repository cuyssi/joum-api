from deep_translator import GoogleTranslator


def translate_word(word: str) -> str:
    try:
        translated = GoogleTranslator(source="es", target="en").translate(word)
        return translated
    except Exception as e:
        print("Error al traducir:", e)
        return "Error al traducir"
