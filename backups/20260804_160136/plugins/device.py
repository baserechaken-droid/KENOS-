from core.device import Device

NAME = "device"
DESCRIPTION = "Display phone information"


def run(args):

    battery = Device.battery() or {}
    wifi = Device.wifi() or {}

    print()
    print("=" * 60)
    print("               DEVICE CONTROL CENTER")
    print("=" * 60)

    print()

    print("BATTERY")
    print("--------------------------------------------")
    print(f"Level        : {battery.get('percentage','?')}%")
    print(f"Status       : {battery.get('status','Unknown')}")
    print(f"Health       : {battery.get('health','Unknown')}")
    print(f"Temperature  : {battery.get('temperature','?')}")

    print()

    print("NETWORK")
    print("--------------------------------------------")

    if wifi:
        print(f"SSID         : {wifi.get('ssid','Disconnected')}")
        print(f"Signal       : {wifi.get('rssi','?')} dBm")
        print(f"IP Address   : {wifi.get('ip','No IP')}")
        print(f"Frequency    : {wifi.get('frequency_mhz','?')} MHz")
    else:
        print("Not connected")

    print()
