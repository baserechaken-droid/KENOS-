import os

NAME = "health"
DESCRIPTION = "Check KenOS installation"


def check(path):

    return "✓" if os.path.exists(path) else "✗"


def run(args):

    print()

    print("KenOS Health Report")

    print("---------------------------")

    print("core       :", check("core"))
    print("plugins    :", check("plugins"))
    print("services   :", check("services"))
    print("logs       :", check("logs"))
    print("data       :", check("data"))
    print("config     :", check("config.json"))

    print()
