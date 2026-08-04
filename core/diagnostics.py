import os
import sys


def startup_check():

    print()
    print("Running startup diagnostics...")
    print()

    print(f"✓ Python {sys.version.split()[0]}")

    folders = [
        "data",
        "logs",
        "plugins",
        "core",
        "services"
    ]

    for folder in folders:

        if os.path.isdir(folder):
            print(f"✓ {folder}/")
        else:
            print(f"✗ {folder}/ missing")

    print()
