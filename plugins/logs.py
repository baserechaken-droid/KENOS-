import os

NAME = "logs"
DESCRIPTION = "View KenOS logs"

LOG_FILE = "logs/kenos.log"


def run(args):

    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("Log file is empty.")
        return

    count = 20

    if args:
        try:
            count = int(args[0])
        except ValueError:
            pass

    print()

    for line in lines[-count:]:
        print(line.rstrip())

    print()
