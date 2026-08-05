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

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    print(f"🕒 Time: {current_time}")
    print(f"📅 Date: {current_date}")

    return f"The time is {current_time}. Today is {current_date}."
