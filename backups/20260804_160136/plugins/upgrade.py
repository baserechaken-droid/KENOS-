import subprocess
import sys

NAME = "upgrade"
DESCRIPTION = "Run the KenOS upgrader"


def run(args):

    subprocess.run([sys.executable, "tools/upgrade.py"])
