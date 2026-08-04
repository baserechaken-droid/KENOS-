import subprocess

NAME = "volume"
DESCRIPTION = "Change media volume"

def run(args):

    if len(args) != 1:
        print("Usage: volume <0-15>")
        return

    subprocess.run([
        "termux-volume",
        "music",
        args[0]
    ])
