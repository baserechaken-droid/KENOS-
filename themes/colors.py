from themes.theme_manager import get_theme

RESET = "\033[0m"

THEMES = {
    "matrix": {
        "primary": "\033[92m",
        "secondary": "\033[96m",
        "accent": "\033[94m",
        "border": "\033[92m",
        "title": "\033[96m",
    },
    "cyber": {
        "primary": "\033[95m",
        "secondary": "\033[96m",
        "accent": "\033[94m",
        "border": "\033[95m",
        "title": "\033[96m",
    },
    "ironman": {
        "primary": "\033[91m",
        "secondary": "\033[93m",
        "accent": "\033[97m",
        "border": "\033[91m",
        "title": "\033[93m",
    },
    "ubuntu": {
        "primary": "\033[91m",
        "secondary": "\033[97m",
        "accent": "\033[93m",
        "border": "\033[91m",
        "title": "\033[97m",
    },
    "minimal": {
        "primary": "\033[97m",
        "secondary": "\033[37m",
        "accent": "\033[90m",
        "border": "\033[97m",
        "title": "\033[37m",
    }
}

def theme():
    return THEMES.get(get_theme().lower(), THEMES["matrix"])
