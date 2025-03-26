from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QProgressBar
)
from PyQt6.QtGui import QMovie, QFont, QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt, QTimer
import psutil  # For real-time system stats


class JarvisUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI Assistant")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #0A0A0A; color: #00FFFF;")

        # 🔹 Background Animation
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 900, 600)
        self.bg_movie = QMovie("assets/ai_bg.gif")  # Add futuristic AI GIF
        self.bg_label.setMovie(self.bg_movie)
        self.bg_movie.start()

        # 🔹 Status Label
        self.loading_label = QLabel("Initializing JARVIS...", self)
        self.loading_label.setFont(QFont("Arial", 14))
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_label.setStyleSheet("color: white;")
        self.loading_label.setGeometry(300, 450, 300, 50)

        # 🔹 Progress Bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 500, 500, 20)
        self.progress.setStyleSheet(
            "QProgressBar { background-color: #222; color: white; border: 2px solid #00FFFF; }"
        )
        self.progress.setValue(0)

        # 🔹 Face Authentication Effect
        self.scan_label = QLabel("🔄 Scanning Face...", self)
        self.scan_label.setFont(QFont("Arial", 14))
        self.scan_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scan_label.setGeometry(300, 350, 300, 50)
        self.scan_label.setStyleSheet("color: #00FF00; font-weight: bold;")
        self.scan_label.hide()  # Hide by default

        # 🔹 Face Camera Window (Embedded Inside UI)
        self.camera_feed = QLabel(self)
        self.camera_feed.setGeometry(250, 100, 400, 300)  # Adjust size and position
        self.camera_feed.setStyleSheet("border: 2px solid #00FFFF; background-color: black;")
        self.camera_feed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.camera_feed.setText("📷 Camera Feed Here")
        self.camera_feed.hide()

        # 🔹 System Dashboard
        self.system_label = QLabel("🖥️ CPU: 0% | RAM: 0%", self)
        self.system_label.setFont(QFont("Arial", 12))
        self.system_label.setGeometry(50, 550, 300, 30)
        self.system_label.setStyleSheet("color: #FF9900;")
        self.system_label.hide()

        self.start_loading()

    def start_loading(self):
        """Fake Loading Effect Before Showing Main UI"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)

    def update_progress(self):
        """Increase progress bar gradually"""
        value = self.progress.value()
        if value < 100:
            self.progress.setValue(value + 2)
        else:
            self.timer.stop()
            self.loading_label.setText("✅ JARVIS Ready!")
            self.progress.hide()  # Hide the progress bar after initialization

    def update_status(self, message):
        """Update status message in UI"""
        self.loading_label.setText(message)

    def start_face_scan_effect(self):
        """Display scanning effect before face authentication"""
        self.scan_label.show()
        self.scan_label.setText("🔄 Scanning Face...")
        self.camera_feed.show()  # Show camera window

    def stop_face_scan_effect(self):
        """Hide scanning effect after authentication"""
        self.scan_label.setText("✅ Face Verified!")
        QTimer.singleShot(2000, self.scan_label.hide)  # Hide after 2 seconds
        QTimer.singleShot(2000, self.camera_feed.hide)  # Hide camera feed after scan

    def start_waveform_animation(self):
        """Show voice authentication animation"""
        self.loading_label.setText("🎙️ Say your password...")

    def stop_waveform_animation(self):
        """Hide voice authentication animation"""
        self.loading_label.setText("✅ Authentication successful!")

    def enable_system_dashboard(self):
        """Enable system status updates (CPU & RAM)"""
        self.system_label.show()
        self.system_timer = QTimer(self)
        self.system_timer.timeout.connect(self.update_system_stats)
        self.system_timer.start(1000)  # Update every second

    def update_system_stats(self):
        """Fetch and display CPU & RAM usage"""
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        self.system_label.setText(f"🖥️ CPU: {cpu}% | RAM: {ram}%")


if __name__ == "__main__":
    app = QApplication([])
    jarvis_ui = JarvisUI()
    jarvis_ui.show()
    app.exec()
