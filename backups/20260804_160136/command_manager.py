import difflib

plugins = {}


def register(name, module):
    plugins[name] = module


def exists(name):
    return name in plugins


def get(name):
    return plugins.get(name)


def list_plugins():
    return plugins


def execute(command, args):

    if command in plugins:

        try:
            plugins[command].run(args)

        except Exception as e:
            print(f"[ERROR] {command}: {e}")

        return

    suggestion = difflib.get_close_matches(
        command,
        plugins.keys(),
        n=1,
        cutoff=0.6
    )

    print(f"\nUnknown command: {command}")

    if suggestion:
        print(f"Did you mean '{suggestion[0]}'?")

    print("Type 'help' to see available commands.\n")
