from datetime import datetime

NAME = "date"

DESCRIPTION = "Show today's date"

SKILLS = [
    "date",
    "today",
    "day",
    "calendar"
]


def run(args):

    now = datetime.now()

    message = now.strftime("📅 %A, %d %B %Y")

    print(message)

    return message
