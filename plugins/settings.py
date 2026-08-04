from core.config import load, save

NAME = "settings"
DESCRIPTION = "View or modify KenOS settings"


def run(args):

    config = load()

    if not args:

        print()

        print("KenOS Settings")

        print("---------------------")

        for key, value in config.items():
            print(f"{key} = {value}")

        print()

        return

    if len(args) < 2:

        print("Usage: settings <key> <value>")
        return

    key = args[0]
    value = " ".join(args[1:])

    config[key] = value

    save(config)

    print("Setting updated.")
