import subprocess
from core.brain import think

NAME = "jarvis"
DESCRIPTION = "Continuous voice assistant"


def speak(text):
    subprocess.run(["termux-tts-speak", text])


def listen():

    result = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def run(args):

    speak("Jarvis activated.")

    print("Say 'stop' to exit.\n")

    while True:

        print("🎤 Listening...")

        text = listen()

        if not text:
            continue

        print(f"You: {text}")

        if text.lower() in (
            "stop",
            "exit",
            "quit",
            "goodbye"
        ):
            speak("Goodbye.")
            break

        if not think(text):

            speak("I don't know how to do that yet.")
