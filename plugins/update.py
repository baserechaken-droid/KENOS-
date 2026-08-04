import subprocess
import sys

NAME = "update"
DESCRIPTION = "Run the KenOS updater"


def run(args):

    subprocess.run(
        [sys.executable, "tools/update.py"]
    )
