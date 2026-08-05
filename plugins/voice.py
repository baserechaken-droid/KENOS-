import json
import os

CONFIG = "data/voice.json"

DEFAULT = {
    "enabled": True,
    "speed": 1.15,
    "pitch": 0.90,
    "voice": "jarvis"
}


NAME = "voice"
DESCRIPTION = "Manage voice settings"

SKILLS = [
    "voice",
    "speech",
    "tts"
]


def load():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CONFIG):

        with open(CONFIG, "w") as f:

            json.dump(DEFAULT, f, indent=4)

        return DEFAULT.copy()

    with open(CONFIG) as f:

        return json.load(f)


def save(cfg):

    with open(CONFIG, "w") as f:

        json.dump(cfg, f, indent=4)


def show(cfg):

    print()
    print("🎙 KenOS Voice Settings")
    print("----------------------------")
    print(f"Enabled : {cfg.get('enabled')}")
    print(f"Profile : {cfg.get('voice')}")
    print(f"Speed   : {cfg.get('speed')}")
    print(f"Pitch   : {cfg.get('pitch')}")
    print()
    print("Examples:")
    print("  voice on")
    print("  voice off")
    print("  voice speed 1.4")
    print("  voice pitch 0.8")
    print()


def run(args):

    cfg = load()

    if not args:

        show(cfg)
        return

    cmd = args[0].lower()

    if cmd == "on":

        cfg["enabled"] = True

    elif cmd == "off":

        cfg["enabled"] = False

    elif cmd == "speed" and len(args) > 1:

        cfg["speed"] = float(args[1])

    elif cmd == "pitch" and len(args) > 1:

        cfg["pitch"] = float(args[1])

    else:

        print("Unknown voice option.")
        return

    save(cfg)

    print("✓ Voice settings updated.")

