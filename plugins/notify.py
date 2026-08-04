from services.notification_service import notify

NAME = "notify"
DESCRIPTION = "Send an Android notification"


def run(args):

    if len(args) < 2:
        print("Usage: notify <title> <message>")
        return

    title = args[0]
    message = " ".join(args[1:])

    notify(title, message)

    print("Notification queued.")
