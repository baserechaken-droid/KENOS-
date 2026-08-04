from datetime import datetime
import os
import platform

from core.device import Device
from core.config import load
from command_manager import list_plugins

NAME = "mission"
DESCRIPTION = "KenOS Mission Control"


def run(args):

    config = load()

    battery = Device.battery() or {}
    wifi = Device.wifi() or {}

    print()
    print("=" * 60)
    print("                 KENOS MISSION CONTROL")
    print("=" * 60)
    print()

    print(f"🤖 Assistant : {config.get('assistant_name', 'Jarvis')}")
    print(f"👤 User      : {config.get('user_name', 'User')}")
    print(f"🧩 Plugins   : {len(list_plugins())}")

    print()

    print("BATTERY")
    print("-" * 60)
    print(f"🔋 Level      : {battery.get('percentage', '?')}%")
    print(f"⚡ Status     : {battery.get('status', 'Unknown')}")
    print(f"❤️ Health     : {battery.get('health', 'Unknown')}")
    print(f"🌡 Temperature: {battery.get('temperature', '?')}")

    print()

    print("NETWORK")
    print("-" * 60)

    if wifi:
        print(f"📶 SSID       : {wifi.get('ssid', 'Disconnected')}")
        print(f"📡 Signal     : {wifi.get('rssi', '?')} dBm")
        print(f"🌐 IP Address : {wifi.get('ip', 'No IP')}")
    else:
        print("📶 Not connected")

    print()

    print("SYSTEM")
    print("-" * 60)
    print(f"💻 OS         : {platform.system()} {platform.release()}")
    print(f"🐍 Python     : {platform.python_version()}")
    print(f"🧠 CPU Cores  : {os.cpu_count()}")

    print()

    print("TIME")
    print("-" * 60)
    print(f"🕒 Time       : {datetime.now().strftime('%H:%M:%S')}")
    print(f"📅 Date       : {datetime.now().strftime('%Y-%m-%d')}")

    print()
    print("=" * 60)
    print(" QUICK COMMANDS")
    print("=" * 60)

    print("battery     torch")
    print("wifi        notes")
    print("doctor      plugins")
    print("settings    logs")
    print("jarvis      mission")
    print("system      exit")

    print("=" * 60)
    print()
