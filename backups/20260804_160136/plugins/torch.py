from core.device import Device
from core.scheduler import schedule

NAME = "torch"
DESCRIPTION = "Control the flashlight"


def turn_off():
    Device.torch(False)


def run(args):

    if not args:
        print("Usage: torch on|off [seconds]")
        return

    state = args[0].lower()

    if state == "on":

        Device.torch(True)

        print("🔦 Torch ON")

        if len(args) > 1:

            try:

                seconds = int(args[1])

                schedule(seconds, turn_off)

                print(f"Torch will turn off in {seconds} seconds.")

            except ValueError:

                print("Invalid timer.")

    elif state == "off":

        Device.torch(False)

        print("🔦 Torch OFF")

    else:

        print("Usage: torch on|off [seconds]")
