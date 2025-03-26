import pyttsx3
import speech_recognition as sr
from deep_translator import GoogleTranslator

recognizer = sr.Recognizer()
translator = GoogleTranslator(source='auto', target='en')

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for female

def listen():
    """Listens for voice input and returns translated text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  
        translated_text = translator.translate(text)  
        return text, translated_text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand.", "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Speech recognition service unavailable.", "Speech recognition service unavailable."

def speak(text):
    """Converts text to speech using pyttsx3 (direct playback)."""
    engine.say(text)
    engine.runAndWait()
