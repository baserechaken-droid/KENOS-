import os

HISTORY_FILE = "data/history.txt"

def save(command):

    os.makedirs("data", exist_ok=True)

    with open(HISTORY_FILE, "a") as file:
        file.write(command + "\n")


def show():

    if not os.path.exists(HISTORY_FILE):
        print("No command history.")
        return

    with open(HISTORY_FILE, "r") as file:
        print(file.read())
