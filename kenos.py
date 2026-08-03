#!/usr/bin/env python3

from command_manager import execute
from plugin_loader import load_plugins

print(r"""
 _  __          _   ___   ___
| |/ /___ _ __ | | / _ \ / __|
| ' // _ \ '_ \| || | | |\__ \
| . \  __/ | | | || |_| |___/
|_|\_\___|_| |_|_| \___/|____/

Android Terminal Assistant
""")

load_plugins()

print("Plugins loaded successfully.")
print("Type 'help' for available commands.\n")

while True:

    try:

        text = input("[KenOS] $ ").strip()
       
        with open("data/history.txt", "a") as history:
            history.write(text + "\n")
 
        if not text:
            continue

        if text.lower() == "exit":
            print("Goodbye!")
            break

        parts = text.split()

        command = parts[0].lower()

        args = parts[1:]

        execute(command, args)

    except KeyboardInterrupt:
        print()

    except Exception as e:
        print("Error:", e)
