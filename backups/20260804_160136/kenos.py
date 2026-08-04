#!/usr/bin/env python3

import os

from command_manager import execute
from plugin_loader import load_plugins

from core.logger import info
from core.boot import boot
from core.crash import save as save_crash

import services.device_service
import services.ai_service

print(r"""
==========================================
              KenOS v8
==========================================

 Android Terminal Assistant

==========================================
""")

os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

boot()

plugins = load_plugins()

print(f"✓ {len(plugins)} plugins loaded successfully.")

print()
print("Type 'help' to view commands.")
print("Type 'exit' to quit.")
print()

while True:

    try:

        text = input("[KenOS] $ ").strip()

        if not text:
            continue

        info(f"Command: {text}")

        with open("data/history.txt", "a") as history:
            history.write(text + "\n")

        if text.lower() == "exit":

            print("Goodbye!")

            break

        parts = text.split()

        command = parts[0].lower()

        args = parts[1:]

        execute(command, args)

    except KeyboardInterrupt:

        print()
        print("Use 'exit' to quit.")

    except Exception as e:

        save_crash(e)

        print(f"[ERROR] {e}")

        info(f"ERROR: {e}")
