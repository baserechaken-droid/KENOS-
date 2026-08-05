from core.voice import listen, speak
from core.router import process

NAME = "listen"
DESCRIPTION = "Voice recognition"

SKILLS = [
    "listen",
    "voice",
    "microphone",
    "mic",
    "jarvis"
]

EXIT_WORDS = {
    "exit",
    "quit",
    "bye",
    "goodbye",
    "stop",
    "stop listening",
    "cancel"
}


def banner():

    print()
    print("══════════════════════════════════════")
    print("🎤        JARVIS VOICE MODE")
    print("══════════════════════════════════════")
    print("Say 'stop listening' to exit.")
    print()


def run(args):

    mode = " ".join(args).lower().strip()

    #
    # Continuous voice mode
    #

    if mode in (
        "",
        "loop",
        "continuous",
        "voice",
        "conversation"
    ):

        banner()

        speak("Jarvis voice mode activated.")

        while True:

            print("🎤 Listening...")

            command = listen()

            if not command:

                print("⚠ No speech detected.")
                speak("Please repeat.")
                continue

            command = command.strip()

            print(f"🗣 You: {command}")

            if command.lower() in EXIT_WORDS:

                speak("Voice mode terminated.")

                print()
                print("👋 Voice mode ended.")
                print()

                break

            try:

                process(command)

            except Exception as e:

                print(f"[ERROR] {e}")

                speak("An error occurred.")

        return

    #
    # Single command mode
    #

    print("🎤 Listening...")

    command = listen()

    if not command:

        print("⚠ No speech detected.")

        speak("I didn't hear anything.")

        return

    command = command.strip()

    print(f"🗣 You: {command}")

    process(command)
