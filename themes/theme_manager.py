import json
import os

CONFIG = "config/settings.json"

DEFAULT = {
    "theme": "matrix",
    "assistant_name": "Jarvis",
    "voice": True,
    "animations": True
}


def _ensure():

    os.makedirs("config", exist_ok=True)

    if not os.path.exists(CONFIG):

        with open(CONFIG, "w") as f:

            json.dump(DEFAULT, f, indent=4)


def load():

    _ensure()

    with open(CONFIG, "r") as f:

        return json.load(f)


def save(cfg):

    with open(CONFIG, "w") as f:

        json.dump(cfg, f, indent=4)


def get_theme():

    return load().get("theme", "matrix")


def set_theme(name):

    cfg = load()

    cfg["theme"] = name

    save(cfg)
