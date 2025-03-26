import cv2
import face_recognition
import numpy as np

SAVED_FACE_PATH = "known_faces/user.jpg"
TEST_IMAGE_PATH = "assets/test_face.jpg"

def capture_face():
    """Captures an image from the webcam and saves it."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return False

    print("📷 Capturing your face... Look at the camera.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Failed to capture image.")
            break

        cv2.imshow("Press SPACE to capture, ESC to cancel", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # Press SPACE to capture
            cv2.imwrite(TEST_IMAGE_PATH, frame)
            print("✅ Face captured successfully!")
            break
        elif key == 27:  # Press ESC to cancel
            print("❌ Capture canceled.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return True

def verify_face():
    """Compares the captured face with the saved owner's face."""
    try:
        saved_image = face_recognition.load_image_file(SAVED_FACE_PATH)
        test_image = face_recognition.load_image_file(TEST_IMAGE_PATH)

        saved_encoding = face_recognition.face_encodings(saved_image)
        test_encoding = face_recognition.face_encodings(test_image)

        if not saved_encoding or not test_encoding:
            print("❌ Face encoding failed. Ensure face is visible in both images.")
            return False

        match = face_recognition.compare_faces([saved_encoding[0]], test_encoding[0])

        if match[0]:
            print("✅ Face matched!")
            return True
        else:
            print("❌ Face does not match!")
            return False

    except Exception as e:
        print(f"❌ Face verification error: {e}")
        return False

if __name__ == "__main__":
    if capture_face():
        verify_face()
