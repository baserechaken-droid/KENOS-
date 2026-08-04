from core.plugins import names

NAME = "help"
DESCRIPTION = "Show all available commands"


def run(args):

    print()

    print("=" * 45)
    print("KenOS Commands")
    print("=" * 45)

    for command in names():
        print(command)

    print()
    print("Built-in Commands")
    print("-----------------")
    print("help")
    print("exit")
    print()
