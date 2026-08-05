import json
import subprocess
import time


WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "ok jarvis"
]


def speak(text):

    if not text:
        return

    try:

        subprocess.run(
            [
                "termux-tts-speak",
                str(text)
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )

    except Exception:

        pass


def listen(prompt=True):

    if prompt:

        print("🎤 Listening...")

    try:

        result = subprocess.run(
            [
                "termux-speech-to-text"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

    except Exception:

        return None

    if result.returncode != 0:

        return None

    text = result.stdout.strip()

    #
    # Some versions of termux-speech-to-text
    # return JSON.
    #

    if text.startswith("{"):

        try:

            obj = json.loads(text)

            text = (
                obj.get("text")
                or obj.get("result")
                or ""
            )

        except Exception:

            pass

    text = text.strip().lower()

    if not text:

        return None

    return text


def wait_for_wake_word():

    print("🤖 Waiting for wake word...")

    while True:

        text = listen(prompt=False)

        if not text:

            continue

        print(f"🎤 {text}")

        if any(word in text for word in WAKE_WORDS):

            speak("Yes Ken?")

            return True

        time.sleep(0.2)
