from core.device import Device
from core.console import title, info

NAME = "battery"
DESCRIPTION = "Show battery information"


def run(args):

    battery = Device.battery()

    if not battery:
        print("Unable to read battery information.")
        return

    title("BATTERY")

    info("Percentage", f"{battery.get('percentage', '?')}%")
    info("Status", battery.get("status", "Unknown"))
    info("Health", battery.get("health", "Unknown"))
    info("Temperature", battery.get("temperature", "?"))
    print()
