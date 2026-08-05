from services.voice.engine import voice

NAME = "speak"
DESCRIPTION = "Make Jarvis speak text"

SKILLS = [
    "speak",
    "say",
    "talk",
    "repeat"
]


def run(args):

    if not args:

        print("Usage:")
        print("  speak Hello Ken")
        return

    message = " ".join(args)

    print(f"🗣 {message}")

    voice.speak(message)

    return message
