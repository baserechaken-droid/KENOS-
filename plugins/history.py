NAME = "history"
DESCRIPTION = "Show or clear command history"

FILE = "data/history.txt"

def run(args):

    if args and args[0] == "clear":
        open(FILE, "w").close()
        print("History cleared.")
        return

    try:
        with open(FILE) as f:
            lines = f.readlines()

        if not lines:
            print("History is empty.")
            return

        print("\nHistory")
        print("-" * 40)

        for i, line in enumerate(lines, 1):
            print(f"{i:3}. {line.strip()}")

    except FileNotFoundError:
        print("No history found.")
