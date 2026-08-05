from core.voice import listen, speak
from core.router import process

NAME = "listen"
DESCRIPTION = "Listen for one voice command"

SKILLS = [
    "listen",
    "voice",
    "microphone",
    "mic"
]


def run(args):

    command = listen()

    if not command:

        speak("I didn't hear anything.")
        print("🤖 I didn't hear anything.")
        return

    print(f"🎤 You said: {command}")

    process(command)
