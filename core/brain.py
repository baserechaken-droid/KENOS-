import re

INTENTS = {

    "battery": [
        "battery",
        "charge",
        "power"
    ],

    "torch": [
        "torch",
        "flashlight",
        "flash"
    ],

    "wifi": [
        "wifi",
        "wi-fi",
        "internet"
    ],

    "open": [
        "open",
        "launch",
        "start"
    ],

    "date": [
        "date",
        "today"
    ],

    "time": [
        "time",
        "clock"
    ],

    "volume": [
        "volume",
        "sound"
    ],

    "music": [
        "music",
        "song"
    ],

    "camera": [
        "camera",
        "photo",
        "picture"
    ],

    "help": [
        "help",
        "commands"
    ]
}


def understand(sentence):

    text = sentence.lower()

    for plugin, words in INTENTS.items():

        for word in words:

            if re.search(r"\b" + re.escape(word) + r"\b", text):

                return plugin

    return None
