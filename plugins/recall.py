from core.memory import memory

NAME = "recall"
DESCRIPTION = "Recall stored information"

SKILLS = [
    "recall",
    "remembered",
    "memory"
]


def run(args):

    if not args:

        data = memory.all()

        if not data:

            print("Memory is empty.")

            return "I don't remember anything yet."

        print()

        print("🧠 Memory")

        print("--------------------")

        for key, value in sorted(data.items()):

            print(f"{key}: {value}")

        print()

        return

    key = args[0]

    value = memory.recall(key)

    if value is None:

        print("Nothing stored.")

        return "I don't remember that."

    print(value)

    return value

