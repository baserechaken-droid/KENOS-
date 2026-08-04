NAME = "time"

DESCRIPTION = "Show current time"

SKILLS = [
    "time",
    "clock",
    "hour",
    "date",
    "today"
]


def run(args):

    from datetime import datetime


    now = datetime.now()


    print(
        "🕒 Time:",
        now.strftime("%H:%M:%S")
    )


    print(
        "📅 Date:",
        now.strftime("%Y-%m-%d")
    )
