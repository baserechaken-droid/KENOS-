from core.memory import recall

NAME = "recall"
DESCRIPTION = "Recall saved information"


def run(args):

    if len(args) == 0:
        print("Usage:")
        print("recall <key>")
        return

    value = recall(args[0])

    if value is None:

        print("Nothing stored.")

    else:

        print(value)
