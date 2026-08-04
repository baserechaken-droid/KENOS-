from core.android import Android

NAME = "control"
DESCRIPTION = "Quick phone controls"


def run(args):

    print()

    print("========== PHONE CONTROL ==========")

    print()

    print("Available commands:")

    print()

    print("control torch on")
    print("control torch off")

    print("control vibrate")

    print("control speak Hello")

    print("control notify")

    print()

    if not args:
        return

    command = args[0].lower()

    if command == "torch":

        if len(args) > 1:

            Android.torch(args[1].lower() == "on")

        return

    if command == "vibrate":

        Android.vibrate()

        return

    if command == "speak":

        Android.speak(" ".join(args[1:]))

        return

    if command == "notify":

        Android.notify(
            "KenOS",
            "Control plugin test."
        )
