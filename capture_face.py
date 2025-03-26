import cv2
import os
import time

# Define a directory to save the captured face image
TEST_IMAGE_PATH = "assets/test_face.jpg"

def capture_face():
    """Captures an image from the webcam automatically after 1 second."""
    cap = cv2.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return False

    print("📷 Capturing your face... Look at the camera.")
    time.sleep(1)  # Wait for 1 second before capturing

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        cap.release()
        return False

    cv2.imwrite(TEST_IMAGE_PATH, frame)
    print("✅ Face captured successfully!")

    cap.release()
    cv2.destroyAllWindows()

    return True  # Return True if face capture is successful
