import subprocess
import json
import platform
import datetime
import os

NAME = "dashboard"
DESCRIPTION = "Shows KenOS system dashboard"


def run(args):

    os.system("clear")

    print("=" * 42)
    print("           KenOS Dashboard")
    print("=" * 42)

    try:

        battery = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        info = json.loads(battery.stdout)

        print(f"Battery  : {info['percentage']}%")
        print(f"Charging : {info['status']}")

    except Exception:

        print("Battery  : Unknown")

    print()

    print("Device   :", platform.node())
    print("System   :", platform.system())
    print("Release  :", platform.release())

    print()

    print(
        "Time     :",
        datetime.datetime.now().strftime("%H:%M:%S")
    )

    print("=" * 42)
