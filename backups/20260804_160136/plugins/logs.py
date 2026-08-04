import os

NAME = "logs"
DESCRIPTION = "View KenOS logs"

LOG_FILE = "logs/kenos.log"


def run(args):

    if not os.path.exists(LOG_FILE):
        print("No logs available.")
        return

    with open(LOG_FILE) as f:
        lines = f.readlines()

    print()

    print("========== LAST LOGS ==========")

    for line in lines[-20:]:
        print(line.rstrip())

    print()
