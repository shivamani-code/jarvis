# # import JarvisBrain
# # import sys
# # from brain import JarvisBrain

# # import time
# # import asyncio
# # import speech_recognition as sr
# # from PyQt6.QtWidgets import QApplication

# # from password_auth_ui import password_auth
# # from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
# # from ui import JarvisUI
# # from speech import listen, speak
# # from ocr import perform_ocr
# # from schedule_manager import add_schedule, view_schedule
# # from face_auth import capture_face, verify_face
# # from voice_auth import verify_voice
# # from system_control import *
# # from text_generator import generate_text
# # from image_generator import generate_image
# # import ollama
# # from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
# # from translator import translate_text, speak_translated_text
# # from task_manager import add_task, view_tasks


# # def get_ollama_response(command):
# #     """Process user commands with Ollama AI."""
# #     try:
# #         if not isinstance(command, str):
# #             command = str(command)
# #         response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": command}])
# #         return response.get('message', {}).get('content', 'No response')
# #     except Exception as e:
# #         return f"Error with Ollama: {e}"


# # def listen_for_jarvis():
# #     """Continuously listen for 'Jarvis' wake word."""
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Waiting for wake word 'Jarvis'...")
# #         while True:
# #             try:
# #                 audio = recognizer.listen(source)
# #                 text = recognizer.recognize_google(audio).lower()
# #                 if "jarvis" in text:
# #                     print("✅ Wake word detected! Listening for command...")
# #                     speak("Yes, how can I assist?")
# #                     return listen()
# #             except sr.UnknownValueError:
# #                 continue
# #             except sr.RequestError:
# #                 print("Speech recognition service error.")


# # def eco_mode(jarvis_ui):
# #     """Voice-based conversation mode."""
# #     speak("Eco mode activated. You can now have a conversation with me.")
# #     jarvis_ui.update_status("🌿 Eco Mode Activated.")

# #     while True:
# #         user_input = listen().lower()
# #         jarvis_ui.update_status(f"🗣️ {user_input}")

# #         if "exit eco mode" in user_input:
# #             speak("Exiting eco mode.")
# #             jarvis_ui.update_status("❌ Exiting Eco Mode.")
# #             break

# #         response = get_ollama_response(user_input)
# #         speak(response)
# #         jarvis_ui.update_status(f"🤖 {response}")


# # def main():
# #     print("\U0001F680 Running Main Function...")
# #     speak("Initializing system...")

# #     # 🔹 Password Authentication
# #     if not password_auth():
# #         print("❌ Access Denied! Exiting...")
# #         sys.exit(1)

# #     print("✅ Password Verified! Proceeding...")

# #     app = QApplication(sys.argv)
# #     jarvis_ui = JarvisUI()
# #     jarvis_ui.show()

# #     # 🔹 Loading Animation Before Face Authentication
# #     jarvis_ui.start_waveform_animation()
# #     time.sleep(3)
# #     jarvis_ui.stop_waveform_animation()

# #     if not capture_face() or not verify_face():
# #         speak("Face verification failed! Exiting.")
# #         jarvis_ui.update_status("❌ Access Denied!")
# #         return

# #     jarvis_ui.stop_face_scan_effect()
# #     jarvis_ui.update_status("✅ Face Verified!")
# #     speak("Face verification successful!")

# #     # 🔹 Voice Authentication
# #     jarvis_ui.start_waveform_animation()
# #     jarvis_ui.update_status("\U0001F3A4 Say your password...")

# #     if not verify_voice():
# #         speak("Voice verification failed! Access denied.")
# #         jarvis_ui.update_status("❌ Access Denied!")
# #         return

# #     jarvis_ui.stop_waveform_animation()
# #     jarvis_ui.update_status("✅ Authentication successful!")
# #     speak("Authentication successful! Welcome, Shiva Mani.")

# #     # 🔹 System Control Dashboard
# #     jarvis_ui.enable_system_dashboard()

# #     while True:
# #         command = listen_for_jarvis()
# #         if command:
# #             jarvis_ui.update_status(f"🗣️ {command}")

# #             if "exit" in command:
# #                 speak("Goodbye! Shutting down.")
# #                 break

# #             elif "shutdown" in command:
# #                 shutdown()
# #             elif "restart" in command:
# #                 restart()
# #             elif "sleep" in command:
# #                 sleep()
# #             elif "lock" in command:
# #                 lock()
# #             elif "volume up" in command:
# #                 adjust_volume('up')
# #             elif "volume down" in command:
# #                 adjust_volume('down')
# #             elif "mute" in command:
# #                 mute()
# #             elif "take screenshot" in command:
# #                 take_screenshot()
# #             elif "empty recycle bin" in command:
# #                 empty_recycle_bin()
# #             elif "create folder" in command:
# #                 create_folder("NewFolder", "C:\\")
# #             elif "delete folder" in command:
# #                 delete_folder("C:\\NewFolder")
# #             elif "open folder" in command:
# #                 open_folder("C:\\")
# #             elif "search file" in command:
# #                 print(search_file("test.txt", "C:\\"))
# #             elif "copy file" in command:
# #                 copy_file("source.txt", "destination.txt")
# #             elif "extract zip" in command:
# #                 extract_zip("archive.zip", "C:\\extracted")
# #             elif "wifi on" in command:
# #                 wifi_on_off(True)
# #             elif "wifi off" in command:
# #                 wifi_on_off(False)
# #             elif "check speed" in command:
# #                 print(check_speed())
# #             elif "get ip" in command:
# #                 print(get_ip())
# #             elif "flush dns" in command:
# #                 flush_dns()
# #             elif "send email" in command:
# #                 send_email_voice()
# #             elif "read emails" in command:
# #                 read_unread_emails_voice()
# #             elif "send whatsapp message" in command:
# #                 send_whatsapp_voice()
# #             elif "send telegram message" in command:
# #                 send_telegram_voice()
# #             elif "battery status" in command:
# #                 print(battery_status())
# #             elif "task manager" in command:
# #                 print(task_manager())
# #             elif "system uptime" in command:
# #                 print(system_uptime())
# #             elif "cpu usage" in command:
# #                 print(get_cpu_ram_usage())
# #             elif "list processes" in command:
# #                 print(list_running_processes())
# #             elif "kill process" in command:
# #                 print(kill_process("notepad.exe"))
# #             elif "play media" in command:
# #                 play_pause_media()
# #             elif "next track" in command:
# #                 next_track()
# #             elif "previous track" in command:
# #                 previous_track()
# #             elif "set wallpaper" in command:
# #                 set_wallpaper("C:\\wallpaper.jpg")
# #             elif "open website" in command:
# #                 open_website("https://google.com")
# #             elif "google search" in command:
# #                 google_search("Python tutorials")
# #             elif "ocr" in command:
# #                 image_path = input("Enter image path: ")
# #                 text = perform_ocr(image_path)
# #                 print("Extracted Text:\n", text)
# #             elif "add schedule" in command:
# #                 event = input("Enter event: ")
# #                 event_time = input("Enter time (e.g., 10:00 AM): ")
# #                 print(add_schedule(event, event_time))
# #             elif "view schedule" in command:
# #                 print("Your Schedule:\n", view_schedule())
# #             elif "generate text" in command:
# #                 prompt = input("Enter your prompt: ")
# #                 result = generate_text(prompt, "ollama")
# #                 print(result)
# #                 speak("Text generation complete.")
# #             elif "translate" in command:
# #                 speak("Please say the text you want to translate.")
# #                 text = listen()
# #                 speak("Which language should I translate to?")
# #                 target_language = listen()
# #                 translated_text = asyncio.run(translate_text(text, str(target_language)))
# #                 speak(f"Translation: {translated_text}")
# #                 speak_translated_text(translated_text, target_language)
# #             elif "change mode to eco" in command:
# #                 eco_mode(jarvis_ui)
# #             else:
# #                 response = get_ollama_response(command)
# #                 speak(response)
# #                 jarvis_ui.update_status(f"🤖 {response}")

# #     sys.exit(app.exec())


# # if __name__ == "__main__":
# #     main()




# import sys
# import time

# import asyncio
# import speech_recognition as sr
# from PyQt6.QtWidgets import QApplication

# # Import Jarvis Brain
# from brain import JarvisBrain
# from password_auth_ui import password_auth
# from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
# from ui import JarvisUI
# from speech import listen, speak
# from ocr import perform_ocr
# from schedule_manager import add_schedule, view_schedule
# from face_auth import capture_face, verify_face
# from voice_auth import verify_voice
# from system_control import *
# from text_generator import generate_text
# from image_generator import generate_image
# import ollama
# from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
# from translator import translate_text, speak_translated_text
# from task_manager import add_task, view_tasks

# # Initialize Jarvis Brain
# jarvis_brain = JarvisBrain()

# def get_ollama_response(command):
#     """Process user commands with Ollama AI."""
#     try:
#         if not isinstance(command, str):
#             command = str(command)
#         response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": command}])
#         return response.get('message', {}).get('content', 'No response')
#     except Exception as e:
#         return f"Error with Ollama: {e}"


# def listen_for_jarvis():
#     """Continuously listen for 'Jarvis' wake word."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Waiting for wake word 'Jarvis'...")
#         while True:
#             try:
#                 audio = recognizer.listen(source)
#                 text = recognizer.recognize_google(audio).lower()
#                 if "jarvis" in text:
#                     print("✅ Wake word detected! Listening for command...")
#                     speak("Yes, how can I assist?")
#                     return listen()
#             except sr.UnknownValueError:
#                 continue
#             except sr.RequestError:
#                 print("Speech recognition service error.")


# def process_command(command, jarvis_ui):
#     """Processes the user command with AI brain first, then system functions."""
#     response = jarvis_brain.analyze_command(command)

#     if response != "I'm still learning. Can you rephrase?":
#         # If the brain understands, process the response
#         speak(response)
#         jarvis_ui.update_status(f"🤖 {response}")
#     else:
#         # Fallback to system functions if the brain doesn’t understand
#         jarvis_ui.update_status(f"🗣️ {command}")

#         if "exit" in command:
#             speak("Goodbye! Shutting down.")
#             sys.exit()

#         elif "shutdown" in command:
#             shutdown()
#         elif "restart" in command:
#             restart()
#         elif "sleep" in command:
#             sleep()
#         elif "lock" in command:
#             lock()
#         elif "volume up" in command:
#             adjust_volume('up')
#         elif "volume down" in command:
#             adjust_volume('down')
#         elif "mute" in command:
#             mute()
#         elif "take screenshot" in command:
#             take_screenshot()
#         elif "empty recycle bin" in command:
#             empty_recycle_bin()
#         elif "create folder" in command:
#             create_folder("NewFolder", "C:\\")
#         elif "change mode to gork" in command:
#            gork_mode(jarvis_ui)

#         elif "delete folder" in command:
#             delete_folder("C:\\NewFolder")
#         elif "open folder" in command:
#             open_folder("C:\\")
#         elif "search file" in command:
#             print(search_file("test.txt", "C:\\"))
#         elif "copy file" in command:
#             copy_file("source.txt", "destination.txt")
#         elif "extract zip" in command:
#             extract_zip("archive.zip", "C:\\extracted")
#         elif "wifi on" in command:
#             wifi_on_off(True)
#         elif "wifi off" in command:
#             wifi_on_off(False)
#         elif "check speed" in command:
#             print(check_speed())
#         elif "get ip" in command:
#             print(get_ip())
#         elif "flush dns" in command:
#             flush_dns()
#         elif "send email" in command:
#             send_email_voice()
#         elif "read emails" in command:
#             read_unread_emails_voice()
#         elif "send whatsapp message" in command:
#             send_whatsapp_voice()
#         elif "send telegram message" in command:
#             send_telegram_voice()
#         elif "battery status" in command:
#             print(battery_status())
#         elif "task manager" in command:
#             print(task_manager())
#         elif "system uptime" in command:
#             print(system_uptime())
#         elif "current_cpu usage" in command:
#             print(get_cpu_ram_usage())
#         elif "list processes" in command:
#             print(list_running_processes())
#         elif "kill process" in command:
#             print(kill_process("notepad.exe"))
#         elif "play media" in command:
#             play_pause_media()
#         elif "next track" in command:
#             next_track()
#         elif "previous track" in command:
#             previous_track()
#         elif "set wallpaper" in command:
#             set_wallpaper("C:\\wallpaper.jpg")
#         elif "open website" in command:
#             open_website("https://google.com")
#         elif "google search" in command:
#             google_search("Python tutorials")
#         elif "ocr" in command:
#             image_path = input("Enter image path: ")
#             text = perform_ocr(image_path)
#             print("Extracted Text:\n", text)
#         elif "add schedule" in command:
#             event = input("Enter event: ")
#             event_time = input("Enter time (e.g., 10:00 AM): ")
#             print(add_schedule(event, event_time))
#         elif "view schedule" in command:
#             print("Your Schedule:\n", view_schedule())
#         elif "generate text" in command:
#             prompt = input("Enter your prompt: ")
#             result = generate_text(prompt, "ollama")
#             print(result)
#             speak("Text generation complete.")
#         elif "translate" in command:
#             speak("Please say the text you want to translate.")
#             text = listen()
# #             speak("Which language should I translate to?")
# #             target_language = listen()
# #             translated_text = asyncio.run(translate_text(text, str(target_language)))
# #             speak(f"Translation: {translated_text}")
# #             speak_translated_text(translated_text, target_language)
# #         elif "change " in command:
# #             eco_mode(jarvis_ui)
# #         else:
# #             response = get_ollama_response(command)
# #             speak(response)
# #             jarvis_ui.update_status(f"🤖 {response}")


# # def main():
# #     print("\U0001F680 Running Main Function...")
# #     speak("Initializing system...")

# #     if not password_auth():
# #         print("❌ Access Denied! Exiting...")
# #         sys.exit(1)

# #     print("✅ Password Verified! Proceeding...")

# #     app = QApplication(sys.argv)
# #     jarvis_ui = JarvisUI()
# #     jarvis_ui.show()

# #     jarvis_ui.start_waveform_animation()
# #     time.sleep(3)
# #     jarvis_ui.stop_waveform_animation()

# #     if not capture_face() or not verify_face():
# #         speak("Face verification failed! Exiting.")
# #         jarvis_ui.update_status("❌ Access Denied!")
# #         return

# #     jarvis_ui.stop_face_scan_effect()
# #     jarvis_ui.update_status("✅ Face Verified!")
# #     speak("Face verification successful!")

# #     jarvis_ui.start_waveform_animation()
# #     jarvis_ui.update_status("\U0001F3A4 Say your password...")

# #     if not verify_voice():
# #         speak("Voice verification failed! Access denied.")
# #         jarvis_ui.update_status("❌ Access Denied!")
# #         return

# #     jarvis_ui.stop_waveform_animation()
# #     jarvis_ui.update_status("✅ Authentication successful!")
# #     speak("Authentication successful! Welcome, Shiva Mani.")

# #     jarvis_ui.enable_system_dashboard()

# #     while True:
# #         command = listen_for_jarvis()
# #         process_command(command, jarvis_ui)

# #     sys.exit(app.exec())


# # if __name__ == "__main__":
# #     main()

# import os
# import psutil
# import pyautogui
# import subprocess
# import shutil
# import webbrowser
# import time
# import speedtest
# import socket
# import ctypes
# import sys
# import asyncio
# import speech_recognition as sr
# from datetime import datetime
# from PyQt6.QtWidgets import QApplication

# # Import modules
# from brain import JarvisBrain
# from password_auth_ui import password_auth
# from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
# from ui import JarvisUI
# from speech import listen, speak
# from ocr import perform_ocr
# from schedule_manager import add_schedule, view_schedule
# from face_auth import capture_face, verify_face
# from voice_auth import verify_voice
# from system_control import *
# from text_generator import generate_text
# from translator import translate_text, speak_translated_text
# from task_manager import add_task, view_tasks
# import ollama

# # Initialize Jarvis Brain
# jarvis_brain = JarvisBrain()

# # Command Processing
# HISTORY_FILE = "history.txt"

# def save_history(command, response):
#     with open(HISTORY_FILE, "a", encoding="utf-8") as file:
#         file.write(f"User: {command}\nJarvis: {response}\n\n")

# def view_history():
#     try:
#         with open(HISTORY_FILE, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "No history found."

# def listen_for_jarvis():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Waiting for wake word 'Jarvis'...")
#         while True:
#             try:
#                 audio = recognizer.listen(source, timeout=None, phrase_time_limit=3)
#                 text = recognizer.recognize_google(audio).lower()
#                 print(f"🗣️ Heard: {text}")
#                 if "jarvis" in text:
#                     speak("Yes, how can I assist?")
#                     return listen_command()
#             except sr.UnknownValueError:
#                 continue
#             except sr.RequestError:
#                 print("⚠️ Speech recognition service error.")
#                 return None

# def listen_command(timeout=5):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print(f"🎤 Listening for command... (Timeout: {timeout}s)")
#         try:
#             audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=4)
#             command = recognizer.recognize_google(audio).lower()
#             print(f"✅ Command received: {command}")
#             return command
#         except sr.UnknownValueError:
#             print("❌ Could not understand.")
#             return None
#         except sr.RequestError:
#             print("⚠️ API error.")
#             return None
#         except sr.WaitTimeoutError:
#             print("⏳ No command detected. Returning to wake mode...")
#             return None

# last_command = None  # Initialize globally

# def prevent_loop(command):
#     global last_command  
#     if command == last_command:
#         return True  # Prevents repeating the same command
#     last_command = command  # Store the last executed command
#     return False



# /

# def main():
#     print("\U0001F680 Running Main Function...")
#     speak("Initializing system...")

#     if not password_auth():
#         print("❌ Access Denied! Exiting...")
#         sys.exit(1)

#     print("✅ Password Verified! Proceeding...")

#     app = QApplication(sys.argv)
#     jarvis_ui = JarvisUI()
#     jarvis_ui.show()

#     jarvis_ui.start_waveform_animation()
#     time.sleep(3)
#     jarvis_ui.stop_waveform_animation()

#     if not capture_face() or not verify_face():
#         speak("Face verification failed! Exiting.")
#         jarvis_ui.update_status("❌ Access Denied!")
#         return

#     jarvis_ui.stop_face_scan_effect()
#     jarvis_ui.update_status("✅ Face Verified!")
#     speak("Face verification successful!")

#     jarvis_ui.start_waveform_animation()
#     jarvis_ui.update_status("\U0001F3A4 Say your password...")

#     if not verify_voice():
#         speak("Voice verification failed! Access denied.")
#         jarvis_ui.update_status("❌ Access Denied!")
#         return

#     jarvis_ui.stop_waveform_animation()
#     jarvis_ui.update_status("✅ Authentication successful!")
#     speak("Authentication successful! Welcome, Shiva Mani.")

#     jarvis_ui.enable_system_dashboard()

#     while True:
#         command = listen_for_jarvis()
#         process_command(command, jarvis_ui)

#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()




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

# ---------------------- ADD THESE IMPORTS AT TOP ---------------------- #
import screen_brightness_control as sbc
import psutil
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ---------------------- ADD THESE FUNCTIONS IN SYSTEM CONTROL SECTION ---------------------- #
def set_brightness(level):
    sbc.set_brightness(level)
    return f"Brightness set to {level}%"

def system_action(action):
    if os.name == 'nt':
        commands = {
            'shutdown': 'shutdown /s /t 1',
            'restart': 'shutdown /r /t 1',
            'sleep': 'rundll32.exe powrprof.dll,SetSuspendState 0,1,0'
        }
    else:
        commands = {
            'shutdown': 'shutdown -h now',
            'restart': 'shutdown -r now',
            'sleep': 'pmset sleepnow'
        }
    os.system(commands[action])
    return f"System {action} initiated"

def volume_control(direction):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    if direction == 'up':
        volume.SetMasterVolumeLevelScalar(min(1.0, current + 0.1), None)
    else:
        volume.SetMasterVolumeLevelScalar(max(0.0, current - 0.1), None)
    return f"Volume {direction}"

# ---------------------- MODIFY PROCESS_COMMAND (UNCOMMENT AND UPDATE) ---------------------- #
def process_command(command, jarvis_ui):
    """Processes the user command with AI brain first, then system functions."""
    response = jarvis_brain.analyze_command(command)

    if response != "I'm still learning. Can you rephrase?":
        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")
    else:
        jarvis_ui.update_status(f"🗣️ {command}")

        # System Control (Uncomment and update)
        if "shutdown" in command:
            response = system_action('shutdown')
        elif "restart" in command:
            response = system_action('restart')
        elif "sleep" in command:
            response = system_action('sleep')
        elif "lock" in command:
            response = system_action('lock')
        elif "volume up" in command:
            response = volume_control('up')
        elif "volume down" in command:
            response = volume_control('down')
        elif "mute" in command:
            response = volume_control('mute')
        elif "brightness" in command:
            level = int(''.join(filter(str.isdigit, command)))
            response = set_brightness(level)

        # Web Automation
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            response = "Opening YouTube"
        elif "search" in command:
            query = command.split("search")[-1].strip()
            webbrowser.open(f"https://google.com/search?q={query}")
            response = f"Searching for {query}"

        # Fallback to AI
        else:
            response = get_ollama_response(command)

        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")

    save_history(command, response)

# def process_command(command, jarvis_ui):
#     """Processes the user command with AI brain first, then system functions."""
#     response = jarvis_brain.analyze_command(command)

#     if response != "I'm still learning. Can you rephrase?":
#         # If the brain understands, process the response
#         speak(response)
#         jarvis_ui.update_status(f"🤖 {response}")
#     else:
#         # Fallback to system functions if the brain doesn’t understand
#         jarvis_ui.update_status(f"🗣️ {command}")

#         if "exit" in command:
#             speak("Goodbye! Shutting down.")
#             sys.exit()
        
#          # Normalize the command
#         if 'cpu temperature' in command:
#             response = get_cpu_temperature()
#         elif 'uptime' in command:
#             response = get_system_uptime()
#         elif 'shutdown' in command:
#             response = shutdown_computer()
#         else:
#             response = "I couldn't recognize that command."
#         jarvis_ui.display_response(response)

        # elif "shutdown" in command:
        #     shutdown()
        # elif "restart" in command:
        #     restart()
        # elif "sleep" in command:
        #     sleep()
        # elif "lock" in command:
        #     lock()
        # elif "volume up" in command:
        #     adjust_volume('up')
        # elif "volume down" in command:
        #     adjust_volume('down')
        # elif "mute" in command:
        #     mute()
        # elif "take screenshot" in command:
        #     take_screenshot()
        # elif "empty recycle bin" in command:
        #     empty_recycle_bin()
        # elif "create folder" in command:
        #     create_folder("NewFolder", "C:\\")
        # elif "change mode to gork" in command:
        #    gork_mode(jarvis_ui)

        # elif "delete folder" in command:
        #     delete_folder("C:\\NewFolder")
        # elif "open folder" in command:
        #     open_folder("C:\\")
        # elif "search file" in command:
        #     print(search_file("test.txt", "C:\\"))
        # elif "copy file" in command:
        #     copy_file("source.txt", "destination.txt")
        # elif "extract zip" in command:
        #     extract_zip("archive.zip", "C:\\extracted")
        # elif "wifi on" in command:
        #     wifi_on_off(True)
        # elif "wifi off" in command:
        #     wifi_on_off(False)
        # elif "check speed" in command:
        #     print(check_speed())
        # elif "get ip" in command:
        #     print(get_ip())
        # elif "flush dns" in command:
        #     flush_dns()
        # elif "send email" in command:
        #     send_email_voice()
        # elif "read emails" in command:
        #     read_unread_emails_voice()
        # elif "send whatsapp message" in command:
        #     send_whatsapp_voice()
        # elif "send telegram message" in command:
        #     send_telegram_voice()
        # elif "battery status" in command:
        #     print(battery_status())
        # elif "task manager" in command:
        #     print(task_manager())
        # elif "system uptime" in command:
        #     print(system_uptime())
        # elif "current_cpu usage" in command:
        #     print(get_cpu_ram_usage())
        # elif "list processes" in command:
        #     print(list_running_processes())
        # elif "kill process" in command:
        #     print(kill_process("notepad.exe"))
        # elif "play media" in command:
        #     play_pause_media()
        # elif "next track" in command:
        #     next_track()
        # elif "previous track" in command:
        #     previous_track()
        # elif "set wallpaper" in command:
        #     set_wallpaper("C:\\wallpaper.jpg")
        # elif "open website" in command:
        #     open_website("https://google.com")
        # elif "google search" in command:
        #     google_search("Python tutorials")
        # elif "ocr" in command:
        #     image_path = input("Enter image path: ")
        #     text = perform_ocr(image_path)
        #     print("Extracted Text:\n", text)
        # elif "add schedule" in command:
        #     event = input("Enter event: ")
        #     event_time = input("Enter time (e.g., 10:00 AM): ")
        #     print(add_schedule(event, event_time))
        # elif "view schedule" in command:
        #     print("Your Schedule:\n", view_schedule())
        # elif "generate text" in command:
        #     prompt = input("Enter your prompt: ")
        #     result = generate_text(prompt, "ollama")
        #     print(result)
        #     speak("Text generation complete.")
     
        # elif 'cpu temperature' in command.lower():
        #     response = get_cpu_temperature()
        # elif 'system uptime' in command.lower():
        #     response = get_system_uptime()
        # elif 'shutdown' in command.lower():
        #     response = shutdown_computer()
        # elif 'open browser' in command.lower():
        #     response = open_browser()
        # elif 'list files' in command.lower():
        #     response = list_files()
        # elif 'play music' in command.lower():
        #     response = play_music()
        # elif 'disk space' in command.lower():
        #     response = check_disk_space()
        # elif 'system info' in command.lower():
        #     response = get_system_info()
        
        # elif "translate" in command:
        #     speak("Please say the text you want to translate.")
        #     text = listen()
        #     speak("Which language should I translate to?")
        #     target_language = listen()
        #     translated_text = asyncio.run(translate_text(text, str(target_language)))
        #     speak(f"Translation: {translated_text}")
        #     speak_translated_text(translated_text, target_language)
        # elif "change " in command:
        #     eco_mode(jarvis_ui)
        # else:
        #     response = get_ollama_response(command)
        #     speak(response)
        #     jarvis_ui.update_status(f"🤖 {response}")






# def process_command(command, jarvis_ui):
#     """Processes user commands and prioritizes system functions before AI."""
#     if not command:
#         return  # If no command, do nothing

#     command = command.lower().strip()  # Normalize input

#     if prevent_loop(command):
#         return  # Stop processing if command repeats too much

#     jarvis_ui.update_status(f"🗣️ {command}")

# #     # ---------------------- SYSTEM CONTROL COMMANDS ---------------------- #
#     if command == "shutdown":
#         shutdown_system()
#     elif command == "restart":
#         restart_system()
#     elif command == "sleep":
#         sleep()
#     elif command == "lock":
#         lock_system()
#     elif command.startswith("weather"):
#         city = command.split(" ", 1)[1]
#         response = get_weather(city)
#     elif command == "cpu temp":
#         response = get_cpu_temperature()
#     elif command.startswith("reminder"):
#         _, text, delay = command.split(" ", 2)
#         set_reminder(text, int(delay))
#     elif command.startswith("open app"):
#         app_name = command.split(" ", 2)[2]
#         open_application(app_name)
#     elif command.startswith("close app"):
#         app_name = command.split(" ", 2)[2]
#         close_application(app_name)
#     elif command == "running processes":
#         list_running_processes()
#     elif command.startswith("kill process"):
#         process_name = command.split(" ", 2)[2]
#         response = kill_process(process_name)
#     elif command.startswith("volume"):
#         level = int(command.split(" ")[1])
#         adjust_volume(level)
#     elif command == "mute":
#         toggle_mute()
#     elif command == "play":
#         play_pause_media()
#     elif command == "next":
#         next_track()
#     elif command == "previous":
#         previous_track()
#     elif command.startswith("create folder"):
#         _, name, path = command.split(" ", 2)
#         create_folder(name, path)
#     elif command.startswith("delete folder"):
#         path = command.split(" ", 2)[2]
#         delete_folder(path)
#     elif command.startswith("open folder"):
#         path = command.split(" ", 2)[2]
#         open_folder(path)
#     elif command.startswith("search file"):
#         _, filename, directory = command.split(" ", 2)
#         response = search_file(filename, directory)
#     elif command.startswith("copy file"):
#         _, src, dest = command.split(" ", 2)
#         copy_file(src, dest)
#     elif command.startswith("extract zip"):
#         _, zip_path, extract_to = command.split(" ", 2)
#         extract_zip(zip_path, extract_to)
#     elif command.startswith("delete file"):
#         file_path = command.split(" ", 2)[2]
#         delete_file(file_path)
#     elif command == "file explorer":
#         open_file_explorer()
#     elif command == "battery status":
#         response = battery_status()
#     elif command == "uptime":
#         response = system_uptime()
#     elif command == "cpu ram usage":
#         response = get_cpu_ram_usage()
#     elif command == "storage check":
#         response = check_storage()
#     elif command == "high cpu process":
#         response = find_high_cpu_process()
#     elif command.startswith("wifi"):
#         state = command.split(" ")[1]
#         wifi_on_off(state)
#     elif command == "speed test":
#         response = check_speed()
#     elif command == "ip address":
#         response = get_ip()
#     elif command == "flush dns":
#         flush_dns()
#     elif command == "screenshot":
#         take_screenshot()
#     elif command == "clear clipboard":
#         clear_clipboard()
#     elif command.startswith("open website"):
#         url = command.split(" ", 2)[2]
#         open_website(url)
#     elif command.startswith("google search"):
#         query = command.split(" ", 2)[2]
#         google_search(query)
#     elif command.startswith("youtube search"):
#         query = command.split(" ", 2)[2]
#         youtube_search(query)
#     elif command == "datetime":
#         response = get_datetime()
#     elif command.startswith("change wallpaper"):
#         image_path = command.split(" ", 2)[2]
#         change_wallpaper(image_path)
#     elif command.startswith("write notepad"):
#         text = command.split(" ", 2)[2]
#         write_in_notepad(text)
#     elif command.startswith("generate password"):
#         length = int(command.split(" ")[2])
#         response = generate_password(length)
#     elif command == "empty recycle bin":
#         empty_recycle_bin()
#     elif command == "clear downloads":
#         clear_downloads()
#     elif command == "list apps":
#         list_installed_apps()
#     elif command.startswith("brightness"):
#         level = int(command.split(" ")[1])
#         adjust_brightness(level)
#     elif command == "calculator":
#         open_calculator()
#     elif command == "system info":
#         response = system_info()



    # if command.startswith("shutdown"):
    #     shutdown()
    # elif command.startswith("restart"):
    #     restart()
    # elif command.startswith("sleep"):
    #     sleep()
    # elif command.startswith("lock"):
    #     lock()
    # elif command.startswith("volume up"):
    #     adjust_volume('up')
    # elif command.startswith("volume down"):
    #     adjust_volume('down')
    # elif command.startswith("mute"):
    #     mute()
    # elif command.startswith("take screenshot"):
    #     take_screenshot()
    # elif command.startswith("empty recycle bin"):
    #     empty_recycle_bin()

    # # ---------------------- IMAGE GENERATION ---------------------- #
    # elif "generate image" in command:
    #     parts = command.split("using")  # Example: "generate image of a car using deepai"
    #     if len(parts) == 2:
    #         prompt = parts[0].replace("generate image", "").strip()
    #         method = parts[1].strip().lower()
    #         image_url = generate_image(prompt, method)
    #         response = f"Image generated using {method}. Opening..."
    #         show_image(image_url)
    #     else:
    #         response = "Invalid format. Use: 'generate image of [object] using [method]'"

    # # ---------------------- FILE & FOLDER MANAGEMENT ---------------------- #
    # elif command.startswith("create folder"):
    #     folder_name = command.replace("create folder", "").strip()
    #     create_folder(folder_name, "C:\\")
    # elif command.startswith("delete folder"):
    #     folder_name = command.replace("delete folder", "").strip()
    #     delete_folder(f"C:\\{folder_name}")
    # elif command.startswith("open folder"):
    #     folder_path = command.replace("open folder", "").strip()
    #     open_folder(folder_path)
    # elif command.startswith("open application"):
    #     app_name = command.replace("open application", "").strip()
    #     open_application(app_name)
    # elif command.startswith("close application"):
    #     app_name = command.replace("close application", "").strip()
    #     close_application(app_name)
    # elif command.startswith("search file"):
    #     file_name = command.replace("search file", "").strip()
    #     search_file(file_name, "C:\\")

    # # ---------------------- NETWORK & SYSTEM INFO ---------------------- #
    # elif command.startswith("wifi on"):
    #     wifi_on_off(True)
    # elif command.startswith("wifi off"):
    #     wifi_on_off(False)
    # elif command.startswith("check speed"):
    #     check_speed()
    # elif command.startswith("get ip"):
    #     get_ip()
    # elif command.startswith("flush dns"):
    #     flush_dns()
    # elif command.startswith("task manager"):
    #     task_manager()

    # # ---------------------- MODE CHANGES ---------------------- #
    # elif command.startswith("change mode to gork"):
    #     gork_mode(jarvis_ui)
    # elif command.startswith("change mode to eco"):
    #     eco_mode(jarvis_ui)

    # # ---------------------- SEARCH COMMANDS ---------------------- #
    # elif command.startswith("search"):
    #     query = command.replace("search", "").strip()
    #     google_search(query)

    # ---------------------- AI RESPONSE FALLBACK ---------------------- #
    # else:
    #     response = get_ollama_response(command)  # **Only call Ollama if no other command matches**
    #     speak(response)
    #     jarvis_ui.update_status(f"🤖 {response}")

    save_history(command, response)


# ---------------------- MAIN FUNCTION ---------------------- #
def main():
    print("🚀 Running Main Function...")
    speak("Initializing system...")

    # if not password_auth():
    #     print("❌ Access Denied! Exiting...")
    #     sys.exit(1)

    # print("✅ Password Verified! Proceeding...")

    app = QApplication(sys.argv)
    jarvis_ui = JarvisUI()
    jarvis_ui.show()

    # if not capture_face() or not verify_face():
    #     speak("Face verification failed! Exiting.")
    #     jarvis_ui.update_status("❌ Access Denied!")
    #     return

    # speak("Face verification successful!")

    # if not verify_voice():
    #     speak("Voice verification failed! Access denied.")
    #     jarvis_ui.update_status("❌ Access Denied!")
    #     return

    # speak("Authentication successful! Welcome!")

    while True:
        command = listen_for_jarvis()  # ✅ Fix: Removed timeout argument
        process_command(command, jarvis_ui)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
