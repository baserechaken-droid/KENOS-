from core.voice import listen, speak
from core.router import process

NAME = "listen"
DESCRIPTION = "Listen for voice commands"

SKILLS = [
    "listen",
    "voice",
    "microphone",
    "mic"
]


EXIT_WORDS = {
    "exit",
    "quit",
    "goodbye",
    "bye",
    "stop listening",
    "stop"
}


def run(args):

    mode = " ".join(args).lower()

    # -----------------------------
    # Continuous voice mode
    # -----------------------------
    if mode in (
        "loop",
        "continuous",
        "voice",
        "conversation"
    ):

        print()
        print("===================================")
        print("     🎤 Jarvis Voice Mode")
        print("===================================")
        print("Say 'goodbye' to exit.")
        print()

        speak("Voice mode activated.")

        while True:

            print("🎤 Listening...")

            command = listen()

            if not command:

                speak("I didn't hear anything.")
                continue

            print(f"🎤 You said: {command}")

            if command.lower().strip() in EXIT_WORDS:

                speak("Goodbye.")

                print("👋 Voice mode ended.")

                print()

                break

            process(command)

        return

    # -----------------------------
    # Original one-shot mode
    # -----------------------------

    command = listen()

    if not command:

        speak("I didn't hear anything.")

        print("🤖 I didn't hear anything.")

        return

    print(f"🎤 You said: {command}")

    process(command)
