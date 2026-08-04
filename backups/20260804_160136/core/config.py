import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "user_name": "Ken",
    "assistant_name": "Jarvis",
    "voice": True,
    "logging": True,
    "boot_diagnostics": True,
    "theme": "default"
}


def load():

    if not os.path.exists(CONFIG_FILE):

        save(DEFAULT_CONFIG)

        return DEFAULT_CONFIG.copy()

    with open(CONFIG_FILE) as f:

        return json.load(f)


def save(config):

    with open(CONFIG_FILE, "w") as f:

        json.dump(config, f, indent=4)
