import json
import os

NAME = "tasks"
DESCRIPTION = "Manage your task list"

FILE = "data/tasks.json"


def load():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def run(args):

    tasks = load()

    if len(args) == 0:
        print("\nUsage:")
        print("tasks list")
        print("tasks add <task>")
        print("tasks done <number>")
        return

    command = args[0].lower()

    if command == "list":

        if not tasks:
            print("\nNo tasks.\n")
            return

        print("\n========== TASKS ==========\n")

        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "•"
            print(f"{i}. {status} {task['title']}")

        print()
        return

    if command == "add":

        title = " ".join(args[1:])

        if not title:
            print("Task cannot be empty.")
            return

        tasks.append({
            "title": title,
            "done": False
        })

        save(tasks)

        print("Task added.")
        return

    if command == "done":

        if len(args) < 2:
            print("Specify task number.")
            return

        try:
            index = int(args[1]) - 1
            tasks[index]["done"] = True
            save(tasks)
            print("Task completed.")
        except:
            print("Invalid task number.")
