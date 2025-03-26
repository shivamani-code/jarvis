import pytesseract
from PIL import Image

# Set the Tesseract path (only for Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def perform_ocr(image_path):
    """Extracts text from an image using OCR."""
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text.strip()
    except Exception as e:
        return f"Error in OCR: {str(e)}"

if __name__ == "__main__":
    path = input("Enter image path: ")
    print(perform_ocr(path))
