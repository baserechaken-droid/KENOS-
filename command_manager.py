import difflib

plugins = {}


def register(name, module):

    if name in plugins:
        raise ValueError(f"Duplicate command: {name}")

    plugins[name] = module


def unregister(name):

    plugins.pop(name, None)


def clear():

    plugins.clear()


def exists(name):

    return name in plugins


def get(name):

    return plugins.get(name)


def list_plugins():

    return dict(sorted(plugins.items()))


def count():

    return len(plugins)


def execute(command, args):

    module = plugins.get(command)

    if module:

        try:

            result = module.run(args)

            return result

        except Exception as e:

            print(f"[ERROR] {command}: {e}")

            return None

    suggestion = difflib.get_close_matches(
        command,
        plugins.keys(),
        n=1,
        cutoff=0.60
    )

    print()
    print(f"Unknown command: {command}")

    if suggestion:
        print(f"Did you mean '{suggestion[0]}'?")

    print("Type 'help' to view commands.")
    print()

    return None
