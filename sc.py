import sys
import time
import asyncio
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication
from image_generation import generate_image, show_image
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

# Command Map for System Functions
command_map = {
    "shutdown": shutdown,
    "restart": restart,
    "sleep": sleep,
    "lock": lock,
    "volume up": lambda: adjust_volume('up'),
    "volume down": lambda: adjust_volume('down'),
    "mute": mute,
    "take screenshot": take_screenshot,
    "empty recycle bin": empty_recycle_bin,
    "wifi on": lambda: wifi_on_off(True),
    "wifi off": lambda: wifi_on_off(False),
    "check speed": check_speed,
    "get ip": get_ip,
    "flush dns": flush_dns,
    "task manager": task_manager,
}

# Process Command Function
def process_command(command, jarvis_ui):
    """Processes the user command dynamically using a command map."""
    
    if command in command_map:
        command_map[command]()  # Execute the function dynamically
        response = f"Executed: {command}"
    elif command.startswith("open application"):
        app_name = command.replace("open application", "").strip()
        open_application(app_name)
        response = f"Opening application: {app_name}"
    elif command.startswith("close application"):
        app_name = command.replace("close application", "").strip()
        close_application(app_name)
        response = f"Closing application: {app_name}"
    elif command.startswith("search file"):
        file_name = command.replace("search file", "").strip()
        search_file(file_name, "C:\\")
        response = f"Searching for file: {file_name}"
    else:
        response = jarvis_brain.analyze_command(command)
        if response == "I'm still learning. Can you rephrase?":
            response = get_ollama_response(command)
    
    speak(response)
    jarvis_ui.update_status(f"🤖 {response}")
    save_history(command, response)

# Main Function
def main():
    print("🚀 Running Main Function...")
    speak("Initializing system...")

    # if not password_auth():
    #     print("❌ Access Denied! Exiting...")
    #     sys.exit(1)

    # print("✅ Password Verified! Proceeding...")
    # speak("Password Verified!")

    # app = QApplication(sys.argv)
    # jarvis_ui = JarvisUI()
    # jarvis_ui.show()

    # if not capture_face() or not verify_face():
    #     speak("Face verification failed! Exiting.")
    #     jarvis_ui.update_status("❌ Access Denied!")
    #     return

    # speak("Face verification successful!")

    # if not verify_voice():
    #     speak("Voice verification failed! Access denied.")
    #     jarvis_ui.update_status("❌ Access Denied!")
    #     return

    # speak("Authentication successful! ")
    # speak("Welcome! shiva mani")

    while True:
        command = listen_for_jarvis()
        process_command(command, jarvis_ui)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
