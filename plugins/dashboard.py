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
