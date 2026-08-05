from datetime import datetime


RESET = "\033[0m"

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BLUE = "\033[94m"

BOLD = "\033[1m"


def prompt():

    now = datetime.now().strftime("%H:%M:%S")

    print()

    print(
        f"{BLUE}╭──────────────────────────────────────────────────────╮{RESET}"
    )

    print(
        f"{BLUE}│{RESET} 🤖 {BOLD}Jarvis{RESET}  "
        f"{GREEN}● ONLINE{RESET}     "
        f"🕒 {YELLOW}{now}{RESET}"
    )

    print(
        f"{BLUE}╰──────────────────────────────────────────────────────╯{RESET}"
    )

    return f"{CYAN}KenOS{RESET} {GREEN}➜{RESET} "
