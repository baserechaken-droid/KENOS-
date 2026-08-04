import json
import os

NAME = "theme"
DESCRIPTION = "Change KenOS theme"

FILE = "data/theme.json"


def save(name):

    os.makedirs("data", exist_ok=True)

    with open(FILE, "w") as f:

        json.dump({"theme": name}, f)


def load():

    if not os.path.exists(FILE):

        return "classic"

    with open(FILE) as f:

        return json.load(f)["theme"]


def run(args):

    if not args:

        print("Current theme:", load())

        return

    save(args[0])

    print("Theme changed to", args[0])
