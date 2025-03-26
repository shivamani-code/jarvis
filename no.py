# from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt6.QtGui import QFont

# class JarvisUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Jarvis AI")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet("background-color: black; color: cyan;")

#         layout = QVBoxLayout()

#         self.label = QLabel("Hello, I am Jarvis", self)
#         self.label.setFont(QFont("Arial", 16))
#         layout.addWidget(self.label)

#         self.btn_wake = QPushButton("Wake Up", self)
#         self.btn_wake.clicked.connect(self.wake_up)
#         layout.addWidget(self.btn_wake)

#         self.btn_sleep = QPushButton("Sleep", self)
#         self.btn_sleep.clicked.connect(self.sleep)
#         layout.addWidget(self.btn_sleep)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def wake_up(self):
#         self.label.setText("I'm Awake!")

#     def sleep(self):
#         self.label.setText("Going to sleep...")
