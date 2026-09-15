# jarvis
# J.A.R.V.I.S — Personal AI Desktop Assistant

A modular Python-based desktop AI assistant inspired by J.A.R.V.I.S., designed to combine conversational AI, voice interaction, biometric-style authentication, desktop automation, and productivity tools into a single application.

JARVIS can listen for a wake word, understand voice commands, authenticate the user using password, face, and voice verification, perform system-level operations, interact with local AI models through Ollama, and provide a graphical interface built with PyQt6.

## ✨ Features

### 🤖 AI Conversation

* Ollama-powered responses using Mistral
* Rule-based command handling for common interactions
* Basic conversational memory
* AI fallback for commands that are not explicitly mapped
* Experimental support for additional AI providers such as Gemini and Together AI

### 🎙️ Voice Interaction

* Continuous microphone listening
* `"Jarvis"` wake-word detection
* Speech-to-text using Google Speech Recognition
* Text-to-speech using `pyttsx3`
* Voice-driven command execution
* Basic translation support

### 🔐 Multi-Layer Authentication

JARVIS includes multiple authentication mechanisms:

1. Password authentication
2. Face verification using webcam input and `face_recognition`
3. Voice verification using MFCC audio features

The voice authentication pipeline extracts MFCC features from a registered voice sample and compares them using FastDTW.

### 🖥️ Desktop Automation

Voice commands can be used for various Windows system operations, including:

* Open and close applications
* Shutdown and restart
* Sleep and lock
* Volume control
* Screenshots
* Wi-Fi control
* DNS flushing
* Network information
* Task Manager
* File and folder operations
* Media controls
* Browser and Google searches

### 🧠 Productivity Tools

* Task management
* Schedule management
* Conversation history
* OCR text extraction
* Voice-based reminders/workflows
* JSON-based local data storage

### 🎨 AI Image Generation

The project contains integrations for AI image generation through external services such as:

* Craiyon
* DeepAI

Generated images can be opened directly through the system browser.

### 📧 Communication Automation

JARVIS contains voice-driven functionality for:

* Sending email
* Reading email data
* Sending WhatsApp messages
* Sending Telegram messages

### 🖥️ PyQt6 Interface

The desktop interface provides:

* Animated startup screen
* Loading/progress animation
* Face scanning feedback
* Authentication status
* Voice interaction status
* CPU and RAM monitoring
* Futuristic JARVIS-inspired visual design

## 🏗️ Project Architecture

```text
JARVIS
│
├── fv.py
│   └── Main application controller
│
├── brain.py
│   └── Command processing + Ollama AI responses
│
├── ai_response.py
│   └── Basic Ollama response interface
│
├── ai_selector.py
│   └── Multiple AI provider selection
│
├── speech.py
│   └── Speech recognition + text-to-speech
│
├── translator.py
│   └── Translation + translated speech
│
├── face_auth.py
│   └── Face capture and verification
│
├── capture_face.py
│   └── Webcam face capture
│
├── record_voice.py
│   └── Voice registration + MFCC extraction
│
├── voice_auth.py
│   └── Voice verification
│
├── password_auth.py
│   └── Password authentication logic
│
├── password_auth_ui.py
│   └── Graphical password authentication
│
├── automation.py
│   └── Email / WhatsApp / Telegram automation
│
├── system_control.py
│   └── Windows system automation
│
├── ocr.py
│   └── Image-to-text OCR
│
├── image_generation.py
│   └── AI image generation integrations
│
├── text_generator.py
│   └── AI text generation
│
├── task_manager.py
│   └── Local task storage
│
├── schedule_manager.py
│   └── Local schedule storage
│
├── gork_mode.py
│   └── Alternate AI conversation mode
│
└── ui.py
    └── PyQt6 graphical interface
```

## 🔄 How JARVIS Works

```text
User
  │
  ▼
Password Authentication
  │
  ▼
Face Verification
  │
  ▼
Voice Verification
  │
  ▼
JARVIS UI
  │
  ▼
Wake Word Detection
  │
  ▼
Voice Command
  │
  ▼
Command Processing
  │
  ├── System Command
  │      └── Desktop Automation
  │
  ├── Productivity Command
  │      └── Task / Schedule / OCR
  │
  ├── AI Command
  │      └── Ollama / Mistral
  │
  └── Other Command
         └── AI Fallback
```

## 🛠️ Technology Stack

| Technology                  | Purpose                    |
| --------------------------- | -------------------------- |
| Python                      | Core application           |
| PyQt6                       | Desktop UI                 |
| Ollama                      | Local AI inference         |
| Mistral                     | Conversational AI model    |
| SpeechRecognition           | Speech-to-text             |
| pyttsx3                     | Text-to-speech             |
| OpenCV                      | Webcam processing          |
| face_recognition            | Face verification          |
| NumPy                       | Numerical/audio processing |
| Librosa                     | Audio feature extraction   |
| FastDTW                     | Voice comparison           |
| Tesseract / pytesseract     | OCR                        |
| Google Translator libraries | Translation                |
| Requests                    | API communication          |
| JSON                        | Local data storage         |

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivamani-code/jarvis.git
cd jarvis
```

### 2. Install Python dependencies

Install the required Python packages used by the modules in the project.

### 3. Install and configure Ollama

Install Ollama and download the model used by JARVIS:

```bash
ollama pull mistral
```

### 4. Configure external services

Some features depend on external APIs and services such as speech recognition, AI providers, messaging services, and image generation providers.

Store credentials in environment variables or a local configuration file rather than committing them to Git.

### 5. Run JARVIS

The primary controller is:

```bash
python fv.py
```

## ⚠️ Current Project Status

This project is an evolving personal AI assistant and experimentation platform.

Some modules are fully implemented while others are experimental, partially integrated, or contain older approaches from earlier development stages. The repository contains several commented-out implementations reflecting the project's development history.

Some system-control features are Windows-specific and may require additional software or configuration.

## 🔒 Security Notice

API credentials and authentication secrets should **never** be committed directly to a public repository.

Before deploying or sharing this project, move API keys, passwords, bot tokens, and other secrets into environment variables or a local `.env` file and rotate any credentials that may already have been exposed.

## 🎯 Future Improvements

* Better command routing and intent detection
* More reliable wake-word detection
* Improved voice authentication
* Secure environment-based configuration
* Cross-platform system controls
* Persistent conversational memory
* Better error handling and logging
* Modular plugin architecture
* More polished PyQt6 interface
* Automated dependency management
* Unit and integration testing

## 👨‍💻 About

JARVIS is a personal experimentation project focused on combining AI, voice interfaces, computer vision, automation, and desktop software into one intelligent assistant.

Built with Python as an exploration of how multiple AI and automation technologies can work together in a practical desktop application.
