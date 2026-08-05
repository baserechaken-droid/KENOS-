from core.voice import conversation, listen, speak
from core.router import process

NAME = "listen"
DESCRIPTION = "Voice Assistant"

SKILLS = [
    "listen",
    "voice",
    "mic",
    "microphone",
    "conversation",
    "talk"
]


EXIT_WORDS = {
    "bye",
    "goodbye",
    "exit",
    "quit",
    "stop listening",
    "stop"
}


def normalize(text):

    if not text:
        return ""

    text = text.lower().strip()

    replacements = {

        "what's": "what is",

        "whats": "what is",

        "it's": "it is",

        "turn on the flash light": "turn on the flashlight",

        "turn off the flash light": "turn off the flashlight",

        "flash light": "flashlight",

        "wi fi": "wifi"

    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    return text


def callback(command):

    command = normalize(command)

    process(command)


def run(args):

    mode = " ".join(args).lower().strip()

    if mode in (
        "",
        "voice",
        "conversation",
        "continuous",
        "loop",
        "chat"
    ):

        conversation(callback)

        return

    command = listen()

    if not command:

        print("🤖 I didn't hear anything.")

        speak("I didn't hear anything.")

        return

    command = normalize(command)

    print(f"🗣 You said: {command}")

    if command in EXIT_WORDS:

        print("👋 Voice mode ended.")

        speak("Goodbye.")

        return

    process(command)

