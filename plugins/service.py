from core.service_manager import (
    start,
    stop,
    running,
    list_services
)

NAME = "service"
DESCRIPTION = "Manage KenOS background services"


def run(args):

    if not args:

        print()

        print("Registered Services")
        print("-------------------")

        for name, service in list_services().items():

            state = "Running" if service["running"] else "Stopped"

            print(f"{name:<15}{state}")

        print()

        return

    cmd = args[0].lower()

    if len(args) < 2:

        print("Usage:")
        print("service start <name>")
        print("service stop <name>")

        return

    name = args[1]

    if cmd == "start":

        if start(name):
            print(f"{name} started.")
        else:
            print("Unknown service.")

        return

    if cmd == "stop":

        stop(name)

        print(f"{name} stopped.")

        return

    print("Unknown option.")
