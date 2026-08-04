from command_manager import plugins

NAME = "help"
DESCRIPTION = "Show all available commands"


def run(args):

    print()

    print("========== KenOS Commands ==========")
    print()

    for name in sorted(plugins):

        description = getattr(
            plugins[name],
            "DESCRIPTION",
            "No description"
        )

        print(f"{name:<15} {description}")

    print()
    print("exit            Exit KenOS")
    print()
