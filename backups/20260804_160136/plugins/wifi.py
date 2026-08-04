from core.device import Device

NAME = "wifi"
DESCRIPTION = "Wi-Fi information"


def run(args):

    wifi = Device.wifi()

    if wifi is None:
        print("Wi-Fi unavailable.")
        return

    if wifi.get("supplicant_state") != "COMPLETED":
        print("Wi-Fi is not connected.")
        return

    print()

    print("Wi-Fi")

    print("----------------")

    print("SSID      :", wifi.get("ssid"))
    print("IP        :", wifi.get("ip"))
    print("Signal    :", wifi.get("rssi"), "dBm")
    print("Frequency :", wifi.get("frequency_mhz"), "MHz")
    print("Speed     :", wifi.get("link_speed_mbps"), "Mbps")

    print()
