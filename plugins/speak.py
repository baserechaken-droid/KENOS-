from core.device import Device

NAME = "speak"
DESCRIPTION = "Speak text"


def run(args):

    if not args:
        print("Usage: speak <text>")
        return

    text = " ".join(args)

    Device.speak(text)
