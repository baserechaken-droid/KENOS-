import subprocess


def speak(text):

    subprocess.run(
        ["termux-tts-speak", text],
        check=False
    )


def listen():

    print("🎤 Speak now...")

    result = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[VOICE] Speech recognition failed.")
        return None

    text = result.stdout.strip()

    print(f"[VOICE DEBUG] Raw: {repr(result.stdout)}")
    print(f"[VOICE DEBUG] Parsed: {text}")

    if text == "":
        return None

    return text.lower()
