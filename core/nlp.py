import re

from plugin_loader import find_skill


class Intent:

    def __init__(self, command=None, args=None):

        self.command = command
        self.args = args or []


OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run"
]

TORCH_WORDS = [
    "torch",
    "flashlight",
    "flash",
    "light"
]

BATTERY_WORDS = [
    "battery",
    "charge",
    "power"
]

WIFI_WORDS = [
    "wifi",
    "internet",
    "network"
]

DATE_WORDS = [
    "date",
    "today"
]

TIME_WORDS = [
    "time",
    "clock"
]


def parse(text):

    original = text.strip()

    text = original.lower()

    words = re.findall(r"[a-zA-Z0-9]+", text)

    # These words belong to conversational context.
    # Jarvis handles them using the previous command.
    conversation_words = {
        "again",
        "it",
        "that",
        "this"
    }

    if not any(word in conversation_words for word in words):

        plugin = find_skill(text)

        if plugin:

            args = words[:]

            if args and args[0] == plugin:

                args = args[1:]

            return Intent(plugin, args)

    # Legacy compatibility

    if any(word in words for word in OPEN_WORDS):

        args = [
            w for w in words
            if w not in OPEN_WORDS
        ]

        return Intent("open", args)

    if any(word in words for word in TORCH_WORDS):

        if "off" in words:

            return Intent("torch", ["off"])

        return Intent("torch", ["on"])

    if any(word in words for word in BATTERY_WORDS):

        return Intent("battery")

    if any(word in words for word in WIFI_WORDS):

        return Intent("wifi")

    if any(word in words for word in DATE_WORDS):

        return Intent("date")

    if any(word in words for word in TIME_WORDS):

        return Intent("time")

    return Intent()
