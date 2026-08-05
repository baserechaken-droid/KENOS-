import time


# KenOS Theme Colors
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"


def progress(message):

    print()

    print(
        f"{CYAN}{message}{RESET}"
    )

    time.sleep(0.3)

    print(
        f"{GREEN}[████████████████████████████████] 100%{RESET}"
    )


def show():

    print()

    print(
f"""
{GREEN}
██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██║ ██╔╝██╔════╝████╗  ██║██╔═══██╗██╔════╝
█████╔╝ █████╗  ██╔██╗ ██║██║   ██║███████╗
██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║  ██╗███████╗██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
{RESET}
"""
    )


    print(
        f"{CYAN}        Android AI Operating System{RESET}"
    )

    print(
        f"{BLUE}             Version 10 AI Edition{RESET}"
    )

    progress(
        "Initializing AI Engine..."
    )

    progress(
        "Loading Plugins..."
    )

    progress(
        "Starting Services..."
    )

    progress(
        "Preparing Voice Assistant..."
    )

    print()
