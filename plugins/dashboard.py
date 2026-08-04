import os
import platform
import shutil
import subprocess

from plugin_loader import loaded_plugins
from core.service_manager import list_services
from core.ui import title, divider

NAME = "dashboard"
DESCRIPTION = "KenOS system dashboard"


def battery():

    try:

        result = subprocess.check_output(
            ["termux-battery-status"],
            text=True
        )

        import json

        data = json.loads(result)

        return f"{data['percentage']}%"

    except:

        return "Unknown"


def wifi():

    try:

        result = subprocess.check_output(
            ["termux-wifi-connectioninfo"],
            text=True
        )

        import json

        data = json.loads(result)

        if data.get("ssid"):
            return data["ssid"]

        return "Disconnected"

    except:

        return "Unknown"


def storage():

    total, used, free = shutil.disk_usage("/")

    percent = int((used / total) * 100)

    return f"{percent}%"


def run(args):

    title("KENOS DASHBOARD")

    print(f"🤖 AI Engine      : Online")
    print(f"🐍 Python         : {platform.python_version()}")
    print(f"📦 Plugins        : {len(loaded_plugins)}")
    print(f"⚙ Services       : {len(list_services())}")
    print(f"🔋 Battery        : {battery()}")
    print(f"📶 WiFi           : {wifi()}")
    print(f"💾 Storage        : {storage()}")
    print(f"📂 Current Folder : {os.getcwd()}")

    divider()

    print("KenOS Status : HEALTHY")

    print()
