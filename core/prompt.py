from datetime import datetime

from themes.theme_manager import get_theme

RESET = "\033[0m"

THEMES = {
    "matrix": {
        "box": "\033[92m",
        "text": "\033[96m",
        "arrow": "\033[92m",
        "status": "🟢"
    },
    "cyber": {
        "box": "\033[95m",
        "text": "\033[96m",
        "arrow": "\033[95m",
        "status": "🟣"
    },
    "ironman": {
        "box": "\033[91m",
        "text": "\033[93m",
        "arrow": "\033[91m",
        "status": "🔴"
    },
    "ubuntu": {
        "box": "\033[91m",
        "text": "\033[97m",
        "arrow": "\033[93m",
        "status": "🟠"
    },
    "minimal": {
        "box": "\033[97m",
        "text": "\033[37m",
        "arrow": "\033[97m",
        "status": "⚪"
    }
}


def get_prompt():

    now = datetime.now().strftime("%H:%M:%S")

    theme = get_theme().lower()

    c = THEMES.get(theme, THEMES["matrix"])

    return (
        "\n"
        f"{c['box']}╭─ 🤖 {c['text']}KenOS AI {c['box']}| "
        f"{c['status']} ONLINE {c['box']}| 🕒 {now} ─╮{RESET}\n"
        f"{c['arrow']}╰─➤ {RESET}"
    )
