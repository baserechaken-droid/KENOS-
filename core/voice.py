import subprocess
import time

from services.voice.engine import voice


WAKE_WORDS = (
    "jarvis",
    "hey jarvis",
    "okay jarvis",
    "ok jarvis",
    "kenos"
)


def speak(text):

    if text:

        voice.speak(str(text))


def listen():

    try:

        result = subprocess.run(
            ["termux-speech-to-text"],
            capture_output=True,
            text=True,
            timeout=12
        )

    except Exception:

        return None

    if result.returncode != 0:

        return None

    text = result.stdout.strip().lower()

    if not text:

        return None

    return text


def strip_wake_word(text):

    text = text.strip()

    for wake in WAKE_WORDS:

        if text.startswith(wake):

            text = text[len(wake):].strip()

            break

    return text


def conversation(callback):

    print()
    print("🎤 Voice Assistant Ready")
    print("Say 'goodbye' to exit.")
    print()

    speak("Voice assistant ready.")

    while True:

        print("🎤 Listening...")

        command = listen()

        if not command:

            continue

        command = strip_wake_word(command)

        if not command:

            continue

        print(f"🗣 {command}")

        if command in (
            "bye",
            "goodbye",
            "exit",
            "quit",
            "stop"
        ):

            speak("Goodbye.")

            print("👋 Voice mode ended.")

            break

        callback(command)

        voice.wait()

        time.sleep(0.05)

