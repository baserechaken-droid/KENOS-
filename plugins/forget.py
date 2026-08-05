from core.memory import memory

NAME = "forget"
DESCRIPTION = "Forget stored memory"

SKILLS = [
    "forget",
    "delete memory"
]


def run(args):

    if not args:

        print("Usage: forget <key>")

        return

    key = args[0]

    memory.forget(key)

    print(f"✓ Forgot '{key}'.")

    return f"I forgot your {key}."

