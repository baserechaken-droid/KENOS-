from datetime import datetime

NAME = "hello"

DESCRIPTION = "Greet Jarvis"


def run(args):

    hour = datetime.now().hour

    if hour < 12:

        print("🌅 Good morning!")

    elif hour < 18:

        print("☀️ Good afternoon!")

    else:

        print("🌙 Good evening!")

    print()

    print("🤖 Jarvis is online.")

    print("How can I help you today?")
