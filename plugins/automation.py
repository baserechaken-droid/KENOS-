import json
import os

FILE = "data/automation.json"

NAME = "automation"
DESCRIPTION = "Manage automation rules"

SKILLS = [
    "automation",
    "automate",
    "rule",
    "rules"
]


def load():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):

        return []

    try:

        with open(FILE) as f:

            return json.load(f)

    except Exception:

        return []


def save(rules):

    with open(FILE, "w") as f:

        json.dump(
            rules,
            f,
            indent=4
        )


def run(args):

    rules = load()

    if not args:

        print()

        print("🤖 Automation Rules")

        print("-" * 40)

        if not rules:

            print("No rules configured.")

            return "No automation rules."

        for i, rule in enumerate(rules, 1):

            print(f"{i}. {rule}")

        print()

        return

    cmd = args[0].lower()

    if cmd == "add":

        if len(args) < 2:

            print("Usage: automation add <rule>")

            return

        rule = " ".join(args[1:])

        rules.append(rule)

        save(rules)

        print("✓ Rule added.")

        return "Automation rule saved."

    if cmd == "clear":

        save([])

        print("✓ Rules cleared.")

        return "All automation rules removed."

    print("Unknown automation command.")

