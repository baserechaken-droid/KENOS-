import json
import subprocess
import os

NAME = "apps"
DESCRIPTION = "Manage installed applications"

FILE = "data/apps.json"


def load():

    if not os.path.exists(FILE):
        return {}

    with open(FILE) as f:
        return json.load(f)


def list_apps():

    apps = load()

    print("\n========== APPS ==========\n")

    for name in sorted(apps):
        print(f"{name:<15} {apps[name]}")

    print()


def open_app(name):

    apps = load()

    if name not in apps:
        print("Unknown app.")
        return

    package = apps[name]

    # Placeholder until Shizuku support
    print(f"Package: {package}")
    print("App launching will be enabled after Shizuku integration.")


def run(args):

    if not args:
        print("Usage:")
        print("apps list")
        print("apps open <name>")
        return

    command = args[0]

    if command == "list":
        list_apps()
        return

    if command == "open":

        if len(args) < 2:
            print("Specify app.")
            return

        open_app(args[1])
        return

    print("Unknown option.")
