import platform
import subprocess
import json
from datetime import datetime

from plugin_loader import get_skills


NAME = "dashboard"
DESCRIPTION = "Show KenOS live dashboard"


def read_file(path):

    try:

        with open(path, "r") as f:
            return f.read().strip()

    except:

        return None



def battery():

    try:

        result = subprocess.check_output(
            ["termux-battery-status"]
        )

        data = json.loads(
            result.decode()
        )

        return (
            str(data.get("percentage", "N/A"))
            + "%"
        )

    except:

        paths = [
            "/sys/class/power_supply/battery/capacity",
            "/sys/class/power_supply/BAT0/capacity"
        ]

        for path in paths:

            value = read_file(path)

            if value:

                return value + "%"

    return "N/A"



def memory():

    data = read_file(
        "/proc/meminfo"
    )

    if not data:

        return "N/A"


    total = 0
    available = 0


    for line in data.splitlines():

        if line.startswith("MemTotal"):

            total = int(
                line.split()[1]
            )


        if line.startswith("MemAvailable"):

            available = int(
                line.split()[1]
            )


    if total:

        used = total - available

        return (
            f"{used // 1024}MB / "
            f"{total // 1024}MB"
        )


    return "N/A"



def uptime():

    value = read_file(
        "/proc/uptime"
    )

    if value:

        try:

            seconds = int(
                float(
                    value.split()[0]
                )
            )

            hours = seconds // 3600

            minutes = (
                seconds % 3600
            ) // 60

            return f"{hours}h {minutes}m"

        except:

            pass


    try:

        result = subprocess.check_output(
            ["uptime"]
        ).decode()


        if "up" in result:

            part = result.split("up")[1]

            part = part.split(",")[0]

            return part.strip()


    except:

        pass


    return "N/A"



def run(args):

    now = datetime.now()


    print()

    print(
        "╭────────────────────────────────────────────╮"
    )

    print(
        "│          KenOS v10 AI Dashboard            │"
    )

    print(
        "├────────────────────────────────────────────┤"
    )

    print(
        "│ 🤖 Jarvis       : ONLINE                   │"
    )

    print(
        "│ 🧠 AI Engine    : READY                    │"
    )

    print(
        f"│ 🐍 Python       : {platform.python_version():<25}│"
    )

    print(
        "│ 📱 System       : Android                  │"
    )

    print(
        f"│ 🔋 Battery      : {battery():<25}│"
    )

    print(
        f"│ 🧠 RAM          : {memory():<25}│"
    )

    print(
        f"│ ⏱ Uptime        : {uptime():<25}│"
    )

    print(
        f"│ 🧩 Plugins      : {len(get_skills()):<25}│"
    )

    print(
        f"│ 📅 Time         : {now.strftime('%d %b %Y %H:%M'):<25}│"
    )

    print(
        "╰────────────────────────────────────────────╯"
    )

    print()
