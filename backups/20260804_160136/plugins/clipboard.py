import subprocess

NAME = "clipboard"
DESCRIPTION = "Read or write the clipboard"

def run(args):

    if not args:
        print("Usage:")
        print("clipboard get")
        print("clipboard set <text>")
        return

    if args[0] == "get":

        subprocess.run(["termux-clipboard-get"])

    elif args[0] == "set":

        subprocess.run(
            ["termux-clipboard-set", " ".join(args[1:])]
        )

    else:

        print("Unknown option.")
