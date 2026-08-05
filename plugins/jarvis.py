from core.jarvis import jarvis
from command_manager import execute, exists

NAME = "jarvis"
DESCRIPTION = "Talk to Jarvis"

SKILLS = [
    "jarvis",
    "assistant",
    "ai"
]


def handle(text):

    plugin, args = jarvis.reply(text)

    if not plugin:

        print("🤖 I don't understand that yet.")
        return

    # Prevent Jarvis from calling itself
    if plugin == "jarvis":

        print("🤖 I'm already talking with you.")
        return

    if not exists(plugin):

        print(f"🤖 Plugin '{plugin}' not found.")
        return

    print(f"🤖 Jarvis → {plugin}")

    execute(plugin, args)


def run(args):

    # Single command mode:
    # jarvis what time is it

    if args:

        handle(" ".join(args))

        return

    # Interactive mode

    print()
    print("===================================")
    print("     🤖 Jarvis Conversation")
    print("===================================")
    print("Type 'exit' to leave.")
    print()

    while True:

        try:

            text = input("You: ").strip()

            if not text:
                continue

            if text.lower() in (
                "exit",
                "quit",
                "bye",
                "goodbye"
            ):

                print()
                print("👋 Goodbye.")
                print()

                break

            handle(text)

        except KeyboardInterrupt:

            print()
            print("👋 Conversation ended.")
            print()

            break
