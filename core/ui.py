import os

class Color:

    RESET = "\033[0m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BOLD = "\033[1m"


def title(text):

    print()
    print(Color.CYAN + Color.BOLD + "=" * 50)
    print(text.center(50))
    print("=" * 50 + Color.RESET)
    print()


def success(text):

    print(Color.GREEN + "✓ " + text + Color.RESET)


def warning(text):

    print(Color.YELLOW + "⚠ " + text + Color.RESET)


def error(text):

    print(Color.RED + "✗ " + text + Color.RESET)


def info(text):

    print(Color.BLUE + "ℹ " + text + Color.RESET)


def jarvis(text):

    print(Color.MAGENTA + "🤖 Jarvis: " + text + Color.RESET)


def divider():

    print(Color.CYAN + "-" * 50 + Color.RESET)
