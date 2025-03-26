import datetime

def log_history(event):
    """Logs events into a history file with timestamps."""
    with open("jarvis_history.log", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {event}\n")
