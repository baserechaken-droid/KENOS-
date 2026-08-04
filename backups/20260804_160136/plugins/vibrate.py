from core.device import Device

NAME = "vibrate"
DESCRIPTION = "Vibrate phone"


def run(args):

    Device.vibrate()

    print("Phone vibrated.")
