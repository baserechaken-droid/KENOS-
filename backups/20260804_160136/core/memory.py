import json
import os

FILE = "data/memory.json"


def load():

    if not os.path.exists(FILE):
        return {}

    try:

        with open(FILE, "r") as f:
            return json.load(f)

    except:
        return {}


def save(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def remember(key, value):

    data = load()

    data[key.lower()] = value

    save(data)


def recall(key):

    data = load()

    return data.get(key.lower())


def all_memory():

    return load()
