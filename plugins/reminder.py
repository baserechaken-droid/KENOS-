from core.scheduler import scheduler

NAME = "reminder"
DESCRIPTION = "Create simple reminders"

SKILLS = [
    "reminder",
    "remind",
    "alarm"
]


def _notify(message):

    print()
    print("🔔 Reminder")
    print("--------------------")
    print(message)
    print()

    try:
        from services.voice.engine import voice
        voice.speak(message)
    except Exception:
        pass


def run(args):

    if len(args) < 2:

        print("Usage:")
        print("  reminder <seconds> <message>")
        return

    try:

        seconds = int(args[0])

    except ValueError:

        print("First argument must be the number of seconds.")
        return

    message = " ".join(args[1:])

    scheduler.schedule(
        seconds,
        _notify,
        message
    )

    print(f"⏰ Reminder scheduled in {seconds} second(s).")

    return f"I'll remind you in {seconds} seconds."

