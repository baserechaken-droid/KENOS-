import json
import os

NAME = "remember"
DESCRIPTION = "Store a memory"

FILE = "data/memory.json"


def load():

    if not os.path.exists(FILE):

        return {}

    with open(FILE, "r") as f:

        return json.load(f)


def save(data):

    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)


def run(args):

    if len(args) < 2:

        print("Usage: remember <key> <value>")

        return

    key = args[0]

    value = " ".join(args[1:])

    data = load()

    data[key] = value

    save(data)

    print(f"✓ Remembered '{key}'.")
