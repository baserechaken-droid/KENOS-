import json
import platform
import shutil
import subprocess
import time
from datetime import datetime

from plugin_loader import get_skills

try:
    from core.scheduler import scheduler
except Exception:
    scheduler = None

try:
    from core.memory import memory
except Exception:
    memory = None

try:
    from core.conversation import conversation
except Exception:
    conversation = None

try:
    from services.voice.engine import voice
except Exception:
    voice = None


NAME = "dashboard"
DESCRIPTION = "KenOS AI live dashboard"

SKILLS = [
    "dashboard",
    "system status",
    "status",
    "overview",
    "health"
]


def command(cmd):

    try:

        return subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL
        ).decode().strip()

    except Exception:

        return None


def battery():

    try:

        raw = command(
            ["termux-battery-status"]
        )

        if not raw:

            return "Unavailable"

        data = json.loads(raw)

        percent = data.get(
            "percentage",
            "?"
        )

        charging = (
            "Charging"
            if data.get("plugged")
            else "Battery"
        )

        temperature = data.get(
            "temperature",
            "?"
        )

        return (
            f"{percent}% "
            f"{charging} "
            f"{temperature}°C"
        )

    except Exception:

        return "Unavailable"


def network():

    try:

        raw = command(
            ["termux-wifi-connectioninfo"]
        )

        if not raw:

            return "Offline"

        data = json.loads(raw)

        ssid = data.get(
            "ssid",
            "Unknown"
        )

        ip = data.get(
            "ip",
            "?"
        )

        return f"{ssid} ({ip})"

    except Exception:

        return "Offline"


def memory_usage():

    try:

        info = open(
            "/proc/meminfo"
        ).read().splitlines()

        total = 0
        available = 0

        for line in info:

            if line.startswith("MemTotal"):

                total = int(
                    line.split()[1]
                )

            elif line.startswith(
                "MemAvailable"
            ):

                available = int(
                    line.split()[1]
                )

        used = total - available

        return (
            f"{used//1024}MB/"
            f"{total//1024}MB"
        )

    except Exception:

        return "Unavailable"


def cpu_usage():

    try:

        first = open(
            "/proc/stat"
        ).readline().split()

        idle1 = int(first[4])

        total1 = sum(
            map(
                int,
                first[1:8]
            )
        )

        time.sleep(0.3)

        second = open(
            "/proc/stat"
        ).readline().split()

        idle2 = int(second[4])

        total2 = sum(
            map(
                int,
                second[1:8]
            )
        )

        total = total2 - total1

        idle = idle2 - idle1

        return f"{100*(total-idle)/total:.1f}%"

    except Exception:

        return "Unavailable"


def storage():

    try:

        total, used, free = shutil.disk_usage("/data")

        return (
            f"{used//1024//1024//1024}GB/"
            f"{total//1024//1024//1024}GB"
        )

    except Exception:

        return "Unavailable"

def uptime():

    try:

        with open("/proc/uptime") as f:

            seconds = int(float(f.read().split()[0]))

        days = seconds // 86400

        hours = (seconds % 86400) // 3600

        minutes = (seconds % 3600) // 60

        if days:

            return f"{days}d {hours}h"

        return f"{hours}h {minutes}m"

    except Exception:

        return "Unavailable"


def plugin_count():

    try:

        return str(len(get_skills()))

    except Exception:

        return "0"


def scheduler_status():

    try:

        if scheduler:

            return str(scheduler.running())

    except Exception:

        pass

    return "Unavailable"


def memory_status():

    try:

        if memory:

            return str(len(memory.all()))

    except Exception:

        pass

    return "0"


def conversation_status():

    try:

        if conversation:

            return "Active"

    except Exception:

        pass

    return "Idle"


def voice_status():

    try:

        if voice:

            return "Ready"

    except Exception:

        pass

    return "Unavailable"


def draw():

    now = datetime.now()

    print()

    print("╔══════════════════════════════════════════════╗")

    print("║           🤖 KenOS AI Dashboard             ║")

    print("╠══════════════════════════════════════════════╣")

    print(f"║ AI Status      : {'ONLINE':<27}║")

    print(f"║ Voice Engine   : {voice_status():<27}║")

    print(f"║ Conversation   : {conversation_status():<27}║")

    print(f"║ Plugins        : {plugin_count():<27}║")

    print(f"║ Memory         : {memory_status():<27}║")

    print(f"║ Scheduler Jobs : {scheduler_status():<27}║")

    print(f"║ Python         : {platform.python_version():<27}║")

    print(f"║ Device         : {platform.machine():<27}║")

    print(f"║ CPU            : {cpu_usage():<27}║")

    print(f"║ RAM            : {memory_usage():<27}║")

    print(f"║ Storage        : {storage():<27}║")

    print(f"║ Battery        : {battery():<27}║")

    print(f"║ Network        : {network():<27}║")

    print(f"║ Uptime         : {uptime():<27}║")

    print(f"║ Time           : {now.strftime('%d %b %Y %H:%M:%S'):<27}║")

    print("╚══════════════════════════════════════════════╝")

    print()


def live():

    try:

        while True:

            print("\033[2J\033[H", end="")

            draw()

            time.sleep(1)

    except KeyboardInterrupt:

        print("\nLeaving dashboard...")


def run(args):

    if args:

        command = args[0].lower()

        if command == "live":

            live()

            return

    draw()

