import json
import os
from datetime import datetime

NAME = "schedule"
DESCRIPTION = "Manage scheduled tasks"

FILE = "data/schedule.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def run(args):

    tasks = load()

    if not args:
        print("Usage:")
        print("schedule add <YYYY-MM-DD HH:MM> <task>")
        print("schedule list")
        return

    cmd = args[0].lower()

    if cmd == "list":

        if not tasks:
            print("No scheduled tasks.")
            return

        print()

        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['time']} - {t['task']}")

        print()
        return

    if cmd == "add":

        if len(args) < 4:
            print("Usage: schedule add YYYY-MM-DD HH:MM task")
            return

        when = args[1] + " " + args[2]
        task = " ".join(args[3:])

        try:
            datetime.strptime(when, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date/time.")
            return

        tasks.append({
            "time": when,
            "task": task
        })

        save(tasks)

        print("Task scheduled.")
        return

    print("Unknown option.")
