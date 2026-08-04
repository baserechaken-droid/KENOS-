import subprocess

NAME = "share"
DESCRIPTION = "Open Android share dialog"

def run(args):

    if not args:
        print("Usage:")
        print("share <text>")
        return

    subprocess.run([
        "termux-share",
        "-a",
        "send",
        " ".join(args)
    ])
