import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"tasks": []}

def save_tasks(tasks):
    """Saves tasks to file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Adds a new task."""
    tasks = load_tasks()
    tasks["tasks"].append(task)
    save_tasks(tasks)
    return f"Task '{task}' added."

def view_tasks():
    """Displays tasks."""
    tasks = load_tasks()["tasks"]
    return "\n".join(tasks) if tasks else "No tasks available."

if __name__ == "__main__":
    print(view_tasks())
