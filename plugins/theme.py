from themes.theme_manager import get_theme, set_theme

NAME = "theme"
DESCRIPTION = "Manage KenOS themes"

SKILLS = [
    "theme",
    "themes",
    "appearance",
    "color",
    "colors",
    "style"
]

THEME_INFO = {
    "matrix": {
        "color": "\033[92m",
        "icon": "🟢",
        "desc": "Green hacker interface"
    },
    "cyber": {
        "color": "\033[95m",
        "icon": "🟣",
        "desc": "Purple cyberpunk interface"
    },
    "ironman": {
        "color": "\033[91m",
        "icon": "🔴",
        "desc": "Red and gold Jarvis interface"
    },
    "ubuntu": {
        "color": "\033[93m",
        "icon": "🟠",
        "desc": "Ubuntu-inspired interface"
    },
    "minimal": {
        "color": "\033[97m",
        "icon": "⚪",
        "desc": "Minimal monochrome interface"
    }
}

RESET = "\033[0m"


def preview(name):

    t = THEME_INFO[name]

    c = t["color"]

    print()
    print(c + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
    print(c + f"{t['icon']} Theme Preview : {name.upper()}" + RESET)
    print(c + f"Description    : {t['desc']}" + RESET)
    print(c + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
    print()


def run(args):

    if not args:

        current = get_theme()

        print()
        print(f"Current theme : {current}")
        print()

        print("Available themes:")

        for name, info in THEME_INFO.items():
            print(f"  {info['icon']} {name:<10} - {info['desc']}")

        print()
        print("Usage:")
        print("  theme matrix")
        print("  theme cyber")
        print("  theme ironman")
        print("  theme ubuntu")
        print("  theme minimal")
        print()

        return

    theme = args[0].lower()

    if theme not in THEME_INFO:

        print("Unknown theme.")
        return

    set_theme(theme)

    preview(theme)

    print(f"✓ Theme changed to {theme}.")
    print("✓ New prompts and screens will use this theme.")
    print()
