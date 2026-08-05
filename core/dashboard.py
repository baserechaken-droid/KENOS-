import os
import platform
import subprocess
import json
from datetime import datetime


def run_command(cmd):

    try:
        return subprocess.check_output(
            cmd,
            shell=True,
            text=True
        ).strip()

    except Exception:

        return "N/A"


def get_battery():

    data = run_command(
        "termux-battery-status"
    )

    if data != "N/A":

        try:

            battery = json.loads(data)

            return (
                f"{battery.get('percentage')}% "
                f"{battery.get('status')}"
            )

        except Exception:

            pass

    return "N/A"


def get_wifi():

    data = run_command(
        "termux-wifi-connectioninfo"
    )

    if data != "N/A":

        try:

            wifi = json.loads(data)

            return wifi.get(
                "ssid",
                "Connected"
            )

        except Exception:

            pass

    return "N/A"


def get_memory():

    data = run_command(
        "cat /proc/meminfo | grep MemAvailable"
    )

    if data != "N/A":

        return data.replace(
            "MemAvailable:",
            ""
        ).strip()

    return "N/A"


def get_cpu():

    return run_command(
        "getprop ro.product.model"
    )


def show():

    os.system("clear")

    now = datetime.now()

    print()

    print("╭────────────────────────────────────────────╮")
    print("│              KenOS v10 AI Dashboard        │")
    print("├────────────────────────────────────────────┤")

    print("│ 🤖 Jarvis       : ONLINE                   │")
    print("│ 🧠 AI Engine    : READY                    │")
    print(
        f"│ 📱 Device       : {get_cpu():<26}│"
    )
    print(
        f"│ 🐍 Python       : {platform.python_version():<26}│"
    )
    print(
        f"│ 🔋 Battery      : {get_battery():<26}│"
    )
    print(
        f"│ 📶 WiFi         : {get_wifi():<26}│"
    )
    print(
        f"│ 🧠 Memory       : {get_memory():<26}│"
    )
    print(
        f"│ 📅 Date         : {now.strftime('%d %B %Y'):<26}│"
    )
    print(
        f"│ 🕒 Time         : {now.strftime('%H:%M:%S'):<26}│"
    )

    print("╰────────────────────────────────────────────╯")
    print()


if __name__ == "__main__":

    show()
