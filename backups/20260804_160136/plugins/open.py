import subprocess

NAME = "open"
DESCRIPTION = "Open apps, URLs or searches"


def run(args):

    if not args:
        print("Usage: open <name>")
        return

    target = " ".join(args)

    lower = target.lower()

    if lower.startswith("http://") or lower.startswith("https://"):
        subprocess.run(["termux-open", target])
        return

    if lower.startswith("www."):
        subprocess.run(["termux-open", "https://" + target])
        return

    if lower.startswith("search "):

        query = target[7:].replace(" ", "+")

        subprocess.run([
            "termux-open",
            f"https://www.google.com/search?q={query}"
        ])

        return

    subprocess.run([
        "termux-open",
        target
    ])
