from PyQt6.QtWidgets import QApplication
from password_auth_ui import PasswordAuthUI  # Import the PasswordAuthUI class from password_auth_ui.py
 
class PasswordAuthentication:
    def __init__(self, correct_password):
        self.correct_password = correct_password

    def check_password(self, entered_password):
        entered_password = entered_password.strip()  # Remove leading/trailing spaces
        if entered_password == self.correct_password:
            print("✅ Password Verified!")
            return True
        else:
            print("❌ Incorrect Password!")
            return False

def main():
    app = QApplication([])

    # Create the application window
    window = PasswordAuthUI()  # Call the UI function here
    window.show()

    # Start the application event loop
    app.exec()

if __name__ == "__main__":
    main()
