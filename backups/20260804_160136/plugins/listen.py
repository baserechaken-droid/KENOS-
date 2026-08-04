from core.voice import listen, speak
from command_manager import execute

NAME = "listen"
DESCRIPTION = "Listen for one voice command"


def run(args):

    command = listen()

    if command is None:

        speak("I didn't hear anything.")

        return

    print(f"You said: {command}")

    parts = command.split()

    if not parts:
        return

    execute(
        parts[0].lower(),
        parts[1:]
    )
