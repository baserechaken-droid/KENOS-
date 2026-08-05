from core.memory import memory

NAME = "remember"
DESCRIPTION = "Remember information"

SKILLS = [
    "remember",
    "save",
    "store"
]


def run(args):

    if len(args) < 2:

        print("Usage: remember <key> <value>")
        return

    key = args[0]

    value = " ".join(args[1:])

    memory.remember(key, value)

    print(f"✓ Remembered '{key}'.")

    return f"I'll remember your {key}."

