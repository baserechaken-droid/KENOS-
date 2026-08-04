import json
import os

NAME = "recall"
DESCRIPTION = "Recall a memory"

FILE = "data/memory.json"


def run(args):

    if not args:

        print("Usage: recall <key>")

        return

    if not os.path.exists(FILE):

        print("No memories stored.")

        return

    with open(FILE, "r") as f:

        data = json.load(f)

    key = args[0]

    if key in data:

        print(data[key])

    else:

        print("Memory not found.")
