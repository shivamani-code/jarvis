import pyttsx3
import speech_recognition as sr
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QTimer

class Communication:
    def __init__(self, ui):
        """Initialize the communication system."""
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.ui = ui  # Reference to UI for updating labels
    
    def speak(self, text):
        """Speaks and updates UI with text output."""
        self.ui.status_label.setText(f"Jarvis: {text}")  # Update UI status
        self.engine.say(text)
        self.engine.runAndWait()

    def start_communication(self):
        """Start Eco Mode for interactive communication."""
        self.speak("Eco mode activated. I am listening.")
        
        while True:
            try:
                with sr.Microphone() as source:
                    self.ui.status_label.setText("Listening in Eco Mode...")  # Update UI
                    print("Listening in Eco Mode...")
                    
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio)
                    
                    self.ui.result_label.setText(f"You said: {command}")  # Update UI with input
                    print("You said:", command)

                    if "exit eco mode" in command.lower():
                        self.speak("Exiting eco mode.")
                        self.ui.status_label.setText("Returning to normal mode...")
                        break  # Exit loop

            except sr.UnknownValueError:
                self.ui.result_label.setText("Sorry, I didn't catch that.")
                self.speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                self.ui.result_label.setText("Speech recognition service unavailable.")
                self.speak("Speech recognition service unavailable.")
