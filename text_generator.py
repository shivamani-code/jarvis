import requests
import ollama
from speech import listen

# ========================= CONFIGURATION =========================
TOGETHER_API_URL = "https://api.together.ai/settings/profile"
TOGETHER_API_KEY = "05f2dfea205800d1f4a82a6b529d841cf2835dee366cdfde24a5f0f9352a6fcf"  # Replace with your API key

GEMINI_API_URL = "https://aistudio.google.com/app/prompts/new_chat"
GEMINI_API_KEY = "AIzaSyB0vlPiCzZt8J7OhcMu4eD4p6lDKchsFNk"  # Replace with your API key

# ========================= TEXT GENERATION FUNCTION =========================
def generate_text(prompt, method):
    if method == "ollama":
        return generate_with_ollama(prompt)
    elif method == "together":
        return generate_with_together(prompt)
    elif method == "gemini":
        return generate_with_gemini(prompt)
    else:
        return "Invalid method. Choose ollama, together, or gemini."

# ========================= OLLAMA (OFFLINE) =========================
def generate_with_ollama(prompt):
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        return f"Ollama Error: {e}"

# ========================= TOGETHER AI (ONLINE API) =========================
def generate_with_together(prompt):
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
    payload = {"model": "mistralai/Mistral-7B-Instruct", "prompt": prompt}

    try:
        response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
        result = response.json()
        return result.get("output", "Together AI Error: No response received.")
    except Exception as e:
        return f"Together AI Error: {e}"

# ========================= GEMINI AI (ONLINE API) =========================
def generate_with_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    payload = {"prompt": {"text": prompt}}

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)
        result = response.json()
        return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Gemini AI Error: No response received.")
    except Exception as e:
        return f"Gemini AI Error: {e}"

# ========================= VOICE COMMAND INPUT =========================
def generate_text_by_voice():
    print("🎙️ Speak the AI model name (Ollama, Together, or Gemini)...")
    model = listen().lower()

    if model not in ["ollama", "together", "gemini"]:
        return "Invalid AI model name. Please say 'Ollama', 'Together', or 'Gemini'."

    print(f"✅ Selected model: {model.capitalize()}")

    print("🎙️ Speak your prompt...")
    prompt = listen()

    if not prompt:
        return "No prompt detected. Please try again."

    print("🔄 Generating text...")
    return generate_text(prompt, model)





# import requests

# # Configuration
# HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
# HUGGINGFACE_API_KEY = "your_huggingface_api_key"  # Replace with your API Key

# def generate_text(prompt, method):
#     if method == "ollama":
#         return f"Generating text using Ollama for: {prompt}"
#     elif method == "huggingface":
#         return f"Generating text using Hugging Face for: {prompt}"
#     else:
#         return "Invalid method. Choose ollama or huggingface."


# # ========================= OLLAMA (OFFLINE) =========================
# def generate_with_ollama(prompt):
#     """
#     Generates text using Ollama (local model).
#     """
#     try:
#         import ollama  # Ensure you have Ollama installed
#         response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
#         return response["message"]["content"]
    
#     except Exception as e:
#         return f"Ollama Error: {e}"

# # ========================= HUGGING FACE (ONLINE API) =========================
# def generate_with_huggingface(prompt):
#     """
#     Generates text using Hugging Face Inference API.
#     """
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
#     payload = {"inputs": prompt}
    
#     try:
#         response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
#         result = response.json()
        
#         if isinstance(result, list) and "generated_text" in result[0]:
#             return result[0]["generated_text"]
        
#         return f"Hugging Face Error: {result}"
    
#     except Exception as e:
#         return f"Hugging Face API error: {e}"
