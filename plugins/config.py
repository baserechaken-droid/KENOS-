from core.config import load, get, set

NAME = "config"
DESCRIPTION = "View and modify KenOS settings"


def run(args):

    if not args:

        cfg = load()

        print()

        print("KenOS Configuration")
        print("-------------------")

        for k, v in cfg.items():
            print(f"{k:<25}{v}")

        print()

        return

    if len(args) == 1:

        print(get(args[0], "Not found"))

        return

    key = args[0]

    value = " ".join(args[1:])

    if value.lower() == "true":
        value = True

    elif value.lower() == "false":
        value = False

    set(key, value)

    print(f"{key} updated.")
