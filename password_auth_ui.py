from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation  # ✅ Corrected Import

from PyQt6.QtCore import Qt, QEasingCurve
from PyQt6.QtGui import QFont
import sys

class PasswordAuthUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔑 Secure Login")
        self.setGeometry(100, 100, 400, 250)

        # 🌟 Vibrant, Modern Theme
        self.setStyleSheet("""
            background-color: #F8F9FA;
            border-radius: 10px;
        """)

        # Title Label
        self.label = QLabel("🔐 Enter Password")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.label.setStyleSheet("color: #333333;")

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setStyleSheet("""
            background-color: white;
            border: 2px solid #6C63FF;
            border-radius: 5px;
            padding: 5px;
            color: #333333;
        """)

        # Submit Button
        self.submit_button = QPushButton("Login")
        self.submit_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.submit_button.setStyleSheet("""
            background-color: #6C63FF;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px;
        """)
        self.submit_button.clicked.connect(self.check_password)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        self.password = "1234"  # ✅ Set your actual password

        # 🌟 Apply Fade-in Animation
        self.apply_animation()

    def check_password(self):
        if self.password_input.text() == self.password:
            self.accept()
        else:
            self.label.setText("❌ Incorrect Password! Try Again")
            self.label.setStyleSheet("color: red;")
    
    def apply_animation(self):
        """Applies a smooth fade-in animation to the window."""
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.animation = QPropertyAnimation(effect, b"opacity")
        self.animation.setDuration(500)  # 0.5 sec fade-in
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.start()

def password_auth():
    """Function to run the password authentication UI."""
    app = QApplication(sys.argv)
    auth_dialog = PasswordAuthUI()
    if auth_dialog.exec() == QDialog.DialogCode.Accepted:
        return True
    return False

# 🌟 Test the UI (Run separately to see the modern login)
if __name__ == "__main__":
    if password_auth():
        print("✅ ACCESS GRANTED!")
    else:
        print("❌ ACCESS DENIED!")
