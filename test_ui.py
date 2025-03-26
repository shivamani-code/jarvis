import importlib
import sys
from PyQt6.QtWidgets import QApplication
import ui  # Import the UI module

importlib.reload(ui)  # Reload to ensure changes take effect
from ui import JarvisUI  # Import the updated UI

def test_ui():
    app = QApplication(sys.argv)
    window = JarvisUI()  # Initialize the new UI
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    test_ui()
