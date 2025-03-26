import smtplib
import pywhatkit
import telebot
from email.message import EmailMessage
from speech import listen, speak  # Import voice functions
import smtplib
import imaplib
import email
import pywhatkit as kit
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ 1. Send Email Using Voice
def send_email_voice():
    """Send an email using voice commands."""
    speak("Who do you want to send an email to?")
    to = listen()

    speak("What is the subject of the email?")
    subject = listen()

    speak("What should I write in the email?")
    body = listen()

    send_email(to, subject, body)
    speak("Email has been sent successfully.")

def send_email(to, subject, body):
    """Function to send an email."""
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_app_password"

    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

# ✅ 2. Read Unread Emails
def read_unread_emails_voice():
    """Read unread emails and speak them aloud."""
    emails = read_unread_emails()
    for email_data in emails:
        sender, subject, body = email_data
        speak(f"Email from {sender}. Subject: {subject}. Message: {body}")

def read_unread_emails():
    """Function to read unread emails (Placeholder)."""
    return [("test@example.com", "Meeting Update", "The meeting is at 5 PM.")]

# ✅ 3. Send WhatsApp Message Using Voice
def send_whatsapp_voice():
    """Send a WhatsApp message using voice commands."""
    speak("Please say the recipient's phone number, including country code.")
    phone = listen()

    speak("What message should I send?")
    message = listen()

    pywhatkit.sendwhatmsg_instantly(phone, message)
    speak("WhatsApp message has been sent.")

# ✅ 4. Send Telegram Message Using Voice
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

def send_telegram_voice():
    """Send a Telegram message using voice commands."""
    speak("What message should I send?")
    message = listen()

    send_telegram_message(message)
    speak("Telegram message has been sent.")

def send_telegram_message(message):
    """Function to send a message via Telegram bot."""
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    bot.send_message(TELEGRAM_CHAT_ID, message)
