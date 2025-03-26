import gorkai
from speech import listen, speak

def get_gork_response(command):
    """Process user commands using Gork AI."""
    try:
        response = gorkai.chat(model="gork:latest", messages=[{"role": "user", "content": command}])
        return response.get('message', {}).get('content', 'No response from Gork AI')
    except Exception as e:
        return f"Error with Gork AI: {e}"

def gork_mode(jarvis_ui):
    """Activate Gork Mode for intelligent conversations."""
    speak("Gork mode activated. You can now communicate with me.")
    jarvis_ui.update_status("🟢 Gork Mode Activated.")

    while True:
        user_input = listen().lower()
        jarvis_ui.update_status(f"🗣️ {user_input}")

        if "exit gork mode" in user_input:
            speak("Exiting Gork mode.")
            jarvis_ui.update_status("❌ Exiting Gork Mode.")
            break

        response = get_gork_response(user_input)
        speak(response)
        jarvis_ui.update_status(f"🤖 {response}")
