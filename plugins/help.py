from plugin_loader import loaded_plugins

NAME = "help"
DESCRIPTION = "Show all commands"

def run(args):

    print()

    print("KenOS Commands")
    print("-" * 40)

    for plugin in sorted(loaded_plugins, key=lambda p: p.NAME):
        print(f"{plugin.NAME:<12} {plugin.DESCRIPTION}")

    print()
