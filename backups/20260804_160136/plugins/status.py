from core.device import Device

NAME = "status"
DESCRIPTION = "Quick system summary"


def run(args):

    battery = Device.battery() or {}
    wifi = Device.wifi() or {}

    print()

    print("KenOS Status")
    print("---------------------------")

    print(f"Battery : {battery.get('percentage','?')}%")

    if wifi:
        print(f"Wi-Fi   : {wifi.get('ssid','Disconnected')}")
    else:
        print("Wi-Fi   : Off")

    print("System  : Ready")

    print()
