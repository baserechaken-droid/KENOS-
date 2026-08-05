from datetime import datetime

NAME = "time"

DESCRIPTION = "Show current time"

SKILLS = [
    "time",
    "clock",
    "hour"
]


def run(args):

    now = datetime.now()

    message = (
        f"🕒 Time: {now.strftime('%H:%M:%S')}\n"
        f"📅 Date: {now.strftime('%Y-%m-%d')}"
    )

    print(message)

    return message
