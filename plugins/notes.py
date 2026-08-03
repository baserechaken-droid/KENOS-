NAME = "notes"
DESCRIPTION = "Create, list and clear notes"

FILE = "data/notes.txt"

def run(args):

    if not args:
        print("Usage:")
        print("  notes add <text>")
        print("  notes list")
        print("  notes clear")
        return

    action = args[0].lower()

    if action == "add":

        if len(args) < 2:
            print("Please enter a note.")
            return

        note = " ".join(args[1:])

        with open(FILE, "a") as f:
            f.write(note + "\n")

        print("Note saved.")

    elif action == "list":

        try:
            with open(FILE) as f:
                notes = f.readlines()

            if not notes:
                print("No notes found.")
                return

            print("\nNotes")
            print("-" * 30)

            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found.")

    elif action == "clear":

        open(FILE, "w").close()

        print("All notes deleted.")

    else:
        print("Unknown action.")
