import os
import sys
import time
import platform
from datetime import datetime


RESET  = "\033[0m"
BOLD   = "\033[1m"

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"


WIDTH = 32


def clear():

    os.system("clear")


def line():

    print(f"{BLUE}{'━'*60}{RESET}")


def progress(title):

    print(f"{CYAN}{title}{RESET}")

    sys.stdout.write("[")

    for i in range(WIDTH):

        sys.stdout.write(f"{GREEN}█{RESET}")

        sys.stdout.flush()

        time.sleep(0.015)

    sys.stdout.write("] ")

    print(f"{GREEN}100%{RESET}")

    print()


def show():

    clear()

    print()

    print(f"""{CYAN}{BOLD}
██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██║ ██╔╝██╔════╝████╗  ██║██╔═══██╗██╔════╝
█████╔╝ █████╗  ██╔██╗ ██║██║   ██║███████╗
██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║  ██╗███████╗██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
{RESET}
""")

    print(f"{GREEN}        Android AI Operating System")
    print(f"{WHITE}             Version 10 AI Edition{RESET}")

    print()

    progress("Initializing AI Engine...")
    progress("Loading Plugins...")
    progress("Starting Services...")
    progress("Preparing Voice Assistant...")

    now = datetime.now()

    line()

    print(f"{GREEN}✓ System      : {platform.system()} {platform.release()}")
    print(f"{GREEN}✓ Python      : {platform.python_version()}")
    print(f"{GREEN}✓ Date        : {now.strftime('%d %B %Y')}")
    print(f"{GREEN}✓ Time        : {now.strftime('%H:%M:%S')}")
    print(f"{GREEN}✓ Status      : READY")

    line()

