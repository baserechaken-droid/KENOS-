from services.voice.engine import voice

NAME = "voice"
DESCRIPTION = "Manage Jarvis voice"

SKILLS = [
    "voice",
    "speaker",
    "speech",
    "talk"
]


def run(args):

    if not args:

        cfg = voice.status()

        print()
        print("🎙 KenOS Voice Settings")
        print("----------------------------")
        print(f"Enabled : {cfg.get('enabled')}")
        print(f"Profile : {cfg.get('voice')}")
        print(f"Speed   : {cfg.get('speed')}")
        print(f"Pitch   : {cfg.get('pitch')}")
        print()
        print("Available voices:")
        print("  jarvis")
        print("  david")
        print("  friday")
        print("  fast")
        print("  silent")
        return

    profile = args[0].lower()

    if not voice.set_voice(profile):

        print("Unknown voice profile.")
        return

    voice.reload()

    print(f"✅ Voice changed to {profile}")

    if profile != "silent":
        voice.speak(f"Hello Ken. Voice changed to {profile}.")
