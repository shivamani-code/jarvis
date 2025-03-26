
import os
import psutil
import pyautogui
import subprocess
import shutil
import webbrowser
import time
import speedtest
import socket
import ctypes
import sys
import asyncio
import speech_recognition as sr
from datetime import datetime
from PyQt6.QtWidgets import QApplication

# Import modules
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
from translator import translate_text, speak_translated_text
from task_manager import add_task, view_tasks
import ollama

# Initialize Jarvis Brain
jarvis_brain = JarvisBrain()

# Command Processing
HISTORY_FILE = "history.txt"

def save_history(command, response):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"User: {command}\nJarvis: {response}\n\n")

def view_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No history found."

def listen_for_jarvis():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Waiting for wake word 'Jarvis'...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=3)
                text = recognizer.recognize_google(audio).lower()
                print(f"🗣️ Heard: {text}")
                if "jarvis" in text:
                    speak("Yes, how can I assist?")
                    return listen_command()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("⚠️ Speech recognition service error.")
                return None

def listen_command(timeout=5):
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
            return None

last_command = None  # Initialize globally

def prevent_loop(command):
    global last_command  
    if command == last_command:
        return True  # Prevents repeating the same command
    last_command = command  # Store the last executed command
    return False



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
    """Processes the user command, first trying AI brain, then system functions."""
    if not command:
        return  # Do nothing if no command is received

    if prevent_loop(command):
        return  # Stop processing if loop detected

    response = jarvis_brain.analyze_command(command)

    if response != "I'm still learning. Can you rephrase?":
        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")
        save_history(command, response)
    else:
        jarvis_ui.update_status(f"🗣️ {command}")

        if "view history" in command:
            history = view_history()
            print(history)
            jarvis_ui.update_status("📜 Showing command history.")
            speak("Here is your command history.")
            return

        elif "clear history" in command:
            open(HISTORY_FILE, "w").close()
            jarvis_ui.update_status("🗑️ Command history cleared.")
            speak("Command history cleared.")
            return

        elif "improve this" in command:
            suggestion = improve_last_command()
            jarvis_ui.update_status(f"💡 {suggestion}")
            return

        elif "shutdown" in command:
            shutdown()
        elif "restart" in command:
            restart()
        elif "sleep" in command:
            sleep()
        elif "lock" in command:
            lock()
        elif "volume up" in command:
            adjust_volume('up')
        elif "volume down" in command:
            adjust_volume('down')
        elif "mute" in command:
            mute()
        elif "take screenshot" in command:
            take_screenshot()
        elif "empty recycle bin" in command:
            empty_recycle_bin()
        elif "create folder" in command:
            create_folder("NewFolder", "C:\\")
        elif "change mode to gork" in command:
           gork_mode(jarvis_ui)

        elif "delete folder" in command:
            delete_folder("C:\\NewFolder")
        elif "open folder" in command:
            open_folder("C:\\")
        elif "search file" in command:
            print(search_file("test.txt", "C:\\"))
        elif "copy file" in command:
            copy_file("source.txt", "destination.txt")
        elif "extract zip" in command:
            extract_zip("archive.zip", "C:\\extracted")
        elif "wifi on" in command:
            wifi_on_off(True)
        elif "wifi off" in command:
            wifi_on_off(False)
        elif "check speed" in command:
            print(check_speed())
        elif "get ip" in command:
            print(get_ip())
        elif "flush dns" in command:
            flush_dns()
        elif "send email" in command:
            send_email_voice()
        elif "read emails" in command:
            read_unread_emails_voice()
        elif "send whatsapp message" in command:
            send_whatsapp_voice()
        elif "send telegram message" in command:
            send_telegram_voice()
        elif "battery status" in command:
            print(battery_status())
        elif "task manager" in command:
            print(task_manager())
        elif "system uptime" in command:
            print(system_uptime())
        elif "current_cpu usage" in command:
            print(get_cpu_ram_usage())
        elif "list processes" in command:
            print(list_running_processes())
        elif "kill process" in command:
            print(kill_process("notepad.exe"))
        elif "play media" in command:
            play_pause_media()
        elif "next track" in command:
            next_track()
        elif "previous track" in command:
            previous_track()
        elif "set wallpaper" in command:
            set_wallpaper("C:\\wallpaper.jpg")
        elif "open website" in command:
            open_website("https://google.com")
        elif "search" in command:
            google_search("Python tutorials")
        elif "ocr" in command:
            image_path = input("Enter image path: ")
            text = perform_ocr(image_path)
            print("Extracted Text:\n", text)
        elif "add schedule" in command:
            event = input("Enter event: ")
            event_time = input("Enter time (e.g., 10:00 AM): ")
            print(add_schedule(event, event_time))
        elif "view schedule" in command:
            print("Your Schedule:\n", view_schedule())
        elif "generate text" in command:
            prompt = input("Enter your prompt: ")
            result = generate_text(prompt, "ollama")
            print(result)
            speak("Text generation complete.")
        elif "translate" in command:
            speak("Please say the text you want to translate.")
            text = listen()
            speak("Which language should I translate to?")
            target_language = listen()
            translated_text = asyncio.run(translate_text(text, str(target_language)))
            speak(f"Translation: {translated_text}")
            speak_translated_text(translated_text, target_language)
        elif "change " in command:
            eco_mode(jarvis_ui)
        

        else:
            response = get_ollama_response(command)
            speak(response)
            jarvis_ui.update_status(f"🤖 {response}")

        save_history(command, response)


def main():
    print("\U0001F680 Running Main Function...")
    speak("Initializing system...")

    if not password_auth():
        print("❌ Access Denied! Exiting...")
        sys.exit(1)

    print("✅ Password Verified! Proceeding...")

    app = QApplication(sys.argv)
    jarvis_ui = JarvisUI()
    jarvis_ui.show()

    jarvis_ui.start_waveform_animation()
    time.sleep(3)
    jarvis_ui.stop_waveform_animation()

    if not capture_face() or not verify_face():
        speak("Face verification failed! Exiting.")
        jarvis_ui.update_status("❌ Access Denied!")
        return

    jarvis_ui.stop_face_scan_effect()
    jarvis_ui.update_status("✅ Face Verified!")
    speak("Face verification successful!")

    jarvis_ui.start_waveform_animation()
    jarvis_ui.update_status("\U0001F3A4 Say your password...")

    if not verify_voice():
        speak("Voice verification failed! Access denied.")
        jarvis_ui.update_status("❌ Access Denied!")
        return

    jarvis_ui.stop_waveform_animation()
    jarvis_ui.update_status("✅ Authentication successful!")
    speak("Authentication successful! Welcome, Shiva Mani.")

    jarvis_ui.enable_system_dashboard()

    while True:
        command = listen_for_jarvis()
        process_command(command, jarvis_ui)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

