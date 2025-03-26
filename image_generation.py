import requests
import webbrowser
import os

CRAIYON_API_URL = "https://www.craiyon.com/user/account/collection"
DEEPAI_API_URL = "https://deepai.org/dashboard/profile"
DEEPAI_API_KEY = "80c6cd8a-3c9a-4e1f-8f8d-b6961f1aafe0"  # Replace with your DeepAI API Key

def generate_image(prompt, method):
    """
    Generate an image based on the selected method.
    Available methods: 'craiyon', 'deepai'
    """
    if method == "craiyon":
        return generate_with_craiyon(prompt)
    elif method == "deepai":
        return generate_with_deepai(prompt)
    else:
        return "Invalid method. Choose: stable_diffusion, huggingface, leonardo, craiyon, or deepai."

# ========================= CRAIYON (Free) =========================
def generate_with_craiyon(prompt):
    """
    Generates an image using Craiyon (Free AI Image Generator).
    """
    try:
        payload = {"prompt": prompt}
        response = requests.post(CRAIYON_API_URL, json=payload)
        image_data = response.json()
        
        if "error" in image_data:
            return f"Craiyon Error: {image_data['error']}"
        
        image_url = image_data["images"][0]  # Get the first generated image
        return image_url
    
    except Exception as e:
        return f"Craiyon API error: {e}"

# ========================= DEEPAI (Limited Free Use) =========================
def generate_with_deepai(prompt):
    """
    Generates an image using DeepAI API.
    """
    headers = {"api-key": DEEPAI_API_KEY}
    payload = {"text": prompt}
    
    try:
        response = requests.post(DEEPAI_API_URL, headers=headers, data=payload)
        image_data = response.json()
        
        if "err" in image_data:
            return f"DeepAI Error: {image_data['err']}"
        
        return image_data["output_url"]  # Returns the image URL
    
    except Exception as e:
        return f"DeepAI API error: {e}"

def show_image(image_url):
    """
    Opens the generated image in the default web browser.
    """
    try:
        if image_url.startswith("http"):
            webbrowser.open(image_url)
        else:
            os.startfile(image_url)  # Opens local image (Windows)
    except Exception as e:
        print(f"Error opening image: {e}")
