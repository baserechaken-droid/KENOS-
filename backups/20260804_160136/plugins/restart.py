import os

NAME = "restart"
DESCRIPTION = "Restart KenOS"


def run(args):

    print("Restarting KenOS...")

    os.execvp("python", ["python", "kenos.py"])
