from command_manager import list_plugins


NAME = "help"
DESCRIPTION = "Show KenOS commands"


CATEGORIES = {

    "🤖 AI & Memory": [
        "jarvis",
        "remember",
        "recall",
        "about"
    ],

    "📱 Device Control": [
        "battery",
        "torch",
        "volume",
        "wifi",
        "sensors",
        "location"
    ],

    "⚙ System": [
        "dashboard",
        "sysinfo",
        "settings",
        "status",
        "doctor",
        "update"
    ],

    "🎤 Voice": [
        "listen",
        "voice",
        "speak"
    ],

    "🛠 Tools": [
        "calc",
        "notes",
        "open",
        "share",
        "clipboard"
    ],

    "🎵 Media": [
        "music",
        "photo",
        "notify"
    ]
}


def run(args):

    plugins = list_plugins()

    print()

    print("╭────────────────────────────────────────────╮")
    print("│              KenOS Commands                │")
    print("├────────────────────────────────────────────┤")

    for title, commands in CATEGORIES.items():

        print()
        print(title)

        for command in commands:

            if command in plugins:

                print(f"  • {command}")

    print()

    print("Other installed commands:")

    shown = set()

    for command in sorted(plugins):

        if command not in shown:

            print(f"  • {command}")

    print()

    print("Type a command or ask Jarvis naturally.")

    print("╰────────────────────────────────────────────╯")
    print()
