import json
import os
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
DESCRIPTION = "KenOS System Dashboard"

SKILLS = [
    "dashboard",
    "status",
    "system status",
    "overview",
    "health"
]


# -------------------------------------------------
# Helpers
# -------------------------------------------------

def command(cmd):

    try:

        return subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL
        ).decode().strip()

    except Exception:

        return None


def row(label, value):

    value = str(value)

    if len(value) > 32:

        value = value[:29] + "..."

    print(
        f"║ {label:<15}: {value:<32}║"
    )


def line():

    print(
        "╠══════════════════════════════════════════════════════╣"
    )


def header():

    print()

    print(
        "╔══════════════════════════════════════════════════════╗"
    )

    print(
        "║               🤖 KenOS AI Dashboard                 ║"
    )

    line()


def footer():

    print(
        "╚══════════════════════════════════════════════════════╝"
    )

    print()


# -------------------------------------------------
# Battery
# -------------------------------------------------

def battery():

    try:

        raw = command(
            ["termux-battery-status"]
        )

        if not raw:

            return "Unavailable"

        data = json.loads(raw)

        percent = data.get("percentage", "?")

        charging = (
            "Charging"
            if data.get("plugged")
            else "Battery"
        )

        temp = data.get(
            "temperature",
            "?"
        )

        return f"{percent}% {charging} {temp}°C"

    except Exception:

        return "Unavailable"


# -------------------------------------------------
# Network
# -------------------------------------------------

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


# -------------------------------------------------
# RAM
# -------------------------------------------------

def ram():

    try:

        total = 0

        available = 0

        with open("/proc/meminfo") as f:

            for line in f:

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


# -------------------------------------------------
# Storage
# -------------------------------------------------

def storage():

    try:

        total, used, free = shutil.disk_usage(
            "/data"
        )

        return (
            f"{used//1024//1024//1024}GB/"
            f"{total//1024//1024//1024}GB"
        )

    except Exception:

        return "Unavailable"

# -------------------------------------------------
# CPU
# -------------------------------------------------

def cpu():

    try:

        raw = command(
            [
                "sh",
                "-c",
                "top -bn1 | grep '%cpu' || top -n 1 | head -5"
            ]
        )

        if raw:

            return raw.splitlines()[0]

    except Exception:

        pass

    try:

        first = open("/proc/stat").readline().split()

        idle1 = int(first[4])

        total1 = sum(int(x) for x in first[1:])

        time.sleep(0.2)

        second = open("/proc/stat").readline().split()

        idle2 = int(second[4])

        total2 = sum(int(x) for x in second[1:])

        total = total2 - total1

        idle = idle2 - idle1

        if total <= 0:

            return "0%"

        usage = 100 * (total - idle) / total

        return f"{usage:.1f}%"

    except Exception:

        return "Unavailable"


# -------------------------------------------------
# Uptime
# -------------------------------------------------

def uptime():

    try:

        raw = command(
            ["uptime"]
        )

        if raw:

            return raw

    except Exception:

        pass

    try:

        with open("/proc/uptime") as f:

            seconds = int(float(f.read().split()[0]))

        days, seconds = divmod(seconds, 86400)

        hours, seconds = divmod(seconds, 3600)

        minutes = seconds // 60

        if days:

            return f"{days}d {hours}h"

        return f"{hours}h {minutes}m"

    except Exception:

        return "Unavailable"


# -------------------------------------------------
# Status
# -------------------------------------------------

def plugins_loaded():

    try:

        return len(get_skills())

    except Exception:

        return 0


def scheduler_jobs():

    try:

        if scheduler:

            return scheduler.running()

    except Exception:

        pass

    return 0


def memory_items():

    try:

        if memory and hasattr(memory, "all"):

            return len(memory.all())

    except Exception:

        pass

    return 0


def conversation_state():

    return (
        "Active"
        if conversation
        else "Idle"
    )


def voice_state():

    return (
        "Ready"
        if voice
        else "Unavailable"
    )


def android():

    version = command(
        [
            "getprop",
            "ro.build.version.release"
        ]
    )

    sdk = command(
        [
            "getprop",
            "ro.build.version.sdk"
        ]
    )

    if version and sdk:

        return f"Android {version} (SDK {sdk})"

    return "Unknown"


def architecture():

    return platform.machine()


def python_version():

    return platform.python_version()


def hostname():

    return platform.node()


def cpu_cores():

    return os.cpu_count() or "Unknown"


def load_average():

    try:

        a = os.getloadavg()

        return f"{a[0]:.2f} {a[1]:.2f} {a[2]:.2f}"

    except Exception:

        return "Unavailable"


# -------------------------------------------------
# Dashboard
# -------------------------------------------------

def draw():

    now = datetime.now()

    header()

    row("AI Status", "ONLINE")
    row("Voice", voice_state())
    row("Conversation", conversation_state())
    row("Plugins", plugins_loaded())
    row("Memory", memory_items())
    row("Scheduler", scheduler_jobs())

    line()

    row("Android", android())
    row("Python", python_version())
    row("Architecture", architecture())
    row("Hostname", hostname())
    row("CPU Cores", cpu_cores())

    line()

    row("CPU", cpu())
    row("RAM", ram())
    row("Storage", storage())
    row("Battery", battery())
    row("Network", network())
    row("Load Avg", load_average())
    row("Uptime", uptime())

    line()

    row(
        "Time",
        now.strftime(
            "%d %b %Y %H:%M:%S"
        )
    )

    footer()


# -------------------------------------------------
# Live Dashboard
# -------------------------------------------------

def live():

    try:

        while True:

            os.system("clear")

            draw()

            time.sleep(1)

    except KeyboardInterrupt:

        print()

        print("Dashboard closed.")

        print()


# -------------------------------------------------
# Plugin Entry
# -------------------------------------------------

def run(args):

    if args:

        option = args[0].lower()

        if option == "live":

            live()

            return

        if option == "refresh":

            draw()

            return

    draw()


if __name__ == "__main__":

    run([])

