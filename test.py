import threading
import time
import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Speech Recognition
import sys

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak output text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I am having trouble with the speech service.")
            return ""

# Task 1 - Open an application
def open_application():
    speak("Opening application...")
    print("Opening application...")
    time.sleep(2)
    # Replace with code to open actual app (e.g., using subprocess)

# Task 2 - Search the web
def search_web(query):
    speak(f"Searching for {query}...")
    print(f"Searching for {query}...")
    time.sleep(3)
    # Replace with actual web search code (e.g., using webbrowser or an API)

# Task 3 - Play music
def play_music():
    speak("Playing music...")
    print("Playing music...")
    time.sleep(2)
    # Replace with actual code to play music (e.g., using a library like pygame)

# Task 4 - Shut down the system
def shut_down_system():
    speak("Shutting down the system...")
    print("Shutting down the system...")
    time.sleep(2)
    sys.exit()

# Task Dispatcher based on voice command
def task_dispatcher(command):
    if "open app" in command:
        open_application()
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    elif "play music" in command:
        play_music()
    elif "shut down" in command:
        shut_down_system()
    else:
        speak("Sorry, I don't recognize that command.")

# Main loop to continuously listen and perform tasks
def main():
    while True:
        command = listen_for_commands()
        if command:
            task_dispatcher(command)

# Run the main loop
if __name__ == "__main__":
    main()
