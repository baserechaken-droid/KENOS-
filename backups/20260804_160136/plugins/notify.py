from core.device import Device

NAME = "notify"
DESCRIPTION = "Show notification"


def run(args):

    if len(args) < 2:
        print("Usage:")
        print("notify <title> <message>")
        return

    title = args[0]
    message = " ".join(args[1:])

    Device.notify(title, message)

    print("Notification sent.")
