import sys
import time  # Keep this import

from PyQt6.QtWidgets import QApplication
# Remove duplicate "import time" statements
from password_auth_ui import password_auth  # ✅ Import password authentication function

from ui import JarvisUI
from speech import listen, speak
from ocr import perform_ocr
from schedule_manager import add_schedule, view_schedule
from face_auth import capture_face, verify_face  
from voice_auth import verify_voice  
from system_control import *  
 
from text_generator import generate_text

import ollama  
from automation import send_email_voice, read_unread_emails_voice, send_whatsapp_voice, send_telegram_voice
from translator import translate_text, speak_translated_text
from task_manager import add_task, view_tasks
import speech_recognition as sr


def get_ollama_response(command):
    """Generate response using Ollama AI"""
    if not isinstance(command, str):
        command = str(command)

    response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": command}])
    return response


def listen_for_jarvis():
    """Continuously listen for 'Jarvis' wake word."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for wake word 'Jarvis'...")
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                if "jarvis" in text:
                    print("✅ Wake word detected! Listening for command...")
                    speak("Yes, how can I assist?")
                    return listen()  
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Speech recognition service error.")




def main():
    print("\U0001F680 Running Main Function...")
    speak("Initializing system...")

    # 🔹 Run Password Authentication Before Anything
    if not password_auth():
        print("❌ Access Denied! Exiting...")
        sys.exit(1)  # ✅ Corrected indentation

    print("✅ Password Verified! Proceeding...")


    app = QApplication(sys.argv)
    jarvis_ui = JarvisUI()
    jarvis_ui.show()
     
    
    # Loading Animation Before Face Authentication
    jarvis_ui.start_waveform_animation()

    time.sleep(3)  # Simulate loading time
    jarvis_ui.stop_waveform_animation()  # Fixed typo (was `stot_waveform_animation()`)
     
    if not capture_face() or not verify_face():
            speak("Face verification failed! Exiting.")
            jarvis_ui.update_status("❌ Access Denied!")
            return

            jarvis_ui.stop_face_scan_effect()
            jarvis_ui.update_status("✅ Face Verified!")
            speak("Face verification successful!")
            jarvis_ui.start_face_scan_effect()
            jarvis_ui.update_status("\U0001F4F7 Scanning Face...")


        

    # Face Authentication with UI Effects
   
    
    # Voice Authentication with Animated Waveform
    jarvis_ui.start_waveform_animation()
    jarvis_ui.update_status("\U0001F3A4 Say your password...")

     
    if not verify_voice():
        speak("Voice verification failed! Access denied.")
        jarvis_ui.update_status("❌ Access Denied!")
        return

    jarvis_ui.stop_waveform_animation()
    jarvis_ui.update_status("✅ Authentication successful!")
    speak("Authentication successful! Welcome, Shiva Mani.")

    # System Control Dashboard (Live CPU, RAM Updates)
    jarvis_ui.enable_system_dashboard()

    while True:
        command = listen_for_jarvis()  
        if command:
            jarvis_ui.update_status(f"🗣️ {command}")

            if "exit" in command:
                speak("Goodbye! Shutting down.")
                break  

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
            elif "battery status" in command:
                print(battery_status())
            elif "task manager" in command:
                print(task_manager())
            elif "system uptime" in command:
                print(system_uptime())
            elif "cpu usage" in command:
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
            elif "google search" in command:
                google_search("Python tutorials")
            elif "send email" in command:
                send_email("test@example.com", "Subject", "Body")
            elif "open whatsapp" in command:
                open_whatsapp()
            elif "ocr" in command:
                image_path = input("Enter image path: ")
                text = perform_ocr(image_path)
                print("Extracted Text:\n", text)
            elif "add schedule" in command:
                event = input("Enter event: ")
                event_time = input("Enter time (e.g., 10:00 AM): ")  # Fixed variable name
                print(add_schedule(event, event_time))
            elif "view schedule" in command:
                print("Your Schedule:\n", view_schedule())
            elif "generate text" in command:
                speak("Please enter your prompt.")
                prompt = input("Enter your prompt: ")
                result = generate_text(prompt, "ollama")
                print(result)
                speak("Text generation complete.")
            elif "send email" in command:
                send_email_voice()
            elif "read emails" in command:
                read_unread_emails_voice()
            elif "send WhatsApp message" in command:
                send_whatsapp_voice()
            elif "translate" in command:
                speak("Please say the text you want to translate.")
                text = listen()
                speak("Which language should I translate to?")
                target_language = listen()
                translated_text = translate_text(text, target_language)
                speak(f"Translation: {translated_text}")
                speak_translated_text(translated_text, target_language)
            elif "send Telegram message" in command:
                send_telegram_voice()
            else:
                response = get_ollama_response(command)
                speak(response)
                jarvis_ui.update_status(f"🤖 {response}")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# import sys
# from PyQt6.QtWidgets import QApplication
# from ui import JarvisUI
# from speech import listen, speak
# from face_auth import capture_face, verify_face  
# from voice_auth import verify_voice  
# from system_control import execute_command
# from password_auth_ui import password_auth  
# from text_generator import generate_text
# from image_generator import generate_image
# import ollama  # Importing Ollama for AI conversation

# def get_ollama_response(prompt):
#     """Generate response using Ollama AI."""
#     response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def image_generation():
#     """Runs image generation when user commands."""
#     speak("Please select an image generation method.")
#     method = input("Select method (stable_diffusion / huggingface / leonardo): ").strip()
#     speak("Please enter your image prompt.")
#     prompt = input("Enter image prompt: ")
#     result = generate_image(prompt, method)
#     print(result)
#     speak("Image generation complete.")

# def text_generation():
#     """Runs text generation when user commands."""
#     speak("Please select a text generation method.")
#     method = input("Select method (ollama / huggingface): ").strip()
#     speak("Please enter your prompt.")
#     prompt = input("Enter your prompt: ")
#     result = generate_text(prompt, method)
#     print(result)
#     speak("Text generation complete.")

# def main():
#     print("\U0001F680 Running Main Function...")
#     speak("Initializing system...")

#     print("\U0001F512 Please authenticate using your password...")
#     speak("Please authenticate using your password.")
#     if not password_auth():  
#         print("❌ Access Denied! Exiting...")
#         speak("Access denied! Exiting system.")
#         return  

#     print("✅ Password Verified. Initializing system...")
#     speak("Password verified. Initializing system.")

#     print("\U0001F5A5️ Starting UI...")
#     app = QApplication(sys.argv)
#     jarvis_ui = JarvisUI()
#     jarvis_ui.show()

#     jarvis_ui.update_status("\U0001F4F7 Scanning Face...")
#     if not capture_face() or not verify_face():  
#         speak("Face verification failed! Exiting.")
#         jarvis_ui.update_status("❌ Access Denied!")
#         return
#     jarvis_ui.update_status("✅ Face Verified!")
#     speak("Face verification successful!")

#     jarvis_ui.update_status("\U0001F3A4 Say your password...")
#     if not verify_voice():
#         speak("Voice verification failed! Access denied.")
#         jarvis_ui.update_status("❌ Access Denied!")
#         return

#     jarvis_ui.update_status("✅ Authentication successful!")
#     speak("Authentication successful! Welcome, Shiva Mani.")

#     while True:
#         jarvis_ui.update_status("\U0001F3A4 Listening for command...")
#         command = listen().lower()
#         jarvis_ui.update_status(f"🗣️ {command}")

#         if "exit" in command:
#             speak("Goodbye! Shutting down.")
#             break  

#         if execute_command(command):  
#             continue  

#         elif "generate image" in command:
#             image_generation()

#         elif "generate text" in command:
#             text_generation()

#         else:
#             response = get_ollama_response(command)
#             speak(response)
#             jarvis_ui.update_status(f"🤖 {response}")

#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()
