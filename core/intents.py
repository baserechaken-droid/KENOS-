import re


RULES = [

    #
    # Time
    #

    (
        [
            r"what('?s| is)? the time",
            r"tell me the time",
            r"time now",
            r"current time",
            r"^time$"
        ],
        "time",
        []
    ),

    #
    # Date
    #

    (
        [
            r"today('?s)? date",
            r"current date",
            r"what('?s| is)? the date",
            r"^date$"
        ],
        "date",
        []
    ),

    #
    # Battery
    #

    (
        [
            r"battery",
            r"battery level",
            r"battery percentage",
            r"battery status",
            r"how much battery",
            r"how much charge"
        ],
        "battery",
        []
    ),

    #
    # Dashboard
    #

    (
        [
            r"dashboard",
            r"show dashboard",
            r"open dashboard"
        ],
        "dashboard",
        []
    ),

    #
    # Status
    #

    (
        [
            r"status",
            r"system status",
            r"device status"
        ],
        "status",
        []
    ),

    #
    # Torch ON
    #

    (
        [
            r"(turn|switch|enable|activate).*(flashlight|flash light|torch|lamp)",
            r"(flashlight|flash light|torch|lamp).*(on)"
        ],
        "torch",
        ["on"]
    ),

    #
    # Torch OFF
    #

    (
        [
            r"(turn|switch|disable|deactivate).*(off).*(flashlight|flash light|torch|lamp)",
            r"(turn|switch|disable|deactivate).*(flashlight|flash light|torch|lamp).*(off)"
        ],
        "torch",
        ["off"]
    ),

    #
    # WiFi
    #

    (
        [
            r"wifi",
            r"wi-fi",
            r"wireless"
        ],
        "wifi",
        []
    ),

    #
    # Volume
    #

    (
        [
            r"volume up",
            r"increase volume",
            r"raise volume",
            r"louder"
        ],
        "volume",
        ["up"]
    ),

    (
        [
            r"volume down",
            r"decrease volume",
            r"lower volume",
            r"quieter"
        ],
        "volume",
        ["down"]
    )

]


def detect(text):

    text = text.lower().strip()

    for patterns, plugin, args in RULES:

        for pattern in patterns:

            if re.search(pattern, text):

                return (
                    plugin,
                    args
                )

    return None

