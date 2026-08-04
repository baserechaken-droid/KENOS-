import subprocess

NAME = "sensors"
DESCRIPTION = "Read phone sensors"

def run(args):

    subprocess.run([
        "termux-sensor",
        "-l"
    ])
