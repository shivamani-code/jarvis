import sys
import time
import asyncio
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication
from image_generation import generate_image, show_image  # Import the functions # Import Jarvis Brain
from brain import JarvisBrain
from password_auth_ui import password_auth
from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
from ui import JarvisUI
from speech import listen, speak
from ocr import perform_ocr
from schedule_manager import add_schedule, view_schedule
from face_auth import capture_face, verify_face
from voice_auth import verify_voice
from system_control import *
from text_generator import generate_text
import ollama
from translator import translate_text, speak_translated_text
from task_manager import add_task, view_tasks

# Initialize Jarvis Brain
jarvis_brain = JarvisBrain()

def get_ollama_response(command):
    """Process user commands with Ollama AI."""
    try:
        if not isinstance(command, str):
            command = str(command)
        response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": command}])
        return response.get('message', {}).get('content', 'No response')
    except Exception as e:
        return f"Error with Ollama: {e}"
# ---------------------- HISTORY FEATURE ---------------------- #
HISTORY_FILE = "history.txt"

def save_history(command, response):
    """Save command and response to history file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"User: {command}\nJarvis: {response}\n\n")

def view_history():
    """Retrieve the stored history."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No history found."

# ---------------------- LISTENING WITH TIMEOUT ---------------------- #
import speech_recognition as sr

def listen_for_jarvis():
    """Listens indefinitely for the wake word 'Jarvis' without a timeout."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Waiting for wake word 'Jarvis'...")

        while True:  # Runs indefinitely until "Jarvis" is heard
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=3)
                text = recognizer.recognize_google(audio).lower()
                print(f"🗣️ Heard: {text}")

                if "jarvis" in text:
                    print("✅ Wake word detected! Listening for command...")
                    speak("Yes, how can I assist?")
                    return listen_command()  # Now listen for the actual command

            except sr.UnknownValueError:
                continue  # No speech detected, keep waiting
            except sr.RequestError:
                print("⚠️ Speech recognition service error.")
                return None

def listen_command(timeout=5):
    """Listens for a command after the wake word is detected, with a shorter timeout."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"🎤 Listening for command... (Timeout: {timeout}s)")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=4)
            command = recognizer.recognize_google(audio).lower()
            print(f"✅ Command received: {command}")
            return command
        except sr.UnknownValueError:
            print("❌ Could not understand.")
            return None
        except sr.RequestError:
            print("⚠️ API error.")
            return None
        except sr.WaitTimeoutError:
            print("⏳ No command detected. Returning to wake mode...")
            return None  # Return to wake word listening
# ---------------------- LOOP PREVENTION ---------------------- #

last_command = None
repeat_count = 0

def prevent_loop(command):
    """Prevents the same command from looping indefinitely."""
    global last_command, repeat_count
    
    if command == last_command:
        repeat_count += 1
    else:
        repeat_count = 0  # Reset counter if command changes

    last_command = command

    if repeat_count >= 3:  # Prevent repeating the same command more than 3 times
        speak("You are repeating the same command. Please try something else.")
        return True  # Stop execution
    return False  # Continue execution

# ---------------------- IMPROVE COMMAND FEATURE ---------------------- #
def improve_last_command():
    """Suggests improvements for the last user command."""
    if last_command:
        improvement = f"I suggest a better way to phrase '{last_command}' for better results."
        speak(improvement)
        return improvement
    else:
        return "No recent command to improve."

# ---------------------- FUNCTION TO PROCESS COMMANDS ---------------------- #



def process_command(command, jarvis_ui):
    """Processes the user command with AI brain first, then system functions."""
    response = jarvis_brain.analyze_command(command)

    if response != "I'm still learning. Can you rephrase?":
        # If the brain understands, process the response
        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")
    else:
        # Fallback to system functions if the brain doesn’t understand
        jarvis_ui.update_status(f"🗣️ {command}")

        if "exit" in command:
            speak("Goodbye! Shutting down.")
            sys.exit()

    if command.startswith("shutdown"):
        shutdown()
    elif command.startswith("restart"):
        restart()
    elif command.startswith("sleep"):
        sleep()
    elif command.startswith("lock"):
        lock()
    elif command.startswith("volume up"):
        adjust_volume('up')
    elif command.startswith("volume down"):
        adjust_volume('down')
    elif command.startswith("mute"):
        mute()
    elif command.startswith("take screenshot"):
        take_screenshot()
    elif command.startswith("empty recycle bin"):
        empty_recycle_bin()

    # ---------------------- IMAGE GENERATION ---------------------- #
    elif "generate image" in command:
        parts = command.split("using")  # Example: "generate image of a car using deepai"
        if len(parts) == 2:
            prompt = parts[0].replace("generate image", "").strip()
            method = parts[1].strip().lower()
            image_url = generate_image(prompt, method)
            response = f"Image generated using {method}. Opening..."
            show_image(image_url)
        else:
            response = "Invalid format. Use: 'generate image of [object] using [method]'"

    # ---------------------- FILE & FOLDER MANAGEMENT ---------------------- #
    elif command.startswith("create folder"):
        folder_name = command.replace("create folder", "").strip()
        create_folder(folder_name, "C:\\")
    elif command.startswith("delete folder"):
        folder_name = command.replace("delete folder", "").strip()
        delete_folder(f"C:\\{folder_name}")
    elif command.startswith("open folder"):
        folder_path = command.replace("open folder", "").strip()
        open_folder(folder_path)
    elif command.startswith("open application"):
        app_name = command.replace("open application", "").strip()
        open_application(app_name)
    elif command.startswith("close application"):
        app_name = command.replace("close application", "").strip()
        close_application(app_name)
    elif command.startswith("search file"):
        file_name = command.replace("search file", "").strip()
        search_file(file_name, "C:\\")

    # ---------------------- NETWORK & SYSTEM INFO ---------------------- #
    elif command.startswith("wifi on"):
        wifi_on_off(True)
    elif command.startswith("wifi off"):
        wifi_on_off(False)
    elif command.startswith("check speed"):
        check_speed()
    elif command.startswith("get ip"):
        get_ip()
    elif command.startswith("flush dns"):
        flush_dns()
    elif command.startswith("task manager"):
        task_manager()

    # ---------------------- MODE CHANGES ---------------------- #
    elif command.startswith("change mode to gork"):
        gork_mode(jarvis_ui)
    elif command.startswith("change mode to eco"):
        eco_mode(jarvis_ui)

    # ---------------------- SEARCH COMMANDS ---------------------- #
    elif command.startswith("search"):
        query = command.replace("search", "").strip()
        google_search(query)

    # ---------------------- AI RESPONSE FALLBACK ---------------------- #
    else:
        response = get_ollama_response(command)  # **Only call Ollama if no other command matches**
        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")

    save_history(command, response)


# ---------------------- MAIN FUNCTION ---------------------- #
def main():
    print("🚀 Running Main Function...")
    speak("Initializing system...")

    if not password_auth():
        print("❌ Access Denied! Exiting...")
        sys.exit(1)

    print("✅ Password Verified! Proceeding...")
    speak("Password Verified!")


    app = QApplication(sys.argv)
    jarvis_ui = JarvisUI()
    jarvis_ui.show()

    if not capture_face() or not verify_face():
        speak("Face verification failed! Exiting.")
        jarvis_ui.update_status("❌ Access Denied!")
        return

    speak("Face verification successful!")

    if not verify_voice():
        speak("Voice verification failed! Access denied.")
        jarvis_ui.update_status("❌ Access Denied!")
        return

    speak("Authentication successful! ")
    speak("Welcome! shiva mani")

    while True:
        command = listen_for_jarvis()  # ✅ Fix: Removed timeout argument
        process_command(command, jarvis_ui)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
