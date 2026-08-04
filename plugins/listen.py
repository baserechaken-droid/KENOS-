from core.voice import listen, speak
from core.router import process

NAME = "listen"
DESCRIPTION = "Listen for one voice command"


def run(args):

    command = listen()

    if not command:

        speak("I didn't hear anything.")
        return

    print(f"🎤 You said: {command}")

    try:

        process(command)

    except Exception as e:

        print(f"[VOICE ERROR] {e}")
        speak("Sorry, I couldn't process that command.")
