from core.plugins import names, count

NAME = "plugins"
DESCRIPTION = "List installed plugins"


def run(args):

    print()

    print("Installed Plugins")
    print("-----------------")

    for plugin in names():
        print(plugin)

    print()
    print(f"Total: {count()}")
    print()
