from core.memory import remember

NAME = "remember"
DESCRIPTION = "Save information"


def run(args):

    if len(args) < 2:
        print("Usage:")
        print("remember <key> <value>")
        return

    key = args[0]

    value = " ".join(args[1:])

    remember(key, value)

    print(f"✓ Saved '{key}'")
