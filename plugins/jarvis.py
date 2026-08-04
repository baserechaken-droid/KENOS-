from core.jarvis import jarvis
from command_manager import execute

NAME = "jarvis"
DESCRIPTION = "Talk to Jarvis"


def run(args):

    if not args:

        print("Usage: jarvis <message>")

        return

    text = " ".join(args)

    command, arguments = jarvis.reply(text)

    if command:

        print(f"🤖 Understood: {command}")

        execute(command, arguments)

    else:

        print("🤖 I don't understand that yet.")
