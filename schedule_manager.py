import json
import os

SCHEDULE_FILE = "schedule.json"

def load_schedule():
    """Loads the schedule from a file."""
    if os.path.exists(SCHEDULE_FILE):
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_schedule(schedule):
    """Saves the schedule to a file."""
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedule, file, indent=4)

def add_schedule(event, time):
    """Adds an event to the schedule."""
    schedule = load_schedule()
    schedule[time] = event
    save_schedule(schedule)
    return f"Event '{event}' added at {time}"

def view_schedule():
    """Displays the schedule."""
    schedule = load_schedule()
    if not schedule:
        return "Your schedule is empty."
    
    return "\n".join([f"{time}: {event}" for time, event in schedule.items()])

if __name__ == "__main__":
    print(view_schedule())
