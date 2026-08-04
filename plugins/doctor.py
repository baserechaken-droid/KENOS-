import os

from command_manager import list_plugins
from core.console import title, success, warning

NAME = "doctor"
DESCRIPTION = "Check KenOS health"


def run(args):

    title("KENOS DIAGNOSTICS")

    if os.path.isdir("data"):
        success("data/ directory found")
    else:
        warning("data/ directory missing")

    if os.path.isdir("logs"):
        success("logs/ directory found")
    else:
        warning("logs/ directory missing")

    print()

    print(f"Plugins Loaded : {len(list_plugins())}")

    print()

    success("Diagnostics complete")
