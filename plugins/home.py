import subprocess
import json
import os
import datetime

NAME = "home"
DESCRIPTION = "KenOS Home Screen"


def battery():

    try:
        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        data = json.loads(result.stdout)

        return f"{data['percentage']}% ({data['status']})"

    except:
        return "Unknown"


def wifi():

    import subprocess
    import json

    try:

        result = subprocess.run(
            ["termux-wifi-connectioninfo"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return "OFF"

        output = result.stdout.strip()

        if output == "":
            return "OFF"

        data = json.loads(output)

        state = data.get("supplicant_state", "")

        if state != "COMPLETED":
            return "OFF"

        ssid = data.get("ssid", "Unknown")

        rssi = data.get("rssi", "?")

        return f"{ssid} ({rssi} dBm)"

    except Exception:
        return "OFF"

def pending_tasks():
    try:
        with open("data/tasks.json", "r") as f:
            tasks = json.load(f)

        return sum(1 for task in tasks if not task["done"])

    except:
        return 0

def plugins():

    count = 0

    for file in os.listdir("plugins"):

        if file.endswith(".py"):

            if file != "__init__.py":

                count += 1

    return count


def run(args):

    import os
    import datetime

    os.system("clear")

    print("=" * 55)
    print("               KENOS CONTROL CENTER")
    print("=" * 55)

    print()

    print("🤖 Assistant :", "Jarvis")
    print("👤 User      :", "Ken")

    print()

    print("🔋 Battery   :", battery())
    print("📶 Wi-Fi     :", wifi())
    print("🧩 Plugins   :", plugins())

    print("🕒 Time      :", datetime.datetime.now().strftime("%H:%M:%S"))
    print("📅 Date      :", datetime.datetime.now().strftime("%A %d %B %Y"))

    print("📋 Pending :", pending_tasks())

    print()

    print("=" * 55)

    print("Quick Commands")

    print("-------------------------")

    print("jarvis")
    print("battery")
    print("torch on")
    print("torch off")
    print("music")
    print("notes")
    print("plugins")

    print("=" * 55)
