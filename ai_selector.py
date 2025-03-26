import requests
import ollama
import google.generativeai as genai
import speech_recognition as sr

# Together AI API URL & Key
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = "your_together_api_key"  # Replace with your API key

# Gemini AI Configuration
genai.configure(api_key="your_gemini_api_key")  # Replace with your API key

def get_ai_response(prompt, method):
    """
    Generate a response based on the selected AI method.
    Available methods: 'ollama', 'gemini', 'together'
    """
    if method == "ollama":
        return generate_with_ollama(prompt)
    elif method == "gemini":
        return generate_with_gemini(prompt)
    elif method == "together":
        return generate_with_together(prompt)
    else:
        return "Invalid method. Choose: ollama, gemini, or together."

# ========================= OLLAMA =========================
def generate_with_ollama(prompt):
    """
    Generates a response using Ollama AI.
    """
    try:
        response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": prompt}])
        return response.get("message", "No response from Ollama.")
    except Exception as e:
        return f"Ollama API error: {e}"

# ========================= GEMINI =========================
def generate_with_gemini(prompt):
    """
    Generates a response using Gemini AI.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text if response else "No response from Gemini."
    except Exception as e:
        return f"Gemini API error: {e}"

# ========================= TOGETHER AI =========================
def generate_with_together(prompt):
    """
    Generates a response using Together AI.
    """
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "mistral",
        "messages": [{"role": "user", "content": prompt}],
    }
    
    try:
        response = requests.post(TOGETHER_API_URL, json=payload, headers=headers)
        data = response.json()
        return data["choices"][0]["message"]["content"] if "choices" in data else "No response from Together AI."
    except Exception as e:
        return f"Together AI API error: {e}"

# ========================= VOICE INPUT =========================
def listen_voice():
    """
    Captures voice input and converts it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for prompt...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"🗣️ Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError:
            print("❌ Speech recognition service error")
            return None
