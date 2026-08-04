import os
import sys

from core.console import success, warning


def check_python():

    if sys.version_info >= (3, 10):
        success(f"Python {sys.version.split()[0]}")
    else:
        warning("Python version is old")


def check_directories():

    for folder in (
        "data",
        "logs",
        "plugins",
        "core",
        "services"
    ):

        if os.path.isdir(folder):
            success(f"{folder}/")
        else:
            warning(f"{folder}/ missing")


def boot():

    print()

    print("Running startup diagnostics...\n")

    check_python()

    check_directories()

    print()
