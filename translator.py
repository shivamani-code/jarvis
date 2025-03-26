from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

import asyncio

from googletrans import Translator

async def translate_text(text, target_language):
    translator = Translator()
    translated = await translator.translate(text, dest=target_language)
    return translated.text

def speak_translated_text(text, lang="en"):
    """Speaks the translated text using gTTS."""
    tts = gTTS(text=text, lang=lang)
    tts.save("temp_audio.mp3")
    os.system("start temp_audio.mp3")  # For Windows (use 'mpg321 temp_audio.mp3' for Linux)

# Example Usage:
# translated_text = translate_text("Hola, ¿cómo estás?", "en")  # Spanish to English
# speak_translated_text(translated_text, "en")
