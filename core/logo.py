import time

from themes.theme_manager import get_theme

RESET = "\033[0m"

THEMES = {
    "matrix": {
        "primary": "\033[92m",
        "secondary": "\033[96m",
        "accent": "\033[94m"
    },
    "cyber": {
        "primary": "\033[95m",
        "secondary": "\033[96m",
        "accent": "\033[94m"
    },
    "ironman": {
        "primary": "\033[91m",
        "secondary": "\033[93m",
        "accent": "\033[97m"
    },
    "ubuntu": {
        "primary": "\033[91m",
        "secondary": "\033[97m",
        "accent": "\033[93m"
    },
    "minimal": {
        "primary": "\033[97m",
        "secondary": "\033[37m",
        "accent": "\033[90m"
    }
}


def colors():

    theme = get_theme().lower()

    return THEMES.get(theme, THEMES["matrix"])


def progress(message):

    c = colors()

    print()

    print(f"{c['secondary']}{message}{RESET}")

    time.sleep(0.30)

    print(f"{c['primary']}[████████████████████████████████] 100%{RESET}")


def show():

    c = colors()

    print()

    print(
f"""{c['primary']}
██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██║ ██╔╝██╔════╝████╗  ██║██╔═══██╗██╔════╝
█████╔╝ █████╗  ██╔██╗ ██║██║   ██║███████╗
██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║  ██╗███████╗██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
{RESET}"""
    )

    print(f"{c['secondary']}        Android AI Operating System{RESET}")

    print(f"{c['accent']}             Version 10 AI Edition{RESET}")

    progress("Initializing AI Engine...")
    progress("Loading Plugins...")
    progress("Starting Services...")
    progress("Preparing Voice Assistant...")

    print()
