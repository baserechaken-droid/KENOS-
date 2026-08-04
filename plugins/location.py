import subprocess

NAME = "location"
DESCRIPTION = "Get current GPS location"

def run(args):

    subprocess.run(
        ["termux-location"]
    )
