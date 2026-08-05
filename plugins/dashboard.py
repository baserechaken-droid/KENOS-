import platform
import subprocess
import json
import time
from datetime import datetime

from plugin_loader import get_skills


NAME = "dashboard"
DESCRIPTION = "Show KenOS live system dashboard"



def command(cmd):

    try:
        return subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL
        ).decode().strip()

    except:
        return None



def battery():

    try:

        data = json.loads(
            command(
                ["termux-battery-status"]
            )
        )

        return str(
            data.get("percentage")
        ) + "%"

    except:

        return "N/A"



def memory():

    try:

        data = open(
            "/proc/meminfo"
        ).read()


        total = 0
        available = 0


        for line in data.splitlines():

            if line.startswith("MemTotal"):
                total = int(line.split()[1])

            if line.startswith("MemAvailable"):
                available = int(line.split()[1])


        return (
            f"{(total-available)//1024}MB/"
            f"{total//1024}MB"
        )

    except:

        return "N/A"



def cpu():

    try:

        first = open(
            "/proc/stat"
        ).readline().split()


        idle1 = int(first[4])
        total1 = sum(
            map(int, first[1:8])
        )


        time.sleep(0.5)


        second = open(
            "/proc/stat"
        ).readline().split()


        idle2 = int(second[4])
        total2 = sum(
            map(int, second[1:8])
        )


        diff_total = total2-total1
        diff_idle = idle2-idle1


        usage = (
            100 *
            (diff_total-diff_idle)
            /
            diff_total
        )


        return f"{usage:.1f}%"

    except:

        return "N/A"



def storage():

    try:

        result = command(
            ["df","-h","/data"]
        )

        if result:

            line = result.splitlines()[1]

            parts = line.split()

            return (
                parts[2]
                +
                "/"
                +
                parts[1]
            )

    except:

        pass


    return "N/A"



def uptime():

    try:

        result = command(
            ["cat","/proc/uptime"]
        )


        if result:

            seconds = int(
                float(
                    result.split()[0]
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

        result = command(
            ["termux-battery-status"]
        )

        if result:

            return "Running"


    except:

        pass


    return "N/A"



def network():

    try:

        info = command(
            ["termux-wifi-connectioninfo"]
        )

        if info:

            return "WIFI"

    except:

        pass


    return "OFFLINE"



def run(args):

    now = datetime.now()


    print()

    print("╭────────────────────────────────────────────╮")
    print("│          KenOS v10.1 AI Dashboard           │")
    print("├────────────────────────────────────────────┤")

    print("│ 🤖 Jarvis       : ONLINE                   │")
    print("│ 🧠 AI Engine    : READY                    │")

    print(
        f"│ 🐍 Python       : {platform.python_version():<25}│"
    )

    print(
        f"│ 📱 Device       : {platform.machine():<25}│"
    )

    print(
        f"│ 🔋 Battery      : {battery():<25}│"
    )

    print(
        f"│ 🧠 RAM          : {memory():<25}│"
    )

    print(
        f"│ ⚙ CPU           : {cpu():<25}│"
    )

    print(
        f"│ 💾 Storage      : {storage():<25}│"
    )

    print(
        f"│ 🌐 Network      : {network():<25}│"
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

    print("╰────────────────────────────────────────────╯")

    print()
