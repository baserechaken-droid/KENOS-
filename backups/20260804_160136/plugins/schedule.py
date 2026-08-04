from core.scheduler import tasks

NAME = "schedule"
DESCRIPTION = "Show scheduled tasks"


def run(args):

    jobs = tasks()

    print()

    print("========== SCHEDULED TASKS ==========")

    if not jobs:
        print("No scheduled tasks.")
        print()
        return

    for i, job in enumerate(jobs, 1):

        print(
            f"{i}. {job['function']} "
            f"({job['delay']} seconds)"
        )

    print()
