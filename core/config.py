import json
import os

CONFIG_FILE = "data/config.json"

DEFAULT_CONFIG = {
    "version": "8.1",
    "voice": True,
    "tts": True,
    "notifications": True,
    "jarvis_autostart": False,
    "scheduler_autostart": True,
    "theme": "default"
}


def load():

    if not os.path.exists(CONFIG_FILE):

        save(DEFAULT_CONFIG)

        return DEFAULT_CONFIG.copy()

    try:

        with open(CONFIG_FILE, "r") as f:

            data = json.load(f)

    except Exception:

        data = DEFAULT_CONFIG.copy()

        save(data)

    for key, value in DEFAULT_CONFIG.items():

        data.setdefault(key, value)

    return data


def save(config):

    os.makedirs("data", exist_ok=True)

    with open(CONFIG_FILE, "w") as f:

        json.dump(config, f, indent=4)


def get(key, default=None):

    return load().get(key, default)


def set(key, value):

    cfg = load()

    cfg[key] = value

    save(cfg)
